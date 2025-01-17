### S7-1200 V4.0 及其以下版本轴资源

S7-1200 V4.0
及其以下版本的运动控制轴只支持开环运动控制，以下是每个型号和版本的具体资源说明。

#### [开环控制方式下，S7-1200 轴资源]{#_Toc428444728}

S7-1200 运动控制轴的资源个数是由 S7-1200 PLC
硬件能力决定的，不是由单纯的添加 IO 扩展模块来扩展的。

S7-1200 的最大的脉冲轴数不能扩展，如果客户需要控制轴数超过 S7-1200
最大支持轴数，并且对轴与轴之间的配合动作要求不高的情况下，可以使用多个
S7-1200 CPU，这些 CPU 之间可以通过以太网的方式进行通信。

表 1 显示了每种 CPU 的开环控制资源个数

                                    CPU轴总资源数量   CPU本体上最大轴数量   添加SB卡后最大轴数量   CPU轴总资源数量   CPU本体上最大轴数量   添加SB卡后最大轴数量   CPU轴总资源数量   CPU本体上最大轴数量   添加SB卡后最大轴数量
  --------------------- ----------- ----------------- --------------------- ---------------------- ----------------- --------------------- ---------------------- ----------------- --------------------- ----------------------
  固件版本：V1.0-V2.2                                 固件版本：V3.0                                                 固件版本：V4.0                                                                       
  CPU 1211C             DC/DC/DC    2                 2                     2                      4                 2                     4                      4                 4                     4
                        DC/DC/RLY                     0                     2                                        0                     2                                        0                     4
                        AC/DC/RLY                                                                                                                                                                         
  CPU 1212C             DC/DC/DC    2                 2                     2                      4                 3                     4                      4                 4                     4
                        DC/DC/RLY                     0                     2                                        0                     2                                        0                     4
                        AC/DC/RLY                                                                                                                                                                         
  CPU 1214C             DC/DC/DC    2                 2                     2                      4                 4                     4                      4                 4                     4
                        DC/DC/RLY                     0                     2                                        0                     2                                        0                     4
                        AC/DC/RLY                                                                                                                                                                         
  CPU 1215C             DC/DC/DC    \-                                                             4                 4                     4                      4                 4                     4
                        DC/DC/RLY                                                                                    0                     2                                        0                     4
                        AC/DC/RLY                                                                                                                                                                         
  CPU 1217C             DC/DC/DC    \-                                                             \-                                                             4                 4                     4

表 1. 轴资源

如上表所示，不同固件版本的 S7-1200 CPU
的轴资源个数不尽相同，客户在使用或购买 S7-1200 CPU
时务必确认轴的资源个数以满足使用要求。

此外从后面的表格可以看到，不同的 DO
点，其脉冲输出频率也不尽相同，请客户务必确认其输出频率能否满足工艺要求。

从表 1 中可以看出，添加信号板并不会超过 CPU 的总资源限制数。对于
DC/DC/DC 类型的 CPU 来说，添加信号板可以把 PTO 的功能移到信号板上，CPU
本体上的 DO 点可以空闲出来作为其他功能。而对于继电器输出类型的 CPU
来说如果需要使用 PTO 功能，则必须添加相应型号的信号板，如表 2 所示。

  信号板类型                 订货号               最大脉冲频率   高速脉冲输出点个数
  ------------ ------------- -------------------- -------------- --------------------
  DQ           4×24VDC       6ES7222-1BD30-0XB0   200kHz         4
               4×5VDC        6ES7222-1AD30-0XB0   200kHz         4
  DI/DQ        2DI/2×24VDC   6ES7223-0BD30-0XB0   20kHz          2
               2DI/2×24VDC   6ES7223-3BD30-0XB0   200kHz         2
               2DI/2×5VDC    6ES7223-3AD30-0XB0   200kHz         2

表 2. 信号板信息

**![](images/4.gif){width="15" height="15"}**上表中的 5V
信号都是集电极开路信号，不是 5V 差分信号。

**![](images/4.gif){width="15" height="15"}**信号板中 200kHz 的 DQ
点支持低电平有效的输出，如果 CPU
有低电平有效的输出需求的话，只能使用信号板。

#### [CPU1211C 脉冲轴资源]{#_Toc4}和脉冲频率

表 3 显示了 CPU 1211C 不同模式下最大轴个数。表 4 显示了 CPU 1211C 集成 Q
点最大输出频率。

