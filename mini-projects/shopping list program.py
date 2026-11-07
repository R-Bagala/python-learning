#shopping list program
shopping_list = []
extra_items = []
response = input("Do you want to go shopping? Type yes or no: ")

if response == "yes":
  items = int(input("How many items do you want to add to your shopping list? Enter: "))
  for i in range(items):
    shopping = input("Enter the product you would like to purchase: ")
    shopping_list.insert(i, shopping)

elif response == "no":
  print("Have a niced day: ")

else:
  print("invalid response")

new_response = input("Do you want to add extra items to your list? Type yes or no: ")

if new_response == "no":
  print(f"here is your complete shopping list: {shopping_list}")

elif new_response == "yes":
  more_items = int(input("How many items do you want to add to your shopping list? Enter:"))
  for i in range(more_items):
    extra_shopping = input("Please enter the name of the item you want to add: ")
    extra_items.insert(i, extra_shopping)

  shopping_list += extra_items
  print(f"here is your complete shopping list: {shopping_list}")

else:
  print(f"invalid response. Here is your shopping list: {shopping_list} ")