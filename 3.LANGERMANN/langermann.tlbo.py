import random
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------
#Funcao custo
def f(x):
    
    a = [3,5,2,1,7]
    b = [5,2,1,4,9]
    c = [1,2,5,2,3]
    
    y = 0.0
    for i in range(5):
        y += -(c[i]*np.exp(-(1/np.pi)*((x[0]-a[i])**2 + (x[1]-b[i])**2))*np.cos(np.pi*((x[0]-a[i])**2 + (x[1]-b[i])**2)))
    #end
    
    return y

def main():
        
    Nrep = 50      #N.repeticoes
    MaxIt = 500        #Maximo iteracoes
    resultados = np.zeros((Nrep,MaxIt))
        
    for rep in range(Nrep):
    
        nVar = 2 #Número variáveis desconhecidas
        #VarSize = [1, nVar] #Matriz tamanho Variaveis desconhecidas
        
        VarMin = -10 #Limite inferior variáveis desconhecidas
        VarMax =  10 #Limite superior variáveis desconhecidas
        
        #----------------------------------------
        #Parâmetros TLBO
        
        
        nPop = 100           #tamanho populacao
        
        #----------------------------------------
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
#        BestSol_Position = pop_Position[:, 0]
        BestSol_Cost = pop_Cost[0,0]
        #inicializar membros populacao
        
            
        # Initializar gravação de melhor custo
        BestCost=np.zeros((MaxIt,1), dtype=float)
        
        
        ##TLBO loop principal
        for it in range (MaxIt):
            
            # Calcular media Populacao
            Mean = 0
            for i in range (nPop):
                Mean = Mean + pop_Position[i,:]
                
            Mean = Mean/nPop;
            
            # Selecionar professor
            Teacher_Position = pop_Position[1,:]
            Teacher_Cost = pop_Cost[1,:]
            
            for i in range(1,nPop):
                if (pop_Cost[i,:] < Teacher_Cost):
                     Teacher_Position = pop_Position[i,:]
                     Teacher_Cost = pop_Cost[i,:]
                
        # Fase professor
            for i in range(nPop):
                # Criando solucao vazia
                newsol_Position = np.zeros((nPop,nVar), dtype=float)
                newsol_Cost = np.zeros((nPop,1), dtype=float)
                
                #Fator professor
                TF = random.randint(1,2)
                
                # Ensinando (movendo em direcao ao professor)
                
                newsol_Position = pop_Position[i,:] + np.multiply(np.random.rand(1,nVar),Teacher_Position - TF*Mean)
                #Clipping
                newsol_Position = np.maximum(newsol_Position, VarMin)
                newsol_Position = np.minimum(newsol_Position, VarMax)
                
                newsol_Position = newsol_Position[0,:]
                #Avaliacao
                newsol_Cost = f(newsol_Position)
                
                #Comparacao
                if (newsol_Cost<pop_Cost[i,:]):
                    pop_Cost[i,:] = newsol_Cost
                    pop_Position[i,:] = newsol_Position
                    if (pop_Cost[i,:] < BestSol_Cost):
                        #BestSol_Position = pop_Position[i,:]
                        BestSol_Cost = pop_Cost[i,:]
                    
        
        #Fase aluno
            for i in range (1,nPop):
                
                A = list(range(0,nPop))
                del A[i]
                
                j = np.random.choice(A)
                
                Step = pop_Position[i,:] - pop_Position[j,:]
                if (pop_Cost[j,:] < pop_Cost[i,:]):
                    Step = -Step
                
                
                #Creiar Solucao vazia
                
                
                # Ensinando (movendo em direcao ao professor)
                newsol_Position = pop_Position[i,:] + np.multiply(np.random.rand(1,nVar),Step)
                
                #Clipping
                newsol_Position = np.maximum(newsol_Position, VarMin)
                newsol_Position = np.minimum(newsol_Position, VarMax)
                
                newsol_Position = newsol_Position[0,:]
                #avaliacao
                newsol_Cost = f(newsol_Position)
                
                #comparacao
                if (newsol_Cost<pop_Cost[i,:]):
                    pop_Position[i,:] = newsol_Position
                    pop_Cost[i,:] = newsol_Cost
                    if (pop_Cost[i,:] < BestSol_Cost):
                        #BestSol_Position = pop_Position[i,:]
                        BestSol_Cost = pop_Cost[i,:]
                    
                    
            
            #Guardar dados da iteracao atual
            BestCost[it] = BestSol_Cost


            print("Repetição: "+str(rep)+" Iteração:" + str(it))
            print("Melhor Custo: "+ str(BestCost[it]))
            
            resultados[rep, it] =  BestCost[it]
        
        print("" + str(rep))
    
    best_results = np.argsort(resultados[:,-1], axis=0)
    np.savetxt("tlbo_eggholder.csv", resultados, delimiter=",")
    
    plt.figure()
    plt.grid(True)
    plt.plot(resultados[best_results[0],:])
    plt.xlabel("Iteração")
    plt.ylabel("Custo")
    plt.title("Custo por Iteração - Função Langermann: TLBO")


if __name__ == '__main__':
    main()       




