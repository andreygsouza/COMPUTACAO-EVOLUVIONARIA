close all
clear all
clc

%% Load datas
load 'pso1.txt'
load 'pso2.txt'
load 'pso3.txt'
load 'pso4.txt'

%% Calculando min,max,mean,std
pos.one = 1;
pos.two = 50;
pos.three = 1;
pos.four = 100;

%Data to compare method
for i = 1:50   
    %Data with x iterations
    data.pso1.melhor(i) = min(pso1(pos.one),pso1(pos.two));
    data.pso1.pior(i) = max(pso1(pos.one),pso1(pos.two));
    data.pso1.media(i) = mean(pso1(pos.one:pos.two));
    data.pso1.desvio(i) = std(pso1(pos.one:pos.two));
    data.pso3.melhor(i) = min(pso3(pos.one),pso3(pos.two));
    data.pso3.pior(i) = max(pso3(pos.one),pso3(pos.two));
    data.pso3.media(i) = mean(pso3(pos.one:pos.two));
    data.pso3.desvio(i) = std(pso3(pos.one:pos.two));
    %Data with 2x iterations
    data.pso2.melhor(i) = min(pso2(pos.three),pso2(pos.four));
    data.pso2.pior(i) = max(pso2(pos.three),pso2(pos.four));
    data.pso2.media(i) = mean(pso2(pos.three:pos.four));
    data.pso2.desvio(i) = std(pso2(pos.one:pos.two));
    data.pso4.melhor(i) = min(pso4(pos.three),pso4(pos.four));
    data.pso4.pior(i) = max(pso4(pos.three),pso4(pos.four));
    data.pso4.media(i) = mean(pso4(pos.three:pos.four));
    data.pso4.desvio(i) = std(pso4(pos.one:pos.two));
    
    pos.one = pos.one+50;
    pos.two = pos.two+50;
    pos.three = pos.three+100;
    pos.four = pos.four+100;
end

%Data to compare algorith
for i = 1:50   
    %Data with x iterations
    data.pso.melhor(i) = min(data.pso1.melhor(i),data.pso1.melhor(i));
    data.pso1.melhor(i) = min(pso1(pos.one),pso1(pos.two));
    data.pso1.pior(i) = max(pso1(pos.one),pso1(pos.two));
    data.pso1.media(i) = mean(pso1(pos.one:pos.two));
    data.pso1.desvio(i) = std(pso1(pos.one:pos.two));
    data.pso3.melhor(i) = min(pso3(pos.one),pso3(pos.two));
    data.pso3.pior(i) = max(pso3(pos.one),pso3(pos.two));
    data.pso3.media(i) = mean(pso3(pos.one:pos.two));
    data.pso3.desvio(i) = std(pso3(pos.one:pos.two));
    %Data with 2x iterations
    data.pso2.melhor(i) = min(pso2(pos.three),pso2(pos.four));
    data.pso2.pior(i) = max(pso2(pos.three),pso2(pos.four));
    data.pso2.media(i) = mean(pso2(pos.three:pos.four));
    data.pso2.desvio(i) = std(pso2(pos.one:pos.two));
    data.pso4.melhor(i) = min(pso4(pos.three),pso4(pos.four));
    data.pso4.pior(i) = max(pso4(pos.three),pso4(pos.four));
    data.pso4.media(i) = mean(pso4(pos.three:pos.four));
    data.pso4.desvio(i) = std(pso4(pos.one:pos.two));
    
    pos.one = pos.one+50;
    pos.two = pos.two+50;
    pos.three = pos.three+100;
    pos.four = pos.four+100;
end


%% Graficos dos melhores resultados (Comparando os parametros)
figure(1)   %Comparando o algoritmo com msm num de iterações para [25,50]
subplot(1,2,1)
plot(data.pso1.melhor); hold on
xlabel('Número de execuções do código')
ylabel('Melhor F(x)')
title('Trajetória dos melhores resultados da função Drop-Wave [50,25]')
subplot(1,2,2)
plot(data.pso3.melhor); hold on
xlabel('Número de execuções do código')
ylabel('Melhor F(x)')
title('Trajetória dos melhores resultados da função Drop-Wave [50,50]')

