import pandas as pd
#class best:
variance_best       = 500           #本次迭代最好方差
std_best            = 500           #迭代过程最好标准差
abs_best            = 500           #迭代过程最好最大绝对值差
data_result_best    = []

def print_list(*data_result):
    for key in data_result:
        print(key)

def print_format_excel(*data_result):
    pd.set_option('display.max_rows', 10000)
    pd.set_option('display.max_columns', 10000)
    pd.set_option('display.width',1000)
    df = pd.DataFrame(data_result)
    print(df,end='')

def  get_input(default_value):
    user_input  =  input()  #  提示用户输入
    if  user_input == "":
        return  default_value  #  若用户未输入,则返回就以值
    else:
        return  user_input  #  若用户输入了内容,则返回用户输入
