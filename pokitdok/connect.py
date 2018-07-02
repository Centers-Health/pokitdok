''' connect '''

import json
import os
import pokitdok
from dotenv import load_dotenv
from pprint import pprint


class Connect:
    def __init__(self, client_id, client_secret):
        ## load environment values from .env
        load_dotenv()

        client_id = os.getenv("client_id")
        client_secret = os.getenv("client_secret")
