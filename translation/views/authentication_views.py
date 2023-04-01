from flask import Blueprint, request, redirect, url_for, render_template, session
from translation.authentication.auth import AuthManager


authentication_views = Blueprint('authentication_views', __name__)
auth_manager = AuthManager()

@authentication_views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        user_name = request.form['user_name']
        password = request.form['password']

        print(f"Username in register is: {user_name}")
        print(f"Pasword in register is: {password}")

        # Register user
        auth_manager.register_user(user_name, password)
        print(auth_manager.get_repository().get_user(user_name))

        # Redirect to login page
        return redirect(url_for('authentication_views.login'))

    # Render registration form
    return render_template('register.html')

@authentication_views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check which button was clicked
        if 'user_a' in request.form:
            user_name = "a"
            password = "user_a_password"
            auth_manager.register_user(user_name, password)
        elif 'user_b' in request.form:
            user_name = "b"
            password = "user_b_password"
            auth_manager.register_user(user_name, password)
        

        # Authenticate user
        authenticated, user_id = auth_manager.authenticate_user(user_name, password)

        if authenticated:
            # Set the session for the user
            session['user_id'] = user_id
            session['user_name'] = user_name

            # Redirect to dashboard page
            return redirect(url_for('profile_views.profile'))
        else:
            # Render login form with error message
            return render_template('login.html', error='Invalid username or password')

    # Render login form
    return render_template('login.html')