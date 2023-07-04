
import os
import math
from folder import *
from file import *
from filesystem import *

#################################################################################
# 超级块
class SuperBlock():
    def __init__(self):
        self.blocksize = 1024   # 单个块大小
        self.numblocks = 32     # 块总数目
        self.numusedblocks = 2  # 已用块数目
        self.numfreeblocks = 30 # 空闲块数目

        self.blockIDs = [i for i in range(0,32)]     # 全部block号
        self.usedblockIDs = [0,1]                    # 已用block号
        self.freeblockIDs = [i for i in range(2,32)] # 剩余block号

        # 位图: 第(0,0)为超级块,第(0,1)为fcb块,第(0,2~5)为inode块,其余为数据存储块
        self.datablockmap = [[1, 1, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0]]


        self.inodesize = 128              # 单个inode大小
        self.numinodes = 26               # inode总数(此处设置只是为了方便实验,并不符合实际)
        self.numusedinodes = 0            # 已用inode数
        self.numfreeinodes = 26           # 剩余inode数

        self.inodeIDs = [i for i in range(7, 32 + 1)]  # 全部inode号
        self.usedinodeIDs = []                         # 已用inode号
        self.freeinodeIDs = [i for i in range(7,32+1)] # 剩余inode号


    # 申请inode
    def applyinode(self):
        if self.numfreeinodes == 0:
            print("无多余inode,申请失败")
            return
        # 剩余更新
        newinodeID = self.freeinodeIDs[0]
        self.numfreeinodes -= 1
        self.freeinodeIDs = self.freeinodeIDs[1:]
        # 已用更新
        self.numusedinodes+=1
        self.usedinodeIDs.append(newinodeID)
        self.usedinodeIDs = sorted(self.usedinodeIDs)
        return newinodeID

    # 释放inode
    def releaseinode(self,inodeID):
        # 剩余更新
        self.numfreeinodes += 1
        self.freeinodeIDs.append(inodeID)
        self.freeinodeIDs = sorted(self.freeinodeIDs)
        # 已用更新
        self.numusedinodes -=1
        self.usedinodeIDs.pop(self.usedinodeIDs.index(inodeID))
        return

    # 申请block
    def applyblock(self,fs):
        if self.numfreeblocks == 0:
            print("无多余block,申请失败")
            return
        newblockID, m, n = -1, -1, -1
        # 位示图更新
        for i in range(6,self.numblocks):
            m,n = int(i/8),i%8
            # print(m,n)
            if self.datablockmap[m][n] == 0:
                self.datablockmap[m][n] = 1
                newblockID = i
                # print(newblockID)
                break
        # datadisk更新
        fs.datadisk.datablockcontent[m][n] = DataBlock()

        # 剩余更新
        self.numfreeblocks -= 1
        self.freeblockIDs = self.freeblockIDs[1:]
        # 已用更新
        self.numusedblocks += 1
        self.usedblockIDs.append(newblockID)
        self.usedblockIDs = sorted(self.usedblockIDs)
        return newblockID


    # 释放block
    def releaseblock(self,fs,firstblockID):
        blockID = firstblockID
        while blockID!= None:
            # block位置
            m,n = int(blockID/8),blockID%8
            # 取出block
            datablock = fs.datadisk.datablockcontent[m][n]


            # 磁盘清空
            fs.datadisk.datablockcontent[m][n] = None
            # 位示图更新
            self.datablockmap[m][n] = 0

            # 剩余更新
            self.numfreeblocks += 1
            self.freeblockIDs.append(blockID)
            self.freeblockIDs = sorted(self.freeblockIDs)

            # 已用更新
            self.numusedblocks -= 1
            self.usedblockIDs.pop(self.usedblockIDs.index(blockID))

            # 下一块
            blockID = datablock.nextblockID
        return




#################################################################################
# FCB
class FCB():
    def __init__(self):
        self.map = []

    def addmap(self,maplist):
        self.map.append(maplist)
        return

    def getmap(self,filepath,isrm=False):
        for maplist in self.map:
            if maplist[0] == filepath:
                inode = maplist[1]
                if isrm == True:
                    self.map.pop(self.map.index(maplist))
                return inode




#################################################################################
# 单块数据块
class DataBlock():
    def __init__(self):
        self.nextblockID = None
        self.content = ""

# 整个磁盘块
class DataDisk():
    def __init__(self,superblock,fcb):
        self.datablockcontent=[[None,None,None,None,None,None,None,None],
                               [None,None,None,None,None,None,None,None],
                               [None,None,None,None,None,None,None,None],
                               [None,None,None,None,None,None,None,None]]
        self.datablockcontent[0][0] = superblock
        self.datablockcontent[0][1] = fcb





#################################################################################
# 文件系统
class FileSystem():
    def __init__(self,username="root"):
        self.username = username                                           # 用户名
        self.home = Folder(father=None, name=username, path="/"+username)  # 主目录
        self.curfolder = self.home                                         # 当前目录
        # 超级块
        self.superblock = SuperBlock()
        # FCB
        self.fcb = FCB()
        # 数据块
        self.datadisk = DataDisk(self.superblock,self.fcb)


    def clear(self):
        os.system("cls")

    def man(self):
        print("     系统操作     ")
        print("查询: man")
        print("清屏: clear")
        print("退出: exit\n")

        print("     目录操作     ")
        print("创建目录: mkdir [目录名]")
        print("删除目录: rmdir [目录名]:")
        print("显示目录: ls    [目录名](默认.)")
        print("切换目录: cd    [目录名](默认当前用户主目录)\n")

        print("     文件操作     ")
        print("创建文件: touch [文件名] [大小]")
        print("删除文件: rm    [文件名]")
        print("打开文件: stat  [文件名]")
        print("读取文件: cat   [文件名]")
        print("写入文件: echo  [写入内容] > [文件名]\n")
