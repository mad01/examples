#!/usr/bin/env python2
from fabric.api import task, parallel, run, execute


def get_hosts():
    return ['10.0.0.1', '10.0.0.2']


@parallel
def _tail():
    try:
        run('sudo tail -f /var/log/*.log')
    except KeyboardInterrupt:
        pass


@task
def tail():
    hosts = get_hosts()
    execute(_tail, hosts=hosts)
