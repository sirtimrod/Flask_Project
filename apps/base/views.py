from flask import render_template, request
from flask.views import MethodView

import requests

from apps.base.models import Page


class HomeView(MethodView):

    def get(self):

        user_data = request
        external_ip = requests.get('https://api.ipify.org').text

        if 'HTTP_X_FORWARDED_FOR' in vars(user_data):
            external_ip = user_data.HTTP_X_FORWARDED_FOR

        country_code = 'RU'

        Page.add_note(user_data.remote_addr, external_ip, country_code)
        get_all = Page.get_all()
        items = []
        for i in get_all:
            items.append(i)
        return render_template('base.html', info=items)
