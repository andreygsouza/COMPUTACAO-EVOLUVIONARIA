# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:48:20 2017

@author: Andrey de Souza
"""

import matplotlib.pyplot as plt
import random
import numpy as np



def f(x):
    x1 = x[0]
    x2 = x[1]
    	
    fact1 = (np.sin(x1**2-x2**2))**2 - 0.5
    fact2 = (1 + 0.001*(x1**2+x2**2))**2
    	
    y = 0.5 + fact1/fact2
    return(y)


def TournamentSelection(genotypes, fitness, TournamentSize):
    nPop = len(genotypes)
    S = np.random.choice(nPop, TournamentSize)
    s_fitness= fitness[S]
    j = np.argmin(s_fitness)
    i = S[j]
    return i

def RouletteWheelSelection(P):
    r = random.random()
    c = np.cumsum(P, axis=0)
    i = np.argwhere(c>=r)
    i = i[0,0]
    return i



def SinglePointCrossover(x1,x2):
    
    nVar = len(x1)
    c = int(np.random.randint(0, nVar))
    
    y1 = np.concatenate((x1[0:c], x2[(c):nVar]),  axis=0)
    
    y2 = np.concatenate((x2[0:c], x1[c:nVar]),  axis=0)
    
    return y1, y2
    

def DoublePointCrossover(x1,x2):
    nVar = len(x1)
    
    cc= np.random.randint(0, nVar, size=2)
    c1 = np.min(cc)
    c2 = np.max(cc)
    
    y1 = np.concatenate((x1[0:c1], x2[c1:c2], x1[c2:nVar]),  axis=0)
    y2 = np.concatenate((x2[0:c1], x1[c1:c2], x2[c2:nVar]),  axis=0)
    
    return y1, y2

def UniformCrossover(x1,x2):
    nVar = len(x1)
    
    alpha = np.random.randint(2, size=nVar)
    
    y1 = np.multiply(alpha, x1) + np.multiply(1-alpha, x2)
    
    y2 = np.multiply(alpha, x2) + np.multiply(1-alpha, x1)
    
    return y1, y2


def Crossover(x1,x2, which):
    
    if which == 1:
        y1, y2 = SinglePointCrossover(x1,x2)
        
    if which == 2:
        y1, y2=DoublePointCrossover(x1,x2)
        
    if which == 3:
        [y1, y2]=UniformCrossover(x1,x2)
    
    return y1, y2

def encoding(NDim, num_bit, PopSize):
    genotypes =  np.random.randint(2, size=(PopSize, num_bit*NDim))
    
    return genotypes

def decoding(genotypes, NDim, num_bit, Bound):
    
    
    PopSize = genotypes.shape[0]
    #StringLength = genotypes.shape[1]
    phenotypes = np.zeros((PopSize, NDim))
    
    for i in range(PopSize):
        chromosome = genotypes[i,:]
        for j in range(NDim):
            bit_section = str(chromosome[j*num_bit:(j+1)*num_bit])
            bit_section = bit_section.replace(" ", "")
            bit_section = bit_section.replace("[", "")
            bit_section = bit_section.replace("]", "")
            bit_section = bit_section.replace(".", "")
            bit_section = bit_section.replace("\n", "")
            
            temp = int(bit_section, 2)
            
            LowerBound = Bound[0]
            UpperBound = Bound[1]
            
            phenotypes[i, j] = LowerBound + temp*(UpperBound - LowerBound)/(2**num_bit-1)
            
    return phenotypes

def Mutate(x,mu):
    prob = random.random()
    
    if prob <= mu:
        nVar = len(x)
        #nmu = int(np.ceil(mu*nVar))
        j=np.random.choice(nVar, 1)
        y=x
        y[j] = 1 - x[j]
    else:
        y=x
    
    return y


#Parametes
    
#%%
def main():
        
    Nrep = 50     #N.repeticoes
    max_iter = 500
    resultados = np.zeros((Nrep,max_iter))
        
    for rep in range(Nrep):
            
        NDim = 2
        
            
        num_bit = 16
        
        PopSize = 100
        
        
        Bound = np.array([-100, 100])
        
        nc=int(round(0.8*PopSize))
        
        nm = int(round(0.4*PopSize))
        
        mu = 0.05
        
        #% Generate initial solution
        
        genotypes = encoding(NDim, num_bit, PopSize)
        
        phenotypes = decoding(genotypes, NDim, num_bit, Bound)
        
        fitness = np.zeros((PopSize,1))
        
        for i in range(PopSize):
                
            fitness[i] = f(phenotypes[i,:])
        
        SortOrder = np.argsort(fitness, axis=0)
        
        phenotypes = phenotypes[SortOrder,:]
        
        phenotypes = phenotypes.reshape(PopSize, NDim)
        
        genotypes = genotypes[SortOrder,:]
        genotypes = genotypes.reshape(PopSize, NDim*num_bit)
        
        best_fitness = np.zeros((max_iter, 1))
#        worst_fitness = fitness[-1]
        
    #    print("Selecione o método desejado:")
    #    print("1: Seleção por Roleta Viciada")
    #    print("2: Seleção por Torneio")
    #    print("3: Seleção Aleatória")
        
    #    option = int(input("Entre com a opção: "))
        option = 2
        
        if option == 1:
            
            beta = 0.5
            
        if option == 2:
            
            TournamentSize = 3
            
            
    #    print("Selecione o método de cruzamento:")
    #    print("1: Single Point Crossover")
    #    print("2: Double Point Crossover")
    #    print("3: Uniform Crossover")
    #    
    #    which = int(input("Entre com a opção: "))
            
        which = 3
            
        offspring_1 =  np.zeros((nc//2, NDim*num_bit))
        offspring_2 =  np.zeros((nc//2, NDim*num_bit))
        
        offspring_m =  np.zeros((nm, NDim*num_bit))
        
        ts = PopSize+nc+nm
        
        fitness_p = np.zeros((ts,1))
        
        for it in range(max_iter):
            
            if option == 1:
        #        P=np.exp(-beta*fitness/worst_fitness)
        #        P = P/np.sum(P)
                P = fitness/np.sum(fitness)
        
            
            # selection
            parents = genotypes[0:nc,:]
            
            offspring = parents
            
            #apply crossover
            
            #randomly select two individuals as parents
        
            for k in range(nc//2):
            
                if option == 1:
                    i1 = RouletteWheelSelection(P)
                    i2 = RouletteWheelSelection(P)
                    
                if option == 2:
                    i1 = TournamentSelection(genotypes, fitness, TournamentSize)
                    i2 = TournamentSelection(genotypes, fitness, TournamentSize)
                    
        
                if option == 3:
        #            idx = np.random.randint(0, high=nc, size=(2, 1))
                    i1 = random.randint(0, nc-1)
                    i2 = random.randint(0, nc-1)
                    #cross_point = np.random.randint(0, high=num_bit)
        
                
                parent_1 = genotypes[i1,:]
                parent_2 = genotypes[i2,:]
                offspring_1[k,:], offspring_2[k,:] = Crossover(parent_1, parent_2, which)
                
                
        #    offspring[idx[0], cross_point:-1] = parents[idx[1], cross_point:-1]
        #    offspring[idx[1], cross_point:-1] = parents[idx[0], cross_point:-1]
            
            
            
            #apply mutation
            
            #parents = genotypes[0:nm,:]
            
            offspring = genotypes
            
            
            for k in range(nm):
                i = np.random.randint(1, PopSize)
                
                mutant = offspring[k,:]
                
                offspring_m[k, :] = Mutate(mutant, mu)
                
                #randomly select a bit
        #        
        #        mutation_bit_1 = np.random.randint(0, high=num_bit)
        #        mutation_bit_2 = np.random.randint(num_bit, high=2*num_bit)
        #        
        #        offspring_m[i, mutation_bit_1] = not offspring[i, mutation_bit_1]
        #        offspring_m[i, mutation_bit_2] = not offspring[i, mutation_bit_2]
                
             # Replace the worst individuals
             
            #genotypes[len(genotypes)-nc:len(genotypes),:] = offspring
         
            
            genotypes_aux = np.zeros((ts,NDim*num_bit))
            
            genotypes_aux = np.concatenate((genotypes, offspring_1,  offspring_2,  offspring_m), axis=0)
             
            phenotypes = decoding(genotypes_aux, NDim, num_bit, Bound) 
            
            
             
            for i in range(ts):
                 
                fitness_p[i] = f(phenotypes[i,:])
                 
            
            SortOrder = np.argsort(fitness_p, axis=0).reshape(ts)
            
            fitness_p = fitness_p[SortOrder]
            fitness_aux = fitness_p[0:PopSize]
            fitness = fitness_aux.reshape(PopSize)
        
            phenotypes_aux = phenotypes[SortOrder,:]
            phenotypes_aux = phenotypes_aux[0:PopSize,:]
            phenotypes = phenotypes_aux.reshape(PopSize, NDim)
            
            genotypes_aux = genotypes_aux[SortOrder,:]
            genotypes_aux = genotypes_aux[0:PopSize,:]
            genotypes = genotypes_aux.reshape(PopSize, NDim*num_bit)
            
        #    fitness = fitness_p[0:PopSize]
        #    genotypes = genotypes[0:PopSize,:]
        #    phenotypes = phenotypes[0:PopSize,:]
        #    
            
            best_fitness[it] = fitness[0]
        
            print("Repetição: "+str(rep)+" Iteração:" + str(it))
            print("Melhor Custo: "+ str(best_fitness[it]))
            
            resultados[rep, it] =  best_fitness[it]
        
        print("" + str(rep))
    
    best_results = np.argsort(resultados[:,-1], axis=0)
    np.savetxt("ga_Schaffer.csv", resultados, delimiter=",")
    
    plt.figure()
    plt.grid(True)
    plt.semilogy(resultados[best_results[0],:])
    plt.xlabel("Iteração")
    plt.ylabel("Custo")
    plt.title("Custo por Iteração - Função Schaffer #2: Algoritmo Genético")


if __name__ == '__main__':
    main()       
