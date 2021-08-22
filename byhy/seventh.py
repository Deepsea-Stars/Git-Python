# 断点测试

# 使用第三方库：requests
import requests

# 用requets获取信息
res = requests.get("http://cdn1.python3.vip/files/py/0016_price")
content = res.text

# 下面两个变量记录了当前销量最多的手机和数量
# 初始值都为 None
mostsoldphone = None
mostsoldcount = None

for info in content.splitlines():
    info = info.strip()
    # 去掉空行
    if not info:
        continue

    items = info.split(",")
    # 销量在倒数第二列，获取销量信息
    soldcount = items[-2]
    # 型号在第一列，获取型号信息
    phonetype = items[0]

    # 如果前面有销量最多的手机记录，和当前这款手机比较
    if mostsoldphone:
        # 如果这款手机销量最高，那么把这款手机设置为最热卖手机
        if mostsoldcount < soldcount:
            mostsoldcount = soldcount
            mostsoldphone = phonetype

    # 如果前面没有销量最多的手机，说明这是第条记录
    # 暂时先把它置为最热卖的手机
    else:
        mostsoldcount = soldcount
        mostsoldphone = phonetype

# 输出结果
print(f"最热卖的手机是{mostsoldphone}，销量为{mostsoldcount}")
