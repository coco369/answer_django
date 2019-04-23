
### 创建问题接口

***

#### 请求地址: /api/back/questions/

#### 请求方式：POST

#### 请求参数

    title 面试标题 str 必填
    
    answer 面试回答 str  必填
    
    pri_key 技术关键字 str  必填
    
    from_company 来源公司 str  必填
    
    token 登陆标识符 str  必填
    
    is_show 是否发布  int 非必填
    
*** 

#### 响应结果

##### 成功响应

    {
        "code": 200,
        "msg": "请求成功",
        "data": {
            "questions": {
                "id": 2,
                "title": "coc1111",
                "answer": "123456",
                "create_time": "2019-04-17T09:58:55.202421Z",
                "pri_key": "coc1111",
                "from_company": "信达",
                "is_show": 1,
                "user": {
                    "username": "coco",
                    "is_delete": false
                },
            }
        }
    }
    
##### 失败响应

1.面试题已存在的情况

    {
        "code": 2002,
        "msg": "喵了个喵，面试题已存在",
        "data": {}
    }
    
2.登陆状态校验失败的情况

    {
        "code": 1006,
        "msg": "用户认证失败，请重新登陆",
        "data": {}
    }
    
3.账号查询用户不存在的情况

    {
        "code": 1001,
        "msg": "登录账号不存在，请更换账号再登录",
        "data": {}
    }
4.面试题保存参数提交不完整或错误的情况

    {
        "code": 2001,
        "msg": "面试题字段校验有误",
        "data": {
            "error": {
                "title": [
                    "问题标题必填"
                ],
                "answer": [
                    "解答必填"
                ],
                "pri_key": [
                    "面试题关键字必填"
                ]
            }
        }
    }

#### 响应参数
    
    title 面试标题 str
    answer 面试回答 str  
    pri_key 技术关键字 str  
    from_company 来源公司 str  
    token 登陆标识符 str 
    is_show 是否发布  int 
    username 用户名 str
    is_delete 是否删除用户  int
