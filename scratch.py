import threading
import time

from matplotlib import pyplot as plt


class Board(threading.Thread):
    def __init__(self,param,param1):
        super(Board, self).__init__()
        self.flag = True
        self.param = param
        self.param1 =param1
    def run(self):
        while self.flag:
            print(self.param)
            print(self.param1)
            time.sleep(1)
        print("end")

    def stop(self):
        self.flag = False
    def restart(self,param,param1): # 用来恢复/启动run
        self.flag = True
        self.param = param
        self.param1 =param1
        self.run()
if __name__ == "__main__":
    t1 =Board('11','22')
    t1.start()
    time.sleep(5)
    t1.stop()
    time.sleep(2)
    t1.restart('33','44')