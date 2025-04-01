
let convertButton = document.getElementById("convertButton");
convertButton.addEventListener("click", function() {
 
    let amount = document.getElementById('amount').value;
    let from_currency = document.getElementById('from').value;
    let to_currency = document.getElementById('to').value;

    if (amount == "") {
        alert("Please enter an amount to convert.");
        return;
    }

    fetch('/exchange', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ amount, from_currency, to_currency })
    })
    .then(response => response.json())
    .then(data => {
        if (data.converted_amount) {
            document.getElementById('result').value = to_currency + ": " + data.converted_amount;
        } else {
            document.getElementById('result').innerText = "Error: " + data.error;
        }
    })
    .catch(error => console.error('Error:', error));



})