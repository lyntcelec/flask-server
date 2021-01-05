from app import create_app
from waitress import serve

if __name__ == "__main__":
    app = create_app()
    if app.config["ENV"] == ".env.production":
        serve(app, host=app.config["BASE_HOST"], port=int(app.config["BASE_PORT"]))
    else:
        app.run(
            host=app.config["BASE_HOST"],
            port=app.config["BASE_PORT"],
            debug=True,
            threaded=True,
        )
