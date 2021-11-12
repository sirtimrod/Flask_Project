import random
import time

from celery_worker import celery_app


@celery_app.task(name='task.generated_ip_inf')
def generated_ip_inf(work):

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
        time.sleep(30)
        return country_codes_list[random.randint(0, 9)]

    if work == 'local':
        time.sleep(15)
        return external_ips_list[random.randint(0, 9)], country_codes_list[random.randint(0, 9)]


def get_ip_inf(_request):

    if 'HTTP_X_FORWARDED_FOR' in _request.environ:
        external_ip = _request.environ['HTTP_X_FORWARDED_FOR']
        async_call = generated_ip_inf.delay('server')
        country_code = async_call.get()
        return {'external_ip': external_ip, 'country_code': country_code}

    if 'HTTP_X_FORWARDED_FOR' not in _request.environ:
        async_call = generated_ip_inf.delay('local')
        external_ip, country_code = async_call.get()
        return {'external_ip': external_ip, 'country_code': country_code}
