import os
import json
def rename(path):
    file_list=os.listdir(path)
    for i in range(0,10):
        for i,fi in enumerate(file_list):
            old_dir=os.path.join(path,fi)
            filename=str(i+1)+"."+str(fi.split(".")[-1])
            new_dir=os.path.join(path,filename)
            try:
                os.rename(old_dir,new_dir)
            except Exception as e:
                print(e)
                print("Failed!")
            else:
                print("Sucess!")



if __name__=="__main__":

    path="./fantaspic/"
    rename(path)
    path="./husband/"
    rename(path)

    fantaspicpath = './fantaspic/'      # 输入文件夹地址
    fantaspicfiles = os.listdir(fantaspicpath)   # 读入文件夹
    num_png = len(fantaspicfiles)       # 统计文件夹中的文件个数
    fantaspic_dict = {'picNum':num_png}
    fantaspic_json_str = json.dumps(fantaspic_dict)
    print(fantaspic_json_str)
    with open("./fantaspics.json","w") as file:
        json.dump(fantaspic_dict,file)
        print("写入成功")
    husbandpath = './husband/'      # 输入文件夹地址
    husbandfiles = os.listdir(husbandpath)   # 读入文件夹
    num_png = len(husbandfiles)       # 统计文件夹中的文件个数
    husband_dict = {'picNum':num_png}
    husband_json_str = json.dumps(husband_dict)
    print(husband_json_str)
    with open("./husbands.json","w") as file:
        json.dump(husband_dict,file)
        print("写入成功")