from .home_views import home_views
from .profile_views import profile_views
from .translation_views import translation_views
from authentication_view import auth_bp

def register_blueprints(app):
    app.register_blueprint(home_views)
    app.register_blueprint(profile_views)
    app.register_blueprint(translation_views)
    app.register_blueprint(auth_bp)
