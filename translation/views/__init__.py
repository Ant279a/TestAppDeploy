from .home_views import home_views
from .profile_views import profile_views
from .translation_views import translation_views
from .authentication_views import authentication_views


def register_blueprints(app):
    app.register_blueprint(home_views)
    app.register_blueprint(profile_views)
    app.register_blueprint(translation_views)
    app.register_blueprint(authentication_views)
