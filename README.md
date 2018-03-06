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
