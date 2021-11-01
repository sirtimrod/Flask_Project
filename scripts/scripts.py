import requests

import config


def get_country_code(external_ip):
    country_code = requests.get(config.COUNTRY_CODE_URL + external_ip).json()

    return country_code['countryCode']
