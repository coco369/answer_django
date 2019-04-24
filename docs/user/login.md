
### 用户登陆接口

***

#### 请求地址: /api/user/user/login/

#### 请求方式：POST

#### 请求参数

    username 用户名 str 必填
    
    password 密码 str  必填
    
*** 

#### 响应结果

##### 成功响应

    {
        "code": 200,
        "msg": "请求成功",
        "data": {
            "user_id": 1,
            "username": "coco",
            "token": "6257f183356740409bba9ef731453b6b"
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
                ]
            }
        }
    }
    
3.账号和密码的输入符合规范，但账号不存在但情况

    {
        "code": 1001,
        "msg": "登录账号不存在，请更换账号再登录",
        "data": {}
    }
    
#### 响应参数

    user_id 登陆用户的id值  int
    username 登陆用户的用户名  str
    token 登陆标示符  str
    code 状态码  int
    msg  响应信息  str
    username  账号错误信息  str
    password  密码错误信息  str
    
