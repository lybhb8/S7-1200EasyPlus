# LIMIT（设置限值）

LIMIT（设置限值）指令

|     |     |     |
| --- | --- | --- |
| ​LAD/FBD | ​SCL | ​说明 |
| ​<br><br>[![](images/39226275211_DV_resource.Stream@PNG-en-US.png)](#) | LIMIT(MN:=\_variant\_in_,  <br>    IN:=\_variant\_in_,  <br>    MX:=\_variant\_in_,  <br>    OUT:=\_variant\_out_); | ​Limit​ 指令用于测试参数 ​IN​ 的值是否在参数 ​MIN​ 和 ​MAX and if not, clamps the value at MIN or MAX.​ 指定的值范围内LIMIT（设置限值） |

1 对于 LAD 和 FBD：单击“???”并从下拉菜单中选择数据类型。

参数的数据类型

|     |     |     |
| --- | --- | --- |
| ​参数 | ​数据类型1 | ​说明 |
| ​MN, IN​ 和 ​MX | ​SInt, Int, DInt, USInt, UInt, UDInt, Real, LReal, Time, Date, TOD·​​常数 | ​数学运算输入 |
| ​OUT | ​SInt, Int, DInt, USInt, UInt, UDInt, Real, LReal, Time, Date, TOD | ​数学运算输出 |

1 参数 MN、IN、MX 和 OUT 的数据类型必须相同。

​如果参数 ​IN​ 的值在指定的范围内，则 ​IN​ 的值将存储在参数 ​OUT​ 中。如果参数 ​IN​ 的值超出指定的范围，则 ​OUT​ 值为参数 ​MIN​ 的值（如果 ​IN​ 值小于 ​MIN​ 值）或参数 ​MAX​ 的值（如果 ​IN​ 值大于 ​MAX​ 值）。

ENO 状态

|     |     |
| --- | --- |
| ​ENO | ​说明 |
| ​1  | ​无错误 |
| ​0  | ​Real：如果 MIN、IN 和 MAX 的一个或多个值是 NaN（不是数字），则返回 NaN。 |
| ​0  | ​如果 MIN 大于 MAX，则将值 IN 分配给 OUT。 |

​SCL 示例：示例，指令LIMIT（设置限值）

* ​MyVal := LIMIT(MN:=10,IN:=53, MX:=40); //​结果：​MyVal = 40
    
* ​MyVal := LIMIT(MN:=10,IN:=37, MX:=40); //​结果：​MyVal = 37
    
* ​MyVal := LIMIT(MN:=10,IN:=8, MX:=40); //​结果：​MyVal = 10