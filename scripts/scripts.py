import requests

import config


def get_ip_inf(_request):

    if 'HTTP_X_FORWARDED_FOR' in _request.environ:
        external_ip = _request.environ['HTTP_X_FORWARDED_FOR']
        country_code = requests.get(f"{config.IP_INF_URL + external_ip}/country/").text
        # return {'external_ip': external_ip, 'country_code': country_code}
        return {'external_ip': external_ip, 'country_code': 'RU'}

    # ip_inf = requests.get(f"{config.IP_INF_URL}/json/").json()
    # return {'external_ip': ip_inf['ip'], 'country_code': ip_inf['country']}
    return {'external_ip': '62.152.35.117', 'country_code': 'RU'}
