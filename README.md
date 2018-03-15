# cdt-auth
账号权限管理系统项目安装

1. 数据库迁移
    ```
    $ python cdt-auth.py db init
    $ python cdt-auth.py db migrate -m "initial migration"
    $ python cdt-auth.py db upgrade
    ```

2. 初始化，创建默认角色和默认用户
    ```
    $ python cdt-auth.py create_role_superadmin
    $ python cdt-auth.py create_role_guest
    $ python cdt-auth.py create_superadmin
    $ python cdt-auth.py create_guest
    ```

3. 20180315已经实现接口用flask-restful扩展实现
4. 使用flask-restful扩展时注意fields模块的时间格式化问题
5. ......