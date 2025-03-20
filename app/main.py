from flask import Flask, request, jsonify
from app.transactions import process_transaction

app = Flask(__name__)

@app.route('/upi/transaction', methods=['POST'])
def upi_transaction():
    data = request.json
    response = process_transaction(data)
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)

