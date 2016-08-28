import falcon

import prometheus_client
from wsgiref import simple_server

from prom_exporter.prom import Collector


class metricHandler:
    def __init__(self, url='', service='', exclude=list):
        self._service = service
        self._url = url
        self._exclude = exclude

    def on_get(self, req, resp):
        resp.set_header('Content-Type', prometheus_client.exposition.CONTENT_TYPE_LATEST)
        registry = Collector(self._url, self._service, exclude=self._exclude)
        collected_metric = prometheus_client.exposition.generate_latest(registry)
        resp.body = collected_metric


def falcon_app(url, service, port=9999, addr='0.0.0.0', exclude=list):
    api = falcon.API()
    api.add_route('/metrics', metricHandler(url=url, service=service, exclude=exclude))

    httpd = simple_server.make_server(addr, port, api)
    httpd.serve_forever()
