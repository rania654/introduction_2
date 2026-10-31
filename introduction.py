import numpy as np
# list1 = [35, 65, 89]
# print(type(list1))
# print(list1)
# for i in range(len(list1)):
#     new = 2*list1[i]
#     list1[i] = new
# print(list1)

# array = np.array(list1)
# print(array)
# print(type(array))
# print(2 * array)
# print(5 + array)

# array2 = np.zeros(4, int)
# print(array2)

# array3 = np.ones(3, int)
# print(array3)
# print(array3.ndim)
# print(array3.shape)

# array4 = np.ones((3,3))
# print(array4)

# array5 = np.arange(1,50)
# print(array5)

# array6 = np.linspace(1,11,6)
# print(array6)

# array7 = np.arange(1,11)
# array8 = array7.reshape(5,2)
# print(array8)

# array9 = np.random.permutation(array7)
# array10 = np.random.permutation(array8)
# print(array9)
# print(array10)

# print(np.sort(array9))
# print(np.sort(array10))

# array11 = np.random.randint(1,10,3)
# print(array11)
# print(array11.reshape(1,3))

# array12 = np.random.randint(1,15,(3,5))
# print(array12)

# array13 = np.random.randint(1,10,5)
# print(array13)
# print(array13[ : :-1])
# print(array13[ : : ])

# array14 = np.random.randint(1,15,(6,6))
# print(array14)
# print(array14[1:4:1,1:4:1])

# array15 = np.random.randint(1,10,5)
# print(array15)
# print(array15[[0,3,2]])
# print(array15[array15 % 2 == 0])
# print(array15[array15 > 5])

# array16 = np.random.randint(1,10,5)
# print(array16)
# print(array15+array16)
# print(2*array15+array16)

r = np.random.randint(1,10,9)
h = np.random.randint(1,10,9)
pie = 3.14
print(h*2*pie*r)