class ForexPairsGenerator:
    def __init__(self):
        self.currencies = [
            "USD", "EUR", "JPY", "GBP", "CHF", "CAD", "AUD", "NZD"
        ]

    def generate_pairs(self):
        pairs = []
        for i in range(len(self.currencies)):
            for j in range(i + 1, len(self.currencies)):
                pairs.extend([f"{self.currencies[i]}_{self.currencies[j]}", f"{self.currencies[j]}_{self.currencies[i]}"])
        return pairs

# Example usage
if __name__ == "__main__":
    generator = ForexPairsGenerator()
    pairs = generator.generate_pairs()
    print("Generated Forex Pairs:")
    for pair in pairs:
        print(pair)
