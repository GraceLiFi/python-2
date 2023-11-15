from dataclasses import dataclass

@dataclass
class Invoice:
    invoice_id: str
    user_id: str
    amount: str
    paid: str

    @staticmethod
    def convert_data(data):
        invoices = []

        for list in data:
            d = [list.strip() for field in list.split(',')]
            invoice = Invoice(*d)
            invoices.append(invoice)
        return invoices