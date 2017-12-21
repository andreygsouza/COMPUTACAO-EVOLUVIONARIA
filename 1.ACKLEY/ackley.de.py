from random import *
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------
#Funcao custo
def f(x):
    arg1 = -0.2 * np.sqrt(0.5 * (x[0] ** 2 + x[1] ** 2))
    arg2 = 0.5 * (np.cos(2. * np.pi * x[0]) + np.cos(2. * np.pi * x[1]))
    return -20. * np.exp(arg1) - np.exp(arg2) + 20. + np.e


#%%

def main():
    
    Nrep = 50      #N.repeticoes
    MaxIt = 500        #Maximo iteracoes
    resultados = np.zeros((Nrep,MaxIt))
        
    for rep in range(Nrep):
        
        nVar = 2 #Número variáveis desconhecidas
        VarSize = [1, nVar] #Matriz tamanho Variaveis desconhecidas
        
        VarMin = -32.768 #Limite inferior variáveis desconhecidas
        VarMax =  32.768 #Limite superior variáveis desconhecidas
        
        #----------------------------------------
        #Parâmetros TLBO
        
        
        nPop = 100  # Número população
        
        beta_min = 0.2   # Lower Bound of Scaling Factor
        beta_max = 0.8    #Upper Bound of Scaling Factor
        
        pCR=0.2          # Crossover Probability
        
        #Inicializacao
        
        #vetor inicializacao populacao
        
        pop_Position = np.zeros((nPop,nVar), dtype=float)
        
        pop_Cost = np.zeros((nPop,1), dtype=float)
        
        for i in range(nPop):
            #Inicia População
            pop_Position[i] = (VarMin + (VarMax-VarMin)*np.random.rand(1, nVar))
            
            #Avalialçao
            pop_Cost[i] = f(pop_Position[i,:])
        
        Costs = pop_Cost
        SortOrder = np.argsort(Costs, axis=0)
        SortOrder = tuple(SortOrder.T)
        Costs = np.sort(Costs,axis=0)
        
        
        pop_Position = pop_Position[SortOrder,:]
        pop_Cost = pop_Cost[SortOrder,:]
            
        pop_Position = pop_Position.reshape(nPop,nVar)
        pop_Cost = pop_Cost.reshape(nPop, 1)
        
        #Inicializar melhor solucao
        BestSol_Position = pop_Position[:, 0]
        BestSol_Cost = pop_Cost[0,0]
        #inicializar membros populacao
        
            
        # Initializar gravação de melhor custo
        BestCost=np.zeros((MaxIt,1), dtype=float)
        
        
        ##TLBO loop principal
        for it in range (MaxIt):
            for i in range (nPop):
                x = pop_Position[i]
                
                A = list(range(0,nPop))
                del A[i]
                A = np.random.permutation(A)
                
                a = A[1]
                b = A[2]
                c = A[3]
                
                #Mutacao
                
                beta = (beta_min + (beta_max-beta_min)*np.random.rand(1, nVar))
                y = pop_Position[a] + np.multiply(beta,(pop_Position[b] - pop_Position[c]))
                
                y=np.maximum(y, VarMin)
                y=np.minimum(y, VarMax)
                
                #Crossover
                z = np.zeros(x.shape)
                J = list(range(0,len(x)))
                j0 = np.random.choice(A)
                
                
                for j in range(len(x)):
                    rand = random()
                    if (j==j0) or (rand<=pCR):
                        z[j] = y[0,j]
                    else:
                        z[j] = x[j]    
                
              
                
                newsol_Position = z
                newsol_Cost = f(newsol_Position)
                
                if (newsol_Cost<pop_Cost[i,:]):
                    pop_Position[i,:] = newsol_Position
                    pop_Cost[i,:] = newsol_Cost
                
                    if (pop_Cost[i,:] < BestSol_Cost):
                           BestSol_Position = pop_Position[i,:]
                           BestSol_Cost = pop_Cost[i,:]
                    
                    
            
            #Guardar dados da iteracao atual
            BestCost[it] = BestSol_Cost
             #Show Iteration Information 
            print("Repetição: "+str(rep)+" Iteração:" + str(it))
            print("Melhor Custo: "+ str(BestCost[it]))
            
            
            resultados[rep, it] =  BestCost[it]
        
        print("" + str(rep))
    
    best_results = np.argsort(resultados[:,-1], axis=0)
    np.savetxt("de_ackley.csv", resultados, delimiter=",")
     
    plt.figure()
    plt.grid(True)
    plt.semilogy(resultados[best_results[0],:])
    plt.xlabel("Iteração")
    plt.ylabel("Custo")
    plt.title("Custo por Iteração - Função Ackley: Evolução Diferencial")


if __name__ == '__main__':
    main()   
        
        
        
        