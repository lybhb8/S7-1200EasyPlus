# MIN（获取最小值）和 MAX（获取最大值）

MIN（获取最小值）和 MAX（获取最大值）指令

|     |     |     |
| --- | --- | --- |
| ​LAD/FBD | ​SCL | ​说明 |
| ​<br><br>[![](images/21946343307_DV_resource.Stream@PNG-en-US.png)](#) | out:= MIN(  <br>    in1:=\_variant\_in_,  <br>    in2:=\_variant\_in_  <br>    \[,...in32\]); | ​MIN 指令用于比较两个参数 ​IN1​ 和 ​IN2​ 的值并将最小（较小）值分配给参数 ​OUT​。MIN（获取最小值） |
| ​<br><br>[![](images/21946347019_DV_resource.Stream@PNG-en-US.png)](#) | out:= MAX(  <br>    in1:=\_variant\_in_,  <br>    in2:=\_variant\_in_  <br>    \[,...in32\]); | ​MAX 指令用于比较两个参数 ​IN1​ 和 ​IN2​ 的值并将最大（较大）值分配给参数 ​OUT​。MAX（获取最大值） |

1 对于 LAD 和 FBD：单击“???”并从下拉菜单中选择数据类型。

参数的数据类型

|     |     |     |
| --- | --- | --- |
| ​参数 | ​数据类型1 | ​说明 |
| ​IN1, IN2  <br>​\[...IN32\] | ​SInt, Int, DInt, USInt, UInt, UDInt, Real, LReal, Time, Date, TOD, ​常数 | ​数学运算输入（最多 32 个输入） |
| ​OUT | ​SInt, Int, DInt, USInt, UInt, UDInt, Real, LReal, Time, Date, TOD | ​数学运算输出 |

1 IN1、IN2 和 OUT 参数的数据类型必须相同。

|     |     |
| --- | --- |
| ​<br><br>[![](images/21945899915_DV_resource.Stream@PNG-en-US.png)](#) | ​要添加输入，请单击“创建”(Create) 图标，或在其中一个现有 ​IN​ 参数的输入短线处单击右键，并选择“插入输入”(Insert input) 命令。 |

​要删除输入，请在其中一个现有 ​IN​ 参数（多于两个原始输入时）的输入短线处单击右键，并选择“删除”(Delete) 命令。

ENO 状态

|     |     |
| --- | --- |
| ​ENO | ​说明 |
| ​1  | ​无错误 |
| ​0  | ​仅适用于 ​Real​ 数据类型：<br><br>* ​至少一个输入不是实数 (NaN)。<br>    <br>* ​结果 OUT 为 +/- INF（无穷大）。 |