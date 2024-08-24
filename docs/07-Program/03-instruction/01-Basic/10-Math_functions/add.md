# 加法、减法、乘法和除法


## 加法、减法、乘法和除法指令

| ​LAD/FBD \*| ​SCL | ​说明 |
|-----|-----|-----|
| ​<br><br>![alt text](image-2.png) | out := in1 + in2;  <br>out := in1 - in2;  <br>out := in1 * in2;  <br>out := in1 / in2; | * ​ADD：加法 (IN1 + IN2 = OUT)<br>    <br>* ​SUB：减法 (IN1 - IN2 = OUT)<br>    <br>* ​MUL：乘法 (IN1 * IN2 = OUT)<br>    <br>* ​DIV：除法 (IN1 / IN2 = OUT)<br>    <br><br>​整数除法运算会截去商的小数部分以生成整数输出。 数学ADD（加法）SUB（减法）MUL（乘法）DIV（除法） |

!!! note "注 * ：对于 LAD 和 FBD：单击“???”并从下拉菜单中选择数据类型。"

## 参数的数据类型（LAD 和 FBD）

| ​参数 | ​数据类型^* | ​说明 |
|---|---|---|
| ​IN1, IN2 | ​SInt, Int, DInt, USInt, UInt, UDInt, Real, LReal​, 常数 | ​数学运算输入 |
| ​OUT | ​SInt, Int, DInt, USInt, UInt, UDInt, Real, LReal | ​数学运算输出 |

!!! note "注 \*  : 参数 IN1、IN2 和 OUT 的数据类型必须相同。"

![alt text](image-3.png){ align=left } ​要添加 ADD 或 MUL 输入，请单击“创建”(Create) 图标，或在其中一个现有 ​IN​ 参数的输入短线处单击右键，并选择“插入输入”(Insert input) 命令。

​要删除输入，请在其中一个现有 ​IN​ 参数（多于两个原始输入时）的输入短线处单击右键，并选择“删除”(Delete) 命令。

​启用数学指令 (EN = 1) 后，指令会对输入值（IN1 和 IN2）执行指定的运算并将结果存储在通过输出参数 (OUT) 指定的存储器地址中。运算成功完成后，指令会设置 ENO = 1。

## ENO 状态 
| ​ENO | ​说明 |
|-----|------------|
| ​1  | ​无错误 |
| ​0  | ​数学运算结果值可能超出所选数据类型的有效数值范围。返回适合目标大小的结果的最低有效部分。 |
| ​0  | ​除数为 0 (IN2 = 0)：结果未定义，返回 0。 |
| ​0  | ​Real/LReal：如果其中一个输入值为 NaN（不是数字），则返回 NaN。 |
| ​0  | ​ADD Real/LReal：如果两个 IN 值均为 INF，但符号不同，则这是非法运算并返回 NaN。 |
| ​0  | ​SUB Real/LReal：如果两个 IN 值均为 INF，且符号相同，则这是非法运算并返回 NaN。 |
| ​0  | ​MUL Real/LReal：如果一个 IN 值为零而另一个为 INF，则这是非法运算并返回 NaN。 |
| ​0  | ​DIV Real/LReal：如果两个 IN 值均为零或 INF，则这是非法运算并返回 NaN。 |