+---------+---------+---------+---------+---------+---------+---------+
| CPU     |         |         | 不      |         |         |         |
| 1211C   |         |         | 同模式  |         |         |         |
|         |         |         | 下最大  |         |         |         |
|         |         |         | 轴个数  |         |         |         |
+=========+=========+=========+=========+=========+=========+=========+
| 固      | CPU     | 信号板  | 单脉冲  | 脉      | 正/反相 | AB 正交 |
| 件版本  | 类型    |         |         | 冲+方向 |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| V1      | D       | \-      | **2**   | 2       | \-      |         |
| .0-V2.2 | C/DC/DC |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | **2**   | 2       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | **2**   | 2       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         | DC      | \-      | 0       | 0       |         |         |
|         | /DC/RLY |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         | AC      |         |         |         |         |         |
|         | /DC/RLY |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | **2**   | 2       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | **1**   | 1       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| V3.0    | D       | \-      | **2**   | 2       |         |         |
|         | C/DC/DC |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | **4**   | 4       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | **3**   | 3       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         | DC      | \-      | 0       | 0       |         |         |
|         | /DC/RLY |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         | AC      |         |         |         |         |         |
|         | /DC/RLY |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | **2**   | 2       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | **1**   | 1       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| V4.0    | D       | \-      | 4       | 2       | 2       | 2       |
|         | C/DC/DC |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | 4       | 4       | 4       | 4       |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | 4       | 3       | 3       | 3       |
+---------+---------+---------+---------+---------+---------+---------+
|         | DC      | \-      | 0       | 0       | 0       | 0       |
|         | /DC/RLY |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         | AC      |         |         |         |         |         |
|         | /DC/RLY |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | 4       | 2       | 2       | 2       |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | 2       | 1       | 1       | 1       |
+---------+---------+---------+---------+---------+---------+---------+

表 3. CPU 1211C 不同模式下最大轴个数

**![](images/4.gif){width="15" height="15"}**\
1. 只有固件版本为 V4.0 的 S7-1200 CPU 才额外支持"正/反向"和"AB 正交"的
PTO 控制方式；\
2. 表 3
中红色的数字实际上说明的是：方式下并不能直接选择"单脉冲"的方式，但是用户可以在"脉冲+方向"的方式下不使用"方向"控制信号来实现"单脉冲"输出。

  CPU 1211C DC/DC/DC   Q0.0                                                  Q0.1       Q0.2       Q0.3
  -------------------- ----------------------------------------------------- ---------- ---------- ----------
  固件版本 V1.0        PTO 0                                                            PTO 1      
                       脉冲信号                                              方向信号   脉冲信号   方向信号
                       100kHz                                                100kHz     100kHz     100kHz
  固件版本 V2.0-V2.2   PTO 0                                                            PTO 1      
                       脉冲信号                                              方向信号   脉冲信号   方向信号
                       100kHz                                                100kHz     100kHz     100kHz
  固件版本 V3.0        PTO 0                                                            PTO 1      
                       脉冲信号                                              方向信号   脉冲信号   方向信号
                       100kHz                                                100kHz     100kHz     100kHz
  固件版本 V4.0        用户可以灵活定义 PTO 0\~PTO 3 这 4 个轴的 DQ 点分配                         
                       100kHz                                                100kHz     100kHz     100kHz

表 4. CPU 1211C 集成 Q 点最大输出频率

**![](images/4.gif){width="15" height="15"}**表 4 中固件版本 V3.0 的
CPU1211C 列出了 PTO 和 PTO1，实际上固件版本 V3.0 版本的 CPU1211C 有 4
个轴的资源，由于 CPU1211C 本体只集成了 4 个 DO 点，因此 CPU1211C
DC/DC/DC 类型的 CPU 最多只能组态 2 个
PTO。如果用户有更多轴的需求，需要添加信号板。

#### [CPU1212C]{#_Toc5} 脉冲轴资源和脉冲频率

表 5 显示了 CPU 1212C 不同模式下最大轴个数。表 6 显示了 CPU 1212C 集成 Q
点最大输出频率。

