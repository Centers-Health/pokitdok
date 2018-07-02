''' eligibility '''

import json
import os
import pokitdok
from pprint import pprint


''' Eligibility '''
class Eligibility:

    def __init__(self):
        # stubbed member test data for query
        self.member_data = {
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

    def get_eligiblity_data(self, pd):
        # api request to eligibility
        result = pd.request('/eligibility/', method='post', data=self.member_data)
        pprint(json.dumps(result))

        ## write result to file
        with open('../data/eligibility-reult.json', 'a') as eligibility_file:
            eligibility_file.write(json.dumps(result))
