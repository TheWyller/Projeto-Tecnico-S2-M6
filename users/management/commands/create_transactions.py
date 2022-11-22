from django.core.management.base import BaseCommand
from transactions.models import Transaction
import ipdb

transactions_list = [
    {
        "type": 1,
        "description": "Débito",
        "nature": "Entrada",
        "sinal": "+",
    },
    {
        "type": 2,
        "description": "Boleto",
        "nature": "Saída",
        "sinal": "-",
    },
    {
        "type": 3,
        "description": "Financiamento",
        "nature": "Saída",
        "sinal": "-",
    },
    {
        "type": 4,
        "description": "Crédito",
        "nature": "Entrada",
        "sinal": "+",
    },
    {
        "type": 5,
        "description": "Recebimento Empréstimo",
        "nature": "Entrada",
        "sinal": "+",
    },
    {
        "type": 6,
        "description": "Vendas",
        "nature": "Entrada",
        "sinal": "+",
    },
    {
        "type": 7,
        "description": "Recebimento TED",
        "nature": "Entrada",
        "sinal": "+",
    },
    {
        "type": 8,
        "description": "Recebimento DOC",
        "nature": "Entrada",
        "sinal": "+",
    },
    {
        "type": 9,
        "description": "Aluguel",
        "nature": "Saída",
        "sinal": "-",
    }
]


class Command(BaseCommand):
    help = 'Populate types list'

    def handle(self, *args, **kwargs):
        for transaction_type in transactions_list:
            # ipdb.set_trace()
            Transaction.objects.get_or_create(**transaction_type)
