import requests

import config


def get_country_code(external_ip):
    country_code = requests.get(f"{config.COUNTRY_CODE_URL + external_ip}?access_key={config.ACCESS_KEY}").json()

    return country_code['country_code']
