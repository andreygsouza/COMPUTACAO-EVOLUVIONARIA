# PSO
import numpy as np
from random import random
import matplotlib.pyplot as plt

# Fitness function------------------------------------------------------------
def f(x):
    
    a = [3,5,2,1,7]
    b = [5,2,1,4,9]
    c = [1,2,5,2,3]
    
    y = 0.0
    for i in range(5):
        y += -(c[i]*np.exp(-(1/np.pi)*((x[0]-a[i])**2 + (x[1]-b[i])**2))*np.cos(np.pi*((x[0]-a[i])**2 + (x[1]-b[i])**2)))
    #end
    
    return y
# PSO-------------------------------------------------------------------------
def main():

# particles and velocities

    
    
    rep = 50      #N.repeticoes
    max_iter = 500
    resultados = np.zeros((rep,max_iter))
    
    
        
    for rep in range(rep):
        
        # Parameters-------------------------------------------------------------------
            
        
        pop_size = 100
        dimensions = 2
        c1 = 2.0
        c2 = 2.0
        MAXV = 1 
        UB = 10
        LB = -10
        weight = 1.2 
#        err_crit = 0.00001
        update_weight = 1
        
        xx = np.zeros((pop_size,dimensions))
        vx = np.zeros((pop_size,dimensions))
        pbestx = np.zeros((pop_size,dimensions))
        
        
        fitness = np.zeros((max_iter))
        
        ## Init particles
        for i in range(pop_size):
            xx[i,:] = np.array([ (UB-LB)*random() + LB  for j in range(dimensions)])
            # pbest inicializado com uma copia das particulas
            pbestx[i,:] = xx[i,:]
            # inicializando velocidade
            vx[i,:] = np.array([ MAXV*random() for j in range(dimensions)])
        
        it = 0
        gbest = 0
        pbest = []
        
        for it in range(max_iter):
            #update inertia weight
            # time variant	weight,linear from weight to 0.4	
            if(update_weight == 1 ):
                weight_up = ( weight-0.4) * (max_iter -it) / max_iter +0.4; 
            else:
                weight_up= weight		#constant inertia weight
            for i in range(pop_size):
                # Fitness Evaluation
                fitness_val = f(xx[i])
                # na primeira vez inicializa o pbest de cada particula com os valores da inicializacao
                if(it==0):
                    pbest.append(fitness_val) 
                # se o fitness calculado for melhor do que o melhor conhecido, atualizar
                if( fitness_val < pbest[i]):
                    pbest[i] = fitness_val
                    pbestx[i,:] = xx[i,:]
                    if(pbest[i] < pbest[gbest]):
                        gbest = i 
        
                fitness[it] = pbest[gbest]
                # calcula uma nova velocidade da particula
                r1 = random()
                r2 = random()
                for j in range(dimensions):
                    vx[i][j] = weight_up * vx[i][j] + c1* r1 * (pbestx[i][j] - xx[i][j]) + c2 * r2 * (pbestx[gbest][j] - xx[i][j]) 
        
                # atualiza posicao da particula i a partir da velocidade calculada
                for j in range(dimensions):
                    xx[i][j] = xx[i][j] + vx[i][j]
                    if (xx[i][j]>UB):
                        xx[i][j] = UB
                    if (xx[i][j]<LB):
                        xx[i][j] = LB
        
        		
        
            print("Repetição: " +str(rep)+" Iteração:" + str(it))
            print("Melhor Custo: "+ str(fitness[it]))
        
            resultados[rep, it] =  fitness[it]
            
            # nova iteracao
    best_results = np.argsort(resultados[:,-1], axis=0)
    np.savetxt("pso_eggholder.csv", resultados, delimiter=",")
    
    plt.figure()
    plt.grid(True)
    plt.plot(resultados[best_results[0],:])
    plt.xlabel("Iteração")
    plt.ylabel("Custo")
    plt.title("Custo por Iteração - Função Langermann: PSO")
    
# Main function----------------------------------------------------------------
if __name__ == '__main__':
    main()       








