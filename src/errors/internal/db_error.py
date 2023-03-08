class DbError(Exception):
    def __init__(self, status_code=500, message="Db issue"):
        self._status_code = status_code # _ protected. __: private
        self._message = message
        super().__init__(self.message)
