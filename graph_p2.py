import numpy as np
import matplotlib.pyplot as plt

# Создаем массивы x1 и x2
x1 = np.linspace(0, 40, 100)
x2 = np.linspace(0, 40, 100)

# Создаем сетку X1 и X2
X1, X2 = np.meshgrid(x1, x2)

# Задаем ограничения
constraint1 = X1 - 2 * X2 <= 30
constraint2 = 5 * X1 - X2 <= 25

plt.figure(figsize=(5, 5))
plt.xlabel('x1')
plt.ylabel('x2')
plt.xlim(-5,50)
plt.ylim(-5,50)
plt.plot(x1, (x1 - 30) / 2, label='x1-2x2=30', color='red', linestyle='dashed')
plt.plot(x1, 5 * x1 - 25, label='5x1-x2=25', color='pink', linestyle='dashed')
plt.axvline(x=0, color='gray', linestyle='dashed', label='x1=0')
plt.axhline(y=0, color='gray', linestyle='dashed', label='x2=0')
plt.fill_between([0, 5, 15,0], [0, 0, 50, 50], color='lavender')
plt.arrow(0, 0, 5, 5, head_width=0.7, head_length=0.7, fc='black', ec='black', label='вектор z')
perpendicular_x = np.array([-5, 5])
perpendicular_y = np.array([5, -5])
plt.plot(perpendicular_x, perpendicular_y, linestyle='dashed', color='green', label='перпендикуляр')

plt.title('Линейная функция')
plt.grid(True)
plt.legend()
plt.show()

#pulp
import pulp
import time
start = time.time()
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
problem = pulp.LpProblem('0',pulp.LpMaximize)
problem += x1 +x2, "Функция цели"
problem += x1- 2*x2 <= 30, "1"
problem +=5*x1-x2<=25, "2"
problem.solve()
print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Прибыль:")
#print (value(problem.objective))
stop = time.time()
print ("Время :")
print(stop- start)

#cvxopt
from cvxopt.modeling import variable, op 
import time 
start = time.time() 
x = variable(2, 'x') 
z=-(1*x[0] +1*x[1])#Функция цели
mass1 = (1*x[0] - 2*x[1] <= 30) #"1"
mass2 = (5*x[0] - 1*x[1] <= 25) # "2"
x_non_negative = (x >= 0) #"3" 
problem =op(z,[mass1,mass2,x_non_negative]) 
problem.solve(solver='glpk') 
problem.status 
print ("Прибыль:") 
print(abs(problem.objective.value()[0])) 
print ("Результат:") 
print(x.value) 
stop = time.time() 
print ("Время :") 
print (stop - start)

#scipy
from scipy.optimize import linprog 
import time 
start = time.time() 
c = [-1,-1] #Функция цели
A_ub = [[1,-2]] #'1' 
b_ub = [30]#'1' 
A_eq = [[5,-1]] #'2' 
b_eq = [25] #'2' 
print (linprog(c, A_ub, b_ub, A_eq, b_eq)) 
stop = time.time() 
print ("Время :") 
print(stop - start)