# Variant类型

Variant类型是一个参数数据类型，只能出现在除FB的静态变量以外的OB/FC/FB接口区。

Variant类型的实参是一个可以指向不同数据类型变量的指针。它可以指向基本数据类型，也可以指向复杂数据类型、UDT等。

Variant 数据类型的操作数不占用背景数据块或工作存储器中的空间，但是将占用CPU 上的装载存储器的存储空间。

调用某个块时，可以将该块的Variant参数连接任何数据类型的变量。除了传递变量的指针外，还会传递变量的类型信息。该块中可以利用Variant的相关指令，将其识别出并进行处理。

Variant指向的实参，可以是符号寻址，也可以是绝对地址寻址，还可以是形如P#DB1.DBX0.0 BYTE 10这种指针形式的寻址。

在早期版本的TIA博途软件中，只有一些通讯指令使用Variant变量。从TIA V13SP1
开始，S7-1200 V4.0开始，可以在程序块实参定义Variant类型变量，并且还可以通过以下指令处理Variant类型的变量。

## 1\. 判断类指令，该类指令作用是检查Variant类型的实参的实际类型，并不参与直接处理，参见表1。

表1 判断类指令

| LAD             | SCL             | 位置                 |
|-----------------|-----------------|--------------------|
| [EQ_Type](../../03-instruction/01-Basic/03-Compare_Variant.md#eq_typene_typetypeof) | [TypeOf](../../03-instruction/01-Basic/03-Compare_Variant.md#eq_typene_typetypeof) |基本指令 -- 比较操作 -- 变量 |
| [NE_Type](../../03-instruction/01-Basic/03-Compare_Variant.md#eq_typene_typetypeof) | [TypeOf](../../03-instruction/01-Basic/03-Compare_Variant.md#eq_typene_typetypeof)                | 基本指令 -- 比较操作 -- 变量                   |
|[EQ_ElemType](../../03-instruction/01-Basic/03-Compare_Variant.md#eq_elemtypene_elemtypetypeofelements) | [TypeOfElements](../../03-instruction/01-Basic/03-Compare_Variant.md#eq_elemtypene_elemtypetypeofelements)  | 基本指令 -- 比较操作 -- 变量                   |
| [NE_ElemType](../../03-instruction/01-Basic/03-Compare_Variant.md#eq_elemtypene_elemtypetypeofelements)      |  [TypeOfElements](../../03-instruction/01-Basic/03-Compare_Variant.md#eq_elemtypene_elemtypetypeofelements)  | 基本指令 -- 比较操作 -- 变量                   |
| [IS_NULL](../../03-instruction/01-Basic/03-Compare_Variant.md#nullis_nullnot_null) | &nbsp;  | 基本指令 -- 比较操作 -- 变量                   |
|[NOT_NULL](../../03-instruction/01-Basic/03-Compare_Variant.md#nullis_nullnot_null) | &nbsp;   |  基本指令 -- 比较操作 -- 变量                  |
|[IS_ARRAY](../../03-instruction/01-Basic/03-Compare_Variant.md#arrayis_array) | [IS_ARRAY](../../03-instruction/01-Basic/03-Compare_Variant.md#arrayis_array)  |  基本指令 -- 比较操作 -- 变量        |
|[CountOfElements](../../03-instruction/01-Basic/04-Move/05-MOVE_Variant].md#countcountofelements) | [CountOfElements](../../03-instruction/01-Basic/04-Move/05-MOVE_Variant].md#countcountofelements) | 基本指令 -- 移动操作 -- 变量 |

## 2\. 处理类指令，该类指令可以对Variant类型的实参进行转化，参见表2。

表2 处理类指令

  |LAD/SCL                                                                         |    位置                  |
  |---------------------------------------------------------------------------------|--------------------------------|
  |[Deserialize](../../03-instruction/01-Basic/04-Move/02-DeserializeSerialize.md#deserialize反序列化serialize序列化) |  基本指令 \-- 移动操作|
  |[Serialize](../../03-instruction/01-Basic/04-Move/02-DeserializeSerialize.md)     | 基本指令 \-- 移动操作|
  |[MOVE_BLK_VARIANT](../../03-instruction/01-Basic/04-Move/01-MOVE.md#cmove_blk_variant)       |基本指令 \-- 移动操作|
  |[VariantGet](../../03-instruction/01-Basic/04-Move/05-MOVE_Variant.md#variantvariantgetvariantput)    |基本指令 \-- 移动操作 \-- 变量|
  |[VariantPut](../../03-instruction/01-Basic/04-Move/05-MOVE_Variant.md#variantvariantgetvariantput)    |基本指令 \-- 移动操作 \-- 变量|

## 3\. 其他指令

DB_ANY_TO_VARIANT与VARIANT_TO_DB_ANY，参见[DB_ANY](./08-DB_ANY.md)。

## P\#指针说明

当Variant类型的实参指向 **[形如]{.underline}** P#DB1.DBX0.0 BYTE
10，指令内部将判断该形参为一个10字节的数组。

## 指针结构

- P#DB1.DBX0.0 BYTE 10这种结构起源于S7-300/S7-400的Any指针，S7-1200无法像S7-300/S7-400一样定义以及拆解Any指针，但是在参数类型为Variant时，可以输入这种指针。并且，如前所述，S7-1200将识别其为数组。
- P#DB1.DBX0.0 BYTE 10的解释：指向从DB1.DBX0.0开始的10个字节，并且DB1必须是非优化的DB块，并包含有10字节长度的变量。
- P#DB1.DBX位置可以替换成其他DB块号例如P#DB10.DBX，或者I区：P#I，Q区：P#Q，M区：P#M。
- 0.0的位置为这种指针的起始地址，例如1.0、100.0、\...\...，并且小数点后一定是0。
- BYTE位置可以是以下类型：Bool、Byte、Word、DWord、Int、DInt、Real、Char、Date、TOD、Time类型。
- 10的位置为指针执行前面数据类型的个数，Bool类型比较特殊，只能是1，或者8的倍数。
- P#指针举例，P#I0.0 Bool 8，P#Q0.0 Word 20，P#M100.0 Int 50。
