%��������Ӧ�Ⱥ���
%���������pop:��Ⱥ��fitvalue:��Ⱥ��Ӧ��
%���������bestindividual:��Ѹ��壬bestfit:�����Ӧ��ֵ
function [bestindividual bestfit] = best(pop,fitvalue)
[px,py] = size(pop);
%px
%py
bestindividual = pop(1,:);
bestfit = fitvalue(1);
for i = 1:px
    if fitvalue(i)>bestfit
        bestindividual = pop(i,:);
        bestfit = fitvalue(i);
    end
end