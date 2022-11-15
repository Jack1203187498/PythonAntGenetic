function main()
clear;
clc;
%��Ⱥ��С
popsize=1000;
%�����Ʊ��볤��
chromlength=10;
%�������
pc = 0.6;
%�������
pm = 0.01;
%��ʼ��Ⱥ
pop = initpop(popsize,chromlength);
pop
for i = 1:500
    %������Ӧ��ֵ������ֵ��
    objvalue = cal_objvalue(pop);
    fitvalue = objvalue;
    %ѡ�����
    %pop
    %fitvalue
    newpop = selection(pop,fitvalue);
    %newpop
    %objvalue1 = cal_objvalue(newpop);
    %objvalue1
    %�������
    newpop = crossover(newpop,pc);
    %�������
    newpop = mutation(newpop,pm);
    %������Ⱥ
    pop = newpop;
    %Ѱ�����Ž�
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
        title(['��������Ϊn=' num2str(i)]);
    end
end
fprintf('The best X is --->>%5.2f\n',x2);
fprintf('The best Y is --->>%5.2f\n',bestfit);
