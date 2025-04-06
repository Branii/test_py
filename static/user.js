

function viewUsers() {
    fetch('/viewusers', {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
    })
    .then(response => response.json())
    .then(data => {
        if (data) {
            let usersList = document.getElementById('userTableBody');
            usersList.innerHTML = ""; // Clear previous results
            let html = "";
            data.forEach(user => {
                html += `<tr><td>${user.uid}</td><td>${user.firstname}</td><td>${user.lastname}</td><td>${user.mobile}</td></tr>`;
            });
            usersList.innerHTML = html;
        }
    })
    .catch(error => console.error('Error:', error));
}
viewUsers();