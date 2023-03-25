from flask import request, redirect, url_for

auth_bp = Blueprint('auth', __name__)
auth_manager = AuthManager()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        user_name = request.form['user_name']
        password = request.form['password']

        # Register user
        auth_manager.register_user(user_name, password)

        # Redirect to login page
        return redirect(url_for('login'))

    # Render registration form
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
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
