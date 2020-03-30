# SHTD-DMP设计文档

DMP( *Data Management Platform*)数据管理平台

## 功能列表

- 数据集群连接
- 数据库绑定
    - MongoDB
    - MySQL
-  数据上传(！大文件)
    - SQLite
    - CSV
    - JSON
    - EXCEL
- 数据量化
- 数据周转
    - 数据库到集群
    - 集群到数据库
- 数据检索
    - 简单检索
    - ES
- 表单审批数据导入表单审批
    - 数据导出表单审批
- 数据导出
    - 下载验证确保数据安全
- 用户注册
    - 单一注册（邮箱+管理员确认激活）
    - 批量注册
- 用户管理
    - 创建
    - 删除
    - 冻结
- 用户组系统
    - 系统功能模块化（超级管理员可以自由组合相应功能的用户组）
    - 权限限制及确认机制





## 表设计

表名：dmp_user

说明：用户表

| 字段               | 数据类型 | 限制       | 介绍                                  |
| ------------------ | -------- | ---------- | ------------------------------------- |
| id                 | Int      | Primay Key | 用户ID                                |
| user_name          | string   | 非空       | 用户名                                |
|                    |          |            | 真实姓名                              |
| email              | string   | Unique     | 用户邮箱                              |
| passwd             | string   | 非空       | 用户密码，加密储存                    |
| confirmed          | boolean  |            | 用户激活状态，默认FALSE               |
| dmp_group_id       | int      |            | 所属用户组ID，默认学生用户组,使用外键 |
| leader_dmp_user_id | Int      |            | 直属管理者，默认是超级管理员用户      |
| last_login         | Date     |            | 最后登录时间                          |
| created_on         | Date     |            | 创建时间                              |
| changed_on         | Date     |            | 修改时间                              |

表名：dmp_group

说明：用户组表

| 字段       | 数据类型 | 限制       | 介绍                                           |
| ---------- | -------- | ---------- | ---------------------------------------------- |
| id         | Int      | Primay Key | 用户组ID                                       |
| group_name | string   | Unique     | 用户组名                                       |
| approval   | Boolearn |            | 是否能审批,默认False                           |
| unlimited  | Boolearn |            | 默认false,是否不受限制，仅超级管理员用户组勾选 |
| created_on | Date     |            | 创建时间                                       |
| changed_on | Date     |            | 修改时间                                       |

表名：dmp_permission

说明：权限表

| 字段            | 数据类型 | 限制       | 介绍         |
| --------------- | -------- | ---------- | ------------ |
| id              | int      | Primay Key | 功能ID       |
| route           | string   | 非空       | 路由         |
| permission_name | string   | 非空       | 路由功能名称 |

表名：dmp_group_permission

说明：用户组_功能表

| 字段              | 数据类型 | 限制               | 介绍     |
| ----------------- | -------- | ------------------ | -------- |
| id                | int      | Primay Key、Unique | ID       |
| dmp_permission_id | int      | 非空               | 权限ID   |
| dmp_group_id      | Int      | 非空               | 用户组ID |





表名：dmp_datebase

说明：数据库表

| 字段          | 数据类型 | 限制       | 介绍           |
| ------------- | -------- | ---------- | -------------- |
| id            | int      | Primay Key |                |
| datebase_name | string   | Unique     | 数据名称       |
| dmp_user_id   | Int      | 非空       | 所属用户ID     |
| db_type       | string   | 非空       | 数据库类型     |
| db_host       | string   | 非空       | 数据库主机地址 |
| db_port       | int      | 非空       | 数据库端口号   |
| db_username   | string   |            | 数据库用户名   |
| db_passwd     | string   |            | 数据库密码     |
| description   | string   |            | 数据库说明     |
| created_on    | Date     | 非空       | 创建时间       |
| changed_on    | Date     |            | 修改时间       |

表名：dmp_data_category

说明: 案例表

| 字段        | 数据类型 | 限制       | 介绍           |
| ----------- | -------- | ---------- | -------------- |
| id          | int      | Primay Key |                |
| category    | String   | 非空       | 案例名称       |
| description | string   |            | 案例说明       |
| url_name    | string   |            | 可视化网站名称 |
| Url         | String   |            | 网址           |

表名：dmp_data_table

说明：数据表

| 字段                 | 数据类型 | 限制       | 介绍               |
| -------------------- | -------- | ---------- | ------------------ |
| id                   | int      | Primay Key |                    |
| data_table_name      | string   | Unique     | 数据名称           |
| db_table_name        |          | 非空       | 数据库内数据表名称 |
| dmp_database_id      | int      | 非空       | 数据库ID           |
| dmp_data_category_id | Int      |            | 所属案例id         |
| user_id              | int      | 非空       | 添加人             |
| description          | String   |            | 数据说明           |
| created_on           | Date     | 非空       | 创建时间           |
| changed_on           | Date     |            | 修改时间           |

表名：dmp_data_table_column

说明：数据列信息

| 字段              | 数据类型 | 限制               | 介绍               |
| ----------------- | -------- | ------------------ | ------------------ |
| id                | int      | Primay Key、Unique |                    |
| dmp_data_table_id | int      | 非空               | 数据ID             |
| column_name       | string   | 非空               | 列名               |
| groupby           | boolearn | 默认FALSE          | 可以进行分组       |
| Wherein           | boolearn | 默认FALSE          | 可以区间筛选       |
| Isdate            | boolearn | 默认FALSE          | 是否为时间日期字段 |
| description       | string   |                    | 字段说明           |

