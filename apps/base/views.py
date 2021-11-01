from flask import render_template, request
from flask.views import MethodView

import requests

from apps.base.models import Page
from scripts import scripts
import config


class HomeView(MethodView):

    def get(self):

        ip_inf = scripts.get_ip_inf()
        external_ip = ip_inf['ip']
        country_code = ip_inf['country']

        if 'HTTP_X_FORWARDED_FOR' in request.environ:
            external_ip = request.environ['HTTP_X_FORWARDED_FOR']
            country_code = scripts.get_ip_inf(external_ip)

        Page.add_note(request.remote_addr, external_ip, country_code)
        get_all = Page.get_all()
        items = []
        for i in get_all:
            items.append(i)
        return render_template('base.html', info=items)
