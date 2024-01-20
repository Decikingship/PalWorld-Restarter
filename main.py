import subprocess
import psutil
import time

root_directory = ''
root_directory = input(r'请输入steamcmd文件夹的路径(默认为C:\Users\Administrator\Desktop\steamcmd)：').replace('\"', '')
if root_directory == '':
    root_directory = r'C:\Users\Administrator\Desktop\steamcmd'

# [不要修改]
monitor_exe = r'steamapps\common\PalServer\Pal\Binaries\Win64\PalServer-Win64-Test-Cmd.exe'
start_exe = r'steamapps\common\PalServer\PalServer.exe'
monitor_exe_path = os.path.join(root_directory, monitor_exe)
start_exe_path = os.path.join(root_directory, start_exe)


def is_process_running(exe_name):
    """检查给定名称的进程是否正在运行"""
    for process in psutil.process_iter(['name']):
        if exe_name.lower() in process.info['name'].lower():
            return True
    return False


# 监控程序的进程名，通常是可执行文件的名称（不包含.exe）
monitor_exe_name = 'PalServer-Win64-Test-Cmd'

while True:
    # 检查程序是否正在运行
    if not is_process_running(monitor_exe_name):
        print(f'监视的程序未运行，启动程序：{start_exe_path}')
        # 启动程序
        subprocess.Popen(start_exe_path, shell=True)
    else:
        print('监视的程序正常运行。')

    # 等待一段时间再次检查
    time.sleep(60)  # 每60秒检查一次
