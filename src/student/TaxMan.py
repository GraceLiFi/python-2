class TaxMan:
    def __init__(self, items, tax):
        self.items = items
        self.tax = tax
        self._total = 0
    def calc_total(self):
        tax_rate = float(self.tax.strip('%')) / 100

        for item in self.items:
            price = item['price']
            self._total += price + price * tax_rate
            self._total = round(self._total, 2)
    def get_total(self):
        return self._total
        
