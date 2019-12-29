from dingapi.apis.base import DingBaseAPI


class DingUser(DingBaseAPI):
    def get_by_mobile(self, mobile):
        return self._client.request(
            'GET',
            '/user/get_by_mobile',
            params={'mobile': mobile}
        )

    def get(self, userid, lang='zh_CN'):
        return self._client.request(
            'GET',
            '/user/get',
            params={'userid': userid, 'lang': lang}
        )

    def delete(self, userid):
        return self._client.request(
            'GET',
            '/user/delete',
            params={'userid': userid}
        )

    def create(self, data):
        return self._client.request(
            'POST',
            '/user/create',
            json=data
        )

    def update(self, userid, data):
        return self._client.request(
            'POST',
            '/user/update',
            json={
                'userid': userid,
                **data
            }
        )

    def getuserinfo(self, code):
        return self._client.request(
            'GET',
            '/user/getuserinfo',
            params={
                'code': code,
            }
        )
