windows开发：

```
D:
cd Dropbox/Coding/django_site
python manage.py runserver 8080


python manage.py runserver
```

### 需求分析：

日常办公中经常需要进行模糊匹配，excel安装fuzzylookup插件可以实现，但是安装和教学还是需要成本，很多人还不会！做一个练手的小网站，实现online fuzzylookup，顺便帮助普及fuzzylookup提升社会效率。

目标把前端，后端，框架，开发流程，部署和growth hacker都顺一遍。做一个有实用性的小作品。

### 建立项目 git



$ django-admin startproject fuzzyonline

$ cd fuzzyonline

$ git init

$ git add .

$ git commit -m "first commit for fuzzyonline"

在github上面创建项目，然后

$ git remote add origin https://github.com/leemoispace/fuzzyonline.git

$ git push -u origin master

下次只用git push

以后开发一个新功能就add/commit/push一次。回滚啥的等后面用到再说。



创建项目：

```
$ python manage.py startapp fuzzyonlineapp
```

运行服务：

```
python manage.py runserver
```

2019-3-23 重新开始，pillow版本不对。

```
pip install pillow==4.2.1
```



### 核心功能

fuzzyonlineapp/views.py里面返回我们需要的东西，这里按按钮调用函数。

按按钮怎么调用Python函数，目前的情况是看到html标签都不熟悉！**返回去看django教程吧。**第三四节。

需要用模板才行。CSRF问题，先在setting中注释掉中间件。

怎么返回结果值给控件textarea？# todo

django模板：https://docs.djangoproject.com/en/1.11/ref/templates/language/



* 数据怎么走
* 如何调用模板渲染，怎么从控件得到数据，调用函数跑，返回到控件。



### 前端：

如何调用模板。查看教程第三节 view and template中创建template。

渲染模板时候填充上下文，涉及数据库设计，见教程第二节。

需要修改setting.py

为了在我们的工程中包含这个应用，我们需要在配置类 [`INSTALLED_APPS`](../ref/settings.html#std:setting-INSTALLED_APPS) 中添加设置。因为 FuzzyonlineappConfig 类写在文件 fuzzyonline/fuzzyonlineapp/apps.py 中，所以它的点式路径是 `'fuzzyonlineapp.apps.FuzzyonlineappConfig'`。在文件 `mysite/settings.py` 中 [`INSTALLED_APPS`](../ref/settings.html#std:setting-INSTALLED_APPS) 子项添加点式路径，'fuzzyonlineapp.apps.FuzzyonlineappConfig',

第一版先做两个多行对话框，可以从excel复制粘贴进来，然后装到数组里，点击按钮调用后端程序。

### 后端：

需要设计数据库和migration，参见教程第二节。目前还不用数据库。

如何从控件中读取，进行处理。todo



搜django button call python function

对两个数组跑fuzzywuzzy, 并生成相似度。

django 处理html form：http://www.runoob.com/django/django-form.html

### 部署：

todo

### 宣传：

todo

### todo

注册账号，保存查询匹配

### 用到的库：

https://github.com/seatgeek/fuzzywuzzy

Levenshtein Distance