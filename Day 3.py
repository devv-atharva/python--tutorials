print("Salary Calculator")

# Taking input

name = ("Chinmay Ghayal")
basic_salary = (25000)
bonus = (10000)
tax_percent = 35 / 100


# Expressions

gross_salary = basic_salary + bonus
tax_amount = (gross_salary * tax_percent) / 100
net_salary = gross_salary - tax_amount


# Output

print("Salary Details")
print("Employee Name: ", name)
print("Gross Salary: ", gross_salary)
print("Tax Amount: ", tax_amount)
print("Net Salary: ", net_salary)


print(type(name))
print(type(basic_salary))
print(type(bonus))
print(type(tax_percent))
print(type(net_salary))
