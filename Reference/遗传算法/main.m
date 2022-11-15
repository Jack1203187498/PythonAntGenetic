function main()
clear;
clc;
%种群大小
popsize=1000;
%二进制编码长度
chromlength=10;
%交叉概率
pc = 0.6;
%变异概率
pm = 0.01;
%初始种群
pop = initpop(popsize,chromlength);
pop
for i = 1:500
    %计算适应度值（函数值）
    objvalue = cal_objvalue(pop);
    fitvalue = objvalue;
    %选择操作
    %pop
    %fitvalue
    newpop = selection(pop,fitvalue);
    %newpop
    %objvalue1 = cal_objvalue(newpop);
    %objvalue1
    %交叉操作
    newpop = crossover(newpop,pc);
    %变异操作
    newpop = mutation(newpop,pm);
    %更新种群
    pop = newpop;
    %寻找最优解
    [bestindividual,bestfit] = best(pop,fitvalue);
    x2 = binary2decimal(bestindividual);
    x1 = binary2decimal(newpop);
    y1 = cal_objvalue(newpop);
    if mod(i,500) == 0
        figure;
        fplot('10*sin(5*x)+7*abs(x-5)+10',[0 10]);
        hold on;
        plot(x2,bestfit,'*r');
        plot(x1,y1,'*');
        title(['迭代次数为n=' num2str(i)]);
    end
end
fprintf('The best X is --->>%5.2f\n',x2);
fprintf('The best Y is --->>%5.2f\n',bestfit);
