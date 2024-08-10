# Calculate（数学计算）

## CALCULATE 指令

|     |     |     |
| --- | --- | --- |
| ​LAD/FBD | ​SCL | ​说明 |
| ​<br><br>[![alt text](image.png)](#) | ​使用标准 SCL 数学表达式创建等式。 | ​CALCULATE​ 指令可以根据定义的等式生成作用于输入（​IN1​、​IN2​、.. ​INn​）并在 ​OUT​ 中生成结果的数学函数。<br><br>* ​首先选择数据类型。所有输入和输出的数据类型必须相同。<br>    <br>* ​要添加其它输入，请单击最后一个输入处的图标。 |

## 参数的数据类型

|     |     |
| --- | --- |
| ​参数 | ​数据类型1 |
| ​IN1, IN2, ..INn | ​SInt, Int, DInt, USInt, UInt, UDInt, Real, LReal, Byte, Word, DWord |
| ​OUT | ​SInt, Int, DInt, USInt, UInt, UDInt, Real, LReal, Byte, Word, DWord |

1 IN 和 OUT 参数必须具有相同的数据类型（通过对输入参数进行隐式转换）。例如：如果 OUT 是 INT 或 REAL，则 SINT 输入值将转换为 INT 或 REAL 值

​单击计算器图标可打开对话框，在其中定义数学函数。输入等式作为输入（如 ​IN1​ 和 ​IN2​）和操作数。单击“确定”(OK) 保存函数时，对话框会自动生成 ​CALCULATE​ 指令的输入。

​对话框显示一个示例，以及可根据 ​OUT​ 参数的数据类型加入的一列指令：

​

[![](images/72188662667_DV_resource.Stream@PNG-zh-CHS.png)](#)

|     |     |     |
| --- | --- | --- |
| 说明  |     |     |
|     |     | ​还必须为函数中的任何常量生成输入。然后会在指令 ​CALCULATE​ 的相关输入中输入该常量值。<br><br>​通过输入常量作为输入，可将 ​CALCULATE​ 指令复制到用户程序的其它位置，从而无需更改函数。之后，不需要修改函数，就可以更改指令输入的值或变量。 |

​当执行 ​CALCULATE​ 并成功完成计算中的所有单个运算时，​ENO​ = 1。否则：​ENO​ = 0。

​有关 CALCULATE 指令的示例，请参见“使用简单指令创建复杂等式”​。