+---------+---------+---------+---------+---------+---------+---------+
| CPU     |         |         | 不      |         |         |         |
| 1212C   |         |         | 同模式  |         |         |         |
|         |         |         | 下最大  |         |         |         |
|         |         |         | 轴个数  |         |         |         |
+=========+=========+=========+=========+=========+=========+=========+
| 固      | CPU     | 信号板  | 单脉冲  | 脉      | 正/反相 | AB 正交 |
| 件版本  | 类型    |         |         | 冲+方向 |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| V1      | D       | \-      | **2**   | 2       | \-      |         |
| .0-V2.2 | C/DC/DC |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | **2**   | 2       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | **2**   | 2       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         | DC      | \-      | 0       | 0       |         |         |
|         | /DC/RLY |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         | AC      |         |         |         |         |         |
|         | /DC/RLY |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | **2**   | 2       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | **1**   | 1       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| V3.0    | D       | \-      | **3**   | 3       |         |         |
|         | C/DC/DC |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | **4**   | 4       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | **4**   | 4       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         | DC      | \-      | 0       | 0       |         |         |
|         | /DC/RLY |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         | AC      |         |         |         |         |         |
|         | /DC/RLY |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | **2**   | 2       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | **1**   | 1       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| V4.0    | D       | \-      | 4       | 4       | 4       | 4       |
|         | C/DC/DC |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | 4       | 4       | 4       | 4       |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | 4       | 4       | 4       | 4       |
+---------+---------+---------+---------+---------+---------+---------+
|         | DC      | \-      | 0       | 0       | 0       | 0       |
|         | /DC/RLY |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         | AC      |         |         |         |         |         |
|         | /DC/RLY |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | 4       | 2       | 2       | 2       |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | 2       | 1       | 1       | 1       |
+---------+---------+---------+---------+---------+---------+---------+

表 5. CPU1212C 不同模式下最大轴个数

**![](images/4.gif){width="15" height="15"}**\
1. 只有固件版本为 V4.0 的 S7-1200 CPU 才额外支持"正/反向"和"AB 正交"的
PTO 控制方式；\
2. 表 5 中红色的数字实际上说明的是：在 TIA Portal 软件中 PTO
控制方式下并不能直接选择"单脉冲"的方式，但是用户可以在"脉冲+方向"的方式下不使用"方向"控制信号来实现"单脉冲"输出。

  CPU 1212C DC/DC/DC   Q0.0                                                 Q0.1       Q0.2       Q0.3       Q0.4       Q0.5
  -------------------- ---------------------------------------------------- ---------- ---------- ---------- ---------- ----------
  固件版本 V1.0        PTO 0                                                           PTO 1                            
                       脉冲信号                                             方向信号   脉冲信号   方向信号              
                       100kHz                                               100kHz     100kHz     100kHz                
  固件版本 V2.0-V2.2   PTO 0                                                           PTO 1                            
                       脉冲信号                                             方向信号   脉冲信号   方向信号              
                       100kHz                                               100kHz     100kHz     100kHz                
  固件版本 V3.0        PTO 0                                                           PTO 1                 PTO 2      
                       脉冲信号                                             方向信号   脉冲信号   方向信号   脉冲信号   方向信号
                       100kHz                                               100kHz     100kHz     100kHz     20kHz      20kHz
  固件版本 V4.0        用户可以灵活定义 PTO 0\~PTO 3 这 4 个轴的 Q 点分配                                               
                       100kHz                                               100kHz     100kHz     100kHz     20kHz      20kHz

表 6. CPU1212C 集成 Q 点最大输出频率

**![](images/4.gif){width="15" height="15"}**表 6 中固件版本 V3.0 的
CPU1212C 列出了 PTO，PTO1 和 PTO2。实际上固件版本 V3.0 版本的 CPU1212C
有 4 个轴的资源，由于 CPU1212C 本体只集成了 6 个 DO 点，因此 CPU1212C
DC/DC/DC 类型的 CPU 最多只能组态 3
个PTO。如果用户有更多轴的需求，需要添加信号板。

#### [CPU1214C 脉冲轴资源和脉冲频率]{#_Toc6}

表 7 显示了 CPU 1214C 不同模式下最大轴个数。表 8 显示了 CPU 1214C 集成 Q
点最大输出频率。

