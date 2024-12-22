import random
from fpdf import FPDF

# 难度级别名称
level_names = {
    1: "100以内连加",
    2: "100以内连减",
    3: "100以内连加连减",
    4: "2 ~ 5乘法",
    5: "6 ~ 9乘法",
    6: "九九乘法表",
    7: "个位乘法求商",
    8: "个位数除法",
}

# 难度级别的题目生成逻辑
def generate_problem(level):
    if level == 1:
        # 100以内连加
        sum_result = 0
        num1 = 0
        num2 = 0
        num3 = 0
        while sum_result > 100 or sum_result == 0:
            num1 = random.randint(5, 99) 
            num2 = random.randint(5, 99) 
            num3 = random.randint(5, 99) 
            sum_result = num1 + num2 + num3
        
        return f"{num1} + {num2} + {num3} ="

    elif level == 2:
        # 100以内连减
        sum_result = 0
        num1 = 0
        num2 = 0
        num3 = 0
        while sum_result > 100 or sum_result <= 0:
            num1 = random.randint(5, 99) 
            num2 = random.randint(5, 98) 
            num3 = random.randint(5, 97) 
            if num1 - num2 <= 0:
                continue
            sum_result = num1 - num2 - num3

        return f"{num1} - {num2} - {num3} ="
                
    elif level == 3:
        # 100以内连加连减
        sum_result = 0
        while sum_result > 100 or sum_result == 0:
            num1 = random.randint(5, 99) 
            num2 = random.randint(5, 97) 
            num3 = random.randint(5, 97) 

            operation1 = random.choice(['+', '-'])
            operation2 = random.choice(['+', '-'])

            if operation1 == '+':
                sum_result = num1 + num2
            elif operation1 == '-':
                sum_result = num1 - num2

            if operation2 == '+':
                sum_result = sum_result + num3
            elif operation2 == '-':
                sum_result = sum_result - num3

            return f"{num1} {operation1} {num2} {operation2} {num3} ="

    elif level == 4:
        # 2 ~ 5乘法
        num1 = random.randint(2, 5) 
        num2 = random.randint(2, 5)
        
        return f"{num1} * {num2} ="

    elif level == 5:
        # 6 ~ 9乘法
        num1 = random.randint(6, 9) 
        num2 = random.randint(6, 9)
        return f"{num1} * {num2} ="   

    elif level == 6:
        # 九九乘法表
        num1 = random.randint(2, 9) 
        num2 = random.randint(2, 9)
        return f"{num1} * {num2} ="     

    elif level == 7:
        # 个位乘法求商
        num1 = random.randint(2, 9) 
        num2 = random.randint(2, 9)
        sum_result = num1 * num2
        return f"{num1} * (        ) = {sum_result}"  

    elif level == 8:
        # 个位数除法
        num1 = random.randint(2, 9) 
        num2 = random.randint(2, 9)
        sum_result = num1 * num2
        return f"{sum_result} ÷ {num1} ="  


# 生成 PDF 文件，标题包含难度级别
def generate_pdf(problems, level, pages, filename="math_problems.pdf"):
    pdf = FPDF()

    if level != 1 and level != 2:
        problems_per_page = 120
        problems_per_column = 24  # 每列24个题目
        num_columns = 5  # 列数
        column_width = 40  # 每列的宽度
        row_height = 10  # 每行的高度
    else:
        problems_per_page = 36
        problems_per_column = 9  # 每列行数
        num_columns = 4  # 列数
        column_width = 50  # 每列的宽度
        row_height = 30  # 每行的高度

    # 每页生成新的一组题目
    for page in range(pages):
        pdf.add_page()
        pdf.add_font('NotoSansSC', '', 'NotoSansSC-VariableFont_wght.ttf', uni=True)
        pdf.set_font('NotoSansSC', '', size=18)

        # PDF 标题包含难度级别和页码
        if level != 1 and level != 2:
            title = f"口算题 【{level_names[level]}】"
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

        else:
            title = f"竖式计算 【{level_names[level]}】"
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
                        x_offset = 10+ col * column_width
                        if row == 0:
                            y_offset = 10
                        elif row == problems_per_column-1:
                            y_offset = (20+ row_height) + (row-1) * row_height  # 设置Y位置
                            pdf.set_xy(x_offset, y_offset)
                            pdf.cell(column_width, 10, txt=f"{page_problems[index]}", ln=False)
                            continue
                        else:
                            y_offset = (10+ row_height) + (row-1) * row_height  # 设置Y位置

                        pdf.set_xy(x_offset, y_offset)
                        pdf.cell(column_width, row_height, txt=f"{page_problems[index]}", ln=False)
                        
                        pdf.set_y(y_offset)

            y_offset =  30 + problems_per_column * row_height 
            # pdf.set_y(y_offset)
            # pdf.set_line_width(0.5)
            # pdf.line(10, y_offset, 200, y_offset)  # 画线的起点和终点

    pdf.output(filename)


# 主函数，输入页数和难度级别，并生成题目
def main():
    # 打印难度级别说明
    print("""
    二年级 难度级别:
    1. 100以内连加
    2. 100以内连减
    3. 100以内连加连减
    4. 2-5乘法
    5. 6-9乘法
    6. 九九乘法表
    7. 个位乘法求商
    8. 个位数除法
    """)

    strlevel = input("请选择难度级别 (1-13): ")
    strpages = input("请输入要生成的页数(1-10): ")

    if strlevel == '':
        level = 1
    else:
        level = int(strlevel)
    
    if strpages == '':
        pages =1
    else:
        pages = int(strpages)

    print("选择难度【",level_names[level] ,"】, 打印【",str(pages) ,"】页。")
    filename = "二年级口算练习.pdf"
    print(f"PDF 文件已保存为 【 {filename} 】")

    if level != 1 and level != 2:
        total_problems = pages * 120
        problems = [generate_problem(level) for _ in range(total_problems)]
    else:
        total_problems = pages * 36
        problems = [generate_problem(level) for _ in range(total_problems)]


    # 生成包含多页的 PDF
    generate_pdf(problems, level, pages,filename)

if __name__ == "__main__":
    main()
