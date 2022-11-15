# Python实现蚁群算法和遗传算法

大概是做过的最不情愿的作业之一了

照着MATLAB敲的Python

很奇怪目前蚁群算法的机器人寻路，蚂蚁经常找不到终点，相比MATLAB里面实现不好

找到bug了，但是略微改了几处，导致已经不记得根本原因是哪个了，凑活用，能跑就行

## 遗传算法
和MATLAB实现基本一致，最终输出当前迭代次数下，获得点的分布，并标记当前最优解

![image-20221115102847228](https://jack-jake-bucket.oss-cn-beijing.aliyuncs.com/Picture/MarkdownPictureimage-20221115102847228.png)

## 蚁群算法

蚁群算法中MATLAB内有多个文件，其中：
+ antMain.py对应main，为机器人寻路算法，其中定义了三个参数用来决定绘制结果：
  + figure1：绘制最优路径更新情况
  + figure2：绘制蚂蚁最优路径
  + figure3：绘制每次迭代中的蚂蚁最优路径
+ antMain1.py对应main1.m，使用mode参数决定是否将每一步显示
  + mode 1：显示蚂蚁的爬行过程，运行很慢
  + mode 2：显示最终蚂蚁运行结果
+ antMain2.py对应main2.m，分成了局部搜索和全局搜索，使用转移状态概率决定是否进行全局搜索，使用mode参数决定是否将每一步显示
  + mode 1：显示蚂蚁的爬行过程，运行很慢
  + mode 2：显示最终蚂蚁运行结果
+ antMain3.py对应main01.m，也就是不更新荷尔蒙，使用mode参数决定是否将每一步显示
  + mode 1：显示蚂蚁的爬行过程，运行很慢
  + mode 2：显示最终蚂蚁运行结果

antMain.py机器人寻路算法结果如下所示：

![image-20221115103234295](https://jack-jake-bucket.oss-cn-beijing.aliyuncs.com/Picture/MarkdownPictureimage-20221115103234295.png)

antMain1.py蚁群算法结果如下：

![image-20221115103320314](https://jack-jake-bucket.oss-cn-beijing.aliyuncs.com/Picture/MarkdownPictureimage-20221115103320314.png)

antMain2.py蚁群算法结果如下：

![image-20221115103356524](https://jack-jake-bucket.oss-cn-beijing.aliyuncs.com/Picture/MarkdownPictureimage-20221115103356524.png)

antMain3.py蚁群算法结果如下：

![image-20221115103417001](https://jack-jake-bucket.oss-cn-beijing.aliyuncs.com/Picture/MarkdownPictureimage-20221115103417001.png)