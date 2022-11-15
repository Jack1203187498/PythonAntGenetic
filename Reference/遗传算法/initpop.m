%初始化种群大小
%输入变量：
%popsize：种群大小
%chromlength：染色体长度-->>转化的二进制长度
%输出变量：
%pop：种群
function pop=initpop(popsize,chromlength)
pop = round(rand(popsize,chromlength));
%rand(3,4)生成3行4列的0-1之间的随机数
% rand(3,4)
%
% ans =
%
%     0.8147    0.9134    0.2785    0.9649
%     0.9058    0.6324    0.5469    0.1576
%     0.1270    0.0975    0.9575    0.9706
%round就是四舍五入
% round(rand(3,4))=
% 1 1 0 1
% 1 1 1 0
% 0 0 1 1
%所以返回的种群就是每行是一个个体，列数是染色体长度