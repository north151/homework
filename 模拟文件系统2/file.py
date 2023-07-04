

import datetime
import re
from filesystem import *
from folder import *

########################################################################################
class InodeBlock():
    def __init__(self,inodeID,firstblockID,type,owner):
        self.inodeID = inodeID           # inode号
        self.firstblockID = firstblockID # 起始block位置
        self.countblock = 1              # 占用block个数
        self.size = 0                    # 文件大小
        self.type = type                 # 文件类型
        self.onwer = owner               # 拥有者
        # 日期
        self.ctime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")  # 上一次inode变动时间
        self.atime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")  # 上一次访问时间
        self.mtime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")  # 上一次文件内容变动时间



class File:
    def __init__(self,father,name,path):
        self.name = name
        self.father = father
        self.path = path


########################################################################################
# 创建文件
def touch(fs,newfile_name):
    flag = False
    for newfile in fs.curfolder.sonfiles:
        if newfile_name == newfile.name:
            flag = True
            break

    if flag == True:
        print("文件已存在,创建失败!")
    else:
        newfile_type = "TXT"
        if "." in newfile_name:
            newfile_type = newfile_name.split(".")[-1].upper()
        # 创建文件
        newfile = File(father=fs.curfolder, name=newfile_name,path=fs.curfolder.path+"/"+newfile_name)
        # 父目录更新记录,访问时间,修改时间
        fs.curfolder.sonfiles.append(newfile)
        fs.curfolder.atime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        fs.curfolder.atime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

        # 申请inodeID
        inodeID = fs.superblock.applyinode()
        # 申请blockID(并标记占用block)
        blockID = fs.superblock.applyblock(fs)
        # 创建inode节点
        inode = InodeBlock(inodeID=inodeID,firstblockID=blockID,type=newfile_type,owner=fs.username)

        # 映射文件名到i节点
        fs.fcb.addmap([newfile.path,inode])
        # print("文件创建成功!")
    return



####################################################################################
# 删除文件
def rm(fs,delfile_name):
    for delfile in fs.curfolder.sonfiles:
        if delfile_name == delfile.name:
            # 获取inode,并取消文件映射
            inode = fs.fcb.getmap(filepath=delfile.path,isrm=True)

            # 父目录更新记录,访问时间,修改时间
            fs.curfolder.size -= inode.size
            fs.curfolder.sonfiles.pop(fs.curfolder.sonfiles.index(delfile))
            fs.curfolder.atime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
            fs.curfolder.atime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

            # 释放inodeID
            fs.superblock.releaseinode(inode.inodeID)
            # 释放blockID(并取消占用block)
            fs.superblock.releaseblock(fs,inode.firstblockID)

            # print("文件删除成功!")                                                        # 成功
            return
                                                                                      # 不存在:
    print("文件不存在,删除失败!")                                                          # 失败:
    return





#################################################################################
# 读取文件
def cat(fs,file_name):
    for file in fs.curfolder.sonfiles:
        if file_name == file.name:
            # 获取inode
            inode = fs.fcb.getmap(filepath=file.path, isrm=False)
            m,n = int(inode.firstblockID/8),inode.firstblockID%8
            while True:
                datablock = fs.datadisk.datablockcontent[m][n]
                print(datablock.content)

                if datablock.nextblockID == None:
                    break
                else:
                    m, n = int(datablock.nextblockID / 8), datablock.nextblockID % 8
            return

    print("文件不存在,读取失败!")
    return





################################################################################
# 写入文件 (为了方便观察实验效果,这里假定每个字符/汉字占128B)
def echo(fs,content,file_name):
    for file in fs.curfolder.sonfiles:
        if file_name == file.name:
            content = content.strip("\"\'") + "\n"
            # 获取inode
            inode = fs.fcb.getmap(filepath=file.path, isrm=False)
            # 获取最后一个block
            datablock = None
            m, n = int(inode.firstblockID / 8), inode.firstblockID % 8
            while True:
                datablock = fs.datadisk.datablockcontent[m][n]
                if datablock.nextblockID == None:
                    break
                else:
                    m, n = int(datablock.nextblockID / 8), datablock.nextblockID % 8
            # 写入当前块
            l1 = (fs.superblock.blocksize - 128*len(datablock.content))/128
            datablock.content = datablock.content + content[:l1]
            # 写入其他块
            content2 = re.findall(r'\w{8}',content)
            content2.append(content[8*len(content2):])
            for i in range(0,len(content2)):
                # 申请块
                blockID = fs.superblock.applyblock(fs)
                datablock.nextblockID = blockID
                # 进入下一个块
                m, n = int(datablock.nextblockID / 8), datablock.nextblockID % 8
                datablock = fs.datadisk.datablockcontent[m][n]
                datablock.content = content2[i]
            # 更新inode
            inode.countblock += len(content2)
            inode.size += 128*len(content)
            # 更新父目录
            fs.curfolder.size += 128*len(content)
            return

    print("文件不存在,写入失败!")
    return






###############################################################################
# 打开文件
def stat(fs,file_name):
    for file in fs.curfolder.sonfiles:
        if file_name == file.name:
            # 获取inode
            inode = fs.fcb.getmap(filepath=file.path, isrm=False)
            print("inodeID: ",inode.inodeID)
            print("inodefirstblockID: ",inode.firstblockID)
            print("countblock: ",inode.countblock)
            print("ctime: ",inode.ctime)
            print("atime: ",inode.atime)
            print("mtime: ",inode.atime)
            return




##############################################################################



