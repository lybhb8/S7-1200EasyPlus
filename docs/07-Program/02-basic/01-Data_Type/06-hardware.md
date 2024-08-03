# 硬件数据类型

硬件数据类型：硬件数据类型由 CPU 提供。 可用硬件数据类型的数目取决于
CPU。

根据硬件配置中设置的模块存储特定硬件数据类型的常量。
在用户程序中插入用于控制或激活已组态模块的指令时，可将这些可用常量用作参数。


| 数据类型              | 基本数据类型          | 说明                  |
|-----------------------|----------------------|----------------------|
| REMOTE                | ANY                   | 用于S7通信PUT/GET指令中指定远程CPU的数据地址，必须以P#指针的形式作为实参 <br> 例如P#DB1.DBX0.0 BYTE 10 |
| HW_ANY                | UINT                  | 任何硬件组件（如模块）的标识|
| HW_DEVICE             | HW_ANY                | DP 从站/PROFINET IO 设备的标识。<br> 例如：在ModuleStates指令中使用 |
| HW_DPSLAVE            | HW_DEVICE             | DP 从站的标识 <br> 例如：在ModuleStates、DPNRM_DG指令中使用 |
| HW_IO                 | HW_ANY                | CPU或接口的标识号,该编号在CPU或硬件配置接口的属性中自动分配和存储 <br>  例如：在LED、DPRD    _DAT、RDREC指令中使用 |
| HW_IOSYSTEM           | HW_ANY                | PN/IO 系统或 DP主站系统的标识 <br>  例如：在DeviceStates指令中使用 |
| HW_SUBMODULE          | HW_IO                 | 重要硬件组件的标识 <br> 例如：在GETIO指令中使用 |
| HW_INTERFACE          | HW_SUBMODULE          | 接口组件的标识        |
| HW_IEPORT             | HW_SUBMODULE          | 端口的标识 (PN/IO)   |
| HW_HSC                | HW_SUBMODULE          | 高速计数器的标识 <br> 例如：在CTRL_HSC、CTRL_HSC_EXT指令中使用 |
| HW_PWM                | HW_SUBMODULE          | 脉冲宽度调制标识 <br>  例如：在CTRL_PWM指令中使用  |
| HW_PTO                | HW_SUBMODULE          | 脉冲发生器标识 <br>  例如：在CTRL_PTO指令中使用  |
| AOM_IDENT             | DWORD                 | AS 运行系统中对象的标识  |
| EVENT_ANY             | AOM_IDENT             | 用于标识任意事件      |
| EVENT_ATT             | EVENT_ANY             | 用于指定动态分配给硬件中断OB 的事件 <br> 例如，在ATTACH、DETACH指令中使用 |
| EVENT_HWINT           | EVENT_ATT             | 用于指定硬件中断事件  |
| OB_ANY                | INT                   | 用于指定任意组织块 <br> 例如，在时间错误OB启动信息中出现  |
| OB_DELAY              | OB_ANY                | 指定调用的延时中断OB <br> 例如，用于SRT_DINT、CAN_DINT、QRY_DINT指令 |
| OB_TOD                | OB_ANY                | 指定调用的时间中断OB <br> 例如，用于SET_TINT、CAN_TINT、ACT_TINT、QRY_TINT指令 |
| OB_CYCLIC             | OB_ANY                | 指定调用的循环中断OB <br> 例如，用于SET_CINT、QRY_CINT指令 |
| OB_ATT                | OB_ANY                | 用于指定动态分配给事件的硬件中断OB <br> 例如，用于ATTACH、DETACH指令  |
| OB_PCYCLE             | OB_ANY                | 用于指定循环OB事件类别事件的组织块 |
| OB_HWINT              | OB_ATT                | 用于指定发生硬件中断时调用的组织块  |
| OB_DIAG               | OB_ANY                | 用于指定发生诊断中断时调用的组织块  |
| OB_TIMEERROR          | OB_ANY                | 用于指定发生时间错误时调用的组织块  |
| OB_STARTUP            | OB_ANY                | 用于指定发生启动事件时调用的组织块  |
| PORT                  | HW_SUBMODULE          | 用于指定通信端口 <br>  例如，用于自由口、ModbusRTU指令 |
| RTM                   | UINT                  | 用于指定运行小时计数器值 <br> 例如，用于RTM指令     |
| CONN_ANY              | WORD                  | 用于指定任意连接    |
| CONN_OUC              | CONN_ANY              | 用于指定通过工业以太网进行开放式通信的连接 <br> 例如，用于TCON、TSEND_C指令 |
| DB_WWW                | DB_ANY                | 通过自定义 Web应用生成的 DB号该数据类型在Temp区域中的长度为0 <br> 例如，用于WWW指令     |
| DB_DYN                | DB_ANY                | 用户程序生成的DB编号 <br> 例如，用于CREAT_DB指令  |
