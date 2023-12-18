import matplotlib.pyplot as plt
import sqlite3


f = open('20046.dat', 'r')
data = []
for s in f.readlines():
    temp = s.split()
                # станция, год, месяц, день, час, напр ветра, осадки, темпер-ра, влажность
    data.append([temp[0], temp[5], temp[6], temp[7], temp[10], float(temp[39]), float(temp[47]), float(temp[-31]), float(temp[-15])])
print(data[:10])

x_range = list(map(int, input().split()))

x = range(len(data[x_range[0]:x_range[1]]))
y = [i[-2] for i in data[x_range[0]:x_range[1]]]

plt.figure(figsize=(7, 7))
plt.subplot(3, 1, 1)
plt.title('Температура')
plt.xlabel('Время')
plt.ylabel('Температура')
plt.grid()
plt.plot(x, y, "g")
plt.show()


