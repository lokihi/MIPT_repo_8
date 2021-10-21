import matplotlib.pyplot as plt
import numpy as np
with open("data.txt","r") as data:
    strlist = data.read().split("\n")
    tmp = [float(i) for i in strlist]
data_array = np.loadtxt("data.txt",dtype=float)
time_array = np.loadtxt("data.txt",dtype=float)
with open("settings.txt","r") as settings:
    strlist = settings.read().split("\n")
    tmp = [float(i) for i in strlist]
settings_array = np.loadtxt("settings.txt",dtype=float)

for i in range(len(data_array)):
    data_array[i]=data_array[i]*settings_array[0]
    time_array[i]=data_array[i]*settings_array[0]
for i in range(len(data_array)):
    time_array[i]= settings_array[1] * i


time1 = data_array.argmax()*settings_array[1]
time2 = (len(data_array)-data_array.argmax())*settings_array[1]



plt.plot(time_array, data_array,color = 'b',label="V(t)",markerfacecolor='red',marker='o',linewidth=2,markevery=30)
plt.axis([min(time_array), 10, min(data_array), 3.5])
plt.text(6, 1.5, "Время зарядки = {0}".format(time1),fontweight="bold")
plt.text(6, 1.25, "Время разрядки = {0}".format(time2),fontweight="bold")
plt.ylabel('Напряжение, В',fontsize=15)
plt.xlabel('Время, с',fontsize=15)
plt.title('Процесс заряда и разряда в RC-цепи',fontsize=15,fontweight='bold')
plt.grid(which="both",linewidth=1)
plt.grid(which="minor",ls="--",linewidth=0.25)
plt.legend(fontsize=13)
plt.minorticks_on()
plt.show()
plt.savefig('plot.svg')
