# 查猪面试搜索引擎后端项目

>author： 王海飞
>
>github：github.com/coco369

查猪面试题搜索引擎后台---使用Django框架提供restful风格接口

### 1. 安装与配置虚拟环境

    创建虚拟环境
    virtualenv --no-site-packages 虚拟环境名称
    
    激活环境
        win: 执行activate
        linux/mac: 执行source activate
    
    安装依赖包
    pip install -r requirement.txt
    
### 2. 启动项目

    python manage.py runserver ip:端口
    
    其中参数 'ip：端口'表示启动的ip地址和端口信息
    

### 2019年7月13号

本项目为面试题搜索网站，作为第一个版本，目前完成了以下罗列的功能点。

管理后台更新内容： 
    
  1. 用户管理模块
  
    登陆接口
    注册接口
    密码重设接口
  
  2. 面试题模块
    
    面试题添加接口
    面试题删除接口
    面试题修改接口
    面试题展示接口
    面试题详情接口
    面试题点赞接口
    排名前十面试题查看接口
    最新面试题查看接口
    面试题搜索接口

前台Vue更新内容：

  1. 首页展示
  2. 面试题列表页
  3. 关于我
  4. 面试题详情页
