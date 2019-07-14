
### 今日访问量接口

***

#### 请求地址: /api/back/visit/

#### 请求方式：GET

#### 请求参数

    token 登陆标示符 str 必填
    
*** 

#### 响应结果

##### 成功响应

    {
        "code": 200,
        "msg": "请求成功",
        "data": {
            "today_visit": 3
        }
    }

##### 响应参数
    
    today_visit 今日访问量 str
