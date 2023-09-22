from __init__ import db, app
from flask_login import LoginManager
from models.user import User

from routes.articles import articles_bp
from routes.users.users import users_bp


app.register_blueprint(users_bp, url_prefix="/api/users")
app.register_blueprint(articles_bp, url_prefix="/api/articles")


if __name__ == "__main__":
    if not app.secret_key:
        print("Secret key not existent")
        exit()
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.run(debug=True)
