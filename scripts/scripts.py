import random
import time

from apps.base.models import Page
from celery_worker import celery_app


@celery_app.task(name='task.generated_ip_inf')
def generated_ip_inf(work, internal_ip, external_ip):

    country_codes_list = ['RU', 'BG', 'US', 'DK', 'IS', 'ES', 'IT', 'CY', 'CU', 'NO']
    external_ips_list = [
        '62.152.35.117',
        '178.71.54.236',
        '149.154.161.10',
        '128.199.196.82',
        '95.213.204.115',
        '162.243.21.164',
        '188.166.79.149',
        '178.62.22.246',
        '46.101.150.160',
        '45.9.250.245'
    ]

    if work == 'server':
        time.sleep(20)
        country_code = country_codes_list[random.randint(0, 9)]
        Page.add_note(internal_ip, external_ip, country_code)
        return external_ip, country_code

    if work == 'local':
        time.sleep(15)
        country_code = country_codes_list[random.randint(0, 9)]
        external_ip = external_ips_list[random.randint(0, 9)]
        Page.add_note(internal_ip, external_ip, country_code)
        return external_ip, country_code


def get_ip_inf(_request):

    if 'HTTP_X_FORWARDED_FOR' in _request.environ:
        external_ip = _request.environ['HTTP_X_FORWARDED_FOR']
        generated_ip_inf.delay('server', _request.remote_addr, external_ip)

    if 'HTTP_X_FORWARDED_FOR' not in _request.environ:
        generated_ip_inf.delay('local', _request.remote_addr, None)
