import logging

import requests

from dingapi.apis import DingUser, DingMessage, DingDepartment
from dingapi.cache import MemoryCache
from dingapi.exception import DingRequestError


class DingApi:

    def __init__(self, app_key, app_secret, agent_id, logger=None, cache=None, token_cache=True,
                 request_extra_params=None):
        """

        :param app_key: 钉钉应用的app_key
        :param app_secret: 钉钉应用的app_secret
        :param agent_id: 钉钉应用的agent_id
        :param logger: 日志记录的logger
        :param cache: 缓存backend,默认为内存，也可指定redis或其他
        :param token_cache: 是否为access_token开启缓存，如果True,第一次获取token会将数据缓存到指定的cache默认为内存
        :param request_extra_params: 作为request额外参数传入，type: dict 比如:{"timeout":60}
        """
        self.host = 'https://oapi.dingtalk.com'
        self.app_key = app_key
        self.app_secret = app_secret
        self.agent_id = agent_id
        self.logger = logger or self.get_base_logger()
        self.cache = cache or MemoryCache()
        self.access_cache = token_cache
        self.request_extra_params = request_extra_params

        self.general_apis()

    @property
    def access_token(self):
        token_key = 'access_token'
        token = self.cache.get(token_key)
        if token is None:
            resp = self.get_access_token()
            token = resp['access_token']
            expires_in = resp.get('expires_in', 7200)
            # 缓存时间设置比实际时间有效期少10分钟，防止在在高并发情况下 最后几秒钟钉钉服务端已过期，本地仍来存在
            if self.access_cache:
                self.cache.set(key=token_key, value=token, ttl=expires_in - 10 * 60)
        return token

    def get_access_token(self):
        resp = self.request(
            'GET',
            '/gettoken',
            params={'appkey': self.app_key, 'appsecret': self.app_secret}
        )
        return resp

    def request(self, method, endpoint, **kwargs):
        """
        :param method:
        :param endpoint:
        :param kwargs: 同requests中的参数，可灵活传入json,data,timeout等参数
        :return:
        """
        url = self.host + endpoint

        params = kwargs.get('params', {})
        if endpoint != '/gettoken':
            params['access_token'] = self.access_token
            kwargs['params'] = params
        try:
            if self.request_extra_params:
                kwargs.update(self.request_extra_params)
            resp = requests.request(method, url, **kwargs).json()
        except Exception as e:
            data = kwargs.get('json', '') or kwargs.get('data', '')
            self.logger.error('api request error.method: %s, url:%s, params:%s, data:%s'
                              % (method, url, params, data), exc_info=True)
            raise e

        if resp.get('errcode') != 0:
            raise DingRequestError(resp.get('errcode'), resp.get('errmsg'))

        return resp

    def get_base_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        log_formatter = logging.Formatter(
            "[%(asctime)-15s]-[%(pathname)s-%(lineno)d]-[%(levelname)s]-[%(message)s]"
        )

        base_handler = logging.StreamHandler()
        base_handler.setLevel(logging.INFO)
        base_handler.setFormatter(log_formatter)

        logger.addHandler(base_handler)
        return logger

    def general_apis(self):
        self.user = DingUser(self)
        self.message = DingMessage(self)
        self.department = DingDepartment(self)

        self.extra_apis()

    def extra_apis(self):
        pass
