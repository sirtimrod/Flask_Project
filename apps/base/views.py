from flask import render_template, request
from flask.views import MethodView

import requests

from apps.base.models import Page


class HomeView(MethodView):

    def get(self):

        user_data = request
        print(vars(user_data))
        external_ip = requests.get('https://api64.ipify.org/').text

        if 'http_x_forwarded_for' in vars(user_data):
            external_ip = user_data.HTTP_X_FORWARDED_FOR
            print('Internal IP inside IF:', user_data.remote_addr)
            print('External IP inside IF:', external_ip)

        country_code = 'RU'

        print('Internal IP outside IF:', user_data.remote_addr)
        print('External IP outside IF:', external_ip)

        Page.add_note(user_data.remote_addr, external_ip, country_code)
        get_all = Page.get_all()
        items = []
        for i in get_all:
            items.append(i)
        return render_template('base.html', info=items)
