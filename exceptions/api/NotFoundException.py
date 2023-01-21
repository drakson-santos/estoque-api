class NotFoundException(Exception):

    def __init__(self, custom_msg=None):
        self.message = custom_msg or f"Resource not found."
        self.http_code = 404
        super().__init__(self.message)