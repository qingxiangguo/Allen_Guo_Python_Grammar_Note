# Qingxiang Guo
# {2022/6/4} {16:41}
'''
如何在PyCharm中安装第三方包？除了pip instal schedule
在PyCharm的settings-->Python Interpreter--->搜索你想要的包，然后选择加号
'''

import schedule  #执行定时任务的包
import time

def job():
    print('qingxiang')

schedule.every(3).seconds.do(job)  #每过3秒，执行一次job函数
#schedule.every(interval=1).(seconds,minutes,hours,days).do(task)，表示表示每隔多少（秒，分钟，小时，天），默认间隔是1，也就是每隔（一秒、一分钟、一小时、一天）要做什么任务（所谓的任务通常是指一段含有数行代码的自定义函数）
#schedule.every().friday.at("05:00").do(job)，每个星期五的早上5点做一次任务

while True:  #是个死循环，只要不使用Ctrl+C停止脚本，或者重启运行脚本的主机的话，该脚本将一直运行下去，也就实现了我们“挂机”的目的。
    schedule.run_pending()  #所有被排入schedule中的任务都不会马上被执行，而是进入pending状态，而schedule.run_pending()这个函数的作用就是立即执行所有状态为pending的函数。
    time.sleep(1)


