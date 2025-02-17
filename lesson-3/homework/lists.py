#q1

# a=["apple" ,"banana","lemon","apple"]
# f="apple"
# print(a.count(f))

#q2
# a = [1, 2, 3, 4, 3, 4, 2]
# print(sum(a))


#q3

# a = [1, 2, 3, 4, 3, 4, 2]
# print(max(a))

#q4
# a = [1, 2, 3, 4, 3, 4, 2]
# print(min(a))

#q5
# a = [1, 2, 3, 4, 3, 4, 2]
# b=4
# print(b in a)
# print(5 in a)


#q6
# a=input("enter the elemets if your list: ").split()
# if len(a) == 0:
#     print("list is empty")
# else:
#     print(a[0])

#q7
# a=input("enter the elemets if your list: ").split()
# if len(a) == 0:
#     print("list is empty")
# else:
#     print(a[-1])

#q8

# a = [1, 2, 3, 4, 3, 4, 2]
# new_list=a[:3]

#q9
# a = [1, 2, 3, 4, 3, 4, 2]
# print(a[::-1])

#q10
# a = [1, 2, 3, 4, 3, 4, 2]
# print(sorted(a))

#q11

# a = [1, 2, 3, 4, 3, 4, 2]
# print(list(set(a)))

#q12
# a = [1, 2, 3, 4, 3, 4, 2]
# b = 6
# ind = 2
# a.insert(ind, b)
# print(a)

#q13
# a = [1, 2, 3, 4, 3, 4, 2]
# print(a.index(2))

#q14

# a = [1, 2, 3, 4, 3, 4, 2]
# print(bool(a))


#q15
# a = [1, 2, 3, 4, 3, 4, 2]
# count = 0
# for i in a:
#     if i%2 == 0:
#         count+=1

# print(count)

#q16
# a = [1, 2, 3, 4, 3, 4, 2]

# count_odd = 0
# for i in a:
#     if i%2 == 1:
#         count_odd+=1

# print(count_odd)

#q17
# a = [1, 2, 3, 4, 3, 4, 2]
# b=[4,5,6]
# a.extend(b)

# print(a)

#q18
# a = [1, 2, 3, 4, 3, 4, 2]
# b=[4,5,6]
# a.extend(b)
# newlist=a
# for i in b:
#     if i in a:
#         print("yes")
#         break


#q19
# a = [1, 2, 3, 4, 3, 4, 2]
# replacer=int(input("enter the num of index u wanna change"))
# a.index[a.index(replacer)]=4
# print(a)

#q20
# a = [1, 2, 3, 4, 3, 4, 2]
# print(sorted(list(set(a)))[-2])

#q21
# print(sorted(list(set(a)))[1])
# a = [1, 2, 3, 4, 3, 4, 2]

#q22
# a = [1, 2, 3, 4, 3, 4, 2]
# only_even = []
# for num in a:
#     if num%2 == 0:
#         only_even.append(num)
# print(only_even)


#q23
# a = [1, 2, 3, 4, 3, 4, 2]
# only_odd = []
# for num in a:
#     if num%2 == 1:
#         only_odd.append(num)
# print(only_odd)

#q24
# a = [1, 2, 3, 4, 3, 4, 2]
# len(a)

#q25
#a1 = a.copy()

#q26
# if len(a) % 2 == 1:
#     print(a[len(a)//2])
# else:
#     print(a[len(a)//2], a[(len(a)//2)-1])


#q27
#print(max[:len(a)+1])

#q28
#print(min[:len(a)+1])


#q29
# index2 = 5
# if index2<len(a)-1:
#     a.pop(index2)


#q30
# a = [1, 2, 3, 4, 3, 4, 2]
# if sorted(a)==a:
#     print(True)
# else:
#     print(False)    

#q31
# a = [1, 2, 3, 4, 3, 4, 2]
# times=int(input("enter number of times"))
# new_list=[]
# for list_item in a:
#     for x in range(times):
    
#         new_list.append(list_item)
# print(new_list)    


#q32
# a = [1, 2, 3, 4, 3, 4, 2]
# b=[4,5,6]
# a.extend(b)
# newlist=a
#print(sorted(newlist))

#q33
# a = [1, 2, 3, 4, 3, 4, 2]
# indexes = []
# value = 2
# for i in range(len(a)):
#     if a[i] == value:
#         indexes.append(i)

# print(indexes)



#34
#i coulnt understand

#35
# start=int(input("enter the start"))
# end=int(input("enter the end"))
# lists=[]
# for i in range(end-start+1):
#     lists.append(start)
#     start+=1
# print(lists)    


#36
# a = [1, -2, 3, 4, -3, 4, 2]
# sum = 0
# for numbers in a:
#     if numbers>0:
#         sum+=numbers
# print(sum)

#37

# a = [1, -2, 3, 4, -3, 4, 2]
# sum = 0
# for numbers in a:
#     if numbers<0:
#         sum+=numbers
# print(sum)

#38
# a = [1, -2, 3, 4, -3, 4, 2]
# if  a==a[::-1]:
#     print(True)
# else:
#     print(False)    


# #39
# a= [1, -2, 3, 4, -3, 4, 2,8,9,11]
# ran=int(input("enter the lenght of each sublist"))
# a1=a[0:ran]
# a2=a[ran-1:(2*ran)-1]
# a3=a[2*ran-1:len(a)-1]
# a4=[]
# a4.append(a1)
# a4.append(a2)
# a4.append(a3)
# print(a4)





# l= [1, -2, 3, 4, -3, 4, 2,8,9,11]
# l2 = []
# l3 = []
# count = 0
# number = int(input("number:  "))
# temp = 0
# if len(l)%number==0 :

#     for i in range(int(len(l)/number)):
#         for j in range(number):
#             l2.append(l[count])
#             count += 1
#         l3.append(l2)
#         l2 = []
# else:
#     for i in range(int(len(l)/number)+1):
#         l2 = []
#         for j in range(number):
            
#             if count != len(l)-1:
#                 l2.append(l[count])
#                 count += 1
                
#         l3.append(l2)
#     l3.append(l2.append(l[count]))
   
# l3.pop()
# print(l3)








#40
# a= [8, 2, 3, 4, 3, 4, 2]
# b=set(a)
# new=[]
# for i in b:
#     if i in a:
#         new.append(i)

# print(new)


