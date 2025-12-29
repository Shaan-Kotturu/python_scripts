#printing the list contents as is
food = ["Milk", "Soya", "Veggies", "apple","banana"]
print(food[:4])
print(food[1:4])
print(food[2:])
print(food[-1])
print(food[-2:])
print("\n")

#slicing the list - print a subset
print("List of fruits: :")
for food_item in food[-2:]:
    print(food_item.title())
print("\n")

#add,remove 

food.append("carrots")
print(food)
new_food = food[:]
new_food.append("litchie")
print(new_food)
