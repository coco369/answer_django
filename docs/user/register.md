
### 用户注册接口

***

#### 请求地址: /api/user/user/register/

#### 请求方式：POST

#### 请求参数

    username 用户名 str 必填
    
    password 密码 str  必填
    
    password2 确认密码 str  必填
    
*** 

#### 响应结果

##### 成功响应

    {
        "code": 200,
        "msg": "请求成功",
        "data": {
            "user_id": 1,
        }
    }
    
##### 失败响应

1.账号和密码没填写的情况

    {
        "code": 1002,
        "msg": "账号或密码错误，请确认登录信息",
        "data": {
            "error": {
                "username": [
                    "账号必填"
                ],
                "password": [
                    "密码必填"
                ],
                "password2": [
                    "确认密码必填"
                ]
            }
        }
    }
    
2.账号和密码长度输入不符合规范的情况

    {
        "code": 1002,
        "msg": "账号或密码错误，请确认登录信息",
        "data": {
            "error": {
                "username": [
                    "用户名不能超过4字符"
                ],
                "password": [
                    "密码不能短于6字符"
                ],
                "password2": [
                    "密码不能短于6字符"
                ]
            }
        }
    }
    
3.账号和密码的输入符合规范，账号已存在的情况和密码以及确认密码不一致的情况

    {
        "code": 1003,
        "msg": "注册账号已存在，请更换账号",
        "data": {}
    }
    
    {
        "code": 1004,
        "msg": "注册密码和确认密码不一致",
        "data": {}
    }
    
    
    
#### 响应参数

    user_id 登陆用户的id值  int
    code 状态码  int
    msg  响应信息  str
    username  账号错误信息  str
    password  密码错误信息  str
    password2  确认密码错误信息  str
    
