''' settings.py '''

import os
import pokitdok
from dotenv import load_dotenv
from flask import Flask

## load environment values from .env
load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

client_settings = {
    'client_id': client_id,
    'client_secret': client_secret,
}

# authenticate to pokitdok
pd = pokitdok.api.connect(**client_settings)

# stubbed test data
member_data = {
    "member": {
        "birth_date": "1970-01-01",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "provider": {
        "organization_name": "PokitDok",
        "npi": "1912301953"
    },
    "trading_partner_id": "1199_national_benefit_fund"
}

# api request to eligibility
result = pd.request('/eligibility/', method='post', data=member_data)

print(result)
