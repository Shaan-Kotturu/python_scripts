
available_toppings = ["mushrooms","olives","jalepino","extra cheese","extra mayo"]
requested_topping = []

while True:
    topping = input("Enter another topping you like (or type 'quit' to finish): ")
    if topping == "quit":
        break
    requested_topping.append(topping)
    

for topping in requested_topping:
    if topping in available_toppings:
        print(f"Adding {topping} to your Pizza !")
    else:
        print(f"{topping} not available")
print("Thank you for ordering. Your Pizza is ready!")