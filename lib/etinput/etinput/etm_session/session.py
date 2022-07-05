from etinput.config import Config

class ETMSession:
    def __init__(self):
        pass

    def send_request(self, keys):
        '''Generator of Results'''
        pass

    def url(self):
        return f"{Config().api_url}{Config().scenario['id']}{self.ENDPOINT}"

    def _handle_response(self, response):
        '''Return the handled response (list/dict of outcomes)'''
        if response.status_code == 422:
            self.fail_with(errors=response.json()['errors'])

        self.fail_with('Something went wrong connecting to the ETM')

    def fail_with(self, message='', errors=[]):
        if not message and errors:
            message = ', '.join(errors)
        raise ETMConnectionError(message)

class ETMConnectionError(BaseException):
    pass
