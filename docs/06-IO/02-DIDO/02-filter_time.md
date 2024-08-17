# 数字量输入/输出（DI/DO）响应速度

S7-1200 CPU 按照以下机制循环工作：

1.  将过程映像输出区中的输出值写入到物理输出
2.  在用户程序执行前读取物理输入，并将输入值保存到过程映像输入区
3.  执行用户程序，进行逻辑运算，并更新过程映像输出区中的输出值

只要CPU处于运行状态，上述步骤就周而复始地执行。在扫描期间会定期处理通讯请求，这可能会中断用户程序的执行。其中第三步执行完程序循环
OB
后执行自检诊断。而中断可能发生在扫描周期的任何阶段，会中断用户程序的执行，转而调用处理该中断事件的
OB。

> ![](images/2.gif){width="15" height="15"} 上述三个步骤是 S7-1200 CPU
> 的软件处理过程，可以认为就是程序扫描时间。

实际上，S7-1200 对数字量的处理速度受到以下几个因素的限制：

A.  输入硬件延时（从输入信号状态改变的那一刻开始，到 CPU
    刷新输入映像区时能够识别其改变的时间）
B.  CPU 的内部处理时间，包括：
    1.  将过程映像输出区中的输出值写入到物理输出
    2.  在用户程序执行前读取物理输入，并将输入值保存到过程映像输入区
    3.  执行用户程序，进行逻辑运算，并更新过程映像输出区中的输出值
C.  输出硬件延时（从输出缓冲区状态改变到输出点真实电平改变的时间）

上述 A，B，C 三段时间，就是限制 PLC 处理数字量响应速度的主要因素。

> ![](images/6.gif){width="12" height="11"}
> 一个实际的系统可能还需要考虑输入、输出器件的延时，如输出点外接的中间继电器动作时间等，不在这里讨论。

## 输入延时时间

CPU
及扩展数字量输入点的延时时间，即输入点的滤波时间，在硬件组态模板属性中
"数字量输入\>通道\>输入滤波器"
对话框中可分组更改，其缺省的滤波时间是6.4ms。

> ![](images/6.gif){width="12" height="11"} 如果把容易受到干扰的信号接到
> CPU 上可改变滤波时间的DI点上，调整滤波时间可能改善信号检测的质量。

> ![](images/2.gif){width="15" height="15"} 上述数据来自《 S7-1200
> 系统手册》。

## 输出延时时间

表1. CPU 输出延时

<table width="1400" data-border="1">
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
</colgroup>
<tbody>
<tr>
<th colspan="2" rowspan="3" scope="col">输出点类型</th>
<th colspan="10" scope="col">CPU 型号</th>
</tr>
<tr>
<th colspan="2" scope="col">CPU 1211C</th>
<th colspan="2" scope="col">CPU 1212(F)C</th>
<th colspan="2" scope="col">CPU 1214(F)C</th>
<th colspan="2" scope="col">CPU 1215(F)C</th>
<th colspan="2" scope="col">CPU 1217C</th>
</tr>
<tr>
<th width="146" scope="col">24VDC 晶体管</th>
<th width="64" scope="col">继电器</th>
<th width="154" scope="col">24VDC 晶体管</th>
<th width="65" scope="col">继电器</th>
<th width="157" scope="col">24VDC 晶体管</th>
<th width="62" scope="col">继电器</th>
<th width="160" scope="col">24VDC 晶体管</th>
<th width="60" scope="col">继电器</th>
<th width="120" scope="col">Qa.4 to Qb.1</th>
<th width="160" scope="col"><p>差分输出点<br />
Qa.0 到 Qa.3<br />
（.0+ 0- 到 .3+ .3-）</p></th>
</tr>
&#10;<tr>
<th rowspan="3" width="55" scope="row">输出延时</th>
<th width="73" scope="row">off to on</th>
<td><p>1.0μs（Qa.0, Qa.3）</p></td>
<td><div data-align="center">
-
</div></td>
<td><p>1.0μs（Qa.0, Qa.3），<br />
50μs（Qa.4, Qa.5）</p></td>
<td><div data-align="center">
-
</div></td>
<td><p>1.0μs（Qa.0, Qa.3），<br />
50μs（Qa.4, Qb.1）</p></td>
<td><p>-</p></td>
<td><p>1.0μs（Qa.0, Qa.3），<br />
50μs（Qa.4, Qb.1）</p></td>
<td>-</td>
<td><div data-align="center">
1.0μs
</div></td>
<td width="160">100ns</td>
</tr>
<tr>
<th scope="row">on to off</th>
<td><div data-align="center">
3.0 μs（Qa.0, Qa.3）
</div></td>
<td><div data-align="center">
-
</div></td>
<td><div data-align="center">
<p>3.0μs（Qa.0, Qa.3），<br />
200μs（Qa.4, Qa.5）</p>
</div></td>
<td><div data-align="center">
-
</div></td>
<td>3.0μs（Qa.0, Qa.3），<br />
200μs（Qa.4, Qb.1）</td>
<td><div data-align="center">
-
</div></td>
<td><p>3.0μs（Qa.0, Qa.3），<br />
200μs（Qa.4, Qb.1）</p></td>
<td>-</td>
<td><div data-align="center">
3.0μs
</div></td>
<td width="160">100ns</td>
</tr>
<tr>
<th height="24">开关</th>
<td><div data-align="center">
-
</div></td>
<td><div data-align="center">
10ms
</div></td>
<td><div data-align="center">
-
</div></td>
<td><div data-align="center">
10ms
</div></td>
<td>-</td>
<td><div data-align="center">
10ms
</div></td>
<td>-</td>
<td>10ms</td>
<td><div data-align="center">
-
</div></td>
<td width="160">-</td>
</tr>
</tbody>
</table>

表2. 扩展信号模块输出延时

| 输出点类型 |     | 24 VDC 晶体管（源） | 24 VDC 晶体管（漏） | 继电器 |
| --- | --- | --- | --- | --- |
| 输出延时 | off to on | 50 μs | 20 μs | -   |
| on to off | 200 μs | 350 μs |
| 开关  | -   | -   | 10ms |

表3\. 200kHz 扩展信号板输出延时

| 输出点类型 |     | 24 VDC 晶体管 | 5 VDC 晶体管 |
| --- | --- | --- | --- |
| 输出延时 | 上升  | 1.5 μs + 300 ns | 200 μs + 300 ns |
| 下降  | 1.5 μs + 300 ns | 200 μs + 300 ns |

表4\. 20kHz 扩展信号板输出延时

| 输出点类型 |     | 24 VDC 晶体管 |
| --- | --- | --- |
| 输出延时 | off to on | 2 μs |
| on to off | 10 μs |

![](images/2.gif){width="15" height="15"} 上述数据来自《S7-1200系统手册》。
