

import datetime

#######################################################################################
class Folder:
    def __init__(self, father, name):
        # 父目录
        self.father = father
        # 目录名
        self.name = name
        # 日期
        self.datetime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        # 类型
        self.type = "DIR"
        # 大小
        self.size = 0
        # 子目录
        self.sonfolders = []
        # 子文件
        self.sonfiles = []



########################################################################################
# 创建目录
def mkdir(fs,newfolder_name):
    flag = False
    for newfolder in fs.curfolder.sonfolders:
        if newfolder_name == newfolder.name:
            flag = True
            break

    if flag == True:                                                               # 已存在
        print("文件夹已存在,创建失败!")                                                  # 报错
    else:                                                                          # 未存在:
        newfolder = Folder(father=fs.curfolder,name=newfolder_name)                  # 创建子目录
        fs.curfolder.sonfolders.append(newfolder)                                    # 记录到父目录
        fs.curfolder.datetime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")   # 父目录更新时间
        # print("文件夹创建成功!")                                                        # 成功
    return                                                                         # 结束





########################################################################################
# 删除目录
def rmdir(fs,delfolder_name):
    for delfolder in fs.curfolder.sonfolders:
        if delfolder.name == delfolder_name:                                          # 存在:
            fs.curfolder.size -= delfolder.size                                         #释放内存
            fs.curfolder.sonfolders.pop(fs.curfolder.sonfolders.index(delfolder))       # 父目录删除记录
            fs.curfolder.datetime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")  # 父目录更新时间
            # print("文件夹删除成功!")                                                       # 成功
            return                                                                    # 不存在:
    print("文件夹不存在，删除失败!")                                                         # 失败:
    return





########################################################################################
# # 显示目录
def ls(fs):
    list = []
    for folder in fs.curfolder.sonfolders:
        list.append([folder.name,folder.datetime,folder.type,folder.size])
    for file in fs.curfolder.sonfiles:
        list.append([file.name,file.datetime,file.type,file.size])
    list = sorted(list)
    print(format("名称","<19"),format("日期","<29"),format("类型","<18"),format("大小","<20"))
    for i in list:
        print(format(i[0],"<20"),format(i[1],"<30"),format(i[2],"<20"),i[3],"B")
    return





#######################################################################################
# 切换目录
def cd(fs,cdfolder_name):
    if cdfolder_name == ".":                                             # 当前目录:
        pass                                                               # 成功

    elif cdfolder_name == "..":                                          # 父目录:
        if fs.curfolder.father == None:                                    # 不存在:
            print("目录不存在,切换失败!")                                        # 失败
        else:                                                              # 存在:
            fs.path = fs.path[:(len(fs.path) - len(fs.curfolder.name)) - 1]  # 路径改变
            fs.curfolder = fs.curfolder.father                               # 当前目录改变

    elif cdfolder_name == "/":                                           # 根目录:
        print("没有权限,切换失败")                                            # 失败

    elif cdfolder_name == "~":                                           # 用户目录:
        fs.path = fs.username                                              # 路径改变
        fs.curfolder = fs.home                                             # 当前目录改变

    else:                                                                # 子目录:
        flag = False
        for cdfolder in fs.curfolder.sonfolders:
            if cdfolder.name == cdfolder_name:                             # 存在:
                flag = True
                fs.path = fs.path + '/' + cdfolder.name                      # 路径改变
                fs.curfolder = cdfolder                                      # 当前目录改变
        if flag == False:                                                  # 不存在:
            print("目录不存在,切换失败!")                                        # 失败

    return                                                                 # 结束






###################################################################################







