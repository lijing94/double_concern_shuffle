from avg_calc import *
from shuffle_list import *
from group import *
from global_val import *


def iteration(per_group_mouse_num,group_num,compare_by_what = 'abs',\
                                    MAX_ITERITER_NUM    = 100000,\
                                    print_num           = 20000,\
                                    *data_sorted):
    variance_acceptable = 5.8           #可接受的方差
    variance_real       = 500           #本次迭代实际方差
    #best.variance_best
    #best.std_best
    #best.abs_best
    global variance_best
    global std_best
    global abs_best
    global data_result_best 

    
    std_acceptable      = 2.4           #可接受的标准差
    
    std_real            = 500           #本次迭代实际标准差
    
    abs_acceptable      = 2.5           #可接受的最大绝对值差
    
    abs_real            = 500           #本次迭代实际最大绝对值差
    data_result         = []

    iteration_num = 1

    while (True):
        #打乱顺序
        data_sorted = shuffle_by_group(per_group_mouse_num,*data_sorted)
    
        #按分组数进行分组
        data_result = group_by_group_nums(group_num,per_group_mouse_num,*data_sorted)

        #计算方差平均值
        variance_real,std_real,abs_real = avg_calc(per_group_mouse_num,group_num,0,*data_result)

        #迭代次数累加
        iteration_num = iteration_num +1

        #记录最好结果
        if(variance_best > variance_real) &(abs_best > abs_real) & (std_best > std_real):
            data_result_best = data_result
            abs_best = abs_real
            std_best = std_real
            variance_best = variance_real
            
    
            
        # 每个500次打印
        if(iteration_num%print_num == 0):
            print("正在进行第"+str(iteration_num)+"次"+compare_by_what+"迭代，目前最好结果：方差"+str(round(variance_best,2))+"标准差"+str(round(std_best,2))+"最大绝对值差"+str(round(abs_best,2)))
        
        #Reaching maximum Iterations
        if(iteration_num > MAX_ITERITER_NUM):
            print("达到最大迭代次数："+str(iteration_num - 1))
            break

    if(len(data_result_best) > per_group_mouse_num*group_num):
        print("迭代过程中发生错误！")
        print_list(*data_result_best)
    return data_result_best

# 循环随机
def random_loop(per_group_mouse_num = 7, \
                group_num           = 10, \
                *data_sorted):
    compare_by_what     = ['abs','std','variance']
    for key in compare_by_what:
        print("        进行"+key+"迭代")
        data_result_best = iteration(per_group_mouse_num,group_num,key,100000,20000,*data_sorted)
        #打印结果
        avg_calc(per_group_mouse_num,group_num,1,*data_result_best)
    return data_result_best