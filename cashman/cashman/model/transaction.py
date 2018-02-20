import datetime as dt

from marshmallow import Schema, fields

#Superclasse para lançamentos de entrada e saída.
class Transaction(object):
  def __init__(self, description, amount, type):
    self.description = description
    self.amount = amount
    self.created_at = dt.datetime.now()
    self.type = type

#__repr__ retorna uma string legivel do objeto - util para serialização e debug
  def __repr__(self):
    return '<Transaction(name={self.description!r})>'.format(self=self)

#Schema para facilitar a serialização para json - 'Schema' é definido no pacote Marshmallow
class TransactionSchema(Schema):
  description = fields.Str()
  amount = fields.Number()
  created_at = fields.Date()
  type = fields.Str()