figure(2)   
subplot(1,2,1)
plot(data.pso2.melhor); hold on
xlabel('Número de execuções do código')
ylabel('Melhor F(x)')
title('Trajetória dos melhores resultados da função Drop-Wave [100,25]')
subplot(1,2,2)
plot(data.pso4.melhor); hold on
xlabel('Número de execuções do código')
ylabel('Melhor F(x)')
title('Trajetória dos melhores resultados da função Drop-Wave [100,50]')

figure(3)   %Comparando o algoritmo com msm num de população para [50,100]
subplot(1,2,1)
plot(data.pso1.melhor); hold on
xlabel('Número de execuções do código')
ylabel('Melhor F(x)')
title('Trajetória dos melhores resultados da função Drop-Wave [25,50]')
subplot(1,2,2)
plot(data.pso2.melhor); hold on
xlabel('Número de execuções do código')
ylabel('Melhor F(x)')
title('Trajetória dos melhores resultados da função Drop-Wave [25,100]')

figure(4)   
subplot(1,2,1)
plot(data.pso3.melhor); hold on
xlabel('Número de execuções do código')
ylabel('Melhor F(x)')
title('Trajetória dos melhores resultados da função Drop-Wave [50,50]')
subplot(1,2,2)
plot(data.pso4.melhor); hold on
xlabel('Número de execuções do código')
ylabel('Melhor F(x)')
title('Trajetória dos melhores resultados da função Drop-Wave [50,100')

%% Graficos dos piores resultados (Comparando os parametros)
figure(5)   %Comparando o algoritmo com msm num de iterações para [25,50]
subplot(1,2,1)
plot(data.pso1.pior); hold on
xlabel('Número de execuções do código')
ylabel('Pior F(x)')
title('Trajetória dos piores resultados da função Drop-Wave [50,25]')
subplot(1,2,2)
plot(data.pso3.pior); hold on
xlabel('Número de execuções do código')
ylabel('Pior F(x)')
title('Trajetória dos piores resultados da função Drop-Wave [50,50]')
 
figure(6)   
subplot(1,2,1)
plot(data.pso2.pior); hold on
xlabel('Número de execuções do código')
ylabel('Pior F(x)')
title('Trajetória dos piores resultados da função Drop-Wave [100,25]')
subplot(1,2,2)
plot(data.pso4.pior); hold on
xlabel('Número de execuções do código')
ylabel('Pior F(x)')
title('Trajetória dos piores resultados da função Drop-Wave [100,50]')
 
figure(7)   %Comparando o algoritmo com msm num de população para [50,100]
subplot(1,2,1)
plot(data.pso1.pior); hold on
xlabel('Número de execuções do código')
ylabel('Pior F(x)')
title('Trajetória dos piores resultados da função Drop-Wave [25,50]')
subplot(1,2,2)
plot(data.pso2.pior); hold on
xlabel('Número de execuções do código')
ylabel('Pior F(x)')
title('Trajetória dos piores resultados da função Drop-Wave [25,100]')
 
figure(8)   
subplot(1,2,1)
plot(data.pso3.pior); hold on
xlabel('Número de execuções do código')
ylabel('Pior F(x)')
title('Trajetória dos piores resultados da função Drop-Wave [50,50]')
subplot(1,2,2)
plot(data.pso4.pior); hold on
xlabel('Número de execuções do código')
ylabel('Pior F(x)')
title('Trajetória dos piores resultados da função Drop-Wave [50,100')
 
%% Graficos das médias dos resultados (Comparando os parametros)
figure(9)   %Comparando o algoritmo com msm num de iterações para [25,50]
subplot(1,2,1)
plot(data.pso1.media); hold on
xlabel('Número de execuções do código')
ylabel('Média F(x)')
title('Trajetória das médias dos resultados da função Drop-Wave [50,25]')
subplot(1,2,2)
plot(data.pso3.media); hold on
xlabel('Número de execuções do código')
ylabel('Média F(x)')
title('Trajetória das médias dos resultados da função Drop-Wave [50,50]')
 
