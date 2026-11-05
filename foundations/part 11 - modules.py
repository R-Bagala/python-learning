from statistics import *
from random import random, randint
import string
def addition(*addition_numbers):
    addition_total = 0
    for i in addition_numbers: 
        addition_total += i
    return addition_total 

def subtraction(*subtraction_numbers):
    subtraction_list = []
    first_number = 0
    for i in subtraction_numbers:      
        subtraction_list.append(i)
    first_number = subtraction_list[0]
    for i in range(1, len(subtraction_list)):
        first_number -= subtraction_list[i]
    return first_number

def calc_mean(*numbers_for_mean):
    mean_list = []
    for i in numbers_for_mean:
        mean_list.append(i)
    return mean(mean_list)

def calc_median(*numbers_for_median):
    median_list = []
    for i in numbers_for_median:
        median_list.append(i)
    return median(median_list)

def calc_mode(*num_for_mode):
    mode_list = []
    for i in num_for_mode:
        mode_list.append(i)
    return mode(mode_list)

def calc_stdev(*num_for_stdev):
    stdev_list = []
    for i in stdev:
        stdev_list.append(i)
    return stdev(stdev_list)
    
def user_id_gen_by_user():
    new_id = ""
    items = string.ascii_letters + string.digits
    characters = []
    password_count = 0
    amount = int(input("Please enter the number of user IDs you which to generate: "))
    size_of_ID = int(input("Please enter how long you want each password to be: "))
    for i in items:
        characters.append(i)    
    while password_count < amount:
        new_id += characters[randint(0, (len(characters)-1))]
        if len(new_id) == size_of_ID:
            print(new_id)
            password_count += 1
            new_id = ""
        
    
        


  

        


            
