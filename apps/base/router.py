from apps.base import views


def install(app):
    app.add_url_rule(
        '/',
        defaults={"page": 1},
        view_func=views.HomeView.as_view('home-page')
    )
    app.add_url_rule(
        '/<int:page>',
        view_func=views.HomeView.as_view('home-page-limit')
    )
