# 导入save模块
import save

# 输入总费用，人名
fee = input("请输入总费用：")
name = input("请输入姓名（用空格分割）：")

# 将人名放入列表，得到数量
peoplelist = name.split(" ")
num = len(peoplelist)

# 计算人均费用
avgfee = int(fee) / num
print("已记账，请及时查看！")

save.savetofile(peoplelist, avgfee)
