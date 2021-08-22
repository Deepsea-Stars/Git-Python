def registerUser():
    phone = input("请输入您的手机号码（不得超过十一位）：\n")
    if len(phone) > 11:
        print("输入无效")
        print("请重新输入")

    print("程序结束")


registerUser()
