from pikachu.core.log import logger


class GetHealth:
    def __init__(self):
        self.log = logger()

    def on_get(self, req, resp):
        self.log.info('GetHealth.status')
        resp.body = '{"status": "OK"}'
