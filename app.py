from flask import Flask, request, render_template, jsonify
from currency_converter import CurrencyConverter
from connection import get_connection,insert_data, fetch_data
c = CurrencyConverter()
app = Flask(__name__)

conn = get_connection()
# insert_data(conn, 'John', 'Doe', '1234567890')
# print(fetch_data(conn))

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/viewusers')
def viewusers():
    data = fetch_data(conn)
    return jsonify(data)

@app.route('/userlist')
def userlist():
    return render_template('userlist.html')

@app.route('/adduser', methods=['POST'])
def add_user():
    try:
        # Ensure the request contains JSON data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON format"}), 400

        # Extract values safely
        firstname = data.get('firstname', '')
        lastname = data.get('lastname', '')
        mobile = data.get('mobile', '')

        if not firstname or not lastname or not mobile:
            return jsonify({"error": "Missing required fields"}), 400

        # Insert data into the database
        insert_data(conn, firstname, lastname, mobile)
        return jsonify({"message": "User added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/exchange', methods=['POST'])
def exchange():
    try:
        # Ensure the request contains JSON data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON format"}), 400

        # Extract values safely
        amount = float(data.get('amount', 0))
        from_currency = data.get('from_currency', '').upper()
        to_currency = data.get('to_currency', '').upper()

        if not amount or not from_currency or not to_currency:
            return jsonify({"error": "Missing required fields"}), 400

        converted_amount = c.convert(amount, from_currency, to_currency)
        return jsonify({"converted_amount": converted_amount})

    except ValueError:
        return jsonify({"error": "Invalid amount"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

# converted_amount = c.convert(100, 'USD', 'EUR')
# print(f"100 USD = {converted_amount} EUR")