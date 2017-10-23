import json

from flask import request
from flask_restful import Resource, Api

from core.adapters import TransferAdapter
from db.repository import TransferRepository


class TransferResource(Resource):
    default_length = 100

    def __init__(self, *args, **kwargs):
        self.super().__init__(*args, **kwargs)
        self.adapter = TransferAdapter(TransferRepository())

    def get(self, number=None):
        if number:
            return self.get_one(number)
        return self.get_list()

    def get_one(self, number):
        invoice = self.adapter.get_list({'number': number})
        return json.dumps(invoice)

    def get_list(self):
        invoices = self.adapter.get_list()
        return json.dumps(invoices)


api = Api()
api.add_resource(TransferResource, '/transfers/<int:number>', '/transfers')