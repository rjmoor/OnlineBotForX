# forex_pairs.py
class ForexPairsGenerator:
    def __init__(self):
        self.base_currencies = ["USD", "EUR", "GBP", "JPY"]
        self.quote_currencies = ["USD", "EUR", "GBP", "JPY"]

    def generate_pairs(self):
        pairs = []
        for base in self.base_currencies:
            for quote in self.quote_currencies:
                if base != quote:
                    pairs.append(f"{base}_{quote}")
        return pairs
