import datetime as dt

from marshmallow import Schema, fields

#Superclasse para lancamentos de entrada e saida.
class Transaction(object):
  def __init__(self, id, description, amount, type):
    self.id = id
    self.description = description
    self.amount = amount
    self.created_at = dt.datetime.now()
    self.type = type

#__repr__ retorna uma string legivel do objeto - util para serializacao e debug
  def __repr__(self):
    return '<Transaction(name={self.description!r})>'.format(self=self)

#Schema para facilitar a serializacao para json - 'Schema' e definido no pacote Marshmallow
class TransactionSchema(Schema):
  id = fields.Int()
  description = fields.Str()
  amount = fields.Number()
  created_at = fields.Date()
  type = fields.Str()
