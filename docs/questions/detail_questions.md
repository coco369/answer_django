
### 面试问题查询详情接口

***

#### 请求地址: /api/back/questions/[id]/

#### 请求方式：GET

#### 请求参数:

    id 面试id值 int
    
*** 

#### 响应结果

##### 成功响应

    {
        "code": 200,
        "msg": "请求成功",
        "data": [
            {
                "id": 1,
                "user": {
                    "username": "coco",
                    "is_delete": false
                },
                "title": "coc1",
                "answer": "123456",
                "create_time": "2019-04-17T09:50:05.488874Z",
                "pri_key": "coc1",
                "from_company": "信达",
                "is_show": 1，
                "is_like": 0
            }
        ]
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
    is_like 点赞量  int