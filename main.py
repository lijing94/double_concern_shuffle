#from typing import TypeVar, overload
from glob import glob0
from access_excel import *
from add_nums import *
from global_val import *
from random_loop import *
import pandas as pd

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
    group_by_which_column = 5
    get_avg_value_column  = 2                
    data                = []
    global data_result_best
    data_result = []
    data_result_for_sort_calc = []
    data_result_for_sort_calc_2 = []
    
    
    #print header
    print("==============双因素随机分组软件================\n作者:lijing \n版本v0.1 ")
    print("目前只支持单因素分组,按照接近中心平均值的方式进行随机分组(目前仅支持一次随机),双因素分布统计(方差,绝对值偏离总体平均值)")
    print("用法:将数据拷贝到表格aaa.xlsx中(不带抬头)输入要分几组,每组多少个")
    print("遇到问题请到github提交issue:https://github.com/lijing94/double_concern_shuffle/issues")
    print("或联系邮箱:lijing94@outlook.com ")
    print("==============================================")
    #读取文件
    data = read_excel_file(*data)

    #get value from keyboard
    print("请输入要分几组(默认值10):")
    group_num = int(get_input(10))    
    print("请输入每组有多少个(默认值7):")
    per_group_mouse_num = int(get_input(7))
    print("依据哪列进行分组?:(默认值5):")
    group_by_which_column = int(get_input(5))
    print("还想统计哪组数据的平均值?:(默认值2):")
    get_avg_value_column = int(get_input(2))

    if(len(data) != group_num*per_group_mouse_num):
        print("分组错误,表格数据总量"+str(len(data))+"输入的分组总数为"+str(group_num*per_group_mouse_num))

    #加入编号
    add_nums(*data)
    data = add_col_num_1to10(group_num,*data)


    #按瘤子重量正序排序
    data_sorted = sorted(data,key=lambda x:x[4])
    
    #print("==========正序排序完成结果打印===============")
    #print(len(data_sorted))
    #print_format_excel(*data_sorted)

    # 循环随机
    #data_result_best = random_loop(per_group_mouse_num,group_num,*data_sorted)

    (data_result,data_result_for_sort_calc,data_result_for_sort_calc_2) = group_by_group_nums_to_2dims_list(group_num,per_group_mouse_num,group_by_which_column,get_avg_value_column,*data_sorted)
    print("==================================分组结果1==================================")
    data_result_for_sort_calc = avg_row_calc_for_2dim_list(group_num,*data_result_for_sort_calc)
    print("==================================分组结果2==================================")
    data_result_for_sort_calc_2 = avg_row_calc_for_2dim_list(group_num,*data_result_for_sort_calc_2)
    #print(len(data_result)) 
    #print_format_excel(*data_result) 

    #保存文件
    #save_excel_file('综合',*data_result)
    file_path = GetExcelPath(1) 
    write = pd.ExcelWriter(file_path)
    
    pd.DataFrame(data_result_for_sort_calc).to_excel(write,\
                                sheet_name = '因素1统计',\
                                header=None,\
                                index = None)
    pd.DataFrame(data_result_for_sort_calc_2).to_excel(write,\
                                sheet_name = '因素2统计',\
                                header=None,\
                                index = None)
    pd.DataFrame(data_result).to_excel(write,\
                                sheet_name = '综合',\
                                header=None,\
                                index = None)
    write._save()
    write.close()
    print("保存文件成功！")
    _close_ = input("按下enter键退出: ")
    #save_excel_file('统计',*data_result_for_sort_calc)
    

if __name__ == "__main__":
    main()




    







