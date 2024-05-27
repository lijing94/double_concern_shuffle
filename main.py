#from typing import TypeVar, overload
from access_excel import *
from add_nums import *
from avg_calc import *
from shuffle_list import *
from group import *

def print_list(*data_result):
    for key in data_result:
        print(key['num'],key)


def iteration(per_group_mouse_num,group_num,compare_by_what = 'abs',*data_sorted):
    MAX_ITERITER_NUM    = 100000        #最大迭代次数
    variance_acceptable = 6.5           #可接受的方差
    variance_real       = 500           #本次迭代实际方差
    variance_best       = 500           #本次迭代最好方差
    std_acceptable      = 2.5           #可接受的标准差
    std_best            = 500           #迭代过程最好标准差
    std_real            = 500           #本次迭代实际标准差
    abs_acceptable      = 2.5           #可接受的最大绝对值差
    abs_best            = 500           #迭代过程最好最大绝对值差
    abs_real            = 500           #本次迭代实际最大绝对值差
    data_sorted         = []
    data_result         = []
    data_result_best    = []
    
    real                = 500
    best                = 500 
    acceptable          = 0

    iteration_num = 1

    while (real >= acceptable):
        #print("第"+str(iteration_num)+"次迭代")
        #打乱顺序
        data_sorted = shuffle_by_group(per_group_mouse_num,*data_sorted)
    
        #按分组数进行分组
        data_result = group_by_group_nums(group_num,per_group_mouse_num,*data_sorted)

        #计算方差平均值
        variance_real,std_real,abs_real = avg_calc(per_group_mouse_num,group_num,0,*data_result)

        match compare_by_what:
            case "abs":
                real       =  abs_real       
                acceptable =  abs_acceptable 
                best       =  abs_best       
            case "std":
                real       =  std_real       
                acceptable =  std_acceptable 
                best       =  std_best       
            case "variance":
                real       =  variance_real       
                acceptable =  variance_acceptable 
                best       =  variance_best

        #迭代次数累加
        iteration_num = iteration_num +1

        #记录最好结果
        if(best > real):
            data_result_best = data_result
            match compare_by_what:
                case "abs":
                    abs_best       =  real       
                case "std":
                    std_best       =  real       
                case "variance":
                    variance_best  =  real
        if(iteration_num%50000 == 0):
            print("正在进行第"+str(iteration_num)+"次迭代，目前最好结果：方差"+str(round(variance_best,2))+"标准差"+str(round(std_best,2))+"最大绝对值差"+str(round(abs_best,2)))
        if(iteration_num > MAX_ITERITER_NUM):
            print("迭代次数："+str(iteration_num))
            break

    if(len(data_result_best) > per_group_mouse_num*group_num):
        print("迭代过程中发生错误！")
        print_list(*data_result_best)
    return data_result_best
    
def main():
    group_num           = 10            #分几组
    per_group_mouse_num = 7             #每组几只
    data                = []
    compare_by_what     = ['abs','std','variance']

    #读取文件
    data = read_excel_file(*data)
    #print(data)
    data = add_col_num_1to10(group_num,*data)

    #加入编号
    add_nums(*data)
    #print(data)

    #按瘤子重量正序排序
    data_sorted = sorted(data,key=lambda x:x[4])
    for key in compare_by_what:
        data_result_best = iteration(per_group_mouse_num,group_num,key,*data_sorted)
        #打印结果
        #print_list(*data_result_best)
        avg_calc(per_group_mouse_num,group_num,1,*data_result_best)

    #保存文件
    save_excel_file(*data_result_best)
    

if __name__ == "__main__":
    main()




    







