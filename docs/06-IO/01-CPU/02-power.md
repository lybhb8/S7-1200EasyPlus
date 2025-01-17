# 电能消耗 

## 最大 I/O 能力计算

S7-1200 最大I/O能力取决于以下几个因素，这些因素之间互相影响、制约，必须综合考虑：

* CPU 输入/输出过程变量映像区大小  
    
* CPU 本体的 I/O 点数  
    
* CPU 带扩展模块的数目，见表1（CPU 所带智能通讯模块安装于 CPU 左侧，不占用扩展模板资源数）
* CPU 的 5 VDC 电源是否满足所有扩展模块的需要

5 VDC 电源需求请参考 **[S7-1200 PLC 电源需求与计算](#电能消耗)**，其它影响因素请参考如下表1 。

表1\. S7-1200 PLC 影响 I/O 能力的性能参数

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| **CPU 参数** | **CPU 1211C** | **CPU 1212C** | **CPU 1214C** | **CPU 1215C** | **CPU 1217C** |
| CPUs | DC/DC/DC, AC/DC/RLY, DC/DC/RLY |     |     |     | DC/DC/DC |
| **CPU 参数** |     | **CPU 1212FC** | **CPU 1214FC** | **CPU 1215FC** |     |
| CPUs |     | DC/DC/DC, DC/DC/RLY |     |     |     |
| 集成数字量 I/O | 6 输入 / 4 输出 | 8 输入/ 6 输出 | ||14 输入 / 10 输出 |
| 集成模拟量 I/O | 2 输入 |     |     | 2 输入/ 2 输出 |     |
| 过程映像区 | 1024 字节输入 / 1024 字节输出 |     |     |     |     |
| 信号板扩展 | 最多1个 |     |     |     |     |
| 信号模块扩展 | 无   | 最多2个 | 最多8个 |     |     |
| 最大本地数字量 I/O | 14  | 82  | 284 |     |     |
| 最大本地模拟量 I/O | 3   | 19  | 67  | 69  | 69  |
| 通信模块扩展 | 最多3个 |     |     |     |     |

## S7-1200 PLC 电源需求与计算

S7-1200 CPU 提供 5 VDC 和 24 VDC 电源：

* 当有扩展模板时，CPU 通过 I/O 总线为其提供 5 VDC 电源，所有扩展模块的 5 VDC 电源消耗之和不能超过该 CPU 提供的电源额定值。若不够用**不能外接 5 VDC 电源**。  
    
* 每个 CPU 都有一个 24 VDC 传感器电源，它为本机输入点和扩展模块输入点及扩展模块继电器线圈提供 24 VDC。如果电源要求超出了 CPU 模块的电源额定值，你**可以增加一个外部** **24 VDC 电源**来提供给扩展模块。

所谓电源计算，就是用 CPU 所能提供的电源容量，减去各模块所需要的电源消耗量。

### S7-1200 系统电源数据简表

详情请参考最新的《 S7-1200 系统手册》或模块说明书。

表2\. CPU 的供电能力

|     |     |     |
| --- | --- | --- |
| CPU 型号 | 电流供应 (mA) |     |
| |5 VDC | 24 VDC |
| CPU 1211C | 750 | 300 |
| CPU 1212(F)C | 1000 | 300 |
| CPU 1214(F)C | 1600 | 400 |
| CPU 1215(F)C | 1600 | 400 |
| CPU 1217C | 1600 | 400 |

表3\. CPU 上及扩展模块上的数字量输入所消耗的电流

|     |     |     |
| --- | --- | --- |
| CPU 上及扩展模块上的数字量 | 电流需求 (mA) |     |
| 5 VDC | 24 VDC |
| 每点输入 | \-\-\-\- | 4 mA/输入 |

**注意：**如果数字量输入点使用外接24VDC电源，则不必纳入计算。

表4\. 数字扩展模块所消耗的电流

|     |     |     |     |
| --- | --- | --- | --- |
| 数字扩展模块型号 | 订货号 | 电流需求 |     |
| | |5 VDC (mA) | 24 VDC |
| SM 1221 8 x 24 VDC 输入 | 6ES7221-1BF32-0XB0 | 105 | 4 mA/输入 |
| SM 1221 16 x 24 VDC 输入 | 6ES7221-1BH32-0XB0 | 130 | 4 mA/输入 |
| SM 1222 8 x 24 VDC 输出 | 6ES7222-1BF32-0XB0 | 120 | 50mA |
| SM 1222 16 x 24 VDC 输出 | 6ES7222-1BH32-0XB0 | 140 | 100mA |
| SM 1222 16 x 24 VDC 漏型输出 | 6ES7222-1BH32-1XB0 | 140 | 40mA |
| SM 1222 8 x 继电器输出 | 6ES7222-1HF32-0XB0 | 120 | 11 mA/输出 |
| SM 1222 8 x 继电器输出切换 | 6ES7222-1XF32-0XB0 | 140 | 16.7 mA/输出 |
| SM 1222 16 x 继电器输出 | 6ES7222-1HH32-0XB0 | 135 | 11 mA/输出 |
| SM 1223 8 x 24 VDC 输入/8 x 24 VDC 输出 | 6ES7223-1BH32-0XB0 | 145 | 150mA |
| SM 1223 16 x 24 VDC 输入/16 x 24 VDC 输出 | 6ES7223-1BL32-0XB0 | 185 | 200mA |
| SM 1223 8 x 24 VDC 输入/8 x 继电器输出 | 6ES7223-1PH32-0XB0 | 145 | 4 mA/输入 11 mA/输出 |
| SM 1223 16 x 24 VDC 输入/16 x 继电器输出 | 6ES7223-1PL32-0XB0 | 180 | 4 mA/输入 11 mA/输出 |
| SM 1223 16 x 24 VDC 输入/16 x 24 VDC 漏型输出 | 6ES7223-1BL32-1XB0 | 185 | 40mA |
| SM 1223 8 x 120/230 VAC 输入/8 x 继电器输出 | 6ES7223-1QH32-0XB0 | 120 | 11 mA/输出 |

表5.模拟扩展模块所消耗的电流

|     |     |     |     |
| --- | --- | --- | --- |
| 模拟扩展模块型号 | 订货号 | 电流需求 (mA) |     |
| ||5 VDC | 24 VDC |
| SM 1231 4 x 13位 模拟量输入 | 6ES7231-4HD32-0XB0 | 80  | 45  |
| SM 1231 8 x 13位 模拟量输入 | 6ES7231-4HF32-0XB0 | 90  | 45  |
| SM 1231 4 x 16位 模拟量输入 | 6ES7231-5ND32-0XB0 | 80  | 65  |
| SM 1232 2 x 模拟量输出 | 6ES7232-4HB32-0XB0 | 80  | 45 (无负载) |
| SM 1232 4 x 模拟量输出 | 6ES7232-4HD32-0XB0 | 80  | 45 (无负载) |
| SM 1234 4 x 模拟量输入/2 x 模拟量输出 | 6ES7234-4HE32-0XB0 | 80  | 60 (无负载) |
| SM 1231 4 x TC 热电偶输入 | 6ES7231-5QD32-0XB0 | 80  | 40  |
| SM 1231 8 x TC 热电偶输入 | 6ES7231-5QF32-0XB0 | 80  | 40  |
| SM 1231 4 x RTD 热电阻输入 | 6ES7231-5PD32-0XB0 | 80  | 40  |
| SM 1231 8 x RTD 热电阻输入 | 6ES7231-5PF32-0XB0 | 90  | 40  |

表6.信号板所消耗的电流

|     |     |     |     |
| --- | --- | --- | --- |
| 信号板型号 | 订货号 | 电流需求 |     |
| ||5 VDC (mA) | 24 VDC |
| SB 1221,200kHz 4 x 24 VDC 输入 | 6ES7221-3BD30-0XB0 | 40  | 7 mA/输入 +20mA |
| SB 1221,200kHz 4 x 5 VDC 输入 | 6ES7221-3AD30-0XB0 | 40  | 15 mA/输入 +15mA |
| SB 1222,200kHz 4 x 24 VDC 输出 | 6ES7222-1BD30-0XB0 | 35  | 15mA |
| SB 1222,200kHz 4 x 5 VDC 输出 | 6ES7222-1AD30-0XB0 | 35  | 15mA |
| SB 1223,200kHz 2 x 24VDC 输入/2 x 24 VDC 输出 | 6ES7223-3BD30-0XB0 | 35  | 7 mA/输入 +30mA |
| SB 1223,200kHz 2 x 5 VDC 输入/2 x 5 VDC 输出 | 6ES7223-3AD30-0XB0 | 35  | 15 mA/输入 +15mA |
| SB 1223 2 x 24 VDC 输入/2 x 24 VDC 输出 | 6ES7223-0BD30-0XB0 | 50  | 4 mA/输入 |
| SB 1231 1 路模拟量输入 | 6ES7231-4HA30-0XB0 | 55  | \-\-\- |
| SB 1231 1 路热电偶输入 | 6ES7231-5QA30-0XB0 | 5   | 20mA |
| SB 1231 1 路热电阻输入 | 6ES7231-5PA30-0XB0 | 5   | 25mA |
| SB 1232 1 路模拟量输出 | 6ES7232-4HA30-0XB0 | 15  | 40 mA (无负载) |
| BB 1297 电池板 | 6ES7297-0AX30-0XA0 | 11  | \-\-\- |

表7.通讯板/模块所消耗的电流

|     |     |     |     |
| --- | --- | --- | --- |
| 通讯模块型号 | 订货号 | 电流供应 (mA) |     |
| | |5 VDC | 24 VDC |
| CM 1241 RS232 | 6ES7241-1AH32-0XB0 | 200 | \-\-\- |
| CM 1241 RS422/485 | 6ES7241-1CH32-0XB0 | 220 | \-\-\- |
| CB 1241 RS485 | 6ES7241-1CH30-1XB0 | 50  | 80  |
| CM 1243-5 | 6GK7243-5DX30-0XE0 | \-\-\- | 100 |
| CM 1242-5 | 6GK7242-5DX30-0XE0 | 150 | \-\-\- |
| CP 1243-1 | 6GK7243-1BX30-0XE0 | 250 | \-\-\- |

### 电源需求计算实例

以下实例是 PLC 电源计算实例，该 PLC 包括一个 CPU 1214C AC/DC/继电器型、1xSM 1231 4 x 13位 模拟量输入、 3xSM 1223 8 DI输入/8 继电器输出和 1xSM 1221 8DI 输入。该实例一共有 46 点输入和 34 点输出 。电源需求如下表8.所示

表8.电源需求计算实例列表

|     |     |     |
| --- | --- | --- |
| CPU 电源计算 | 5 VDC | 24 VDC |
| CPU 1214C AC/DC/继电器型 | 1600 mA | 400 mA |
| 减   |     |     |
| 系统要求 | 5 VDC | 24 VDC |
| CPU 1214C， 14点输入 | \-\-\- | 14 * 4 mA = 56 mA |
| 1 个 SM 1231 | 1 * 80 mA = 80 mA | 1 * 45 mA = 45 mA |
| 3 个 SM 1223 | 3 * 145 mA = 435 mA | 3 * 8 * 4 mA = 96 mA |
| 3 * 8 * 11 mA = 264 mA |
| 1 个 SM 1221 | 1 * 105 mA = 105 mA | 8 * 4 mA = 32 mA |
| 总要求 | 620 mA | 493 mA |
| 等于  |     |     |
| 电流差额 | 5 VDC | 24 VDC |
| 总电流差额 | 980 mA | \- 93 mA |

 **![](images/4.gif) 注意：该 CPU 已分配驱动内部继电器线圈所需的电源，则电源计算中无需包括 CPU 内部继电器线圈的功率要求。**

由表中可以看出，所选 CPU 已经为 SM 提供了足够的 5 VDC 电流，但没有通过传感器电源为所有输入和扩展继电器线圈提供足够的 24 VDC 电流。I/O 需要 493 mA 而 CPU 只能提供 400 mA。则该系统而外需要一个至少为 93 mA 的 24 VDC 电源以运行所有包括的 24 VDC 输入和输出。

## 常见问题

 **![](images/5.gif) CPU 提供的 5 VDC 电源能否使用外部电源扩展？**

**答：**不能，根据模板 5 VDC 电源使用情况选择合适的 CPU 。  

![](images/5.gif) **CPU 提供的 24 VDC 电源不够用时，能否使用外部电源扩展？**

**答：**可以，根据需要可以选择使用外部电源。  

 **![](images/5.gif) 通讯模板（CM）和信号板（SB）是否占用信号扩展模板数量？**  

**答：**

* 扩展模板仅指信号模板，安装于 CPU 的右侧，共有 8 个扩展槽位
* 通讯模块安装于 CPU 左侧，并不占用扩展模板资源数
* 信号模块安装于 CPU 上侧，每个 CPU 最多只能安装 1 个，并不占用扩展模板资源数

S7-1200 模板安装位置如下：

![](images/s7-1200%20rack.JPG)

* 1 号槽位为CPU
* 红色图框为信号板（SB）安装位置
* 蓝色图框内为 101 ~ 103 三个槽位，为通讯模板（CM）安装位置
* 绿色图框内为 2 ~ 9 八个槽位，为信号模板（SM）安装位置  
    

 **![](images/5.gif) 通电时能否插拔模板？**

**答：**不能，所有的信号板、信号模板和通讯模板都不支持通电时的插入和拔除 。