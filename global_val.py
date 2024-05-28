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
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    df = pd.DataFrame(data_result)
    print(df)