#!/usr/bin/env python
import os
import codecs
from random import randint


def random_hex():
    """returns a random hex using os.urandom"""
    return codecs.encode(os.urandom(randint(8, 10)), 'hex').decode()


def random_email(domain):
    _hex = random_hex()
    email = 'rand-%s@%s' % (_hex, domain)
    return email
