import matplotlib.pyplot as plt
import numpy as np

k = 0.1115717757
people = 1500 #number of people in company

def delta(rn,k):
    return  k*rn*(people-rn)

def plot(rns):
    x = np.arange(len((rns)))
    plt.plot(x, rns)
    plt.title("Vitesse de Propagation", fontsize=11)
    plt.ylabel("Nombre d'étudiants", fontsize=10)
    plt.xlabel("Jours", fontsize=10)
    plt.show()



def rumors(k):
    rns = []
    rn = 1          # number of people who heard rumor
    print("k = ",k, " rn = ", rn)
    days = 0  
    delta_value = 0    
    
    while(1):
        delta_value = delta(rn,k)
        print('delta : ',delta_value)
        if delta_value > 0.1:
            days += 1
        else:
            break
        rn += delta(rn,k)
        rns.append(rn)
        print('day: ', days,' number of people: ',(rn))
    plot(rns)
    print('number of days', days)
