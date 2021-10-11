from apps.base import views


def install(app):
    app.add_url_rule(
        '/',
        view_func=views.HomeView.as_view('home-page')
    )
