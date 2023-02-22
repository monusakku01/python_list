lst=[10,20,30,40,50,60,70,80]
print(type(lst))
#all index with value
for i in enumerate(lst):
    print (i)

#slicing the list with index number

print("This print 0 index to 4th index:",lst[0:5])
#negative index
print("It is return reverse index ",lst[::-1])

print("Some othe index:",lst[2::3])
print("return 3rd elelment of list",lst[4])

