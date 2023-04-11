const messageForm = document.getElementById('message-form');

messageForm.addEventListener('submit', (event) => {
    event.preventDefault();
  
    const recipient = document.getElementById('recipient_username').value;
    const content = document.getElementById('content').value;
  
    console.log(recipient)

  
  
    fetch('/send_message', {
      method: 'POST',
      body: JSON.stringify({
        recipient_username: recipient,
        content: content
      }),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
  
      updateMessages(recipient);
  
      // Clear the input box after sending the message
      document.getElementById('content').value = '';
  
      // Clear the existing messages in the message list
      const messagesWrapper = document.querySelector('.previous-messages-wrapper');
      messagesWrapper.innerHTML = '';
  
      // Update the message list with the new translated messages
      data.messages.forEach(message => {
        const messageBubble = document.createElement('div');
        messageBubble.classList.add('bubble');
        if (message.sent_by_current_user) {
          messageBubble.classList.add('sent', 'user1');
        } else {
          messageBubble.classList.add('received', 'user2');
        }
        messageBubble.textContent = message.content;
        messagesWrapper.appendChild(messageBubble);
      });
      scrollToBottom()
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  });

  
  

function updateMessages(recipient) {
    fetch('/fetch_messages', {
      method: 'POST',
      body: JSON.stringify({
        recipient_username: recipient,
      }),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => {
      // Clear the existing messages in the message list
      const messagesWrapper = document.querySelector('.previous-messages-wrapper');
      messagesWrapper.innerHTML = '';
  
      // Update the message list with the new translated messages
      data.messages.forEach(message => {
        const messageBubble = document.createElement('div');
        messageBubble.classList.add('bubble');
        if (message.sent_by_current_user) {
          messageBubble.classList.add('sent', 'user1');
        } else {
          messageBubble.classList.add('received', 'user2');
        }
        messageBubble.textContent = message.content;
        messagesWrapper.appendChild(messageBubble);
      });
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  }




const languageSelect = document.getElementById('language-select');

languageSelect.addEventListener('change', (event) => {
  event.preventDefault();
  
  const selectedLanguage = event.target.value;

  fetch('/update_preferred_language', {
    method: 'POST',
    body: JSON.stringify({
      language: selectedLanguage,
    }),
    headers: {
      'Content-Type': 'application/json',
    },
  })
  .then((response) => {
    if (response.ok) {
      console.log('Preferred language updated successfully');
      // You can also reload or refresh the messages if needed.
    } else {
      console.error('Error updating preferred language');
    }
  })
  .catch((error) => {
    console.error('Error:', error);
  });
});


const initialRecipient = document.querySelector('.recipient-select').value;
if (initialRecipient) {
  updateMessages(initialRecipient);
}

setInterval(() => {
    const currentRecipient = document.querySelector('.recipient-select').value;
    if (currentRecipient) {
      updateMessages(currentRecipient);
    }
  }, 5000);


  function scrollToBottom() {
    const messagesWrapper = document.querySelector('.previous-messages-wrapper');
    messagesWrapper.scrollTop = messagesWrapper.scrollHeight;
}

// Define a function to handle the friend list item click event
function handleFriendListItemClick(event) {
  // Get the friend's username from the list item
  const username = event.target.textContent.trim();

  // Set the recipient dropdown value to the friend's username
  const recipientDropdown = document.querySelector('.recipient-select');
  recipientDropdown.value = username;

  // Call the updateMessages() function with the new recipient value
  updateMessages(username);
}

// Get all the friend list items
const friendListItems = document.querySelectorAll('.friends-list li');

// Loop through each list item and add a click event listener
friendListItems.forEach((item) => {
  item.addEventListener('click', handleFriendListItemClick);
});


