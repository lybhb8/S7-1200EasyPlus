# MOD（返回除法的余数）


## 取模MOD 指令
| ​LAD/FBD \*| ​SCL | ​说明 |
| --- | --- | --- |
| ​![alt text](image-4.png) | out := in1 MOD  in2; | ​可以使用 ​MOD​ 指令返回整数除法运算的余数。用输入 ​IN1​ 的值除以输入 ​IN2​ 的值，在输出 ​OUT​ 中返回余数。 MOD（返回除法的余数） |

!!! note "\* : LAD 和 FBD：单击“???”并从下拉菜单中选择数据类型。"

## 参数的数据类型


| ​参数 | ​数据类型*| ​说明 |
| --- | --- | --- |
| ​IN1​ 和 ​IN2 | ​SInt, Int, DInt, USInt, UInt, UDInt, ​常数 | ​求模输入 |
| ​OUT | ​SInt, Int, DInt, USInt, UInt, UDInt | ​求模输出 |

!!! note "* :参数 IN1、IN2 和 OUT 的数据类型必须相同。"

## ENO 值
| ​ENO | ​说明 |
| --- | --- |
| ​1  | ​无错误 |
| ​0  | ​值 ​IN2​ = 0，​OUT​ 被赋以零值 |