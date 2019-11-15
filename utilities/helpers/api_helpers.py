"""This file houses helper functions used for hitting various APIs"""
import uuid
import os
import re
import urllib3
from decimal import Decimal as Decimal
from configuration.device_config import ADDRESSES
# PySocks uses a deprecated import.  We are temporarily suppressing this warning until a new release fixes it: AQ-195
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    import requests


def get_galileo_balance(prn):
    """Hits the Galileo API and returns their record of the balance
    associated with the given PRN"""
    # Our test environments do not yet have certificates.  We will deliberately ignore the warnings this causes: AQ-202
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    transaction_id = str(uuid.uuid4())

    url = \
        'https://api.galileo.proxy.aspiration-corp.com/intserv/4.0/getBalance'
    headers = {}
    proxies = {
        'http': 'socks5://{0}'.format(ADDRESSES['vpc_tunnel_proxy']),
        'https': 'socks5://{0}'.format(ADDRESSES['vpc_tunnel_proxy'])
    }
    data = (
        dict(
            apiLogin=os.environ['GALILEO_API_LOGIN'],
            apiTransKey=os.environ['GALILEO_API_TRANS_KEY'],
            providerId=os.environ['GALILEO_API_PROVIDER_ID'],
            transactionId=transaction_id,
            accountNo=prn
            )
    )

    response = requests.post(url, headers=headers, data=data, verify=False,
                             proxies=proxies)

    balance = re.sub(".*<balance>", '', response.text, flags=re.DOTALL)
    balance = re.sub("</balance>.*", '', balance, flags=re.DOTALL)
    return Decimal(balance)
