foods = []
prices = []
total = 0

while True :
    food = input("Enter a food to buy or press q to quit:  ")
    if food.lower() == 'q' :
        break
    else :
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
    
    
        
print("----Your Cart----")
    
for food in foods:
        print(food)
    
for price in prices :
       total += price
       
print(f"Your total is : R{total}")
        
        
        