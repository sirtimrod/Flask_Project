from app import create_app


app = create_app()


@app.teardown_appcontext
def shutdown_session(exception=None):

    """This function closing the session"""

    from db import session
    session.remove()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
