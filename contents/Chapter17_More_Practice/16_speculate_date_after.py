# Qingxiang Guo
# {2022/6/28} {1:07}
'''推测几天后的日期'''
import datetime
def inputdate():
    indate=input('请输入开始日期:(20200808)后按回车')
    indate=indate.strip()  #删除字符串前导和尾随空格的字符串，类似perl里面的chomp
    datestr=indate[0:4]+'-'+indate[4:6]+'-'+indate[6:]  #利用切片操作，将字符串的日期数据提取出来，并赋予datetime库能识别的格式
    return datetime.datetime.strptime(datestr,'%Y-%m-%d')  #按照特定时间格式将字符串转换为时间类型，返回特定格式的对象

if __name__ == '__main__':
    print('-----------推算几天后的日期-----------------')
    sdate=inputdate()  #输入一个日期，通过函数，转换为特定格式
    in_num=int(input('输入间隔天数'))
    fdate=sdate+datetime.timedelta(days=in_num)  #timedelta算天数
    print('您推算的日期是'+str(fdate))