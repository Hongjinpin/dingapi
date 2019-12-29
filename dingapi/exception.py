class DingRequestError(Exception):
    def __init__(self, errcode, errmsg):
        self.errcode = errcode
        self.errmsg = errmsg

    def __str__(self):
        return 'errcode: %s, errmsg: %s' % (self.errcode, self.errmsg)
