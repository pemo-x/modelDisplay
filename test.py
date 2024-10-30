import subprocess


def CreateTask(command, directory):
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=directory,
    )
    return process


def getRunstatu(process):
    exit_code = process.poll()

    if exit_code is None:
        return "子进程仍在运行"
    else:
        return f"子进程已结束，退出码为：{exit_code}"


def getReturn(process):
    global stdout, stderr
    Runstatu = getRunstatu(process)
    if Runstatu != "子进程仍在运行":
        stdout, stderr = process.communicate()
        # 检查子进程是否成功完成
        if process.returncode == 0:
            print("Command executed successfully")
            print(stdout)
        else:
            print("Command failed with error")
            print(stderr)
        return 1
    else:
        return 0


stdout, stderr = None, None
if __name__ == "__main__":
    # command = f'python /data/home/temp/Desktop/model/st-gcn-cam-org/main.py shapleycam --skeleton S003C001P007R002A019'.split(' ')
    command = f"python /data/home/temp/Desktop/model/test/main.py".split(" ")
    print(command)
    directory = f"/data/home/temp/Desktop/model/test"
    process = CreateTask(command, directory)
    while not getReturn(process):
        continue
    print(
        type(stdout)
    )  # stdout是模型程序运行过程中所有的输出，是一长个字符串，换行用\n，请按照你们想要展示的内容格式提取成字典
    # 比如什么result['top1'],result['top2']....
