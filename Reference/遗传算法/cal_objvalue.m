%���㺯��Ŀ��ֵ
%�����������������ֵ
%���������Ŀ�꺯��ֵ
function [objvalue] = cal_objvalue(pop)
x = binary2decimal(pop);
%ת����������Ϊx�����ı仯��Χ����ֵ
objvalue=10*sin(5*x)+7*abs(x-5)+10;