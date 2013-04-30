"""
RdioUtil.py
"""

CONSUMER_KEY = '...'
CONSUMER_SECRET = '...'
domain = "example.com"

# https://github.com/rdio/rdio-python
from rdio import Rdio
from pprint import pprint

state = {}
rdio = Rdio(CONSUMER_KEY, CONSUMER_SECRET, state)

pprint(rdio.getPlaybackToken(domain=domain))