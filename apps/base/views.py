from flask import render_template, request
from flask.views import MethodView

import requests

from apps.base.models import Page


class HomeView(MethodView):

    def get(self):

        user_ip = request

        # external_ip = requests.get('https://api.ipify.org').text
        user_data = requests.get(f'https://ipinfo.io/?ip={user_ip}').json()
        # country_code = requests.get(endpoint, verify=True).json()
        print(vars(user_ip))

        Page.add_note(user_ip.remote_addr, user_data['ip'], user_data['country'])
        get_all = Page.get_all()
        items = []
        for i in get_all:
            items.append(i)
        return render_template('base.html', info=items)
