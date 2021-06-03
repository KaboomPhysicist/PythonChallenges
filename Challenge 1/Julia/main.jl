include("port.jl")
using .generator
using Plots
plotly()

function main(NP,N)
    confs=[]
    Energias=[]

    ti=time()
    TI=time()

    if NP>1000000
        Paso=10000
    elseif NP<40
        Paso=1
    else
        Paso=NP/20
    end

    for i in 1:NP
        if (i%Paso==0)
            tiempo=round((time()-ti),digits=3)
            P=round(i/NP*100,digits=2)
            print("$P % de avance $i/$NP Tiempo de iteración: $tiempo s. ")
            ETA=round((NP-i)*tiempo/Paso,digits=2)
            println("ETA $ETA s")
            ti=time()
        end
        temp=Emain(N-1)
        push!(Energias,temp[1])
        push!(confs,temp[2])
        if (i%Paso*3==0)
            confs=[confs[findall(x->x==minimum(Energias),Energias)[1]]]
            Energias=[minimum(Energias)]
        end
    end

    println("Tiempo total: $(time()-TI)")
    println("Tiempo medio de iteración [ms]: $((time()-TI)/NP*1000)")
    

    #println(Energias)
    conf_opt_pos=findall(x->x==minimum(Energias),Energias)[1]
    #println(conf_opt_pos)
    
    conf_opt=confs[conf_opt_pos]
    graph(conf_opt)
end

t1=time()
print("Número de iteraciones: ")
NP=readline()
NP=parse(Int64,NP)

N=print("Número de circulos: ")
N=readline()
N=parse(Int64,N)

main(NP,N)
savefig("gen imgs/circulos$N-$NP")
savefig("gen imgs/circulos$N-$NP.png")
t2=time()
println(t2-t1)