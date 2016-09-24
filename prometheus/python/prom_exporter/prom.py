import time
import random
from prometheus_client import Metric


class Collector(object):
    def __init__(self, endpoint, service, exclude=list):
        self._endpoint = endpoint
        self._service = service
        self._labels = {}
        self._set_labels()
        self._exclude = exclude

    def _set_labels(self):
        self._labels.update({'service': self._service})

    def filter_exclude(self, metrics):
        return {k: v for k, v in metrics.items() if k not in self._exclude}

    def _get_metrics(self):
        metrics = {
            'requests': 100,
            'requests_status_2xx': 90,
            'requests_status_4xx': 3,
            'requests_status_5xx': 7,
            'uptime_sec': 123,
            'exclude_me': 1234,
            }

        if self._exclude:
            metrics = self.filter_exclude(metrics)

        time.sleep(random.uniform(0.1, 0.4))
        return metrics

    def collect(self):
        metrics = self._get_metrics()

        if metrics:
            for k, v in metrics.items():
                metric = Metric(k, k, 'counter')
                labels = {}
                labels.update(self._labels)
                metric.add_sample(k, value=v, labels=labels)

                if metric.samples:
                    yield metric
                else:
                    pass
