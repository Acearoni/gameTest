document.addEventListener('DOMContentLoaded', function() {
    const yesButton = document.getElementById('yesButton');
    const noButton = document.getElementById('noButton');

    if (yesButton && noButton) {
        yesButton.addEventListener('click', function() {
            handleResponse('yes');
        });

        noButton.addEventListener('click', function() {
            handleResponse('no');
        });
    }
});

function handleResponse(response) {
    if (response === 'yes') {
        window.location.href = '/welcome';
    } else if (response === 'no') {
        alert("Come back when you're ready.");
    }
}
