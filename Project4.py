import random
print("There are 5 numbers in the box. One of them is the winning number.You need to guess that number.Number is between 1 to 10")
trial_number=0
total_guess=0
while trial_number<1000:
    numbers_list=[random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]
    number_user_choose=random.randint(1,10)
    guess=1
    while number_user_choose!=numbers_list[2]:
        guess=guess+1
        number_user_choose=random.randint(1,10)
    total_guess+=guess
    trial_number+=1
Average=int(total_guess/trial_number)
print(Average)