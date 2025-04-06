
// let convertButton = document.getElementById("convertButton");
// convertButton.addEventListener("click", function() {
 
//     let amount = document.getElementById('amount').value;
//     let from_currency = document.getElementById('from').value;
//     let to_currency = document.getElementById('to').value;

//     if (amount == "") {
//         alert("Please enter an amount to convert.");
//         return;
//     }

//     fetch('/exchange', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ amount, from_currency, to_currency })
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.converted_amount) {
//             document.getElementById('result').value = to_currency + ": " + data.converted_amount;
//         } else {
//             document.getElementById('result').innerText = "Error: " + data.error;
//         }
//     })
//     .catch(error => console.error('Error:', error));
// })

let submitButton = document.getElementById("submitButton");
submitButton.addEventListener("click", function() {
    let firstname = document.getElementById('firstname').value;
    let lastname = document.getElementById('lastname').value;
    let mobile = document.getElementById('mobile').value;

    if (firstname == "" || lastname == "" || mobile == "") {
        alert("Please fill in all fields.");
        return;
    }

    fetch('/adduser', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ firstname, lastname, mobile })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
        } else {
            alert("Error: " + data.error);
        }
    })
    .catch(error => console.error('Error:', error));
})

// let viewusersButton = document.getElementById("viewUsersButton");
// viewusersButton.addEventListener("click", function() {
//     alert("Fetching user list...");
//     window.location.href = "/userlist.html";
// })

function viewUsers() {
    fetch('/viewusers', {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
    })
    .then(response => response.json())
    .then(data => {
        if (data.users) {
            let usersList = document.getElementById('userTableBody');
            usersList.innerHTML = ""; // Clear previous results
            data.users.forEach(user => {
                let li = document.createElement('li');
                li.textContent = `${user.firstname} ${user.lastname} - ${user.mobile}`;
                usersList.appendChild(li);
            });
        } else {
            alert("Error: " + data.error);
        }
    })
    .catch(error => console.error('Error:', error));
}