'''
一键发送邮件
by:ice
'''
# coding: utf8
import smtplib
from email.mime.text import MIMEText
# smtp服务器
smtpserver = 'smtp.qq.com'
# 发送方信息
user = '2357725809@qq.com'
passwd = 'koyfoyjyesjeebed'
# 小号授权码koyfoyjyesjeebed
# 大号授权码tvhvmldgsethbhij
# 接收方信息2357725809
#奶子鹏1964834615
#普元1981108163
#此处接受方
textmassage='那时哥还小，邻居家一个哥哥比我大很多。我当时只会做1加1等于2，而他会做1万加1万等于两万。他居然可以做到那么大的数字，我很佩服。他还说，等他上了大学就可以知道1亿加1亿是多'
rubbish1='曾经有一段真挚的爱情摆在我面前，我没有珍惜，现在想起来，还好没有珍惜'
rubbish2='20岁认为诸葛亮有水平，30岁认为刘备有水平，40岁发现刘禅有水平。20岁恋爱考虑结果，30岁恋爱考虑后果，40岁恋爱考虑因果。'
rubbish3='垃圾'
rubbish4='舔狗最后一无所有'
receiver = "1103971604@qq.com"
message = MIMEText(rubbish1, "plain", "utf-8")
message["from"] = user
message["to"] = receiver
message["subject"] = '你有一封邮件'
count=0
# for i in range(10):
while True:
    server = smtplib.SMTP(host=smtpserver, port=25)
    server.login(user, passwd)
    server.sendmail(from_addr=user, to_addrs=receiver, msg=message.as_string())
    server.quit()
    # print("finish")
    count+=1
    print(count)
