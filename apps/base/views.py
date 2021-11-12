from flask import render_template, request
from flask.views import MethodView

from apps.base.models import Page
from scripts import scripts


class HomeView(MethodView):

    def get(self, page):

        if page == 1:
            ip_inf = scripts.get_ip_inf(request)
            Page.add_note(request.remote_addr, ip_inf['external_ip'], ip_inf['country_code'])

        get_all, prev_url, next_url = Page.get_limit(page)
        items = []
        for i in get_all:
            items.append(i)
        return render_template('base.html', info=items, prev_url=prev_url, next_url=next_url)
