# pyWebApp
backend: django (python)     frontend: angular js      user sign in, register, information edit

1.添加数据库表需要在tables文件夹里面添加py文件以及在models.py里面进行引用
2.添加完需要使用manage.py 进行与数据库同步 用法如下
   python manage.py makemigrations pyWebApp
   python manage.py migrate
3.打开服务器需要先开mysql
  然后使用manage.py  
    python manage.py runserver 
  需要特定端口号如下
    python manage.py runserver 8080

项目需要安装一些python的package，在requirement.txt里面有包括
