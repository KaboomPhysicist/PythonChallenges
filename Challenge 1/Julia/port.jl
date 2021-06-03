module generator
export Emain,graph

using Plots
plotly()

abstract type Figura
end

mutable struct circulo <: Figura
    radio :: Float64
    pos :: Array
end

function norma(x)
    n=0
    for i in x
        n+=i^2
    end
    return n^0.5
end


function generar(circ,objs)
    n=length(objs)
    circ_base=objs[rand(1:n)]
    ang_rand=rand(Float64)*2*pi

    npos=circ_base.pos+2*circ.radio.*[cos(ang_rand),sin(ang_rand)]

    errors=0

    for i in objs
        if norma(i.pos-npos)<2*circ.radio
            errors=1
            break
        end
    end

    if errors==0
        push!(objs,circulo(circ.radio,npos))
    else
        generar(circ,objs)
    end
end

function graph(objs)
    ang=range(0,2*pi,length=10000)
    for circle in objs
        X=circle.radio.*cos.(ang)
        Y=circle.radio.*sin.(ang)
        for i in 1:length(X)
            X[i]-=circle.pos[1]
            Y[i]-=circle.pos[2]
        end
        #println("A graficar!")
        plot!(X,Y,color="blue",legend=false,aspect_ratio=:equal)
    end
end

function E(m,r)
    -m^2/r
end
function energia(objs)
        Etotal=0
        for i in 1:length(objs)
            for j in 1:length(objs)
                if i<j
                    Etotal+=E(1,norma(objs[i].pos-objs[j].pos))
                end
            end
        end
        return Etotal
end

function Emain(N)
    circulos=[circulo(1.0,[0.0,0.0])]
    for i in 1:N
        generar(circulos[i],circulos)
    end
    Energia=energia(circulos)

    return Energia,circulos
end

end