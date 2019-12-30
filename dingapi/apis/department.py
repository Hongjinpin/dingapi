from dingapi.apis.base import DingBaseAPI


class DingDepartment(DingBaseAPI):
    def list(self, id, lang='zh_CN', fetch_child=False):
        return self._client.request(
            'GET',
            '/department/list',
            params={'id': id, 'lang': lang, 'fetch_child': fetch_child}
        )
