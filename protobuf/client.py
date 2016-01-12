#!/usr/bin/env python3
import argparse
from lib import client_api
from lib.shared import ProtoShared


def call(msg='', channel=''):
    shared = ProtoShared()
    api = client_api.Client()
    cmd = api.send_ping(
        msg=msg,
        channel=channel,
        pingId='PING'
        )

    print('Response: %s' % shared.pingName(cmd.ping.pingId))
    print('message sent: %s' % cmd.ping.msg)
    print('to channel: %s' % cmd.ping.channel)


def main():
    description = 'command line tool send messages to a channel'
    parser = argparse.ArgumentParser(description)
    parser.add_argument('-m', '--message', help='add message', required=True)
    parser.add_argument('-c', '--channel', help='set channel', required=True)
    args = parser.parse_args()
    call(
        msg=args.message,
        channel=args.channel
        )


if __name__ == '__main__':
    main()
