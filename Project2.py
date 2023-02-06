#Hey Mr.Jones,this is Abinash's project for Unit 2
#This code calculates the amount of simple interest which is earned over a certain time at a specific rate. Then, it calculates the total amount of money at the end of time period.
from math import *
#Firstly, I imported this math package which is needed for calculations
print("Hello, world! This is Python 3!")
print("Today we will calculate the simple interest and total amount of money at the time period")
#Line 12 describes what this programs is going to do
Principal_amount=int(input("Firstly,please enter you Principal value:"))
Time_period=int(input("Now please enter the time period for the amount:"))
Rate_of_interest=int(input("Finally, please input the rate of interest:"))
#Line 14,15 and 16 ask the user to input the principal amount, time they keep their money and the rate of interest they get respectively.
Simple_interest=(Principal_amount*Time_period*Rate_of_interest)/(100)
#Line 12 is the operation part. This is the formula for simple interest i.e SI=PTR/100. It multiplies principal, time and rate. Then, divides it by 100
print("Your simple interest is " + str(Simple_interest))
#line 14 prints the amount of simple interest
Total_amount_at_the_time_period= Simple_interest+Principal_amount
#This is the other calculation part. This adds the principal amount and the simple interest earned. That is the total amount at the end of time period
print("Your total amount at the end of time period is " + str(Total_amount_at_the_time_period))
#Line 18 is your total amount at the end of the time period

#Short example of the program above
#Principal=500
#Time_period=3
#Rate_of_interest =7
#Simple_interest=(Principal*Time_period*Rate_of_interest)/(100)
#                = (500*3*7)/100
#                = 105.0
#Now, total amount over time= Principal+Simple_interest
#                           = 500+105.0
#                           = 605.0
