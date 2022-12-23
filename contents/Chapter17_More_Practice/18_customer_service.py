# Qingxiang Guo
# {2022/6/28} {17:27}
'''客户服务，自动回答'''
def find_answer(question):  #question是你输入的
    with open('reply.txt','r',encoding='gbk') as file:
        while True:
            line=file.readline()
            if not line:  #如果读到文件末尾
                break
            #关键词分割
            keyword=line.split('|')[0]
            reply=line.split('|')[1]
            if keyword in question:
                return reply
    return False

if __name__ == '__main__':
    question=input('有什么能帮你的？')
    while True:
        if question=='bye':
            break
        #开始在文件中查找
        reply=find_answer(question)
        if not reply: #如果返回的是False
            question=input('不知道你在说什么，问一些订单，物流，账户，支付问题，退出输入bye')
        else:
            print(reply)
            question=input('你还可以继续，问一些订单，物流，账户，支付问题，退出输入bye')
    print('再见')