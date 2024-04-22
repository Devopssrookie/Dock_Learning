let form = document.getElementById('login-form')

form.addEventListener('submit', (e) => {
    e.preventDefault()
    console.log('Form was submitted')

    let formData = {
        'username': form.username.value,
        'password': form.password.value
    }

    console.log('FORM DATA:', formData)

    fetch('http://127.0.0.1:8000/api/users/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // You may need additional headers based on your JWT configuration
        },
        body: JSON.stringify(formData)
    })
        .then(response => response.json())
        .then(data => {
            console.log('DATA:', data.access)
            if (data.access) {
                localStorage.setItem('token', data.access)
                window.location = 'file:///C:/Users/richu/Documents/Practice_Django/frst_proj/frontend/members.html'    
            } else {
                alert('Username OR password did not work')
            }
        })
})
