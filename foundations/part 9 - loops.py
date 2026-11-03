# for loops
names = ["Thomas", "Elliot", "Robert", "Jim"]
jobs = ["Nurse", "Doctor", "Firefighter", "Policeman"]

for name in names:
    print(name)

for job in jobs:
    print(job)

for i in range (len(names)):
    print(f"{names[i]} works as a {jobs[i]}.")

word = "Hello"

for i in range(len(word)):
    print(word[i]) #one character at a time

#writing a sequence
end_number = 300
start = [1]
for i in start:
    start.append(i*2)
    print(i)
    if i > end_number:
        break

prime_list = []
divisible_count = 0
for i in range(100):
    for j in range(i):
        prime_list.append(i+1)
    for h in range(1, (len(prime_list) + 1)):
        if i % h == 0:
            divisible_count += 1
    if divisible_count == 2:
        print("")
    else:
        print(i)

#while loops
temperature = 100
while temperature > 0:
    print(f"{temperature} degrees celcius is still too hot to drink.")
    temperature = temperature - 1
    if temperature < 60:
        print(f"{temperature} degrees celcius is cool enough to drink.")
        break


while True:
    answer = input("What is the answer to life, the universe and everything?")
    if answer != "42":
        print("Nope that is not it")
    else:
        print("Correct, you're awesome")
        break

#above code but with attempts
count = 0
while True:
    answer = input("What is the answer to life, the universe and everything?")
    if answer != "42":
        print("Nope that is not it")
        count = count + 1
        if count > 2:
            print("You have exceeded the number of attemps.")
            break
    else:
        print("Correct, you're awesome")
        break