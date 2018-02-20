from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = [
  { 'description': 'salary', 'amount': 5000 }
]

#GET
@app.route('/incomes') #registra a view
def get_incomes():
  return jsonify(incomes)

#POST
@app.route('/incomes', methods=['POST'])
def add_income():
  incomes.append(request.get_json())
  return '', 204