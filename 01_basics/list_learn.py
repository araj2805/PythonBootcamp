myList = []
myList.append(1)
myList.append(2)
myList.append(3)

print(myList)

myList = [4,5,6,7]

print(myList)

print(myList[0])

myList.remove(4)

print(myList[0])

n = myList.count(5)

print(n)
myList.append(34)
myList.append(2344)
myList.append(5235)
myList.append("sfasd")
myList.append("fdgs")
myList.append(True)
myList.append(54.23)

print(myList)


# for obj in myList:
#     if isinstance(obj,bool):
#         print("{} is Boolean".format(obj))
#     elif isinstance(obj,int) or isinstance(obj,float):
#         # print(" Is Number or Float")
#         print("{} Is Number or Float".format(obj))
#     elif isinstance(obj,str):
#         print("{} Is String".format(obj))

print("Length of myList : {}".format(len(myList)))

print(type(myList))

print("Last Element in myList : {}".format(myList[-1]))

print(myList[2:2])