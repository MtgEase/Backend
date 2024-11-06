"""会易约的MariaDB存储驱动"""
from fastapi import HTTPException
import logging
import pymysql
import os
import yaml
from Database.StorageDriver.MariaDB import util
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
# fh = logging.FileHandler(filename='./log/server.log')
logger.addHandler(ch)  # 将日志输出至屏幕
# logger.addHandler(fh)  # 将日志输出至文件
logger = logging.getLogger(__name__)


class MariaDB:
    """MariaDB存储驱动对象"""

    def __init__(self, **config):
        super().__init__()
        self.host: str = config['host']
        self.port: int = config['port']
        self.user: str = config['user']
        self.passwd: str = config['password']
        self.database: str = config['database']
        self.config: dict = config
        try:
            self.connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.passwd,
                database=self.database,
                autocommit=True
            )
            self.cursor = self.connection.cursor()
            logger.info(f'[Database/MariaDB] Connected to MariaDB!')
        except pymysql.err.MySQLError as e:
            logger.error(f'[Database/MariaDB] CAN NOT connect to MariaDB!\n\t{str(e)}')
            exit(1)

        try:
            self.__check_tables()
            logger.info(f'[Database/MariaDB] Database struct OK!')
        except (AssertionError, pymysql.err.MySQLError):
            logger.error(f'[Database/MariaDB] Database struct ERROR!')
            backup_file = f"corrupt_database_{self.database}_{datetime.now().strftime('%Y%m%d-%H%M%S')}.sql"
            backup_file = os.path.join(self.config['auto_backup_dir'], backup_file)
            # 备份失败就终止程序
            if os.system(f'mysqldump -h {self.host} -P {self.port} -u {self.user} -p {self.passwd} {self.database} > '
                         f'{backup_file}') != 0:
                logger.error(f'[Database/MariaDB] "mysqldump" DID NOT run correctly. Have you already installed it? '
                             f'(Return non-zero exit code)')
                exit(1)
            logger.info(f'[Database/MariaDB] Corrupt database backed at: {backup_file}')
            if self.config['init_database_confirm']:
                try:
                    with open('Config/config.yaml', 'r', encoding='utf-8') as __f:
                        full_config = yaml.safe_load(__f)
                    full_config['Database']['DriverArgs']['init_database_confirm'] = False
                    with open('Config/config.yaml', 'w', encoding='utf-8') as __f:
                        yaml.safe_dump(full_config, __f)
                except Exception as e:
                    logger.error(f'[Database/MariaDB] CAN NOT write config file: Config/config.yaml\n\t{str(e)}')
                    exit(1)
                try:
                    self.__init_tables()
                except pymysql.err.MySQLError as e:
                    logger.error(f'[Database/MariaDB] CAN NOT connect to MySql!\n\t{str(e)}')
                    exit(1)
                logger.info(f'[Database/MariaDB] Database inited.')
            else:
                logger.info(f'[Database/MariaDB] Exiting...')
                exit(1)

    def __check_tables(self):
        """检查表结构"""
        standard_structs = util.get_sql_structs()
        for table in standard_structs.keys():
            self.cursor.execute(f'DESCRIBE `{table}`')
            current_struct = self.cursor.fetchall()
            standard_struct = tuple(standard_structs[table])
            assert current_struct == standard_struct

    def __init_tables(self):
        """初始化表结构"""
        for file in os.listdir('Database/StorageDriver/MariaDB/SqlMap/'):
            if file.endswith('.sql'):
                with open(os.path.join('Database/StorageDriver/MariaDB/SqlMap/', file), 'r', encoding='utf-8') as f:
                    sql = f.readlines()
                    correct_sql = []
                    temp_sql = ''
                    for line in sql:
                        if line == '\n' or line.startswith('--'):
                            pass
                        else:
                            if line.endswith(';\n'):
                                correct_sql.append(temp_sql + line.rstrip('\n'))
                                temp_sql = ''
                            else:
                                temp_sql += line.rstrip('\n')
                    for line in correct_sql:
                        self.cursor.execute(line)

    def insert_data(self, table: str, data: dict) -> None:
        # 插入数据
        try:
            self.connection.ping(reconnect=True)
        except pymysql.err.MySQLError as e:
            logger.error(f'[Database/MariaDB] CAN NOT connect to MariaDB!\n\t{str(e)}')
            raise HTTPException(status_code=503)
        placeholders = ', '.join(['%s'] * len(data))
        columns = ', '.join(data.keys())
        values = tuple(data.values())
        insert_query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(insert_query, values)

    def update_data(self, table: str, data: dict, condition: dict) -> None:
        # 更新数据
        try:
            self.connection.ping(reconnect=True)
        except pymysql.err.MySQLError as e:
            logger.error(f'[Database/MariaDB] CAN NOT connect to MariaDB!\n\t{str(e)}')
            raise HTTPException(status_code=503)
        set_clause = ', '.join([f"{key}=%s" for key in data.keys()])
        condition_clause = ' AND '.join([f"{key}=%s" for key in condition.keys()])
        values = tuple(list(data.values()) + list(condition.values()))
        update_query = f"UPDATE {table} SET {set_clause} WHERE {condition_clause}"
        self.cursor.execute(update_query, values)

    def delete_data(self, table: str, condition: dict) -> None:
        # 删除数据
        try:
            self.connection.ping(reconnect=True)
        except pymysql.err.MySQLError as e:
            logger.error(f'[Database/MariaDB] CAN NOT connect to MariaDB!\n\t{str(e)}')
            raise HTTPException(status_code=503)
        self.connection.ping(reconnect=True)
        condition_clause = ' AND '.join([f"{key}=%s" for key in condition.keys()])
        values = tuple(condition.values())
        delete_query = f"DELETE FROM {table} WHERE {condition_clause}"
        self.cursor.execute(delete_query, values)

    def select_data(self, table: str, columns: list | None = None, condition: dict | None = None,
                    limit: int | None = None, offset: int | None = None) -> tuple:
        # 查询数据
        try:
            self.connection.ping(reconnect=True)
        except pymysql.err.MySQLError as e:
            logger.error(f'[Database/MariaDB] CAN NOT connect to MariaDB!\n\t{str(e)}')
            raise HTTPException(status_code=503)
        self.connection.ping(reconnect=True)
        columns_clause = ', '.join(columns) if columns else '*'
        condition_clause = ' AND '.join([f"{key}=%s" for key in condition.keys()]) if condition else '1'
        limit_clause = f"LIMIT {limit}" if limit else ''
        offset_clause = f"OFFSET {offset}" if offset else ''
        select_query = f"SELECT {columns_clause} FROM {table} WHERE {condition_clause} {limit_clause} {offset_clause}"
        values = tuple(condition.values()) if condition else ()
        self.cursor.execute(select_query, values)
        return self.cursor.fetchall()

    def close_connection(self):
        # 关闭连接
        self.cursor.close()
        self.connection.close()

    def __del__(self):
        self.close_connection()
