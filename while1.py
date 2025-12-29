available_tops = ['olives','jalepenos','extra cheese','mayo']
current_order = []
print("Today's available toppings are : ")
print(available_tops)
while True:
    a= input("Need extra toppings? what do you prefer? (enter q to quit) : ")
    if a == 'q':
        break
    elif a in available_tops:
        current_order.append(a)
        continue
    elif a not in available_tops:
        print("Sorry! requested toppings not available")
print("Thank you ! Your order is ready with the extra toppings")
print(current_order)

    