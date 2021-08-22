import datetime

# 打印日期
a = datetime.date.today().strftime("%Y%m%d")

# 打印时间
b = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")

# 打印
print(a)
print(b)
