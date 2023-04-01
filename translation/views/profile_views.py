from translation.views.authentication_views import auth_manager
from translation.adapters.memory_repository import MemoryRepository
from flask import Blueprint, render_template, session, request, redirect, url_for, jsonify
from translation.services.translation import translate_text

profile_views = Blueprint("profile_views", __name__)

@profile_views.route('/profile')
def profile():
    # Get the username of the currently logged-in user from the session
    user_id = session.get('user_id')
    print(f"User is in session their id is {user_id}")
    if user_id is None:
        # User is not logged in, redirect to login page
        return redirect('/login')
    

    # Get the user from the repository using the username
    memory_repo: MemoryRepository = auth_manager.get_repository()
    user = memory_repo.get_user_by_id(user_id)
    
    # Get the recipient's username from the request form data
    recipient_username = request.form.get('recipient_username')

    # Retrieve the recipient from the repository using their username
    recipient = memory_repo.get_user(recipient_username)

    # Retrieve the previous messages between the sender and recipient
    messages = []
    if recipient is not None:
        messages = memory_repo.fetch_messages(sender_id, recipient.user_id, sender_lang)


    # Render the profile page with the user information and previous messages
    return render_template('profile.html', user=user, messages=messages)


@profile_views.route('/add_friend', methods=['POST'])
def add_friend():
    friend_username = request.form['friend_username']
    memory_repo: MemoryRepository = auth_manager.get_repository()
    user_id = session.get('user_id')
    user = memory_repo.get_user_by_id(user_id)
    friend = memory_repo.get_user_by_username(friend_username)

    if user is None:
        return redirect('/home')

    if friend and friend != user:
        user.add_friend(friend)
        memory_repo.update_user(user)

    return redirect(url_for('profile_views.profile'))




@profile_views.route('/remove_friend', methods=['POST'])
def remove_friend():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect('/login')

    friend_username = request.form['friend_username']
    memory_repo: MemoryRepository = auth_manager.get_repository()
    user = memory_repo.get_user_by_id(user_id)
    friend = memory_repo.get_user_by_username(friend_username)

    if friend is not None and friend in user.friends:
        user.friends.remove(friend)
        memory_repo.update_user(user)

    return redirect(url_for('profile_views.profile'))

@profile_views.route('/send_message', methods=['POST'])
def send_message():
    # Get sender and recipient information from session
    sender_id = session['user_id']
    sender_username = session['user_name']

    # Get recipient_username and content from JSON data
    data = request.get_json()
    recipient_username = data['recipient_username']
    content = data['content']


    # Get recipient information from repository
    memory_repo: MemoryRepository = auth_manager.get_repository()
    recipient = memory_repo.get_user_by_username(recipient_username)
    if recipient is None:
        return jsonify({'error': 'Recipient not found'})

    # Fetch all messages between sender and recipient from repository
    sender_lang = memory_repo.get_user_by_id(sender_id).preferred_language
    recipient_lang = recipient.preferred_language

    memory_repo.send_message(sender_id, recipient.user_id, content, sender_lang, recipient_lang)
    
    messages = memory_repo.fetch_messages(sender_id, recipient.user_id, sender_lang)

    messages_data = [{
        'content': message.content,
        'sent_by_current_user': message.sender_id == sender_id
    } for message in messages]


    return jsonify({'success': 'Message sent', 'messages': messages_data})



@profile_views.route('/update_preferred_language', methods=['POST'])
def update_preferred_language():
    # Get the ID of the currently logged-in user from the session
    user_id = session.get('user_id')
    if user_id is None:
        # User is not logged in, redirect to login page
        return redirect('/login')

    # Get the new preferred language from the request data
    data = request.get_json()
    new_language = data['language']

    # Get the user from the repository using the user ID
    memory_repo: MemoryRepository = auth_manager.get_repository()
    user = memory_repo.get_user_by_id(user_id)

    # Update the user's preferred language
    user.preferred_language = new_language
    memory_repo.update_user(user)

    return jsonify({'success': 'Preferred language updated'})


@profile_views.route('/fetch_messages', methods=['POST'])
def fetch_messages():
    # Get sender and recipient information from session and form data
    sender_id = session['user_id']
    data = request.get_json()
    recipient_username = data['recipient_username']

    # Get recipient information from repository
    memory_repo: MemoryRepository = auth_manager.get_repository()
    recipient = memory_repo.get_user_by_username(recipient_username)
    if recipient is None:
        return jsonify({'error': 'Recipient not found'})

    # Fetch all messages between sender and recipient from repository
    sender_lang = memory_repo.get_user_by_id(sender_id).preferred_language
    recipient_lang = recipient.preferred_language
    messages = memory_repo.fetch_messages(sender_id, recipient.user_id, sender_lang)

    # Prepare the translated messages for the JSON response
    messages_data = [{
        'content': message.content,
        'sent_by_current_user': message.sender_id == sender_id
    } for message in messages]

    # Return a JSON response with the translated messages
    return jsonify({'messages': messages_data})