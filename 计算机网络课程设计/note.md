



## 拓扑



```
线类型:
	直通线：用来连接不同类型的设备，如路由器与交换机。
	
	交叉线：用来连接相同类型的设备,如路由器与路由器、换机与交换机，
		   PC机与路由器属于同类型设备，
		   交换机与集线器属于同类型设备，他们之间也用交叉线相连。
	
	反转线：用来连接可网管设备的console口和主机的com口，
		   主机通过反转电缆与设备的console口相连接以进入设备的控制台对设备进行配置。

	DCE串口线: serial口将两路由器相连
```



```
线端口:
	fastethernet: 快速以太网口,局域网连接端口
	serial:      串行口,于广域网连接端口

```





## 路由

```
1.通过网关ip找到路由器
  数据从PC到达路由器
2.在路由表上找到 [目标ip所在网段] 对应的 [目标路由]
  数据转发到目的路由器
2.通过目标ip找到目标机
  数据转发给目标机
  
多层交换机具有路由功能(转发),但不能做单臂路由
```

![image-20230306160945021](https://cdn.jsdelivr.net/gh/north151/ImageBed/image_Windows2/image-20230306160945021.png)

```
区域1:现在实际有的接口
区域2:可以添加的模块，接口位于模块上,通过添加模块添加接口
区域3:说明
区域4: 模块可插入到的插槽
区域5:电源开关

模块对应接口:
	WIC-1T模块: 有一个serial口
	WIC-2T模块: 有两个serial口
安装模块前需断电,安装后接线前需接电
```

```
# 我的标准
路由相连IP: 192.168. [第几个相连].                        [1,3(单数) 或 2,4(双数)]
网关接口IP: 192.168. [第几台路由器(1位),第几个接口(2位)].  [254]
设备接口IP: 192.168. [第几台路由器(1位),第几个接口(2位)].  [该接口下第几个设备(三位)] 
```







### 静态路由(两路由)

```
网关是虚拟存在的,只要组了网就有网关,可以没有路由器进行通信,

网段: 局域网ip可以改变的那一位,每一位就是一个网段

三层交换机需要配置ip,即网关在交换机


优点: 处理时间短
缺点: 大型网络维护困难
```



```shell
# 没有路由器时的通信:
	只需要通信的设备ip在同一网段就行                    

# 一个路由器下子网的内部通信:
	1.有路由器时,网关就是连接路由器的那个接口,网关地址就是接口地址
	2.同一个路由器的不同接口(即网关地址)必须在不同的网段中 (第二位必须不同)
	3.接口下连接的设备必须在网关所在的网段中              (第三位才能开始不同)


# 多个路由器之间的通信:
	 1.连接两路由器的两接口必须处于同一网段,且设定好时钟频率(64000)
	 2.路由表配置(静态路由),两个路由都要配置到对方的路由表
	   Network: [目标网络中需要通信到的设备的网段:192.168.网段.0]
	   Mask: [子网掩码]
	   Next Hop: 连接到的目标路由器接口的ip
	   
# 无论几个路由器组成内网都不能用相同IP
# 用不同IP可以直接ping通其他路由器下的设备
```





### 单臂路由(单路由vlan-vlan)

```
	一个路由器的接口分为多个子接口(虚拟接口)
	每个子接口是交换机下一个VLAN的网关
	# 交换机上连接到路由器的端口必须为trunk  (哪些vlan可以通过这个接口)
优点: 实现了不同vlan之间的通信
缺点: 容易成为网络单点故障(一处故障整个系统无法工作)
```



```shell
	# 交换机默认所有接口都只允许通过vlan1, 所有设备在vlan里面
	# 所有需要在该交换机通过的vlan,必须在该交换机生命才能trunk通过
	# 经过vlan时会被打上vlan_Tag
	
	1.保证路上所有交换机都允许该vlan通过
	2.保证路由接口/逻辑接口 配置为对应vlan网关

	
	# 配置交换机
    	# 创建虚拟端口
		config
		vlan 2  # 创建虚拟端口2
		exit    # 退出
        
        # 分配到虚拟端口
		int fa0/1  # 选中要被指的端口
		switchport access vlan 2 # 只允许该接口通过vlan2内的设备
		exit  
		
	   # 交换机连接到路由器的接口的配置
		int fa 0/1
		##重要### switchport mode trunk  # 允许该接口通过多个设备
         exit
	
	
    # 配置路由器 子接口
    	interface fastethernet 0/0.1  # 进入子接口,1第一个子接口
        encapsulation dot1Q vlan号    # 子接口对应到交换机vlan
        ip address [设为对应vlan网关ip] [子网掩码]
        exit
        
    
	no shutdown # 把当前端口打开
	

```





### RIP动态路由

```
跳数: 两设备之间通信经过的其他设备  >=16设为不可达
一个路由器建立路由表的过程:
	1.该路由器向相邻路由器广播请求报文
	2.周围路由器将自己的路由表封装到报文,广播回去
	3.该路由器收到报文后形成自己的路由表
	那么该路由就可以访问相邻路由下的网络
	
```

```shell
 ip routing  # 开启多层交换机的 路由功能

router rip #
version 1/2  # 选择rip版本
network ip   # 相连的网段
no auto-summary  # 关闭自动汇总


# 使三层交换机接口可以配ip
1.进入接口
2.no switchport
3.ip address [接口ip] [子网掩码]

# 备份
Switch(config)#int vlan 10
Switch(config-if)#
Switch(config-if)#standby 10 priority 120    # 优先级默认100,越大越先
Switch(config-if)#standby 10 preempt         # vlan 10 优先抢占该设备 

Switch(config-if)#standby track f0/1         # 跟踪接口
Switch(config-if)#standby track f0/2
Switch(config-if)#

Switch(config-if)#standby 10 ip 192.168.10.252  # vlan 10的虚拟地址
```





### OSPF动态路由

```
1.按单臂路由前划分好vlan
2.配置交换机vlan为网关
	interface vlan vlan号  # 选中vlan
	ip address [网关ip] [子网掩码]
3.
```









## 配置

```
主机：IP地址。(桌面条目下)

交换机: 命令行配置
		用户模式: switch> ; 
		特权模式: switch# ;可看配置
		全局配置: switch(config)# ; 对交换机/路由器进行全局配置
		接口配置: switch(config-if)#;对交换机/路由器配置某个接口
		

用户模式 eble 特权模式
特权模式 config terminal 全局配置模式
全局配置 interface 接口配置

exit到上一级模式,end到特权模式

单击ALL/NONE先清除所有的协议类型，然后再单击ICMP，只显示ICMP数据包
```



```
绿点: 物理上连通
橙色: 物理上没问题,但未连通
红点: 链路有问题,无法通信 (检查链路是否up,即接口是否打开)

```









## 命令

```
两种模式:
	实时模式：实时的模式，如现在用PC1Ping PC2结果会立刻显示在PC1的DOS窗口中。
	模拟模式：模拟数据包的传送过程，用PC1去Ping PC2，可以看到数据包是通过怎样的路径被传递给PC2的。

当配置与验证配置时推荐采用实时模式，
当利用仿真软件学习网络协议原理，观察数据包封装格式时，推荐采用模拟模式。(接下来对设备的配置全部在实时模式下进行)


? 查询命令
执行错误配置
重输该配置命令在开头加no ctrl+A 快捷间跳开头
```



### 交换机

```shell
1.切换模式
	Switch>用户模式，只能使用一些查看命令
	Switch>enable  			 # 进入交换机特权模式
	Switch#configureterminal  # 进入交换机全局配置模式
	Switch(config)		     #全局配置模式
	Switch(config)    		 #interface fastEthernet 0/1 进入交换机接口
	Switch(config-if) 		 #端口配置命令模式

2.检查、查看命令
	Switch#showversion           #查看交换机的版本信息
	Switch#showvlan              #查看交换机的vlan信息
	Switch#showrunning-config    #查看交换机当前
	Switch#show interface s0/0   # 显示接口serial上的信息
	Switch#show ip route         # 显示IP路由表
	
	
3.配置IP地址及默认网关
	Switch#conf t
	Switch(config)#interface f0/1                              # 进入指定接口
	Switch(config-if)#ip address 192.168.0.253 255.255.255.0   # 设置该接口ip,该接口子网掩码
	Switch(config-if)#no shutdown                              #
	Switch(config-if)#ip default-gateway 192.168.0.254         # 交换机的网关
	
```



### 路由器

```shell
1.切换模式
	同交换机

2.检查、查看命令
	Router#showversion			# 路由器的版本信息
	Router#showvlan 1        	 # 路由器有关ip协议的配置
	Router#showrunning-config    # 路由器配置信息
	Router#show interface s0/0   # 显示知道接口信息
	Router#show ip route         # 显示IP路由表


4.配置IP地址及默认网关
	Router#conf t                    
	Router(config)#interface f0/1                            # 进入指定接口
	Router(config-if)#ip address 19.168.0.253 255.255.255.0  # 设置该接口ip
	Router(config-if)#no shutdown


5.配置串口参数（DCE的配置）
	Router>enable
	Router#conf t
	Router(config)#interface serial 0/0         # 进入指定接口
	Router(config-if)#clock rate 64000          # 提供时钟频率为64000
	Router(config-if)#no shut


6.配置路由器的静态路由、默认路由、RI路由P协议
静态路由:
	RouterA（config)#ip router   192.168.3.0    255.255.255.0    192.168.2.1
	RouterB (config)#ip router   192.168.1.0    255.255.255.0    192.168.2.2
	
默认路由:
	RouterA(config)#ip route   0.0.0.0    0.0.0.0    192.168.2.1
	RouterB(config)#ip route   0.0.0.0    0.0.0.0    192.168.2.2

RIP路由协议
	RouterA(config)#router rip
	RouterA(config-router)#network 192.168.1.0
	RouterA(config-router)#network 192.168.2.0
	
	RouterB(config)#router rip
	RouterA(config-router)#network  192.168.2.0
	RouterA(config-router)#network 192.168.3.0

```

​	   

```
Router0#conft


Router0(config)#int f0/0                                   # 选择配置接口
Router0(config-if)#ip address 192.168.1.1 255.255.255.0    # 配置接口ip,子网掩码
Router0(config-if)#no shut                                 # 
Router0(config-if)#exit                                    # 退出接口
Router0(config-if)#clock rate 64000                        # 两路由通信要配置时钟频率

Router0(config)#ip route 0.0.0.0 0.0.0.0 192.168.2.1

```















```python
1.简单企业网
	静态路由配置
	OSPT动态路由配置
	RIP配置

2.交换网络
	VLAN
	
3.
	路由策略
	动态NAT
	
4.影响分析
	静态路由失效对网络的影响
	路由失效对ospf的影响
	路由失效对rip的影响
	
	

```



















