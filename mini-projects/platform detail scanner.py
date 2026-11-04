
username = input("Please enter a suitable username. Username must be longer than 7 characters and should contain at least 1 capital letter and 1 number: ")
condition_count = 0
capital_count = 0
number_count = 0

while condition_count != 1:
  for i in range(len(username)):
    if username[i].isupper():
      capital_count += 1
    if username[i].isnumeric():
      number_count += 1
  if len(username) >= 7 and capital_count > 0 and number_count > 0:
    condition_count = 1
  else:
    print("This username is not suitable. Please try again.")
    username = input("Please enter a suitable username. Username must be longer than 7 characters and should contain at least 1 capital letter and 1 number: ")

print(f"{username} is now your new username on this platform.")
condition_count = 0
email_platforms = ["gmail", "outlook", "yahoo", "bluemailx"]
email = input(f"Please enter your email adress. Be advised, we only use certain email platforms for this website. These include - {email_platforms}. Enter your email ")
while condition_count != 1:
    for i in range(len(email_platforms)):
      if email.endswith(f"{email_platforms[i]}.com"):
        condition_count += 1
        break
    else:
      print("This email is not suitable. Please try again.")
      email = input("Please enter your email adress. Be advised, we only use certain email platforms for this website: ")

print(f"Your email adress for the platform is - {email}.")

password = input("Please enter a suitable password. Password must contain 9 characters, a number, a capital letter and a small letter: ")
password_small_letter, password_capital_letter, password_number, password_length, condition_count = 0, 0, 0, 0, 0
while condition_count != 1:
  for i in range(len(password)):
    if len(password) >= 9:
      password_length = 1
    if password[i].isupper():
      password_capital_letter = 1
    if password[i].islower():
      password_small_letter = 1
    if password[i].isnumeric():
        password_number = 1
  if password_length == 1 and password_capital_letter == 1 and password_small_letter == 1 and password_number == 1:
    condition_count = 1

  else:
    print("This password is not suitable. Please try again.")
    password = input("Please enter a suitable password. Password must contain 9 characters, a number, a lower and upper case letter:")
print(f"Your password for this platform is - {password}.")

skills = []
entries = "x"

while entries != "stop" or len(skills) > 9:
  entries = input("Please enter skills you have: ")
  skills.append(input)

skills_set = set(skills)
print(f"Your skills are - {skills_set}")
  
