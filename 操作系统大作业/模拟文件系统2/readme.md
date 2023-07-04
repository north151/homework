```python
# 模拟操作系统设计了两种方法
# src1 为第一种方法代码,可以成功运行
# src2 为第二种方法代码,时间不充裕,还存在bug

# src1(功能全部正常)
    main.py   main文件
    file.py   文件操作
    folder.py 目录操作
 
# src2(代码尚需改进)
    main.py        main文件
    file.py        文件操作
    folder.py      目录操作
    filesystem.py  文件系统

# readme.md   说明文档


运行方式: python main.py
```



# 1.题目要求

```python
设计实现一个模拟的文件系统,并对其进行基本功能的验证。
要求: 有设计文档,程序能运行,输出结果正确。

实现一个模拟的文件系统:
1.它被整个存储在磁盘上一个普通文件中。
2.这个磁盘文件会包含: 目录、i节点、空闲块信息和文件数据块等。
3.选择合适的算法来维护空闲块信息和分配数据库: 连续的、索引的、链表的。
4.你的程序会接受来自用户的系统命令: 
	创建、删除目录; 
	列出目录的内容;
	创建、删除、打开文件; 
	读取、写入一个指定文件;

```



# 2.第一种设计

```
关于文件的大小,这里假定所有字符均占2字节
```

```
定义 文件类,目录类,文件系统类 来实现模拟文件系统的搭建
```



## 命令

```bash
查看目录: man
清空屏目: clear
退出系统: exit

创建目录: mkdir [目录名]
删除目录: rmdir [目录名]
显示目录: ls    [目录名] (默认.)
切换目录: cd    [目录名] (默认/)

创建文件: touch [文件名]
删除文件: rm    [文件名]
读取文件: cat   [文件名]
写入文件: echo  [写入内容] [文件名]

```



## 部分代码定义

### 文件系统

```python
class FileSystem():
    def __init__(self,username="root",maxdisk=1024,maxflag=20):
        self.username = username                        # 系统用户名
        self.home = Folder(father=None, name=username)  # 系统主目录
        self.path = username                            # 当前绝对路径
        self.curfolder = self.home                      # 当前目录
```

### 目录

```python
class Folder:
    def __init__(self, father, name):
        self.father = father   # 父目录
        self.name = name       # 目录名
        self.datetime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")  # 日期
        self.type = "DIR"      # 类型
        self.size = 0          # 大小
        self.sonfolders = []   # 子目录
        self.sonfiles = []     # 子文件
```

### 文件

```python
class File:
    def __init__(self,father,name,size=0,type="TXT"):
        self.name = name
        self.father = father
        self.content = []
        self.datetime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        self.type = type
        self.size = 0
```



## 部分示例

<img src="./.image/1.png" alt="1" style="zoom:80%;" />



# 3.第二种设计

```python
为例方便观察块的管理,这里假定任何一个字符均为 128B
由于时间不充裕,此种设计方法还存在bug未解决
```

```
定义 磁盘类   来创建磁盘,实际为一个二维矩阵
定义 超级块类 来创建超级块,存储在磁盘矩阵(0,0)位置
定义 FCB类   来实现文件到inode的映射,存储在磁盘矩阵(0,1)位置
定义 块类    来实现数据存储,每个数据块包含下一个存储数据的块位置 和 当前块存储的内容

定义 inode类 来创建inode,全部inode按申请顺序存储在磁盘矩阵(0,2~5)位置,每个磁盘块可以存储8各inode
定义 文件类  在创建文件时存储文件名,文件路径信息
定义 目录类  来创建目录

定义 文件系统类 来创建组合 超级块,FCB,Inode,和数据存储块

```



## 命令

```bash
查看目录: man
清空屏目: clear
退出系统: exit

创建目录: mkdir [目录名]
删除目录: rmdir [目录名]
显示目录: ls    [目录名] (默认.)
切换目录: cd    [目录名] (默认/)

创建文件: touch [文件名]
删除文件: rm    [文件名]
读取文件: cat   [文件名]
写入文件: echo  [写入内容] [文件名]
查看信息: stat  [文件名] 
```



## 部分代码定义

### 超级块

```python
# 除定义外有方法: 
# applyinode申请inode; releaseinode释放inode; 
# applyblock申请block; release释放block
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
```

### FCB

```python
class FCB():
    def __init__(self):
        self.map = []
    # 添加文件到inode的映射 
    def addmap(self,maplist):
        self.map.append(maplist)
        return
    # 获取文件对应的inode
    def getmap(self,filepath,isrm=False):
        for maplist in self.map:
            if maplist[0] == filepath:
                inode = maplist[1]
                if isrm == True:
                    self.map.pop(self.map.index(maplist))
                return inode
```

### 磁盘块

```python
# 单块数据块
class DataBlock():
    def __init__(self):
        self.nextblockID = None  # 下一个块的位置
        self.content = ""        # 块内存储内容
# 整个磁盘块
class DataDisk():
    def __init__(self,superblock,fcb):
        # 磁盘块(单个数据块被占有时被添加到磁盘块对应位置)
        self.datablockcontent=[[None,None,None,None,None,None,None,None],
                               [None,None,None,None,None,None,None,None],
                               [None,None,None,None,None,None,None,None],
                               [None,None,None,None,None,None,None,None]]
        self.datablockcontent[0][0] = superblock  # 第一个为超级块
        self.datablockcontent[0][1] = fcb         # 第二个为FCB; 3~6为inode存储,在inode申请时才正式占用
```

### 文件系统

```python
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
```

### 目录

```python
class Folder:
    def __init__(self, father, name, path):
        self.father = father # 父目录
        self.name = name     # 目录名
        self.path = path     # 绝对路径
        self.ctime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")  # 创建时间
        self.atime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")  # 上一次访问时间
        self.mtime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")  # 上一次修改时间
        self.type = "DIR"    # 类型
        self.size = 0        # 大小
        self.sonfolders = [] # 子目录
        self.sonfiles = []   # 子文件
```

### 文件

```python
# inode
class InodeBlock():
    def __init__(self,inodeID,firstblockID,type,owner):
        self.inodeID = inodeID           # inode号
        self.firstblockID = firstblockID # 起始block位置
        self.countblock = 1              # 占用block个数
        self.size = 0                    # 文件大小
        self.type = type                 # 文件类型
        self.onwer = owner               # 拥有者
        self.ctime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")  # 上一次inode变动时间
        self.atime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")  # 上一次访问时间
        self.mtime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")  # 上一次文件内容变动时间
        
# 文件
class File:
    def __init__(self,father,name,path):
        self.name = name
        self.father = father
        self.path = path
```



## 部分正确示例

<img src="./.image/2.png" alt="1" style="zoom:80%;" />