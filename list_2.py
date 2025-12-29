locations=["Paris","Dubai","Turkey","Bali","Sydney"]
print(locations) # original order
print(sorted(locations)) # sorted- temporary
locations.reverse()  
print(locations) # reversed list
locations.reverse()
print(locations) # back to original list
locations.sort()
print(locations) # sorted permanent
locations.sort(reverse=True)
print(locations)