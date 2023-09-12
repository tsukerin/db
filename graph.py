import matplotlib.pyplot as plt

x1, y1 = [35, 0], [0, 28]
x2, y2 = [0, 6], [0, 10]
x3, y3 = [0, 17], [19, 19]
x4, y4 = [19, 19], [0, 17]
x5, y5 = [19, 19], [12.8, 12.8]
x6, y6 = [11.25, 11.25], [19, 19]
plt.plot(x1, y1, color='black')
plt.title('График нахождения наибольшего значения')
plt.xlabel('Ось Х')
plt.ylabel('Ось Y')
plt.text(8, 10, 'Z(6,10)',fontsize=9)
plt.xlim(0,50)
plt.ylim(0,50)
plt.plot(x3, y3, linestyle='--', color = "r")
plt.plot(x4, y4, linestyle='--', color = "g")
plt.fill_between([19, 11.25], [12.8, 19], color = 'silver')
plt.fill_between([0, 11.25], [19, 19], color = 'silver')
plt.plot(x5, y5, marker = 'o', color = "g")
plt.text(20, 12.8, 'A',fontsize=9)
plt.plot(x6, y6, marker = 'o', color = "r")
plt.text(11.25, 20, 'B',fontsize=9)
plt.arrow(0, 0, 6, 10, head_width=1)
plt.legend()
plt.show()