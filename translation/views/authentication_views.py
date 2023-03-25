from flask import Blueprint, request, redirect, url_for, render_template
from translation.authentication.auth import AuthManager



authentication_views = Blueprint('authentication_views', __name__)
auth_manager = AuthManager()

@authentication_views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        user_name = request.form['user_name']
        password = request.form['password']

        # Register user
        auth_manager.register_user(user_name, password)

        # Redirect to login page
        return redirect(url_for('authentication_views.login'))

    # Render registration form
    return render_template('register.html')

@authentication_views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        user_name = request.form['user_name']
        password = request.form['password']

        # Authenticate user
        authenticated = auth_manager.authenticate_user(user_name, password)

        if authenticated:
            # Redirect to dashboard page
            return redirect(url_for('dashboard'))
        else:
            # Render login form with error message
            return render_template('login.html', error='Invalid username or password')

    # Render login form
    return render_template('login.html')
