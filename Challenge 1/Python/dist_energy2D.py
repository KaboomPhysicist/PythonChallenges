import numpy as np
import matplotlib.pyplot as plt
import random


###SETUP
fig=plt.figure(1,figsize=(20,20))
global ax
ax=fig.add_subplot()

E=lambda m,r: -m**2/r   #-6.674e-11

class circulo:
    def __init__(self,R,M,x,y):
        self.radio=R
        self.pos=np.array([x,y])
        self.masa=M

    def circunferencia(self):
        theta=np.linspace(0,2*np.pi,10000)
        Y=self.radio*np.sin(theta)-self.pos[1]
        X=self.radio*np.cos(theta)-self.pos[0]
        
        cir=np.array([X,Y])
        return cir

    def graph(self):
        plt.figure(1)
        ax.set_aspect('equal', adjustable='box')
        plt.plot(*self.circunferencia(),'b')
    
    def generar(self,ob):
        circ_base=random.choice(ob).pos
        ang_rand=np.random.random_sample()*2*np.pi

        npos=circ_base+2*self.radio*np.array([np.cos(ang_rand),np.sin(ang_rand)])
        
        errors=0

        for i in ob:
            if ((np.linalg.norm(i.pos-npos)<(2*self.radio))):
                errors=1
                break
        
        if errors==0:
            ob.append(circulo(self.radio,self.masa,*npos))
            #print("Agregado!")
        else:
            self.generar(ob)

    def energia(self,ob):
        Etotal=0
        
        for i in ob[ob.index(self)+1:]:
            Etotal+=E(self.masa,np.linalg.norm(i.pos-self.pos))
        return Etotal

    def limite(self,a,b,ob):
        if (self.pos[0]+self.radio>a or self.pos[1]+self.radio>b or self.pos[0]-self.radio<-a or self.pos[1]-self.radio<-b):
            print("Fuera!")
            ob.pop(ob.index(self))

def Emain(N,R):
    objs=[]
    objs.append(circulo(R,1,0,0))

    for i in range(N-1):
        objs[i].generar(objs)
        
    #for i in objs:
    #    i.limite(5,5,objs)
    
    EE=0
    for i in objs:
        #i.graph()
        EE+=i.energia(objs)
    
    #plt.show()
    return objs,EE
