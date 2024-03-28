document.getElementById('sketchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const feature = document.getElementById('feature').value;
    const description = document.getElementById('description').value;

    fetch('/add_feature', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ feature, description }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('sketchDisplay').innerHTML = data.sketch_html;
    })
    .catch(error => console.error('Error:', error));
});
