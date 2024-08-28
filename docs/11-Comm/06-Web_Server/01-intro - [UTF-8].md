### Web 服务器

借助 S7-1200 的 Web 服务器，用户可经由 Web 页面来访问 CPU
相关数据以及过程数据。

#### 标准 Web 页面

S7-1200 包含可通过 PC 的 Web 浏览器进行访问或通过移动设备访问的标准 Web
页面：

-   介绍 - 标准 Web 页面的进入点；
-   起始页面 - 有关 CPU 的常规信息；
-   诊断 - 有关 CPU
    的详细信息，包括序列号、订货号和版本号、程序保护和存储器使用情况；
-   诊断缓冲区 - 诊断缓冲区；
-   模块信息 - 有关本地机架中的模块和固件更新功能的信息
-   通信 -
    有关网络地址、通信接口的物理属性、统计、参数的信息，以及连接概要和诊断信息；
-   变量状态 - CPU 变量和 I/O，可通过地址或 PLC 变量名称进行访问；
-   监控表 - 在 STEP 7 中组态的监控表；
-   在线备份 - 能够备份在线 CPU 或恢复之前进行的在线备份；
-   数据日志 - 可用于查看 PLC 上所有数据日志的列表，将数据日志从 PLC
    下载到计算机，从 PLC 中删除数据日志，以及检索并清除 PLC
    中的数据日志；
-   用户文件 - 可用于查看 PLC 上用户文件的列表，将用户文件从 PLC
    下载到计算机，将用户文件从计算机上传到 PLC，以及删除 PLC
    上的用户文件；
-   用户定义的页面 - 创建用户定义的 Web 页面以访问 CPU 数据；
-   文件浏览器 - 用于浏览存储在 CPU
    或存储卡内部的文件（如数据日志和配方）的浏览器；
-   登录 - 以其他用户身份登录，或注销。

这些页面内置于 S7-1200 CPU
中，提供英语、德语、法语、西班牙语、意大利语和简体中文等版本。
有些页面需要在 STEP 7 中组态附加用户权限以查看页面。 有关标准 Web
页面以及如何访问这些页面的详细信息，请参见[链接](06-Standard/01-Standard.html)。

#### 用户定义的 Web 页面

S7-1200 还支持创建可访问 CPU 数据的用户定义的 Web 页面。 可以使用所选的
HTML 创作软件来开发这类页面，并且可将预定义的\"AWP\"（Automation Web
Programming，自动化 Web 编程）命令包含在 HTML 代码中以访问 CPU 数据。

有关开发用户定义 Web 页面以及在 STEP 7
中进行相关组态和编程的具体信息，请参见[链接](07-User_Define/01-Intro.html)。

可通过 PC 或移动设备，从标准 Web 页面访问用户定义页面。

#### Web 浏览器要求

Web 服务器支持以下 PC / 移动设备 Web 浏览器：

-   Internet Explorer 11
-   Microsoft Edge V44
-   Microsoft Edge Chromium Based V86
-   Mozilla Firefox V64
-   Opera V58
-   Google Chrome V75
-   Android Pie V9 的 Android 浏览器
-   Android Pie V9 的 Mobile Chrome
-   iOS V13 的 Mobile Safari 和 Chrome

#### Web 组态访问链接集合

[基本组态](02-WebServer_GeneralSetting.html)

[安全设置](03-WebServer_SecuritySetting.html)

[PC 端访问](04-WebServer_AccessFromPC.html)

[手机端访问](05-WebServer_AccessFromMobile.html)

[标准页面](06-Standard/01-Standard.html)

[自定义页面](07-User_Define/01-Intro.html)\