表名：dmp_table_column_range

说明：数据列区间

| 字段                     | 数据类型 | 限制               | 介绍 |
| ------------------------ | -------- | ------------------ | ---- |
| id                       | int      | Primay Key、Unique |      |
| dmp_data_table_column_id | Int      | 非空               | 列ID |
| context                  | String   | 非空               | 内容 |

表名：dmp_from_add_data_table

说明：数据从数据库添加表单表

| 字段            | 数据类型 | 限制               | 介绍     |
| --------------- | -------- | ------------------ | -------- |
| id              | int      | Primay Key、Unique |          |
| submit_on | date     | 非空 | 提交时间 |
| submit_dmp_user_id | int      | 非空 | 提交人   |
| data_table_name | string   | Unique     | 数据名称           |
| db_table_name   |          | 非空       | 数据库内数据表名称 |
| database_id     | int      | 非空 | 数据库ID           |
| category_id     | Int      | 非空 | 所属案例id         |
| description              | string   |                    | 说明             |
| approve_dmp_user_id      | Int      |                    | 审批人           |
| approve_on             | date     |                    | 审批时间         |
| approve_result           | int      |                    | 审批结果,默认为0，通过是1不通过是2 |
| answer | string | | 审批答复 |
| created_on | Date | 非空 | 创建时间 |
| changed_on | Date | | 修改时间 |





表名：dmp_from_upload

说明：数据文件上传单表

| 字段                        | 数据类型 | 限制               | 介绍                               |
| --------------------------- | -------- | ------------------ | ---------------------------------- |
| id                          | int      | Primay Key、Unique |                                    |
| submit_on                   | date     | 非空               | 提交时间                           |
| submit_dmp_user_id          | int      | 非空               | 提交人                             |
| filetype                    | Int      | 非空               | 文件类型                           |
| filepath                    | string   | 非空               | 文件路径                           |
| column_line                 | Int      |                    | 列名行号                           |
| column                      | string   |                    | 自定义列名                         |
| json_dimension_reduction    | Boolearn |                    | json数据是否遍历存储               |
| destination_dmp_datebase_id | int      | 非空               | 目标数据库ID                       |
| new_table_name              | string   | 非空               | 表名                               |
| method                      | String   | 非空               | 新建还是添加覆盖                   |
| dmp_data_category_id        | Int      | 非空               | 所属案例                           |
| description                 | string   |                    | 说明                               |
| approve_user_id             | Int      |                    | 审批人                             |
| approval_on                 | date     |                    | 审批时间                           |
| approve_result              | int      |                    | 审批结果,默认为0，通过是1不通过是2 |
| answer                      | String   |                    | 审批答复                           |
| upload                      | bool     |                    | 是否成功                           |
| upload_result               | string   |                    | 数据上传结果                       |
| created_on                  | Date     | 非空               | 创建时间                           |
| changed_on                  | Date     |                    | 修改时间                           |



表名：dmp_from_migrate

说明：数据迁移表单表

| 字段                        | 数据类型 | 限制               | 介绍                               |
| --------------------------- | -------- | ------------------ | ---------------------------------- |
| id                          | int      | Primay Key、Unique |                                    |
| submit_on                   | date     | 非空               | 提交时间                           |
| submit_dmp_user_id          | int      | 非空               | 提交人                             |
| origin_table_id             | int      | 非空               | 起点数据表                         |
| rule                        | string   |                    | 数据提取规则                       |
| destination_dmp_datebase_id | int      | 非空               | 目标数据库ID                       |
| new_table_name              | string   | 非空               | 新表名                             |
| method                      | String   | 非空               | 覆盖添加新建                       |
| description                 | string   |                    | 说明                               |
| approve_dmp_user_id         | int      |                    | 审批人                             |
| approval_on                 | date     |                    | 审批时间                           |
| approve_result              | int      |                    | 审批结果,默认为0，通过是1不通过是2 |
| answer                      | string   |                    | 审批答复                           |
| migrate                     | Boolearn |                    | 迁移成功                           |
| migrate_result              | string   |                    | 迁移结果                           |
| created_on                  | Date     | 非空               | 创建时间                           |
| changed_on                  | Date     |                    | 修改时间                           |



表名：dmp_from_download

说明：数据下载表单表

| 字段               | 数据类型 | 限制               | 介绍                               |
| ------------------ | -------- | ------------------ | ---------------------------------- |
| id                 | int      | Primay Key、Unique |                                    |
| submit_on          | date     | 非空               | 提交时间                           |
| submit_dmp_user_id | int      | 非空               | 提交人                             |
| dmp_data_table_id  | int      | 非空               | 源数据表ID                         |
| rule               | string   |                    | 数据提取规则                       |
| description        | string   |                    | 说明                               |
| approve_user_id    | int      |                    | 审批人                             |
| approval_on        | date     |                    | 审批时间                           |
| approve_result     | int      |                    | 审批结果,默认为0，通过是1不通过是2 |
| answer             | string   |                    | 审批答复                           |
| ftp_url            | string   |                    | FTP下载链接                        |
| ftp_pid            | int      |                    | FTP进程号                          |
| filepath           | string   |                    | 文件路径                           |
| finish             | boolearn |                    | 是否完成                           |
| created_on         | Date     | 非空               | 创建时间                           |
| changed_on         | Date     |                    | 修改时间                           |

