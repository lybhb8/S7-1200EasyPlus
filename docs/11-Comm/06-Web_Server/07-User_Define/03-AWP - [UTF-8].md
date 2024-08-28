### S7-1200 Web 服务器支持的 AWP 命令

S7-1200 Web 服务器提供了以 HTML 注释形式嵌入用户定义的 Web 页面中的 AWP
命令，这些命令具有以下用途：

-   读取变量
-   写入变量
-   读取特殊变量
-   写入特殊变量
-   定义枚举类型
-   为枚举类型分配变量
-   创建片段数据块

本文档只介绍最常用的读取和写入变量，其他命令使用请参见[系统手册](../../../01-resource/03-online_doc.htm#a)，"用户定义的
Web 页面"章节。

#### 1. 一般语法

除读取变量的命令之外，AWP 命令的语法如下：

\<!\-- AWP\_ \<command name and parameters\> \--\>

AWP 命令与典型的 HTML 表单命令一起使用时，可将变量写入 CPU。介绍 AWP
命令时采用如下惯例：

-   方括号 \[ \] 中包含的项为可选项。
-   尖括号 \< \> 中包含的项是要指定的参数值。
-   引号是命令的文字部分。 它们必须按所示的形式出现。
-   根据具体用法，变量或数据块名称中的特殊字符必须进行转义或用引号括号来。

使用文本编辑器或 HTML 编辑模式可将 AWP 命令插入页面中。

AWP 命令所需的语法

-   AWP
    命令公式中\"\<!\--\"之后的空格和\"\--\>\"之前的空格，对于命令的正确编译至关重要。疏漏空格字符可能导致编译器无法生成正确代码。
    这种情况下，编译器不会显示错误。\

#### 2. AWP 命令汇总

**读取变量**

-   :=\<Varname\>:

**写入变量**

-   \<!\-- AWP_In_Variable Name=\'\<Varname1\>\'
    \[Use=\'\<Varname2\>\'\] \... \--\>

该 AWP 命令只是声明 Name 子句中的变量可写入。 HTML 代码将按 HTML
表单中\<input\>、\<select\> 或其它 HTML 语句中的名称写入变量。

**读取特殊变量**

-   \<!\-- AWP_Out_Variable Name=\'\<Type\>:\<Name\>\'
    \[Use=\'\<Varname\>\'\] \--\>

**写入特殊变量**

-   \<!\-- AWP_In_Variable Name=\'\<Type\>:\<Name\>\'
    \[Use=\'\<Varname\>\'\]\--\>

**定义枚举类型**

-   \<!\--AWP_Enum_Def Name=\'\<Enum type name\>\' Values=\'\<Value\>,
    \<Value\>,\... \' \--\>

**引用枚举类型**

-   \<!\-- AWP_In_Variable Name=\'\<Varname\>\' Enum=\"\<Enum
    类型名称\>\" \--\>
-   \<!\-- AWP_Out_Variable Name=\'\<Varname\>\' Enum=\"\<Enum
    类型名称\>\" \--\>

**创建片段**

-   \<!\-- AWP_Start_Fragment Name=\'\<Name\>\'
    \[Type=\<Type\>\]\[ID=\<id\>\] \--\>

**导入片段**

-   \<!\-- AWP_Import_Fragment Name=\'\<名称\>\' \--\>
