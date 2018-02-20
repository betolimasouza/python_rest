from flask import Flask, jsonify, request

from cashman.model.expense import Expense, ExpenseSchema
from cashman.model.income import Income, IncomeSchema
from cashman.model.transaction_type import TransactionType

app = Flask(__name__)


transactions = [
  Income(1, 'Salary', 5000),
  Income(2, 'Dividends', 200),
  Expense(1, 'pizza', 50),
  Expense(2, 'Rock Concert', 100)
]


@app.route('/incomes') #GET receitas
def get_incomes():
  schema = IncomeSchema(many=True)
  incomes = schema.dump( 
    filter(lambda t: t.type == TransactionType.INCOME, transactions)
  )
  return jsonify(incomes.data) 


@app.route('/incomes', methods=['POST']) #POST receitas
def add_income():
  income = IncomeSchema().load(request.get_json()) #JSON -> Dados
  transactions.append(income.data) #Insere dados
  return "", 204 # Codigo de Status HTTP 204 - The server has successfully fulfilled the request


@app.route('/incomes/<int:id>', methods=['DELETE'])
def delete_income(id):
  try:
    #TODO DELETE
    schema = IncomeSchema(many=True)
    incomes = schema.dump( 
    filter(lambda t: t.type == TransactionType.INCOME, transactions)
    )
    
  except ValueError:
    pass
  
  return "", 204


@app.route('/expenses')
def get_expenses():
  #seleciona todas as transacoes com o tipo INCOME
  schema = ExpenseSchema(many=True)
  expenses = schema.dump(
      filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
  )
  return jsonify(expenses.data)


@app.route('/expenses', methods=['POST'])
def add_expense():
  expense = ExpenseSchema().load(request.get_json())
  transactions.append(expense.data)
  return "", 204


if __name__ == "__main__":
    app.run()
