// This part of the code handles the member creation form submission
let memberForm = document.getElementById('member-form');

memberForm.addEventListener('submit', (e) => {
    e.preventDefault();
    console.log('Member form was submitted');

    let memberData = {
        'title': memberForm.title.value,
        'body': memberForm.body.value
    };

    console.log('MEMBER FORM DATA:', memberData);

    // Fetch call to create a new member
    fetch('http://127.0.0.1:8000/api/members/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}` // Include JWT token in the Authorization header
        },
        body: JSON.stringify(memberData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('NEW MEMBER DATA:', data);
        // Handle response data as needed
        window.location.href = 'http://127.0.0.1:8000/';
    })
    .catch(error => {
        console.error('Error creating member:', error);
    });
});
