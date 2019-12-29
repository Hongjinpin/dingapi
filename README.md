### 描述

基于 [钉钉开放平台](https://ding-doc.dingtalk.com/doc#/serverapi2/gh60vz) 封装的 轻量级Python-Sdk

因目前个人需求 只需要发送工作通知到钉钉,所以目前只封装了工作通知消息的接口和部分用户相关的接口

### 安装

```tex
pip install -U dingapi
```

### 使用

```
from dingapi.client import DingApi

AppKey = 'xxxxx'
AppSecret = 'xxxxx'
AgentId = 'xxxxx'
# 创建一个客户端
dingApi = DingApi(AppKey, AppSecret, AgentId)

# 获取用户信息
r = dingApi.user.get(user_id)
print(r)

# 发送工作通知给钉钉用户
r = dingApi.message.asyncsend_v2({
"msgtype": "text",
"text": {
"content": "消息内容",
},
},
userid_list='' # 用户 id列表
)
print(r)

```