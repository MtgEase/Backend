# Database 模块说明

此模块的用途是与会易约存储后端交互，实现前端调用与后端存储细节的解耦。

---

## 目录结构

- `README.md`：帮助文档。
- `__init__.py`：模块的初始化代码。
- `StoragDriver/`：存放不同存储池驱动代码的目录。默认包含MySQL的驱动。

## 多存储后端说明

会易约被设计为支持多存储后端的模式，可以方便地根据不同的存储后端编写存储池驱动。 只要编写了相应的存储池驱动，数据就可以统一、规范地存储在不同的存储池中。

会易约默认具有MySQL和MariaDB数据库的驱动。

## 存储池驱动开发流程

可参照已有的`MySql`或`MariaDB`驱动开发。

开发时需要在`Database/StorageDriver/`目录下新建存储驱动包，包名即为驱动名。

在包中创建与驱动名同名的类，需要能够被实例化和被外部导入。

实例需要实现增删改查和初始化的功能。

增删改查函数需要严格约定如下：

- `insert_data(table: str, data: dict)`

    在table表中插入data数据。

- `delete_data(table: str, condition: dict)`

    在table表中按condition条件删除数据。

- `update_data(table: str, data: dict, condition: dict)`

    在table表中按condition条件更新数据为data。

- `select_data(table: str, columns: list = None, condition: dict = None, limit: int | None = None, offset: int | None = None)`

    在table表中按condition条件查询并返回数据，columns指定需要的列，offset指定要跳过的数量，limit指定要取的数据条数。

存储的数据表及其对应的字段：

```
tables = {
    'user': ['uid', 'name', 'email', 'wxid', 'hashed_password'],
    'group': ['gid', 'name', 'belong_to', 'permissions', 'targets'],
    'determine': ['did', 'is_meeting', 'id'],
    'meeting': ['mid', 'topic', 'time_start', 'time_stop', 'room', 'tip', 'status', 'determine_step', 'created_by'],
    'room': ['rid', 'name', 'position', 'tip', 'available', 'capacity', 'devices', 'rest'],
    'tag': ['tid', 'name', 'permissions', 'targets', 'expire', 'created_by']
}
```

此外考虑到初次运行和数据损坏的情况，驱动在初始化的时候需要自行检查数据、初始化表。

## 配置项

各驱动所需的配置项存储于项目配置文件`Config/config.yaml`文件内，存储于`Database`键下。项目启动时会自动读取参数并按配置启动。

在`Database`键下通过`Driver`项指定要使用的驱动，填入驱动名即可。默认为MySql。正确填写后程序会自行导入并初始化。

在`Database`键下的DriverArgs键下配置驱动所需的参数。参数名和类型需要和驱动的构造函数所需的参数相同。
