#!/usr/bin/env python3
import falcon
from pikachu.core import handlers


api = falcon.API()
api.add_route('/health', handlers.GetHealth())
