# Valut xD

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} G, {self.sickles} S, {self.knuts} K"

    def __add__(self, other):  # overloaded operator to add two vaults together
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)


weasly = Vault(25, 50, 100)
print(weasly)

galleons = potter.galleons + weasly.galleons
sickles = potter.sickles + weasly.sickles
knuts = potter.knuts + weasly.knuts

total = potter + weasly
print(total)
