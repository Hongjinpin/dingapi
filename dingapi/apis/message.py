from dingapi.apis.base import DingBaseAPI


class DingMessage(DingBaseAPI):
    def asyncsend_v2(self, msg, userid_list=None, dept_id_list=None, to_all_user=False):
        if isinstance(userid_list, (list, tuple, set)):
            userid_list = ",".join(userid_list)
        if isinstance(dept_id_list, (list, tuple, set)):
            dept_id_list = ",".join(dept_id_list)
        return self._client.request(
            'POST',
            '/topapi/message/corpconversation/asyncsend_v2',
            json={
                'agent_id': self._client.agent_id,
                'msg': msg,
                'userid_list': userid_list,
                'dept_id_list': dept_id_list,
                'to_all_user': to_all_user,
            }
        )

    def getsendprogres(self, task_id):
        return self._client.request(
            'POST',
            '/topapi/message/corpconversation/getsendprogress',
            json={
                'agent_id': self._client.agent_id,
                'task_id': task_id,
            }
        )

    def getsendresult(self, task_id):
        return self._client.request(
            'POST',
            '/topapi/message/corpconversation/getsendresult',
            json={
                'agent_id': self._client.agent_id,
                'task_id': task_id,
            }
        )
