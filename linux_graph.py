from numpy import linspace
import matplotlib.pyplot as plt
t = []
y = []
i = 0
with open('data.txt') as f:
    for line in f.readlines()[::25]:
        y.append(int(line))
        t.append(i)
        i += 1

plt.plot(t,y)
plt.xlabel(u'time stamp')
plt.ylabel(u'number y')
plt.show()
