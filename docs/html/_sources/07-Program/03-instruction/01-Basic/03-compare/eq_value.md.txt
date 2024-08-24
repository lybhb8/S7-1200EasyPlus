# 比较值指令



比较指令

|     |     |     |     |
| --- | --- | --- | --- |
| ​LAD \*| ​FBD \*| ​SCL | ​说明 |
| ​<br><br> ![alt text](image.png) | ​<br><br> | out := in1 = in2;<br><br>​或<br><br>IF in1 = in2   <br>    THEN out := 1;  <br>    ELSE out := 0;  <br>    END_IF; | ​比较数据类型相同的两个值。该 LAD 触点比较结果为 TRUE 时，则该触点会被激活。如果该 FBD 功能框比较结果为 TRUE，则功能框输出为 TRUE。指令比较值比较值SCL（结构化控制语言）比较值== 框（FBD 比较运算） |

!!! note "\*  对于 LAD 和 FBD：单击指令名称（如“==”），以从下拉列表中更改比较类型。单击“???”并从下拉列表中选择数据类型。"

参数的数据类型

|     |     |     |
| --- | --- | --- |
| ​参数 | ​数据类型 | ​说明 |
| ​IN1, IN2 | ​Byte, Word, DWord, SInt, Int, DInt, USInt, UInt, UDInt, Real, LReal, String, WString, Char, Char, Time, Date, TOD, DTL,​ 常数 | ​要比较的值 |

比较说明

|     |     |
| --- | --- |
| ​关系类型 | ​满足以下条件时比较结果为真 ... |
| ​=  | ​IN1 等于 IN2 |
| ​<> | ​IN1 不等于 IN2 |
| ​>= | ​IN1 大于或等于 IN2 |
| ​<= | ​IN1 小于或等于 IN2 |
| ​>  | ​IN1 大于 IN2 |
| ​<  | ​IN1 小于 IN2 |