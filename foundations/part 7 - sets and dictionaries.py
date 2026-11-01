#sets
set1 = {"Cat", "Dog", "Pig", "Cow"}
set2 = {"Cat", "Cow", "Rat", "Fish"}

#union
U = set1.union(set2)
print(U)

#intersection
X = set1.intersection(set2)
print(X)

#adding and removing
set1.remove("Cat")
set2.add("Goat")
print(set1)

#dictionaries
customer = {
    "Name":"Thomas",
    "Age":42,
    "products":[{"name": "cream", "price": 12.99}, {"name": "cookies", "price": 5.99}]
}

#accessing key values
print(customer.keys())

#accessing values
print(customer.values())

#accessing from the list
print(customer["products"][0]["name"])