%���ڱ���
%����˵��
%���������pop����������Ⱥ��pm���������
%���������newpop�����Ժ����Ⱥ
function [newpop] = mutation(pop,pm)
[px,py] = size(pop);
newpop = ones(size(pop));
for i = 1:px
    if(rand<pm)
        mpoint = round(rand*py);
        if mpoint <= 0;
            mpoint = 1;
        end
        newpop(i,:) = pop(i,:);
        if newpop(i,mpoint) == 0
            newpop(i,mpoint) = 1;
        else newpop(i,mpoint) == 1
            newpop(i,mpoint) = 0;
        end
    else newpop(i,:) = pop(i,:);
    end
end;