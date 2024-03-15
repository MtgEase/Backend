"""会易约的MySQL存储驱动"""
from Database import Database
import pymysql
import os


class MySqlKeyMissingError(Exception):
    """MySql数据库缺少必要的键的异常"""
    def __init__(self, table, key):
        self.args = (f'Table {table} is missing key {key}.',)


class MySql(Database):
    """MySQL存储驱动对象"""
    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        super().__init__()
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            autocommit=True
        )
        self.cursor = self.connection.cursor()

        try:
            self.__check_tables()
        except MySqlKeyMissingError:
            # Todo: Backup current database
            self.__init_tables()

    def __check_tables(self):
        """检查表结构"""
        for table, keys in Database.tables.items():
            self.cursor.execute(f'DESCRIBE {table}')
            result = [i[0] for i in self.cursor.fetchall()]
            for key in keys:
                if key not in result:
                    raise MySqlKeyMissingError(table, key)

    def __init_tables(self):
        """初始化表结构"""
        for file in os.listdir('Database/SqlMap/'):
            if file.endswith('.sql'):
                with open('Database/SqlMap/' + file, 'r', encoding='utf8') as f:
                    sql = f.read()
                    self.cursor.execute(sql)

    def insert_data(self, table_name, data):
        # 插入数据
        placeholders = ', '.join(['%s'] * len(data))
        columns = ', '.join(data.keys())
        values = tuple(data.values())
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(insert_query, values)
        self.connection.commit()

    def update_data(self, table_name, data, condition):
        # 更新数据
        set_clause = ', '.join([f"{key}=%s" for key in data.keys()])
        condition_clause = ' AND '.join([f"{key}=%s" for key in condition.keys()])
        values = tuple(list(data.values()) + list(condition.values()))
        update_query = f"UPDATE {table_name} SET {set_clause} WHERE {condition_clause}"
        self.cursor.execute(update_query, values)
        self.connection.commit()

    def delete_data(self, table_name, condition):
        # 删除数据
        condition_clause = ' AND '.join([f"{key}=%s" for key in condition.keys()])
        values = tuple(condition.values())
        delete_query = f"DELETE FROM {table_name} WHERE {condition_clause}"
        self.cursor.execute(delete_query, values)
        self.connection.commit()

    def select_data(self, table_name, columns=None, condition=None, limit=None, offset=None):
        # 查询数据
        columns_clause = ', '.join(columns) if columns else '*'
        condition_clause = ' AND '.join([f"{key}=%s" for key in condition.keys()]) if condition else '1'
        limit_clause = f"LIMIT {limit}" if limit else ''
        offset_clause = f"OFFSET {offset}" if offset else ''
        select_query = f"SELECT {columns_clause} FROM {table_name} WHERE {condition_clause} {limit_clause} {offset_clause}"
        values = tuple(condition.values()) if condition else ()
        self.cursor.execute(select_query, values)
        return self.cursor.fetchall()

    def close_connection(self):
        # 关闭连接
        self.cursor.close()
        self.connection.close()

    def __del__(self):
        self.close_connection()
