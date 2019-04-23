
### 问题查看接口

***

#### 请求地址: /api/back/questions/

#### 请求方式：GET


#### 响应结果

##### 成功响应

    {
        "code": 200,
        "msg": "请求成功",
        "data": {
            "count": 7,
            "next": "http://127.0.0.1:8000/api/back/questions/?page=2&token=8abf2a78861a49269e2082b35af7f470",
            "previous": null,
            "results": [
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
                    "is_show": 0,
                    "is_delete": 0,
                    "is_like": 1
                },
                {
                    "id": 2,
                    "user": {
                        "username": "coco",
                        "is_delete": false
                    },
                    "title": "coc1111",
                    "answer": "123456",
                    "create_time": "2019-04-17T09:58:55.202421Z",
                    "pri_key": "coc1111",
                    "from_company": "信达",
                    "is_show": 1,
                    "is_delete": 0,
                    "is_like": 1
                }
            ]
        }
    }
    
#### 响应参数
    count 总条数 int
    next 下一页地址  str
    previous 上一页地址 str
    
    title 面试标题 str
    answer 面试回答 str  
    pri_key 技术关键字 str  
    from_company 来源公司 str  
    token 登陆标识符 str 
    is_show 是否发布  int 
    username 用户名 str
    is_delete 是否删除用户  int
    is_like 点赞量  int