### S7-1200 参数汇总

S7-1200 最新参数汇总如下：

* [S7-1200 基本功能](#s7-1200-plc-基本功能)
* [S7-1200 通信功能](#s7-1200-plc-通信功能)
* [S7-1200 工艺功能](#s7-1200-plc-工艺功能)

### S7-1200 PLC 基本功能

#### **1\. S7-1200** **CPU** **实时时钟保持时间**

通常为 20 天，40℃ 时最少为 12 天（免维护超级电容）；

使用 BB1297 电池板和 CR1025 电池实时时钟断电保持时间大约为 1 年。

#### **2\. S7-1200** **CPU** **数据断电保持时间**

设置了断电保持的数据理论上断电保持的时间是无限的，实际保持时间可能与运行环境、电源、EMC 等有关，所以尽可能按照安装要求进行安装、供电等。

#### **3\. S7-1200 CPU 断电保持数据区大小**

* 固件版本为 V4.0 - V4.4 的 CPU 保持性存储器大小为 10k Byte
* 固件版本为 V4.5 及其以上的 CPU 保持性存储器大小为 14k Byte

#### 4\. **S7-1200 CPU 工作存储器大小**

表 1 工作存储器

<table width="1594" border="1">
  <tr>
    <th width="100" rowspan="2" scope="col">CPU</th>
    <th colspan="3" scope="col">CPU 1211C</th>
    <th colspan="3" scope="col">CPU 1212C</th>
    <th colspan="3" scope="col">CPU 1214C</th>
    <th colspan="3" scope="col">CPU 1215C</th>
    <th scope="col">CPU 1217C</th>
  </tr>
  <tr>
    <td width="100"><div align="center">AC/DC/RLY</div></td>
    <td width="100"><div align="center">DC/DC/DC</div></td>
    <td width="100"><div align="center">DC/DC/RLY</div></td>
    <td width="100"><div align="center">AC/DC/RLY</div></td>
    <td width="100"><div align="center">DC/DC/DC</div></td>
    <td width="100"><div align="center">DC/DC/RLY</div></td>
    <td width="100"><div align="center">AC/DC/RLY</div></td>
    <td width="100"><div align="center">DC/DC/DC</div></td>
    <td width="100"><div align="center">DC/DC/RLY</div></td>
    <td width="100"><div align="center">AC/DC/RLY</div></td>
    <td width="100"><div align="center">DC/DC/DC</div></td>
    <td width="100"><div align="center">DC/DC/RLY</div></td>
    <td width="100"><div align="center">DC/DC/DC</div></td>
  </tr>
  <tr>
    <td><div align="center">标准型</div></td>
    <td colspan="3"><div align="center">75kB</div></td>
    <td colspan="3"><div align="center">100kB</div></td>
    <td colspan="3"><div align="center">150kB</div></td>
    <td colspan="3"><div align="center">200kB</div></td>
    <td width="100"><div align="center">250kB</div></td>
  </tr>
  <tr>
    <td><div align="center">故障安全型</div></td>
    <td colspan="3"><div align="center">无</div>
      <div align="center"></div>
      <div align="center"></div></td>
    <td><div align="center">无</div></td>
    <td colspan="2"><div align="center">150kB</div>
      <div align="center"></div></td>
    <td><div align="center">无</div></td>
    <td colspan="2"><div align="center">200kB</div>
      <div align="center"></div></td>
    <td><div align="center">无</div></td>
    <td colspan="2"><div align="center">250kB</div>
      <div align="center"></div></td>
    <td><div align="center">无</div></td>
  </tr>
</table>

#### **5\.** **S7-1200 CPU 装载存储器大小**

表 2 装载存储器

<table width="1594" border="1">
  <tr>
    <th width="100" rowspan="2" scope="col">CPU</th>
    <th colspan="3" scope="col">CPU 1211C</th>
    <th colspan="3" scope="col">CPU 1212C</th>
    <th colspan="3" scope="col">CPU 1214C</th>
    <th colspan="3" scope="col">CPU 1215C</th>
    <th scope="col">CPU 1217C</th>
  </tr>
  <tr>
    <td width="100"><div align="center">AC/DC/RLY</div></td>
    <td width="100"><div align="center">DC/DC/DC</div></td>
    <td width="100"><div align="center">DC/DC/RLY</div></td>
    <td width="100"><div align="center">AC/DC/RLY</div></td>
    <td width="100"><div align="center">DC/DC/DC</div></td>
    <td width="100"><div align="center">DC/DC/RLY</div></td>
    <td width="100"><div align="center">AC/DC/RLY</div></td>
    <td width="100"><div align="center">DC/DC/DC</div></td>
    <td width="100"><div align="center">DC/DC/RLY</div></td>
    <td width="100"><div align="center">AC/DC/RLY</div></td>
    <td width="100"><div align="center">DC/DC/DC</div></td>
    <td width="100"><div align="center">DC/DC/RLY</div></td>
    <td width="100"><div align="center">DC/DC/DC</div></td>
  </tr>
  <tr>
    <td><div align="center">标准型</div></td>
    <td colspan="3">1MB</td>
    <td colspan="3">2MB</td>
    <td colspan="3">4MB</td>
    <td colspan="3">4MB</td>
    <td>4MB</td>
  </tr>
  <tr>
    <td width="100"><div align="center">故障安全型</div></td>
    <td colspan="3"><div align="center">无</div>
      <div align="center"></div>
      <div align="center"></div></td>
    <td width="100"><div align="center">无</div></td>
    <td colspan="2"><div align="center">2MB</div>
      <div align="center"></div></td>
    <td width="100"><div align="center">无</div></td>
    <td colspan="2"><div align="center">4MB</div>
      <div align="center"></div></td>
    <td width="100"><div align="center">无</div></td>
    <td colspan="2"><div align="center">4MB</div>
      <div align="center"></div></td>
    <td width="100"><div align="center">无</div></td>
  </tr>
</table>
<h4><strong>4. S7-1200 PLC 额定电压</strong></h4>
<p>表 3 电源范围</p>
<table width="688" border="1">
  <tr>
    <th width="118" scope="col">CPU 类型</th>
    <th width="118" scope="col">额定电压</th>
    <th width="430" scope="col">范围</th>
  </tr>
  <tr>
    <td>DC/DC/DC DC/DC/RLY</td>
    <td>24V DC</td>
    <td>20.4V DC 到 28.8V DC</td>
  </tr>
  <tr>
    <td>AC/DC/RLY</td>
    <td>120/230V AC</td>
    <td>85V AC 到 264V AC，47 到 63Hz</td>
  </tr>
</table>

#### **4\. S7-1200 PLC 额定电压**

表 3 电源范围

| CPU 类型 | 额定电压 | 范围  |
| --- | --- | --- |
| DC/DC/DC DC/DC/RLY | 24V DC | 20.4V DC 到 28.8V DC |
| AC/DC/RLY | 120/230V AC | 85V AC 到 264V AC，47 到 63Hz |

#### **5\. S7-1200 CPU 切断电源后，CPU 的电容维持时间**

取决于 CPU 的供电类型：AC 120V 时为 20ms；AC 240V 时为 80ms；DC 24V 时为 10ms。

#### **6.** **S7-1200 PLC** **支持的代码块、定时器和计数器**

表 4 代码块、定时器和计数器

|     | 元素 | 说明  |
| --- | --- | --- |
| **块** | 类型  | OB、FB、FC、DB |
| |大小  | 最大可达工作存储器的大小 |
| |数量  | 最多可达 1024 个块（OB + FB + FC + DB） |
| |FB、FC、DB 地址范围 | FB 和 FC：1 到 65535  <br>DB：1 到 59999 |
| |嵌套深度 | 16（从程序循环 OB 或启动 OB 开始）  <br>6（从任意中断事件） |
| |监视  | 可以同时监视 2 个代码块的状态 |
| **定时器** | 类型  | IEC |
| |数量  | 仅受存储器大小限制 |
| |存储  | DB 结构，每个定时器 16 个字节 |
| **计数器** | 类型  | IEC |
| |数量  | 仅受存储器大小限制 |
| |存储  | DB 结构，大小取决于计数类型  <br>SInt 和 USInt：3 个字节  <br>Int 和 UInt：6 个字节  <br>DInt 和 UDInt：12 个字节 |

表 5 组织块

| 组织块 | 类型  | 默认优先级 | 可能的 OB 编号 | 允许的 OB 数量 |
| --- | --- | --- | --- | --- |
| |程序循环 | 1   | 1，≥123 | 多个  |
| |启动  | 1   | 100，≥123 | 多个  |
| |时间中断 | 2   | ≥10 | 2   |
| |延时中断 | 3   | ≥20 | 4（每个事件 1 个） |
| |循环中断 | 8   | ≥30 | 4（每个事件 1 个） |
| |硬件中断 | 18  | ≥40 | 50（每个事件 1 个） |
| |时间错误中断 | 22  | 80  | 1   |
| |诊断错误中断 | 5   | 82  | 1   |
| |拔出或插入模块 | 6   | 83  | 1   |
| |机架或站故障 | 6   | 86  | 1   |

#### **7\. S7-1200 PLC 安装环境**

表 6 安装环境

| **S7-1200 自动化系统适用于不受气候影响的固定位置。运行条件符合 DIN IEC 60721-3-3 的要求：**  <br>**类别 3M3 （机械要求）**  <br>**类别 3K3** （气候要求**）** |     |
| --- | --- |
| 环境温度范围  <br>（设备下部 25mm 进风距离） | -20℃ 到 60℃ 水平安装  <br>-20℃ 到 50℃ 垂直安装  <br>湿度 95%，不结露 |
| 大气压 | 1140 至 795 hPa（相当于海拔 -1000 到 2000 m） |
| 污染物浓度 | SO2 < 0.5ppm；H2S < 0.1ppm；RH < 60%，不结露 |
| |ISA-S71.04 严重度 G1、G2、G3 |
| EN 60068-2-14，测试 Nb，温度变化 | 0℃ 到 60℃ |
| EN 60068-2-17，机械冲击 | 15g，11 ms 脉冲，3 个轴向上 6 次冲击 |
| EN 60068-2-6，正弦振动 | DIN 导轨安装：5-9 Hz 时 3.5mm，8.4-150 Hz时 1G  <br>面板安装：5-8.4Hz 时 7.0mm，8.4-150Hz 时 2G  <br>每个轴 10 次摆动，每分钟 1 倍频程 |

### S7-1200 PLC 通信功能

#### **1\. S7-1200 CPU 控制 IO设备 / DP 从站数量**

S7-1200 CPU 作为 PROFINET IO 控制器时支持 16 个 IO 设备，所有 IO 设备的子模块数量最多为 256 个。  
S7-1200 CPU 可以组态最多 3 个 PROFIBUS 通信模块，可以使 CM 1243-5 或 CM 1242-5 的任意组合。每个 DP 主站（CM 1243-5）最多控制 32 个 DP 从站，每个 DP 主站最多扩展 512 个子模块。

#### **2\. S7-1200 CPU 串口通信模块和通信板**

表 7 串口模块

| 类型  | CM1241 RS232 | CM1241 RS422/485 | CB1241 RS485 |
| --- | --- | --- | --- |
| 通信口类型 | RS 232 | RS 422/485 | RS 485 |
| 流量控制 | 硬件流控；软件流控 | 软件流控（仅 RS422） | 不支持 |
| 通信距离 | 最长 10 米 | 最长 1000 米 | 最长 1000 米 |
| 波特率 | 300、600、1.2K、2.4K、4.8K、9.6K、19.2K、38.4K、57.6K、76.8K、115.2K |     |     |
| 校验方式 | 无校验、偶校验、奇校验、Mark 校验、Space 校验、任意奇偶校验 |     |     |
| 接收缓冲区 | 1 kB |     |     |
| **支持的协议** |     |     |     |
| 自由口 | √   | √   | √   |
| 3964（R） | √   | √   | ×   |
| Modbus RTU | √   | √   | √   |
| USS | ×   | √   | √   |

#### **3.** **S7-1200 CPU** **以太网通信**

表 8 支持的以太网通信协议

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | PG 通信 | HMI 通信 | S7 通信 | OUC 通信 | Modbus TCP | IO 控制器 | 智能设备 | 共享设备 | OPC UA 服务器 |
| V4.4 - V4.6 | √   | √   | √   | √   | √   | √   | √   | √   | √   |
| V4.1 - V4.3 | √   | √   | √   | √   | √   | √   | √   | √   | ×   |
| V4.0 | √   | √   | √   | √   | √   | √   | √   | ×   | ×   |

#### **4\. S7-1200 CPU 连接资源**

表 9 连接资源

|     | V4.5 及其以上 |     | V4.4-V4.0 |     |
| --- | --- | --- | --- | --- |
| 预留/动态资源 | 34/34 |     | 62/6 |     |
| 类型  | 预留  | 最大值 | 预留  | 最大值 |
| PG 通信 | 4   | 4   | 4   | 4   |
| HMI 通信 | 12  | 18  | 12  | 18  |
| S7 通信 | 8   | 14  | 8   | 14  |
| 开放式用户通信 | 8   | 14  | 8   | 14  |
| Web 通信 | 2   | 30  | 30  | 30  |

### S7-1200 PLC 工艺功能

#### **1\. S7-1200 CPU 运动控制**

S7-1200 本体运动控制轴资源：

开环控制方式下：最大的脉冲轴个数为 4，无法扩展。

闭环控制方式下：固件版本 V4.1 及其以上的版本的 S7-1200 都可以通过 PROFIdrive 或模拟驱动器接口控制最多 8 个驱动器。

#### **2\. S7-1200 CPU 高速计数器功能**

S7-1200 本体和扩展信号板总共提供 6 个高速计数器，可连接 PNP 或 NPN 脉冲输入信号，支持增量型旋转编码器。

S7-1200 高速计数器支持的工作模式有以下 4 种：

* 单相计数，方向由内部或外部控制
* 两相位
* A/B 正交计数器
* A/B 正交计数器四倍频

表 10 S7-1200 CPU 本体输入最大频率

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CPU | CPU输入通道 | 单相  |     | 两相位 |     | A/B 正交 |     |
| 频率/kHz | 高速计数最大数量 | 频率/kHz | 高速计数最大数量 | 频率/kHz | 高速计数最大数量 |
| 1211C | Ia.0 - Ia.5 | 100 | 6   | 100 | 3   | 80  | 3   |
| 1212C | Ia.0 - Ia.5 | 100 | 6   | 100 | 3   | 80  | 3   |
| |Ia.6 - Ia.7 | 30  | 2   | 30  | 1   | 20  | 1   |
| 1214C/1215C | Ia.0 - Ia.5 | 100 | 6   | 100 | 3   | 80  | 3   |
| |Ia.6 - Ib.5 | 30  | 6   | 30  | 4   | 20  | 4   |
| 1217C | Ia.0 - Ia.5 | 100 | 6   | 100 | 3   | 80  | 3   |
| |Ia.6 - Ib.1 | 30  | 4   | 30  | 2   | 20  | 2   |
| |Ib2 - Ib5 | 1MHz | 4   | 1MHz | 2   | 1MHz | 2   |

注意： CPU 1217C 的 Ib2 - Ib5 是 5V 差分信号（RS 422），不是 24V 单端信号。

表 11 信号板 SB 输入最大频率

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SB 信号板 | SB 输入通道 | 单相  |     | 两相位 |     | A/B 正交 |     |
| 频率/kHz | 高速计数最大数量 | 频率/kHz | 高速计数最大数量 | 频率/kHz | 高速计数最大数量 |
| 6ES7221-3BD30-0XB0 | Ie.0 - Ie.3 | 200 | 4   | 200 | 2   | 160 | 2   |
| 6ES7223-3BD30-0XB0 | Ie.0 - Ie.1 | 200 | 2   | 200 | 1   | 160 | 1   |
| 6ES7223-0BD30-0XB0 | Ie.0 - Ie.1 | 30  | 2   | 30  | 1   | 20  | 1   |

#### **3\. S7-1200 PLC PID 功能**

S7-1200 提供 3 个 PID 指令：PID\_Compact、PID\_3Step、PID_Temp。

S7-1200 所支持的 PID 回路数仅受程序量大小及程序执行时间的影响，没有具体数量的限制，可以同时进行多个回路数的控制。

表 12 单个 PID 所需存储区与处理时间

|     | 背景DB的存储区需求 |     | CPU处理时间（典型） |     |
| --- | --- | --- | --- | --- |
| PID_Compact | 装载存储区，约 | 12000 字节 | 固件版本 ≥ V4.1 | 300微秒 |
| |工作存储区 | 788 字节 |||
| |保持性存储区 | 44 字节 |||
| PID_3Step | 装载存储区，约 | 15000 字节 | 固件版本 ≥ V4.1 | 410微秒 |
| |工作存储区 | 1040 字节 |||
| |保持性存储区 | 60 字节 |||
| PID_Temp | 装载存储区，约 | 17000 字节 | 固件版本 ≥ V4.1 | 580微秒 |
| |工作存储区 | 1280 字节 |||
| |保持性存储区 | 100 字节 |||

表 13 PID 指令功能对比

| 指令  | PID_Compact | PID_3Step | PID_Temp |
| --- | --- | --- | --- |
| 模拟量输出 | √   | √   | √   |
| PWM | √   | √   | √   |
| 加热/制冷输出 | ×   | ×   | √   |
| 死区  | ×   | √   | √   |
| 控制带 | ×   | ×   | √   |
| 串级控制 | ×   | ×   | √   |
| 预调节 | √   | √   | √   |
| 精确调节 | √   | √   | √   |
| 抗积分饱和 | √   | √   | √   |
| 执行器阀位控制 | ×   | √   | ×   |