close all
clear all
clc

%% Load datas
clonalg = load('clonalg_ackley.csv');
de = load('de_ackley.csv');
ga = load('ga_ackley.csv');
pso = load('pso_ackley.csv');
tlbo = load('tlbo_ackley.csv');

%% Calculando min,max,mean,std

%Data to compare method



for i = 1:500   
    %Data with x iterations
    data.clonalg.melhor(i) = min(clonalg(:, i));
    data.clonalg.pior(i) = max(clonalg(:, i));
    data.clonalg.media(i) = mean(clonalg(:, i));
    data.clonalg.desvio(i) = std(clonalg(:, i));
end

for i = 1:500   
    %Data with x iterations
    data.de.melhor(i) = min(de(:, i));
    data.de.pior(i) = max(de(:, i));
    data.de.media(i) = mean(de(:, i));
    data.de.desvio(i) = std(de(:, i));
end

for i = 1:500   
    %Data with x iterations
    data.ga.melhor(i) = min(ga(:, i));
    data.ga.pior(i) = max(ga(:, i));
    data.ga.media(i) = mean(ga(:, i));
    data.ga.desvio(i) = std(ga(:, i));
end

for i = 1:500   
    %Data with x iterations
    data.ga.melhor(i) = min(ga(:, i));
    data.ga.pior(i) = max(ga(:, i));
    data.ga.media(i) = mean(ga(:, i));
    data.ga.desvio(i) = std(ga(:, i));
end
for i = 1:500   
    %Data with x iterations
    data.pso.melhor(i) = min(pso(:, i));
    data.pso.pior(i) = max(pso(:, i));
    data.pso.media(i) = mean(pso(:, i));
    data.pso.desvio(i) = std(pso(:, i));
end

for i = 1:500   
    %Data with x iterations
    data.tlbo.melhor(i) = min(tlbo(:, i));
    data.tlbo.pior(i) = max(tlbo(:, i));
    data.tlbo.media(i) = mean(tlbo(:, i));
    data.tlbo.desvio(i) = std(tlbo(:, i));
end

%%
figure(1)
semilogy(data.clonalg.media,'LineWidth',1.5)
legend('Clonalg')
hold on
semilogy(data.de.media,'LineWidth',1.5)
legend('Evo. Diferencial')
semilogy(data.ga.media,'LineWidth',1.5)
legend('Alg. Genético')
semilogy(data.pso.media,'LineWidth',1.5)
legend('PSO')
semilogy(data.tlbo.media,'LineWidth',1.5)
legend('Clonalg','Evo. Diferencial','Alg. Genético','PSO','TLBO')
title('Média de desempenho das Funções para Função Ackley')
xlabel('Geração')
ylabel('Melhor F(x)')
grid on

%%
last_it.clonalg = clonalg(:,end);
last_it.de = de(:,end);
last_it.ga = ga(:,end);
last_it.pso = pso(:,end);
last_it.tlbo = tlbo(:,end);
boxplot([last_it.ga])

[~,~,stats] = anova1([last_it.clonalg, last_it.de, last_it.ga, last_it.pso, last_it.tlbo]);
c = multcompare(stats);
boxplot([last_it.clonalg, last_it.de, last_it.ga, last_it.pso, last_it.tlbo])


