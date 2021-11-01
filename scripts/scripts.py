import requests

import config


def get_ip_inf(external_ip=None):

    if external_ip:
        country_code = requests.get(f"{config.IP_INF_URL + external_ip}/country/").text
        return country_code

    ip_inf = requests.get(f"{config.IP_INF_URL}/json/").json()
    return ip_inf
