from dingapi.apis.base import DingBaseAPI


class DingMedia(DingBaseAPI):
    def upload(self, type, media):
        files = {'media': open(media, 'rb')}

        return self._client.request(
            'POST',
            '/media/upload',
            data={'type': type},
            files=files

        )
