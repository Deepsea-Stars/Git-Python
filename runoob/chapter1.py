# 联系实例 1
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且不重复的三位数？并输出。

# 分析：
# 可填在百位、个位、十位的数字都是1、2、3、4。组成排列后去掉不满足条件的。

# 方法一：
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                print(i, j, k)

# 方法二：
list = []
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                list.append([i, j, k])
print("组合数量为：" + str(len(list)))
print(list)