figure(10)   
subplot(1,2,1)
plot(data.pso2.media); hold on
xlabel('Número de execuções do código')
ylabel('Média F(x)')
title('Trajetória das médias resultados da função Drop-Wave [100,25]')
subplot(1,2,2)
plot(data.pso4.media); hold on
xlabel('Número de execuções do código')
ylabel('Média F(x)')
title('Trajetória das médias resultados da função Drop-Wave [100,50]')
 
figure(11)   %Comparando o algoritmo com msm num de população para [50,100]
subplot(1,2,1)
plot(data.pso1.media); hold on
xlabel('Número de execuções do código')
ylabel('Média F(x)')
title('Trajetória das médias dos resultados da função Drop-Wave [25,50]')
subplot(1,2,2)
plot(data.pso2.media); hold on
xlabel('Número de execuções do código')
ylabel('Média F(x)')
title('Trajetória das médias dos resultados da função Drop-Wave [25,100]')
 
figure(12)   
subplot(1,2,1)
plot(data.pso3.media); hold on
xlabel('Número de execuções do código')
ylabel('Média F(x)')
title('Trajetória das médias dos resultados da função Drop-Wave [50,50]')
subplot(1,2,2)
plot(data.pso4.media); hold on
xlabel('Número de execuções do código')
ylabel('Média F(x)')
title('Trajetória das médias dos resultados da função Drop-Wave [50,100')

%% Graficos dos desvios dos resultados (Comparando os parametros)
figure(13)   %Comparando o algoritmo com msm num de iterações para [25,50]
subplot(1,2,1)
plot(data.pso1.desvio); hold on
xlabel('Número de execuções do código')
ylabel('Desvio F(x)')
title('Trajetória dos desvios dos resultados da função Drop-Wave [50,25]')
subplot(1,2,2)
plot(data.pso3.desvio); hold on
xlabel('Número de execuções do código')
ylabel('Desvio F(x)')
title('Trajetória dos desvios dos resultados da função Drop-Wave [50,50]')
 
figure(14)   
subplot(1,2,1)
plot(data.pso2.desvio); hold on
xlabel('Número de execuções do código')
ylabel('Desvio F(x)')
title('Trajetória dos desvios resultados da função Drop-Wave [100,25]')
subplot(1,2,2)
plot(data.pso4.desvio); hold on
xlabel('Número de execuções do código')
ylabel('Desvio F(x)')
title('Trajetória dos desvios resultados da função Drop-Wave [100,50]')
 
figure(15)   %Comparando o algoritmo com msm num de população para [50,100]
subplot(1,2,1)
plot(data.pso1.desvio); hold on
xlabel('Número de execuções do código')
ylabel('Desvio F(x)')
title('Trajetória dos desvios dos resultados da função Drop-Wave [25,50]')
subplot(1,2,2)
plot(data.pso2.desvio); hold on
xlabel('Número de execuções do código')
ylabel('Desvio F(x)')
title('Trajetória dos desvios dos resultados da função Drop-Wave [25,100]')
 
figure(16)   
subplot(1,2,1)
plot(data.pso3.desvio); hold on
xlabel('Número de execuções do código')
ylabel('Desvio F(x)')
title('Trajetória dos desvios dos resultados da função Drop-Wave [50,50]')
subplot(1,2,2)
plot(data.pso4.desvio); hold on
xlabel('Número de execuções do código')
ylabel('Desvio F(x)')
title('Trajetória dos desvios dos resultados da função Drop-Wave [50,100')
 
%% Graficos dos melhores resultados (Comparando os metodos)


%% Graficos dos piores resultados  (Comparando os metodos)


%% Graficos das medias dos resultados  (Comparando os metodos)


%% Graficos dos desvios dos resultados  (Comparando os metodos)

