import os
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
       