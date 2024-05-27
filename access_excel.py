import pandas as pd 
import os

def GetExcelPath(inout = 0):
    PATH = ''
    if inout == 1:
        PATH =  os.path.join(os.path.expanduser("~"), 'Desktop')+"\\double_concern_shuffle\\bbb.xlsx"
    else:
        PATH =  os.path.join(os.path.expanduser("~"), 'Desktop')+"\\double_concern_shuffle\\aaa.xlsx"
    PATH.replace("\\\\","\\")
    #print(PATH)
    return PATH
#读文件
def read_excel_file(*data):
    print("read start")
    #with open(r"C:\Users\lijing\OneDrive\桌面\double_concern_shuffle\aaa.xlsx","r",encoding='UTF-8') as file:
    file_path = GetExcelPath(0) 
    #file_path = r"C:\Users\lijing\OneDrive\桌面\double_concern_shuffle\aaa.xlsx"
    #print(file_path)
    df = pd.read_excel(file_path,header=None)
    pd.set_option('display.max_rows', 500)
    data = df.to_dict('records')
    print("read over")
    #file.close()
    return data


def save_excel_file(*data):
    #with open(r"C:\Users\lijing\OneDrive\桌面\double_concern_shuffle\bbb.xlsx","w+") as file:
    print("save start")
    #with open(r"C:\Users\lijing\OneDrive\桌面\double_concern_shuffle\aaa.xlsx","r",encoding='UTF-8') as file:
    file_path = GetExcelPath(0) 
    pd.DataFrame(data).to_excel(file_path,\
                                sheet_name = 'Sheet2',\
                                header=None,\
                                index = None)
    print("保存文件成功！")