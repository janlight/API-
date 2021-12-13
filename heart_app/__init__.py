from flask import Flask



def create_app():
    app = Flask(__name__)
    from heart_app.routes import home_routes
    from heart_app.routes import main_routes
    from heart_app.routes import predict_routes
    from heart_app.routes import map_routes
    from heart_app.routes import search_routes
    from heart_app.routes import db_routes
    app.register_blueprint(predict_routes.bp)
    app.register_blueprint(home_routes.bp)
    app.register_blueprint(map_routes.bp)
    app.register_blueprint(main_routes.bp)
    app.register_blueprint(search_routes.bp)
    app.register_blueprint(db_routes.bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()