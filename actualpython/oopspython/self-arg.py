class Chai:
    size=150
    def describe(self):
        print(f"This is a {self.size} ml cup of chai")
        
chai1=Chai()
print(chai1.describe())
print(Chai.describe(chai1))