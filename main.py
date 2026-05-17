import random
import statistics
#print(random.randint(1, 100))
#generate random numbers between 1-100 thousand times.and store each nu,ber inside a list. and the find which number is epeated the most times.
nums=[]
for i in range(1, 20+1):
    nums.append(random.randint(1, 10))
print(nums)
#print("The most appearing number is", statistics.mode(nums))
nums_info=[]
for i in range(1, 10):
    nums_info.append({"num":i,"repeated":nums.count(i)})
    
print("Below are the numbers info.")
print(nums_info)