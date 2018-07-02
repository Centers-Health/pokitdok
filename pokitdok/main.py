''' main '''

from connect_pokitdok import ConnectPokitdok
from eligibility import Eligibility

c = ConnectPokitdok()
pd = c.call_pokitdok()

e = Eligibility()
e.get_eligiblity_data(pd)
