class ForexPairsGenerator:
    def __init__(self, base_currencies=None, quote_currencies=None):
        """
        Initialize the ForexPairsGenerator with optional base and quote currencies.
        :param base_currencies: List of base currencies. Defaults to ["USD", "EUR", "GBP", "JPY"].
        :param quote_currencies: List of quote currencies. Defaults to ["USD", "EUR", "GBP", "JPY"].
        """
        self.base_currencies = base_currencies or ["USD", "EUR", "GBP", "JPY"]
        self.quote_currencies = quote_currencies or ["USD", "EUR", "GBP", "JPY"]

    def generate_pairs(self):
        """
        Generate forex pairs from the base and quote currencies.
        :return: List of forex pairs.
        """
        return [f"{base}_{quote}" for base in self.base_currencies for quote in self.quote_currencies if base != quote]
