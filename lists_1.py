
guests=["Kunal","Ravi","Rohan"]
#print(f"Hi {guests[0]},{guests[1]},{guests[2]} I cordially invite you to my house warming ceremony. I would be happy to have you along with your family")
p=guests.pop(0)
guests.append("Amar")
#print(f"Unfortunately,{p} would not be able to join due to personal reasons")
#print(f"Hi {guests[0]},{guests[1]},{guests[2]} I cordially invite you to my house warming ceremony. I would be happy to have you along with your family")

guests.insert(0,"Vishnu")
guests.insert(3,"Arun")
guests.append("Kiran")
print("Guests Invited: ")
print(guests) 

print("\nSorry, I can invite only 2 people for the dinner")
while len(guests)>2:
    a=guests.pop()
    print(f"Sorry {a},our table is full")

print("\nGuests still invited:")
for guest in guests:
    print(f"{guest}, you are still invited")

del guests[0:2]
print(guests)

