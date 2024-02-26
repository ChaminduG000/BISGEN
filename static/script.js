function generateName() {
    const nameInput = document.getElementById('nameInput').value;
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input: nameInput }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('nameOutput').innerText = 'Recommended Business Name: ' + data.response;
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('nameOutput').innerText = 'Error generating name.';
    });
}
