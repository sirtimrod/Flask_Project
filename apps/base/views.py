from flask import render_template, request
from flask.views import MethodView

from apps.base.models import Page


class HomeView(MethodView):

    def get(self):
        user_ip = request.remote_addr
        new_note = Page.add_note(str(user_ip))
        # get_all = Page.get_all()
        # items = []
        # for i in get_all:
        #     items.append(i.ip)
        #     print(i.ip)
        # print(items)
        return render_template('base.html', info=new_note)
