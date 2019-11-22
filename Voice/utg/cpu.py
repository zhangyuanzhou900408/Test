import psutil
import os,datetime,time


def GetCPUstate(time_count=1):  # cpu物理个数   +   cpu总使用率
    return (str(psutil.cpu_count(logical=False)) + "---" + str(psutil.cpu_percent(time_count, 0)) + "%")


# function of evryone state
def GetCPUsatus(time_count=1):  # 每个cpu的使用率
    return (str(psutil.cpu_percent(time_count, 1)) + "%")


# function of memory state
def GetMemorystate():
    phymem = psutil.virtual_memory()
    string = str(int(phymem.total / 1024 / 1024)) + "M"  # 内存总数
    string += "---"
    string += str(int(phymem.used / 1024 / 1024)) + "M"  # 已使用内存
    string += "---"
    string += str(int(phymem.free / 1024 / 1024)) + "M"  # 剩余内存
    string += "---"
    sum_mem = str(int(phymem.used / 1024 / 1024) / int(phymem.total / 1024 / 1024) * 100)  # 内存使用率
    string += sum_mem[0:5] + "%"
    return (string)

    #单个经常占用cpu
    # p1 = psutil.Process(4420)  # 进程4420占用的CPU
    # for x in range(3):
    #     psutil.cpu_percent(interval=1, percpu=True)

# 流量消耗
# def net_stat():
#     net = []
#     f = open("/proc/net/dev")
#     lines = f.readlines()
#     f.close()
#     for line in lines[2:]:
#         con = line.split()
#         """
#         intf = {}
#         intf['interface'] = con[0].lstrip(":")
#         intf['ReceiveBytes'] = int(con[1])
#         intf['ReceivePackets'] = int(con[2])
#         intf['ReceiveErrs'] = int(con[3])
#         intf['ReceiveDrop'] = int(con[4])
#         intf['ReceiveFifo'] = int(con[5])
#         intf['ReceiveFrames'] = int(con[6])
#         intf['ReceiveCompressed'] = int(con[7])
#         intf['ReceiveMulticast'] = int(con[8])
#         intf['TransmitBytes'] = int(con[9])
#         intf['TransmitPackets'] = int(con[10])
#         intf['TransmitErrs'] = int(con[11])
#         intf['TransmitDrop'] = int(con[12])
#         intf['TransmitFifo'] = int(con[13])
#         intf['TransmitFrames'] = int(con[14])
#         intf['TransmitCompressed'] = int(con[15])
#         intf['TransmitMulticast'] = int(con[16])
#         """
#         intf = dict(
#             zip(
#                 ('interface', 'ReceiveBytes', 'ReceivePackets',
#                  'ReceiveErrs', 'ReceiveDrop', 'ReceiveFifo',
#                  'ReceiveFrames', 'ReceiveCompressed', 'ReceiveMulticast',
#                  'TransmitBytes', 'TransmitPackets', 'TransmitErrs',
#                  'TransmitDrop', 'TransmitFifo', 'TransmitFrames',
#                  'TransmitCompressed', 'TransmitMulticast'),
#                 (con[0].rstrip(":"), int(con[1]), int(con[2]),
#                  int(con[3]), int(con[4]), int(con[5]),
#                  int(con[6]), int(con[7]), int(con[8]),
#                  int(con[9]), int(con[10]), int(con[11]),
#                  int(con[12]), int(con[13]), int(con[14]),
#                  int(con[15]), int(con[16]),)
#             )
#         )
#
#         net.append(intf)
#     print(net)
#     return net


def main(count):
    for i in range(count):
        info = GetCPUstate()
        info2 = GetCPUsatus()
        info3 = GetMemorystate()
        time.sleep(2)
        print("第%d组" % i + "\t\n" + "cpu物理个数和cpu总使用率分别为: %s" % info  + "\t\n" + "每个cpu的使用率%s" % info2 + "\t\n" + "内存总数/使用内存/剩余内存/内存使用率分别为：%s" % info3)
if  __name__=="__main__":
    #main(10)
    net_stat()