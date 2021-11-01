from flask import render_template, request
from flask.views import MethodView

import ipapi

from apps.base.models import Page


class HomeView(MethodView):

    def get(self):

        ip_inf = ipapi.location()
        external_ip = ip_inf['ip']
        country_code = ip_inf['country']

        if 'HTTP_X_FORWARDED_FOR' in request.environ:
            external_ip = request.environ['HTTP_X_FORWARDED_FOR']
            country_code = ipapi.location(ip=external_ip, output='country')

        Page.add_note(request.remote_addr, external_ip, country_code)
        get_all = Page.get_all()
        items = []
        for i in get_all:
            items.append(i)
        return render_template('base.html', info=items)
