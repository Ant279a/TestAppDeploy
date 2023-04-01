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

  const recipientDropdown = document.querySelector('.recipient-select');
recipientDropdown.addEventListener('change', (event) => {
  event.preventDefault();
  updateMessages(event.target.value);
});

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

