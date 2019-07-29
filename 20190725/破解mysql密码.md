先进入root权限
# /etc/init.d/mysql stop
# mysqld_safe --user=mysql --skip-grant-tables --skip-networking &
# mysql -u root
mysql> update user set password=password("newpassword") where user='root';
mysql> update user set authentication_string=password('*******') where user='*******'
mysql> flush privileges;
mysql> quit
# /etc/init.d/mysql restart
# mysql -uroot -p
enter password: <输入新设的密码newpassword>
mysql>
