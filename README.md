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

3. 本项目主要就是从登录页请求登录数据，后台能对数据进行校验并且返回结果，当前已经通过测试，但是由于本项目涉及的所有工具都是通过java实现的，因此不在继续进行开发，后续逐步将所用的工具用python实现，欢迎关注后续内容