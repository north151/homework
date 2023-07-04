

import datetime

from file import *




#######################################################################################
class Folder:
    def __init__(self, father, name, path):
        # 父目录
        self.father = father
        # 目录名
        self.name = name
        # 绝对路径
        self.path = path
        # 日期
        self.ctime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")  # 创建时间
        self.atime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")  # 上一次访问时间
        self.mtime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")  # 上一次修改时间
        # 类型
        self.type = "DIR"
        # 大小
        self.size = 0
        # 子目录名称
        self.sonfolders = []
        # 子文件名称
        self.sonfiles = []




########################################################################################
# 创建目录
def mkdir(fs,newfolder_name):
    for newfolder in fs.curfolder.sonfolders:
        if newfolder_name == newfolder.name:
            print("文件夹已存在,创建失败!")
            return
    newfolder = Folder(father=fs.curfolder,name=newfolder_name,path=fs.curfolder.path+"/"+newfolder_name)
    # 添加新目录
    fs.curfolder.sonfolders.append(newfolder)
    # 父目录更新时间
    fs.curfolder.atime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
    fs.curfolder.atime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
    # print("文件夹创建成功!")                                                        #
    return





########################################################################################
# 删除目录
def rmdir(fs,delfolder_name):
    for delfolder in fs.curfolder.sonfolders:
        if delfolder.name == delfolder_name:
            # 父目录
            fs.curfolder.size -= delfolder.size                                         # 释放内存
            fs.curfolder.sonfolders.pop(fs.curfolder.sonfolders.index(delfolder))       # 父目录删除记录
            fs.curfolder.atime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")     # 父目录更新访问时间
            fs.curfolder.atime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")     # 父目录更新修改时间


            curfolder = fs.curfolder
            fs.curfolder = delfolder
            # 释放该目录下所有文件
            for file in delfolder.sonfiles:
                rm(fs,file.name)
            # 删除该目录下所有目录
            for folder in delfolder.sonfolders:
                rmdir(fs,folder.name)
            fs.curfolder = curfolder

            # print("文件夹删除成功!")                                                       # 成功
            return                                                                    # 不存在:
    print("文件夹不存在，删除失败!")                                                         # 失败:
    return





########################################################################################
# # 显示目录
def ls(fs):
    lsit,list1,list2 = [],[],[]
    for folder in fs.curfolder.sonfolders:
        list1.append([folder.name,folder.mtime,folder.type,folder.size])

    for file in fs.curfolder.sonfiles:
        inode = fs.fcb.getmap(filepath=file.path, isrm=False)
        list2.append([file.name,inode.mtime,inode.type,inode.size])

    list = list1 + list2
    list = sorted(list)
    print(format("名称","<19"),format("日期","<29"),format("类型","<18"),format("大小","<20"))
    for i in list:
        print(format(i[0],"<20"),format(i[1],"<30"),format(i[2],"<20"),i[3],"B")
    return





#######################################################################################
# 切换目录
def cd(fs,cdfolder_name):
    if cdfolder_name == ".":
        pass

    elif cdfolder_name == "..":
        if fs.curfolder.father == None:
            print("目录不存在,切换失败!")
        else:
            fs.curfolder = fs.curfolder.father

    elif cdfolder_name == "/":
        print("没有权限,切换失败")

    elif cdfolder_name == "~":
        fs.curfolder = fs.home

    else:
        flag = False
        for cdfolder in fs.curfolder.sonfolders:
            if cdfolder.name == cdfolder_name:
                flag = True
                fs.curfolder = cdfolder
        if flag == False:
            print("目录不存在,切换失败!")

    return






###################################################################################







