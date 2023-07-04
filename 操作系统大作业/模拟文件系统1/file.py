

import datetime

########################################################################################
class File:
    def __init__(self,father,name,size=0,type="TXT"):
        self.name = name
        self.father = father
        self.content = []
        self.datetime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        self.type = type
        self.size = 0

########################################################################################
# 创建文件
def touch(fs,newfile_name,newfile_size=1024):
    flag = False
    for newfile in fs.curfolder.sonfiles:
        if newfile_name == newfile.name:
            flag = True
            break

    if flag == True:                                                                               # 已存在:
        print("文件已存在,创建失败!")                                                                    # 报错
    else:                                                                                          # 未存在:
        newfile_type = "TXT"                                                                         # 文件类型
        if "." in newfile_name:
            newfile_type = newfile_name.split(".")[-1].upper()
        newfile = File(father=fs.curfolder, name=newfile_name,size=newfile_size,type=newfile_type)   # 创建文件
        fs.curfolder.sonfiles.append(newfile)                                                        # 记录到父目录
        fs.curfolder.datetime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")                   # 父目录更新时间
        # print("文件创建成功!")                                                                          # 成功
    return                                                                                         # 结束





####################################################################################
# 删除文件
def rm(fs,delfile_name):
    for delfile in fs.curfolder.sonfiles:
        if delfile_name == delfile.name:                                              # 存在:
            fs.curfolder.size -= delfile.size                                           # 释放内存
            fs.curfolder.sonfiles.pop(fs.curfolder.sonfiles.index(delfile))             # 父目录删除记录
            fs.curfolder.datetime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")  # 父目录更新时间
            # print("文件删除成功!")                                                        # 成功
            return
                                                                                      # 不存在:
    print("文件不存在,删除失败!")                                                          # 失败:
    return





#################################################################################
# 读取文件
def cat(fs,file_name):
    flag = False
    for file in fs.curfolder.sonfiles:
        if file_name == file.name:
            flag = True
            for line in file.content:
                print(line,end="")
            break
    if flag == False:
        print("文件不存在,读取失败!")
    return





################################################################################
# 写入文件
def echo(fs,content,file_name):
    flag = False
    for file in fs.curfolder.sonfiles:
        if file_name == file.name:
            flag = True
            content = content.strip("\"\'") + "\n"
            file.size += 2*len(content)
            file.content.append(content)
            fs.curfolder.size += 2*len(content)
            break
    if flag == False:
        print("文件不存在,写入失败!")
    return






###############################################################################
# 打开文件
def stat():
    pass





##############################################################################



