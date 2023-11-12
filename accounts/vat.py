# def get_vat():
#     vat = 6
#     try:
#         value = float(input("Enter figure to get VAT: "))
#         equation = float(value) / float(vat)
#         return equation
#     except ValueError:
#         return 'Please enter a number'
    

# def add_vat():
#     vat = 1.2
#     try:
#         value = float(input("Enter number to add vat: "))
#         equation = float(value) * float(vat)
#         return equation
#     except ValueError:
#         return 'There was an error'
    
# def remove_vat():
#     vat = 1.2
#     try:
#         value = float(input("Enter a number to remove VAT: "))
#         equation = float(value) / float(vat)
#         return equation
#     except ValueError:
#         return "There was an error"
    

class VATCalculator:
    def __init__(self):
        self.vat_rate = 0.2  # Default VAT rate (20%)
        self.discount = 0.05
    def set_vat_rate(self, rate):
        self.vat_rate = rate
    def find_vat(self, value):
        try:
            value = float(value)
            vat_amount = value * self.vat_rate
            return f"The VAT is {vat_amount}"
        except ValueError:
            return 'Please enter a number'
    def add_vat(self, value):
        try:
            value = float(value)
            total_with_vat = value + (value * self.vat_rate)
            return f"Adding VAT to {value} equals {total_with_vat}"
        except ValueError:
            return 'There was an error'
    def remove_vat(self, value):
        try:
            value = float(value)
            value_excluding_vat = value / (1 + self.vat_rate)
            return f"Removing VAT from {value} equals {value_excluding_vat}"
        except ValueError:
            return 'There was an error'
    

# Usage example:
vat_calculator = VATCalculator()
vat_calculator.set_vat_rate(0.06)  # Set a custom VAT rate (6%)

value = input("Enter a value: ")
vat_amount = vat_calculator.get_vat(value)
print(f"VAT Amount: {vat_amount}")
