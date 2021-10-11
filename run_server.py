from app import install_app


app = install_app()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
