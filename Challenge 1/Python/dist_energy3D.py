from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

class esfera:
    def __init__(self,R,M,x,y,z):
        self.radio=R
        self.pos=np.array([x,y,z])
        self.masa=M

    def superficie(self):
        u, v = np.mgrid[0:2*np.pi:60j, 0:np.pi:30j]
        X = self.radio*np.cos(u)*np.sin(v)+self.pos[0]
        Y = self.radio*np.sin(u)*np.sin(v)+self.pos[1]
        Z = self.radio*np.cos(v)+self.pos[2]

        cir=np.array([X,Y,Z])
        return cir

    def graph(self):
        fig = plt.figure(1,figsize=(14,9))
        ax = fig.gca(projection='3d')

        # Plot the surface.
        surf = ax.plot_wireframe(*self.superficie())

        # Customize the z axis.
        #ax.set_xlim(-20,20)
        #ax.set_ylim(-20,20)
        #ax.set_zlim(-20, 20)

        # Add a color bar which maps values to colors.
        #fig.colorbar(surf, shrink=0.5, aspect=5)

    def generar(self,ob):
        #total debe ser una lista con las posiciones de cada uno de los círculos
        circ_base=random.choice(ob).pos
        #print(circ_base)
        t_rand=np.random.random_sample()*2*np.pi
        p_rand=np.random.random_sample()*np.pi

        npos=circ_base+2*self.radio*np.array([np.sin(p_rand)*np.cos(t_rand),np.sin(p_rand)*np.sin(t_rand),np.cos(p_rand)])
        #print("Pos nueva",npos)
        
        errors=0

        for i in ob:
            if ((np.linalg.norm(i.pos-npos)<(2*self.radio))):
                errors+=1
                break
        
        if errors==0:
            ob.append(esfera(self.radio,self.masa,*npos))
            #print("Agregado!")
        else:
            self.generar(ob)

    def energia(self,ob):
        E=lambda m,r: -6.674e-11*m**2/r
        Etotal=0
        #print(self)

        for i in ob[ob.index(self)+1:]:
            Etotal+=E(self.masa,np.linalg.norm(i.pos-self.pos))
        return Etotal

def Emain3D(N,R):
    objs=[]
    objs.append(esfera(R,1,0,0,0))

    for i in range(N-1):
        objs[i].generar(objs)
    
    EE=0

    for i in objs:
        i.graph()
        #EE+=i.energia(objs)
    
    plt.show()