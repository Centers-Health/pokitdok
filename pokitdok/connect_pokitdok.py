''' connect_pokitdok '''

import os
import pokitdok
from dotenv import load_dotenv
from os.path import join, dirname, os

''' ConnectPokitdok '''
class ConnectPokitdok:

    def __init__(self):
        ## load environment values from .env
        dotenv_path = join(dirname(__file__), '../.env')
        load_dotenv(dotenv_path)

        self.client_id = os.getenv("client_id")
        self.client_secret = os.getenv("client_secret")

        self.client_settings = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }

    def call_pokitdok(self):
        print(self.client_settings)
        # authenticate to pokitdok
        pd = pokitdok.api.connect(**self.client_settings)

        return pd
