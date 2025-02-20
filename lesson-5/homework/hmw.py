#task 1


# def convert_cel_to_far(celsius):
#     return (celsius*9)/5 + 32
# def convert_far_to_cel(far):
#     return (far - 32)*5/9

# a = float(input("Enter a temperature in degrees F: "))
# b = round((convert_far_to_cel(a)), 2)
# print(f"{a} degrees F = {b} degrees C")
# c = float(input("Enter a temperature in degrees C: "))
# d = round((convert_cel_to_far(c)), 2)
# print(f"{c} degrees C = {d} degrees F")


#task 2
# def invest(amount, rate, years):
#      for i in range(1,years+1):
#         amount = amount * (1 + rate / 100)
#         print(f"Year {i}: {amount:.2f}")

# amount=int(input("enter the amount u wanna deposit: "))
# rate=int(input("enter yearly interest rates: "))
# years=int(input("enter the number of years: "))
# invest(amount,rate,years)

#task3

# def factors(num):
#     for i in range(1,num+1):
#         if num%i==0:
#             print(f" {i} is a factor of {num}")


# num=int(input("enter a positive number: "))
# factors(num)


#task 4
# def  enrollment_stats(univer):
#     fees = []
#     totals = []
#     for item in univer:
#         university, total, fee = item
#         totals.append(total)
#         fees.append(fee)
#     return totals, fees

# def mean(list1):
#     return (sum(list1))/(len(list1))

# def meadian(list2):
#     if len(list2) % 2 == 1:
#         return((sorted(list2))[len(list2)//2])
#     else:
#         return (((sorted(list2))[len(list2)//2]) + ((sorted(list2))[len(list2)//2-1]))/2

# universities = [
#     ['California Institute of Technology', 2175, 37704],
#     ['Harvard', 19627, 39849],
#     ['Massachusetts Institute of Technology', 10566, 40732],
#     ['Princeton', 7802, 37000],
#     ['Rice', 5879, 35551],
#     ['Stanford', 19535, 40569],
#     ['Yale', 11701, 40500]
# ]
# num_students, tuitions = enrollment_stats(universities)
# student_mean = round(mean(num_students), 2)
# student_median = meadian(num_students)
# tuition_mean = round(mean(tuitions), 2)
# tuition_median = meadian(tuitions)
# print("******************************")
# print(f"Total students: {sum(num_students)}")
# print(f"Total tuition: $ {sum(tuitions)}")
# print("")
# print(f"Student mean: {student_mean}")
# print(f"Student median: {student_median}")
# print("")
# print(f"Tuition mean: $ {tuition_mean}")
# print(f"Tuition median: $ {tuition_median}")
# print("******************************")


#task 5
# from math import *

# def is_prime(num):
#     for i in range(2,int(sqrt(num))+1):
#         if num%i==0:
#            print("False")
#            break
#         else:
#             print("True")
#             break

# num=int(input("enter a number to check wheter it's prime or not : ")) 
# if num>0:

#     is_prime(num)   
# else :
#     print("pls enter a positve num")
#     num=int(input("enter a number to check wheter it's prime or not : "))

