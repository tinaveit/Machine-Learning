import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Exercise 5
array1 = np.full((3, 4), 0.5)        #a
array2 = np.random.random((5, 5))    #b
array3 = np.ones((2, 2))             #c

# Exercise 7
dates = pd.date_range("20130101", periods=10)
df = pd.DataFrame(np.random.randn(10, 4), index=dates, columns=list("ABCD"))

top5 = df.head()                    #a
bottom5 = df.tail()                 #b
column_a = df['A']                  #c

# Exercise 8
x_values = range(1, 11)
y_values = [x for x in x_values]

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')

plt.title('Plot of y = x')
plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)
plt.show()

# Exercise 9
data = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]

plt.hist(data, edgecolor="red", bins=6)
plt.show()
