

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from flask_wtf import CSRFProtect
from contextlib import contextmanager
from flask_migrate import Migrate


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


login_manager = LoginManager()
db = SQLAlchemy()
csrf = CSRFProtect()
migrate = Migrate()


@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    user = User.query.get(int(user_id))
    return user


login_manager.login_view = 'cms.user+login'
