from dingapi.apis.base import DingBaseAPI


class DingUser(DingBaseAPI):
    def get_by_mobile(self, mobile):
        """根据手机号获取userid"""
        return self._client.request(
            'GET',
            '/user/get_by_mobile',
            params={'mobile': mobile}
        )

    def get(self, userid, lang='zh_CN'):
        """获取用户详情"""
        return self._client.request(
            'GET',
            '/user/get',
            params={'userid': userid, 'lang': lang}
        )

    def delete(self, userid):
        """删除用户"""
        return self._client.request(
            'GET',
            '/user/delete',
            params={'userid': userid}
        )

    def create(self, data):
        """创建用户"""
        return self._client.request(
            'POST',
            '/user/create',
            json=data
        )

    def update(self, userid, **kwargs):
        """更新用户"""
        return self._client.request(
            'POST',
            '/user/update',
            json={
                'userid': userid,
                **kwargs
            }
        )

    def getuserinfo(self, code):
        """企业内部免登 通过code 获取用户userid """
        return self._client.request(
            'GET',
            '/user/getuserinfo',
            params={
                'code': code,
            }
        )

    def getDeptMember(self, deptId):
        """获取部门用户userid列表
        "userIds": ["1","2"]
        """
        return self._client.request(
            'GET',
            '/user/getDeptMember',
            params={
                'deptId': deptId,
            }
        )

    def simplelist(self, department_id, **kwargs):
        """获取部门用户
        "userlist": [
        {
            "userid": "zhangsan",
            "name": "张三"
        }
    ]
        """
        return self._client.request(
            'GET',
            '/user/simplelist',
            params={
                'department_id': department_id,
                **kwargs
            }
        )

    def listbypage(self, department_id, offset, size, **kwargs):
        """
        获取部门用户详情
          "userlist":[
        {
            "userid": "zhangsan",
            "unionid": "PiiiPyQqBNBii0HnCJ3zljcuAiEiE",
            "mobile": "1xxxxxxxxxx",
            "tel" : "xxxx-xxxxxxxx",
            "workPlace" :"",
            "remark" : "",
            "order" : 1,
            "isAdmin": true,
            "isBoss": false,
            "isHide": true,
            "isLeader": true,
            "name": "张三",
            "active": true,
            "department": [1, 2],
            "position": "工程师",
            "email": "test@xxx.com",
            "avatar":  "xxx",
            "jobnumber": "xxx",
            "extattr": {
                "爱好":"旅游",
                "年龄":"24"
                }
        }
    ]
        """
        return self._client.request(
            'GET',
            '/user/listbypage',
            params={
                'department_id': department_id,
                'offset': offset,
                'size': size,
                **kwargs
            }
        )
