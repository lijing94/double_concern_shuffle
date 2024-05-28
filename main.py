#from typing import TypeVar, overload
from glob import glob0
from access_excel import *
from add_nums import *
from random_loop import *


variance_best       = 500           #本次迭代最好方差
std_best            = 500           #迭代过程最好标准差
abs_best            = 500           #迭代过程最好最大绝对值差
data_result_best    = []

def mux_by_text(compare_by_what = 'abs',x1=0,x2=0,x3=0):
    match compare_by_what:
        case "abs":
            x = x1   
        case "std":
            x = x2
        case "variance":
            x = x3
    return x
def get_the_best(real=0,best=0,*data):
    if(best > real):
        print(real,best)
        best = real
        return data
    
def main():
    group_num           = 10            #分几组
    per_group_mouse_num = 7             #每组几只
    data                = []
    global data_result_best
    
    

    #读取文件
    data = read_excel_file(*data)

    #加入编号
    add_nums(*data)
    data = add_col_num_1to10(group_num,*data)


    #按瘤子重量正序排序
    data_sorted = sorted(data,key=lambda x:x[4])
    print_list(*data_sorted)
    
    # 循环随机
    random_loop(group_num,per_group_mouse_num,*data_sorted)

    #保存文件
    save_excel_file(*data_result_best)
    

if __name__ == "__main__":
    main()




    







