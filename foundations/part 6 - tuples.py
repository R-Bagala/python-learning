random_tuple = (2, 4, 5, 6, 67, 89, 123, 453, 543)
digit_count = 0
right_numbers_count = 0
for i in range(len(random_tuple)):
  digit_count = len(str(abs(random_tuple[i])))
  if digit_count > 1:
    right_numbers_count+=1
print(right_numbers_count)
print(random_tuple[7:9])