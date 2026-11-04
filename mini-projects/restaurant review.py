#restaurant review

feelings = int(input("On a scale of 1-5, how was your experience at this restaurant? "))

while feelings < 1 or feelings > 5:
  print("Please enter a number between 1 and 5.")
  feelings = int(input("On a scale of 1-5, how was your experience at this restaurant? "))


if feelings == 1 or feelings == 2:
  print("We are very sorry to hear that.")
  reasons = input("Can you explain why you didn't like your experience.")
  print("Thank you for sharing your experience.")

elif feelings == 3 or feelings == 4:
  print("thank you for sharing your experience.")
  improvement = input("Can you explain how your experience could have been better? ")
  print("Thank you for sharing your experience.")

else:
  print("Thank you for sharing your experience. We hope you will come again.")
