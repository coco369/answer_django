
### 用户密码重设接口

***

#### 请求地址: /api/user/user/reset_password/

#### 请求方式：POST

#### 请求参数

    username 用户名 str 必填
    
    password 密码 str  必填
    
    password2 重设密码 str  必填
    
    token 登陆标识符 str 必填
*** 

#### 响应结果

##### 成功响应

    {
        "code": 200,
        "msg": "重置密码成功",
        "data": {}
    }
    
##### 失败响应

1.账号和密码和确认密码没填写的情况

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
                    "重设密码必填"
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
    
3.账号和密码的输入符合规范，但账号不存在的情况

    {
        "code": 1005,
        "msg": "重设密码账号不存在，请更换账号",
        "data": {}
    }    

4.账号和密码的输入符合规范，但账号存在，但原始密码错误的情况

    {
        "code": 1008,
        "msg": "原始密码错误，请确认登陆密码是否正确",
        "data": {}
    }
    
5.token认证失败

    {
        "code": 1006,
        "msg": "用户认证失败，请重新登陆",
        "data": {}
    }
    
#### 响应参数

    code 状态码  int
    msg  响应信息  str
    username  账号错误信息  str
    password  密码错误信息  str
    password2  确认密码错误信息  str
    
