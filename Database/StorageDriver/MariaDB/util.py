"""工具包"""
import re
import os


def get_sql_structs(path: str = 'Database/StorageDriver/MariaDB/SqlMap/'):
    """从SQL语句中得到表结构"""
    results = {}
    for file in os.listdir(path):
        with open(path + file, 'r', encoding='utf-8') as f:
            sql = f.read()

        table_name_match = re.search(r'CREATE TABLE `(.+?)`', sql)
        if not table_name_match:
            return None

        table_name = table_name_match.group(1)
        sql = re.sub(r'CHARACTER SET .+? COLLATE .+? ', '', sql)
        primary_key_match = re.search(r'PRIMARY KEY \(`(.+?)`\)', sql)
        primary_key = primary_key_match.group(1) if primary_key_match else None
        columns = []
        column_matches = re.findall(r'`(.+?)` (.+?) (NOT NULL|NULL)(.*?)(?:,|\))', sql)
        for match in column_matches:
            column_name, column_type, nullability, extra = match
            nullability = 'NO' if nullability == 'NOT NULL' else 'YES'
            key = 'PRI' if column_name == primary_key else ''
            # default = 'NULL' if 'DEFAULT NULL' in extra else None
            default = None
            extra_info = ''
            columns.append((column_name, column_type, nullability, key, default, extra_info))
        results[table_name] = columns

    return results