+---------+---------+---------+---------+---------+---------+---------+
| CPU     |         |         | 不      |         |         |         |
| 1214C   |         |         | 同模式  |         |         |         |
|         |         |         | 下最大  |         |         |         |
|         |         |         | 轴个数  |         |         |         |
+=========+=========+=========+=========+=========+=========+=========+
| 固      | CPU     | 信号板  | 单脉冲  | 脉      | 正/反相 | AB 正交 |
| 件版本  | 类型    |         |         | 冲+方向 |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| V1      | D       | \-      | **2**   | 2       | \-      |         |
| .0-V2.2 | C/DC/DC |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | **2**   | 2       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | **2**   | 2       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         | DC      | \-      | 0       | 0       |         |         |
|         | /DC/RLY |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         | AC      |         |         |         |         |         |
|         | /DC/RLY |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | **2**   | 2       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | **1**   | 1       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| V3.0    | D       | \-      | **4**   | 4       |         |         |
|         | C/DC/DC |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | **4**   | 4       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | **4**   | 4       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         | DC      | \-      | 0       | 0       |         |         |
|         | /DC/RLY |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         | AC      |         |         |         |         |         |
|         | /DC/RLY |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | **2**   | 2       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | **1**   | 1       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| V4.0    | D       | \-      | 4       | 4       | 4       | 4       |
|         | C/DC/DC |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | 4       | 4       | 4       | 4       |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | 4       | 4       | 4       | 4       |
+---------+---------+---------+---------+---------+---------+---------+
|         | DC      | \-      | 0       | 0       | 0       | 0       |
|         | /DC/RLY |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         | AC      |         |         |         |         |         |
|         | /DC/RLY |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | 4       | 2       | 2       | 2       |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | 2       | 1       | 1       | 1       |
+---------+---------+---------+---------+---------+---------+---------+

表 7. CPU1214C 不同模式下最大轴个数

**![](images/4.gif){width="15" height="15"}**\
1. 只有固件版本为 V4.0 的 S7-1200 CPU 才额外支持"正/反向"和"AB 正交"的
PTO 控制方式；\
2. 表 7 中红色的数字实际上说明的是：在 TIA Portal 软件中 PTO
控制方式下并不能直接选择"单脉冲"的方式，但是用户可以在"脉冲+方向"的方式下不使用"方向"控制信号来实现"单脉冲"输出。

  CPU 1214C DC/DC/DC   Q0.0                                                 Q0.1       Q0.2       Q0.3       Q0.4       Q0.5       Q0.6       Q0.7       Q1.0    Q1.1
  -------------------- ---------------------------------------------------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ------- -------
  固件版本 V1.0        PTO 0                                                           PTO 1                 \-                                                  
                       脉冲信号                                             方向信号   脉冲信号   方向信号                                                       
                       100kHz                                               100kHz     100kHz     100kHz                                                         
  固件版本 V2.0-V2.2   PTO 0                                                           PTO 1                                                                     
                       脉冲信号                                             方向信号   脉冲信号   方向信号                                                       
                       100kHz                                               100kHz     100kHz     100kHz                                                         
  固件版本 V3.0        PTO 0                                                           PTO 1                 PTO 2                 PTO3                  \-      
                       脉冲信号                                             方向信号   脉冲信号   方向信号   脉冲信号   方向信号   脉冲信号   方向信号           
                       100kHz                                               100kHz     100kHz     100kHz     20kHz      20kHz      20kHz      20kHz              
  固件版本 V4.0        用户可以灵活定义 PTO 0\~PTO 3 这 4 个轴的 Q 点分配                                                                                        
                       100kHz                                               100kHz     100kHz     100kHz     20kHz      20kHz      20kHz      20kHz      20kHz   20kHz

表 8. CPU1214C 集成 Q 点最大输出频率

#### [CPU1215C 脉冲轴资源和脉冲频率]{#_Toc7}

表 9 显示了 CPU 1214C 不同模式下最大轴个数。表 10 显示了 CPU 1214C 集成
Q 点最大输出频率。

+---------+---------+---------+---------+---------+---------+---------+
| CPU     |         |         | 不      |         |         |         |
| 1215C   |         |         | 同模式  |         |         |         |
|         |         |         | 下最大  |         |         |         |
|         |         |         | 轴个数  |         |         |         |
+=========+=========+=========+=========+=========+=========+=========+
| 固      | CPU     | 信号板  | 单脉冲  | 脉      | 正/反相 | AB 正交 |
| 件版本  | 类型    |         |         | 冲+方向 |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| V3.0    | D       | \-      | **4**   | 4       | \-      |         |
|         | C/DC/DC |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | **4**   | 4       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | **4**   | 4       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         | DC      | \-      | 0       | 0       |         |         |
|         | /DC/RLY |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         | AC      |         |         |         |         |         |
|         | /DC/RLY |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | **2**   | 2       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | **1**   | 1       |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| V4.0    | D       | \-      | 4       | 4       | 4       | 4       |
|         | C/DC/DC |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | 4       | 4       | 4       | 4       |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | 4       | 4       | 4       | 4       |
+---------+---------+---------+---------+---------+---------+---------+
|         | DC      | \-      | 0       | 0       | 0       | 0       |
|         | /DC/RLY |         |         |         |         |         |
|         |         |         |         |         |         |         |
|         | AC      |         |         |         |         |         |
|         | /DC/RLY |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DQ      | 4       | 2       | 2       | 2       |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | DI/DQ   | 2       | 1       | 1       | 1       |
+---------+---------+---------+---------+---------+---------+---------+

