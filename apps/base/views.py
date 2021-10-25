from flask import render_template, request
from flask.views import MethodView

import requests

from apps.base.models import Page


class HomeView(MethodView):

    def get(self):

        user_data = request
        print(vars(user_data))
        external_ip = requests.get('https://api64.ipify.org/').text
        country_code = requests.get(f'http://api.ipstack.com/{external_ip}?'
                                    f'access_key=74a3ef2e0e526908b52d42f40bd961ef').json()

        if 'HTTP_X_FORWARDED_FOR' in user_data.environ:
            external_ip = user_data.environ['HTTP_X_FORWARDED_FOR']
            country_code = requests.get(f'http://api.ipstack.com/{external_ip}?'
                                        f'access_key=74a3ef2e0e526908b52d42f40bd961ef').json()

        Page.add_note(user_data.remote_addr, external_ip, country_code['country_code'])
        get_all = Page.get_all()
        items = []
        for i in get_all:
            items.append(i)
        return render_template('base.html', info=items)
