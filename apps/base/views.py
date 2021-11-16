from flask import render_template, request, flash
from flask.views import MethodView

from apps.base.models import Page
from scripts import scripts


class HomeView(MethodView):

    def get(self, page):

        if page == 1:
            scripts.get_ip_inf(request)
            flash('Detection of your country code has started, please refresh the page in 20 seconds')

        get_all, prev_url, next_url = Page.get_limit(page)
        items = []
        for i in get_all:
            items.append(i)
        return render_template('base.html', info=items, prev_url=prev_url, next_url=next_url)