表 9. CPU1215C 不同模式下最大轴个数

**![](images/4.gif){width="15" height="15"}** \
1. 只有固件版本为 V4.0 的 S7-1200 CPU 才额外支持"正/反向"和"AB 正交"的
PTO 控制方式；\
2. 表格中红色的数字实际上说明的是：在 TIA Portal 软件中 PTO
控制方式下并不能直接选择"单脉冲"的方式，但是用户可以在"脉冲+方向"的方式下不使用"方向"控制信号来实现"单脉冲"输出。

  CPU 1215C DC/DC/DC   Q0.0                                                 Q0.1       Q0.2       Q0.3       Q0.4       Q0.5       Q0.6       Q0.7       Q1.0    Q1.1
  -------------------- ---------------------------------------------------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ------- -------
  固件版本V1.0         PTO 0                                                           PTO 1                 \-                                                  
                       脉冲信号                                             方向信号   脉冲信号   方向信号                                                       
                       100kHz                                               100kHz     100kHz     100kHz                                                         
  固件版本V2.0-V2.2    PTO 0                                                           PTO 1                                                                     
                       脉冲信号                                             方向信号   脉冲信号   方向信号                                                       
                       100kHz                                               100kHz     100kHz     100kHz                                                         
  固件版本V3.0         PTO 0                                                           PTO 1                 PTO 2                 PTO3                  \-      
                       脉冲信号                                             方向信号   脉冲信号   方向信号   脉冲信号   方向信号   脉冲信号   方向信号           
                       100kHz                                               100kHz     100kHz     100kHz     20kHz      20kHz      20kHz      20kHz              
  固件版本 V4.0        用户可以灵活定义 PTO 0\~PTO 3 这 4 个轴的 Q 点分配                                                                                        
                       100kHz                                               100kHz     100kHz     100kHz     20kHz      20kHz      20kHz      20kHz      20kHz   20kHz

表 10. CPU1215C 集成 Q 点最大输出频率

#### [CPU1217C 脉冲轴资源和脉冲频率]{#_Toc8}

表 11 显示了 CPU 1217C 不同模式下最大轴个数。表 12 显示了 CPU 1217C 集成
Q 点最大输出频率。

**![](images/4.gif){width="15" height="15"}**由于 CPU1217C 本体只集成了
6 个集电极开路 24V 源型输出信号点，因此 CPU1217C 本体最多只能组态 3 个
DC 24 V 的脉冲+方向的
PTO。如果用户有更多轴的需求，需要添加信号板。差分信号点和 DC 24 V
信号点无法混用。

  CPU 1217C                       不同模式下最大轴个数                         
  ----------- ---------- -------- ---------------------- ----------- --------- ---------
  固件版本    CPU 类型   信号板   单脉冲                 脉冲+方向   正/反相   AB 正交
  V4.0        DC/DC/DC   \-       4                      4           4         4
                         DQ       4                      4           4         4
                         DI/DQ    4                      4           4         4

表 11. CPU1217C 不同模式下最大轴个数

  CPU 1217C DC/DC/DC   Q0.0                                                      Q0.1        Q0.2        Q0.3      Q0.4                          Q0.5   Q0.6   Q0.7   Q1.0   Q1.1
  -------------------- ---------------------------------------------------- ---- ------ ---- ------ ---- ------ -- ----------------------------- ------ ------ ------ ------ ------
  \+                   \-                                                   \+   \-     \+   \-     \+   \-                                                                  
  固件版本 V4.0        差分信号                                                                                    集电极开路 24V 源型输出信号                               
                       1MHz                                                                                        100kHz                                                    
                       用户可以灵活定义 PTO 0\~PTO 3 这 4 个轴的 Q 点分配                                                                                                    

表 12. CPU1217C 集成 Q 点最大输出频率
