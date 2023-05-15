#1

num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the firsecondst number: '))
print(f"Absolute value of {num_1} - {num_2} is {abs(num_1 - num_2)}")

#2

product_price = round(float(input("Enter the price of a product: ")), 2)
delivery_cost = product_price * 0.03
print(f"The cost of delivery is {delivery_cost}")
final_price = round(product_price + delivery_cost)
print(f"The final price of the product including delivery is {final_price}")