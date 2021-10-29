from flask import render_template, request
from flask.views import MethodView

import requests

from apps.base.models import Page
from scripts import scripts
import config


class HomeView(MethodView):

    def get(self):

        user_data = request
        external_ip = requests.get(config.EXTERNAL_IP_URL).text
        country_code = scripts.get_country_code(external_ip)

        if 'HTTP_X_FORWARDED_FOR' in user_data.environ:
            external_ip = user_data.environ['HTTP_X_FORWARDED_FOR']
            country_code = scripts(external_ip)

        Page.add_note(user_data.remote_addr, external_ip, country_code)
        get_all = Page.get_all()
        items = []
        for i in get_all:
            items.append(i)
        return render_template('base.html', info=items)
