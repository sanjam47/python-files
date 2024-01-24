def expensiveFruit(fruit_stock=''):
    max_price = 0
    max_fruit_name = ''
    for fruit_name, fruit_price in fruit_stock:
        if (fruit_price > max_price):
            max_fruit_name = fruit_name
            max_price = fruit_price
    return (max_price, max_fruit_name)

fruit_stock = [('Apple', 200), ('Banana', 50), ('Cherry', 250), ('Watermelon', 350)]

#Tuple Unpacking from function
fruit_price,fruit_name=expensiveFruit(fruit_stock)

print(fruit_name)
print(fruit_price)
print(expensiveFruit(fruit_stock))
