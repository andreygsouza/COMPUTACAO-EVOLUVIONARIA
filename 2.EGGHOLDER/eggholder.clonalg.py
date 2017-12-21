
#-----------------------import math
import numpy as np
import matplotlib.pyplot as plt


#Função custo 
def f(x):
    x1 = x[0]
    x2 = x[1]
    	
    term1 = -(x2+47) * np.sin(np.sqrt(abs(x2+x1/2+47)))
    term2 = -x1 * np.sin(np.sqrt(abs(x1-(x2+47))))
    	
    y = term1 + term2
    return(y)

def main():


    Nrep = 50     #N.repeticoes
    MaxIt = 500        #Maximo iteracoes
    resultados = np.zeros((Nrep,MaxIt))

    for rep in range(Nrep):
        
        #Parametros iniciais
        tam_pop = 100      #tamanho da população
#        MaxIt = 300         #Número máximo de iterações 
        Beta =  1           #numero de clones gerados por cada anticorpo
        Rho = 0.01          #intensidade da hipermutação dos clones
        nAleatorio = 10      #numero de anticorpos de menor afinidade que devem ser substuidos
        nSelecao = 10       #numero de anticorpos a serem selecionados na clonagem
        nVar = 2            #Número variáveis desconhecidas
        VarSize = [1, nVar] #Matriz tamanho Variaveis desconhecidas
        VarMin=-512      #Limite inferior da função
        VarMax= 512    #Limite superio da função------------------------------------------------------------
    
    
            
        #Inicialização das funções
        pop_Position = np.zeros((tam_pop,nVar), dtype=float) 
        pop_Cost = np.zeros((tam_pop,1), dtype=float)
        
        #Inicialização da População
        for i in range(tam_pop):
            #Inicia população com valores aleatórios
            pop_Position[i,:] = (VarMin + (VarMax-VarMin)*np.random.rand(1, nVar))
            #Fitness inicial
            pop_Cost[i] = f(pop_Position[i,:])
        
        #Ordenação do vetor
        Costs = pop_Cost
        SortOrder = np.argsort(Costs, axis=0) #Ordena os índicies do vetor
        Costs = np.sort(Costs,axis=0)         #Returna uma cópia do vetor ordenado
        
        pop_Position = pop_Position[SortOrder[:,0],:]
        pop_Cost = pop_Cost[SortOrder[:,0]]
        
        #pop_Position = pop_Position.reshape(tam_pop,nVar) #Dá um novo formato ao vetor sem alterar seus dados
        #pop_Cost = pop_Cost.reshape(tam_pop, 1)
        BestCost=np.zeros((MaxIt,1), dtype=float)
        
        for ite in range(MaxIt):
            nClones = np.zeros((nSelecao,1), dtype=int)
            selected = np.zeros((nSelecao,nVar), dtype=float)
            selected_Cost = np.zeros((nSelecao,1), dtype=float)
            for i in range(nSelecao):
                
                 selected[i,:] = pop_Position[i,:]
            #
                 nClones[i] = np.round(Beta*tam_pop/(i+1)) #Número de clones de cada anticorpo
                 
            soma_clones = 0
            for k in range(nSelecao):
                soma_clones = soma_clones + nClones[k]
                
            Clonados = np.zeros((int(soma_clones),nVar), dtype=float)
            Soma_aux = 0
            for l in range(nSelecao):
                for j in range(Soma_aux,Soma_aux + nClones[l,0]):
                    Clonados[j,:] = selected[l,:]
                Soma_aux = Soma_aux + nClones[l,0]    
            
                
            for i in range(nSelecao):
                selected_Cost[i] = f(selected[i,:])
            MaxSol_Cost = max(selected_Cost)
            MinSol_Cost = min(selected_Cost)          #Seleciona o valor mais baixo do vetor para normalizar os demais
            BestSol_Cost = selected_Cost/MaxSol_Cost #Normaliza as possíveis soluções 
            
            Maturate_Rate = np.zeros((nSelecao,1), dtype=float)       
            for it in range(nSelecao):
                #Maturação
                Maturate_Rate[it,0] = (BestSol_Cost[it,:]/50)*np.exp(-Rho*BestSol_Cost[it,:]) 
                #Clone_Best_Pop = selected[:,it]+Maturate_Rate*((np.random.rand(tam_pop,1)-np.random.rand(tam_pop,1))*selected)    
                
        
                
            s = np.zeros((int(soma_clones)), dtype=float) 
            mu = 0 # mean 
            for z in range(nSelecao):
                if z==0:
                    for k in range(nClones[z, 0]):    
                    #Distribuição normal com Maturate_Rate como desvio padrão
                        s[k] = np.random.normal(mu, Maturate_Rate[z], 1)
                if z>0:
                    for k in range(np.sum(nClones[0:(z)]), np.sum(nClones[0:(z)])+nClones[z, 0]):    
                    #Distribuição normal com Maturate_Rate como desvio padrão
                        s[k] = np.random.normal(mu, Maturate_Rate[z], 1)
                        
        
                    
            #Gerar novos indivíduos maturados
            newPop_Position = np.zeros((int(soma_clones),nVar), dtype=float) 
            newPop_Position[:,0] = np.multiply(s, Clonados[:,0])
            newPop_Position[:,1] = np.multiply(s, Clonados[:,1])
            
            #Comparar o fitness dos indíviduos maturados com o original
            newsol_Cost = np.zeros((int(soma_clones),1), dtype=float)  
            for n in range(int(soma_clones)):
                newsol_Cost[n] = f(newPop_Position[n,:])
                
            #Ordenação do vetor
            newCosts = newsol_Cost
            newSortOrder = np.argsort(newCosts, axis=0) #Ordena os índicies do vetor
            newCosts = np.sort(newCosts,axis=0)         #Returna uma cópia do vetor ordenado
            
            newPop_Position = newPop_Position[newSortOrder,:]
            
            newPop_Position = newPop_Position.reshape(int(soma_clones),nVar) #Dá um novo formato ao vetor sem alterar seus dados
            
            #comparacao
        #    pop_total = np.zeros(((int(soma_clones)+tam_pop,nVar)))
        #    
        #    pop_total = np.concatenate((newPop_Position, pop_Position), axis=0)
        #    
        #    cost_total = np.zeros(((int(soma_clones)+tam_pop, 1)))
        #    
        #    for i in range(int(soma_clones)+tam_pop):
        #        cost_total[i] = f(pop_total[i,:])
        #        
        #    sort_total = np.argsort(cost_total, axis=0)
        #    
        #    pop_total = pop_total[sort_total[:,0],:]
        #    
        #    cost_total = cost_total[sort_total[:,0]]
        #    
        #    pop_Position = pop_total[0:tam_pop,:]
        #    Costs = cost_total[0:tam_pop]
        #    pop_Cost = cost_total[0:tam_pop]
            sub = 0
            tam_pop = tam_pop + 10
            newer_Population = np.zeros((tam_pop,nVar), dtype=float)
            for w in range(nAleatorio):        
                    if (newCosts[w,:]<pop_Cost[w,:]):
                        newer_Population[w,:] = newPop_Position[w,:]
                    else:
                        newer_Population[w,:] = pop_Position[w,:]
                 
            pop_Position = newer_Population 
               
            pop_Cost = np.zeros((tam_pop,1), dtype=float)
        
        #Redefiniçaõ da População
            for i in range(nAleatorio+1, tam_pop):
            #Inicia população com valores aleatórios
                 pop_Position[i,:] = (VarMin + (VarMax-VarMin)*np.random.rand(1, nVar))
            #Fitness inicial
            for j in range(tam_pop):    
                 pop_Cost[j] = f(pop_Position[j,:])
         
        #Ordenação do vetor
            Costs = pop_Cost
            SortOrder = np.argsort(Costs, axis=0) #Ordena os índicies do vetor
            Costs = np.sort(Costs,axis=0)         #Returna uma cópia do vetor ordenado
        
            pop_Position = pop_Position[SortOrder[:,0],:]
            pop_Cost = pop_Cost[SortOrder[:,0]]
            
            BestSol_Cost = pop_Cost[0,:]
                
            #Guardar dados da iteracao atual
            BestCost[ite] = BestSol_Cost


            print("Repetição: "+str(rep)+" Iteração:" + str(ite))
            print("Melhor Custo: "+ str(BestCost[ite]))

            resultados[rep, ite] =  BestCost[ite]

        print("" + str(rep))

    best_results = np.argsort(resultados[:,-1], axis=0)
    np.savetxt("clonalg_eggholder.csv", resultados, delimiter=",")

    plt.figure()
    plt.grid(True)
    plt.plot(resultados[best_results[0],:])
    plt.xlabel("Iteração")
    plt.ylabel("Custo")
    plt.title("Custo por Iteração - Função Eggholder: Clonalg")


if __name__ == '__main__':
    main()
