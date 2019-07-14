
### 用户登陆记录接口

***

#### 请求地址: /api/user/user/record/

#### 请求方式：GET

#### 请求参数

    token 登陆标识符 str 必填
    
*** 

#### 响应结果

##### 成功响应

    {
        "code": 200,
        "msg": "请求成功",
        "data": {
            "user_login": [{
                "id": 9,
                "l_ip": "127.0.0.1",
                "status": "成功",
                "create_time": "2019-07-13 19:27:18"
            }, {
                "id": 8,
                "l_ip": "127.0.0.1",
                "status": "失败",
                "create_time": "2019-07-13 19:27:14"
            }],
            "count": 4,
            "last_ip": "127.0.0.1",
            "last_time": "127.0.0.1"
        }
    }
    
##### 失败响应

1.token认证失败

    {
        "code": 1006,
        "msg": "用户认证失败，请重新登陆",
        "data": {}
    }
    
#### 响应参数

    user_login 用户登陆的记录信息  
    id 登陆用户记录的id值  int
    l_ip 登陆用户的ip str
    status 登陆状态  str
    create_time 登陆时间 str
    msg  响应信息  str
    count  登陆次数  int
    last_ip  最后一次登陆ip信息  str
    last_time 最后一次登陆时间 str
    
