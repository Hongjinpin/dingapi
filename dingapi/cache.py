import time


class BaseCache:

    def get(self, key, default=None):
        raise NotImplementedError()

    def set(self, key, value, ttl=None):
        raise NotImplementedError()

    def delete(self, key):
        raise NotImplementedError()


class MemoryCache(BaseCache):

    def __init__(self):
        self._data = {}

    def set(self, key, value, ttl=300):
        ts = time.time() + ttl
        self._data[key] = (value, ts)

    def get(self, key, default=None):
        if key not in self._data:
            return default

        value, ts = self._data[key]
        if time.time() > ts:
            self.delete(key)
            return default

        return value

    def delete(self, key):
        if key not in self._data:
            return
        del self._data[key]

    def clear(self):
        self._data = {}
