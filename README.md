# PalWorld-Restarter
这个项目用于监控PalWorld的服务端,如果崩溃则会重启服务端
## 使用方法
###  方法一:使用exe文件
直接下载并使用该文件,由于这个程序会强行拉起其他程序(服务端),因此会被WindowsDefender判定为病毒,如果不放心请直接使用源代码:

https://github.com/Decikingship/PalWorld-Restarter/releases/tag/Windows
###  方法二:使用源代码
1. 安装Python3.x(如已安装请跳过): https://www.python.org/downloads/
2. 安装git(如已安装请跳过): https://git-scm.com/downloads
3. 克隆本项目: `git clone https://github.com/Decikingship/PalWorld-Restarter.git`
4. 使用cmd进入项目目录。
5. cmd执行安装依赖: `pip install -r requirements.txt`
6. 运行本项目: `python main.py`
7. 输入你的steamcmd文件夹路径并回车,默认的路径是`C:\Users\Administrator\Desktop\steamcmd`,也就是你把它放在了桌面上。

## License
本项目基于Apache-2.0协议开源,可以随意修改。

