from flask import Flask, request, render_template, jsonify
from currency_converter import CurrencyConverter
c = CurrencyConverter()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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

converted_amount = c.convert(100, 'USD', 'EUR')
print(f"100 USD = {converted_amount} EUR")