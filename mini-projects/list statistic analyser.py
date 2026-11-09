#This program takes a list and calculates several statistics such as mean, median and standard deviation. List can only have between 5 and 12 values
import math
import sys
new_list = []

while True:
  try:
      new_value = float(input("Please enter a new value to add to your list. List can only hold a minimum of 5 and maximum of 12 values. Enter 00 if you are finished: "))
      if new_value == 00:
        if len(new_list) < 5:
          print("List must have a minimum of 5 values: ")
        else:
          break
      else:
        new_list.append(new_value)
      if len(new_list) == 12:
        break
        
  except ValueError:
    new_value = float(input("Incorrect input. Please enter a new value to add to your list. List can only hold a maximum of 10 values. Enter 00 if you are finished: "))
    new_list.append(new_value)
    if len(new_list) == 12:
      break
    elif new_value == 00:
      new_list.remove(00)
      break

print(f"This is your list which you will perform statistical analysis on: {new_list}.")

print("(1): mean, (2): median, (3): mode, (4): range, (5): variance, (6): standard deviation")
    
def calculate_mean():
  total = 0
  for i in range(len(new_list)):
    total += new_list[i]
  mean = total / len(new_list)
  return mean
    
def calculate_median():
  sorted_list = sorted(new_list)
  n = len(sorted_list)
  if n % 2 != 0:
    return sorted_list[n//2]
  else:
    return(sorted_list[n//2 - 1] + sorted_list[n//2]) / 2

def calculate_mode():
  counting_position = 0
  mode_count = 0
  modes = []
  for i in range(len(new_list)):
    current_value = new_list[counting_position]
    current_count = new_list.count(current_value)
    if current_count > mode_count:
      mode_count = current_count
    counting_position += 1
  if mode_count == 1:
    return "no mode as all values occur once"
  counting_position = 0
  for i in range(len(new_list)):
    current_value = new_list[counting_position]
    current_count = new_list.count(current_value)
    if current_count == mode_count and current_value not in modes:
      modes.append(current_value)
    counting_position += 1
  if len(modes)==1:
    return modes[0]
  return modes
     
def calculate_range():
  return max(new_list) - min(new_list)

def calculate_variance():
  variance_total = 0
  squared_total = 0
  for i in range(len(new_list)):
    variance_total += new_list[i]
    squared_total += new_list[i]**2
  variance = (squared_total - (variance_total**2 / len(new_list))) / (len(new_list) - 1)
  return variance

def calculate_SD():
  return math.sqrt(calculate_variance())

while True:
  try:

    calculation = int(input("Choose a calculation. Press 0 to stop: "))

    if calculation == 0:
      print("Closing Program")
      break 
    elif calculation == 1:
      result = calculate_mean()
      print(f"The mean of your list is: {result}")
    elif calculation == 2:
      result = calculate_median()
      print(f"The median of your list is: {result}")
    elif calculation == 3:
      result = calculate_mode()
      print(f"The mode of your list is: {result}")
    elif calculation == 4:
      result = calculate_range()
      print(f"The range of your list is: {result}")
    elif calculation == 5:
      result = calculate_variance()
      print(f"The variance of your list is: {result}")
    elif calculation == 6:
      result = calculate_SD()
      print(f"The standard deviation of your list is: {result}")
    else:
      print("Input is not acceptable.")

  except ValueError:
    calculation = int(input("Please enter a suitable input"))