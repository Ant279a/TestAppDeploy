const languageForm = document.getElementById('language-form');

languageForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const selectedLanguage = document.getElementById('language-select').value;

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
        } else {
            console.error('Error updating preferred language');
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
