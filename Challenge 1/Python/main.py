from dist_energy2D import Emain
import numpy as np
import matplotlib.pyplot as plt

import time

def main(NP,N,R):

    confs=[]
    Energias=[]

    ti=time.time()
    TI=time.time()

    if NP>1000000:
        Paso=10000
    else:
        Paso=NP/20

    for i in range(NP):
        if (i%Paso==0):
            tiempo=(time.time()-ti)
            P=i/NP*100
            print("%.2f%% de avance %s/%s Tiempo de iteración: %.2f s."%(P,i,NP,tiempo),end="  ")
            print("ETA %.2f s"%((NP-i)*tiempo/Paso))
            ti=time.time()
        temp=Emain(N,R)
        Energias.append(temp[1])
        confs.append(temp[0])
        if (i%Paso*3==0):
            confs=[confs[np.where(Energias==np.min(Energias))[0][0]]]
            Energias=[np.min(Energias)]
            

    print("Tiempo total: ",time.time()-TI)
    print("Tiempo medio de iteración [ms]: ",(time.time()-TI)/NP*1000)
    
    conf_opt_pos=np.where(Energias==np.min(Energias))
    conf_opt=confs[conf_opt_pos[0][0]]

    for i in conf_opt:
        i.graph()
    
    Em=np.min(Energias)

    fig=plt.figure(1,figsize=(20,20))
    ax=fig.add_subplot()
    plt.text(0.15, 0.01,'E=%.12e'%Em, horizontalalignment='center', verticalalignment='center', transform = ax.transAxes)

    """plt.hlines(-5,-5,5)
    plt.hlines(5,-5,5)
    plt.vlines(-5,-5,5)
    plt.vlines(5,-5,5)"""
    plt.show()

radio=float(input("Radio de los circulos: "))
iter=int(input("Número de iteraciones: "))
cir=int(input("Número de círculos: "))

main(iter,cir,radio)