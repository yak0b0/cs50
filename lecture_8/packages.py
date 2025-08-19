class Package:
    def __init__(self, sender, reciever, weight, number):
        self.number = number
        self.sender = sender
        self.reciever = reciever
        self.weight = weight

    def __str__(self):
        return f"Package nr {self.number}, from {self.sender} to {self.reciever}, weighs {self.weight} KG"

    def calculate_cost(self, cost_per_kg):
        return float(self.weight * cost_per_kg)


def main():
    packages = [
        Package(sender="Alice", reciever="Bob", weight=10, number=1),
        Package(sender="Bob", reciever="Charlie", weight=5, number=2)
    ]
    for package in packages:
        print(f"{package} costs ${package.calculate_cost(10)} USD")


main()
