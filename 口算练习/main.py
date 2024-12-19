import os

def main():
    # 打印难度级别说明
    print("""
    1. 一年级 5分钟口算练习:
    2. 二年级 口算与竖式练习:
    """)

    strpages = int(input("请输入进入的页面(1-2): "))

    if strpages == '':
        pages =1
    else:
        pages = int(strpages)

    if pages == 1:
        os.system('python3 practice1.py')
    elif pages == 2:
        os.system('python3 practice2.py')


if __name__ == "__main__":
    main()