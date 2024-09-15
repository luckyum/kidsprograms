import random
from fpdf import FPDF

# 难度级别名称
level_names = {
    1: "10 以内加减法",
    2: "10 分解组合法",
    3: "20以内 凑10法",
    4: "20以内 退位减法",
    5: "20以内 进位、退位加减法",
    6: "20以内加减法综合练习",
    7: "100以内不进位加法",
    8: "100以内不退位减法",
    9: "100以内不退位加减法练习",
    10: "100以内进位加法",
    11: "100以内退位减法",
    12: "100以内进退位加减法练习",
    13: "100以内加减法综合练习",
}

# 难度级别的题目生成逻辑
def generate_problem(level):
    if level == 1:
        # 10以内加减法
        while True:
            # 随机选择加法或减法
            operation = random.choice(['+', '-'])
            
            if operation == '+':
                # 生成两个随机数（1到9），确保和不大于10
                num1 = random.randint(1, 9)
                num2 = random.randint(1, 9)
                if num1 + num2 <= 10:
                    return f"{num1} + {num2} ="
            else:
                # 生成两个随机数（1到9），确保结果不小于1以避免结果为0
                num1 = random.randint(2, 9)
                num2 = random.randint(1, num1 - 1)  # num2 不大于 num1-1 以确保结果大于0
                return f"{num1} - {num2} ="
            
    elif level == 2:
        # 10分解组合法
        while True:
            # 随机选择加法或减法
            num1 = random.randint(1, 9)
            num2 = 10 - num1
            if num2 > 0:
                return f"{num1} + {num2} ="
                
    elif level == 3:
        # 凑10法
        while True:
            num1 = random.randint(1, 9) 
            num2 = random.randint(1, 9) 
            
            if num1 + num2 <= 20 and num1 + num2 > 10:
                return f"{num1} + {num2} ="

    elif level == 4:
        # 退位减法
        num1 = random.randint(11, 15) 
        num2 = random.randint(6, 9)  # 减数必须小于被减数
        
        return f"{num1} - {num2} ="

    elif level == 5:
        # 20以内进位、退位加减法
        level = random.randint(3, 4) 
        return generate_problem(level)        

    elif level == 6:
        # 20以内加减法综合练习
        level = random.randint(1,5)
        if level == 5:
            while True:
                num1 = random.randint(11, 15) 
                num2 = random.randint(6, 9)  # 减数必须小于被减数
                
                if num1 + num2 <= 20:
                    return f"{num1} + {num2} =" 
        else: 
            return generate_problem(level)     

    elif level == 7:
        # 100以内不进位加法
        while True:
            num1 = random.randint(10, 90)
            num2 = random.randint(10, 90)
            tmp = int(num1 / 10) + int(num2 / 10) + 1

            if num1 + num2 <= 100 and tmp * 10 > num1 + num2:
                return f"{num1} + {num2} ="

    elif level == 8:
        # 100以内不退位减法
        while True:
            num1 = random.randint(12, 90)
            num2 = random.randint(10, num1 - 1)
            tmp = int(num1 / 10) - int(num2 / 10)

            if num1 - num2 <= 100 and tmp * 10 < num1 - num2:
                return f"{num1} - {num2} ="

    elif level == 9:
        # 100以内不退位加减法练习
        level = random.randint(7, 8) 
        return generate_problem(level)   

    elif level == 10:
        # 100以内进位加法
        while True:
            num1 = random.randint(10, 90)
            num2 = random.randint(10, 90)
            tmp = int(num1 / 10) + int(num2 / 10) + 1

            if num1 + num2 <= 100 and tmp * 10 < num1 + num2:
                return f"{num1} + {num2} ="  
    elif level == 11:
        # 100以内退位减法
        while True:
            num1 = random.randint(12, 90)
            num2 = random.randint(10, num1 - 1)
            tmp = int(num1 / 10) - int(num2 / 10)

            if num1 - num2 <= 100 and tmp * 10 > num1 - num2:
                return f"{num1} - {num2} ="
            
    elif level == 12:
        # 100以内进退位加减法练习
        level = random.randint(10, 11) 
        return generate_problem(level)  
    
    elif level == 13:
        # 100以内加减法综合练习
        level = random.randint(9, 12) 
        return generate_problem(level)  


# 生成 PDF 文件，标题包含难度级别
def generate_pdf(problems, level, pages, filename="math_problems.pdf"):
    pdf = FPDF()

    problems_per_page = 120
    problems_per_column = 24  # 每列24个题目
    num_columns = 5  # 列数
    column_width = 40  # 每列的宽度
    row_height = 10  # 每行的高度

    # 每页生成新的一组题目
    for page in range(pages):
        pdf.add_page()
        pdf.add_font('NotoSansSC', '', 'NotoSansSC-VariableFont_wght.ttf', uni=True)
        pdf.set_font('NotoSansSC', '', size=18)

        # PDF 标题包含难度级别和页码
        title = f"5分钟口算题 【{level_names[level]}】"
        pdf.cell(200, 10, txt=title, ln=True, align='C')

        pdf.set_font('NotoSansSC', '', size=14)

        start = page * problems_per_page
        end = start + problems_per_page
        page_problems = problems[start:end]

        # 分5列打印
        for row in range(problems_per_column):
            for col in range(num_columns):
                index = col * problems_per_column + row
                if index < len(page_problems):
                    # 设置列的起始位置
                    x_offset = 10 + col * column_width
                    y_offset = 30 + row * row_height  # 设置Y位置
                    pdf.set_xy(x_offset, y_offset)
                    pdf.cell(column_width, row_height, txt=f"{page_problems[index]}", ln=False)
                    
                    pdf.set_y(y_offset)
                    if index == 12:
                        pdf.set_line_width(1)
                    else:    
                        pdf.set_line_width(0.5)
                    pdf.line(10, y_offset, 200, y_offset)  # 画线的起点和终点

        y_offset =  30 + problems_per_column * row_height 
        pdf.set_y(y_offset)
        pdf.set_line_width(0.5)
        pdf.line(10, y_offset, 200, y_offset)  # 画线的起点和终点
    pdf.output(filename)
    print(f"PDF 文件已保存为 {filename}")

# 主函数，输入页数和难度级别，并生成题目
def main():
    # 打印难度级别说明
    print("""
    1年级 难度级别:
    1. 10以内加减法,如 3+5,8-2
    2. 10分解组合法,比 7+3=10、6+4=10
    3. 凑10法,如 8+6,先凑成 10,即 8+2=10,再加上剩余的4
    4. 退位减法，如 15-7,先借位,用10-7=3,在计算 5+3=8
    5. 20以内进位、退位加减法
    6. 20以内加减法综合练习
    7. 100以内不进位加法
    8. 100以内不退位减法
    9. 100以内不退位加减法练习
    10. 100以内进位加法
    11. 100以内退位减法
    12. 100以内进退位加减法练习
    13. 100以内加减法综合练习
    """)

    level = int(input("请选择难度级别 (1-13): "))
    pages = int(input("请输入要生成的页数(1-10): "))

    # 每页 120 道题目，总共生成 页数 * 120 道题目
    total_problems = pages * 120
    problems = [generate_problem(level) for _ in range(total_problems)]

    # 生成包含多页的 PDF
    generate_pdf(problems, level, pages)

if __name__ == "__main__":
    main()
