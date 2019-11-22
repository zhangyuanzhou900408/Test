import os
from email import encoders
import time
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from_addr = 'yuanzhou.zhang@hongfans.cn'
to_addr = '1026928681@qq.com'
smtp_server = 'smtp.exmail.qq.com' #发件服务器
password = 'Zyz@0408 '
msg1 = 'HELO , this is just a send test'
subject = u'自动化测试结果'

'''发送测试邮件'''

def format_addr(s):
      name, addr = parseaddr(s)
      return formataddr((Header(name,'utf-8').encode(),addr))
def email_sender():
    server = smtplib.SMTP(smtp_server,25)
    print(server)
    #server.debuglevel(1) #打印server日志
    server.login(from_addr,password)
    server.connect(smtp_server)
    msg = MIMEMultipart()
    msg["From"] = format_addr('元周 <%s> ' % from_addr)
    msg['to'] = format_addr('猪猪 <%s>'  % to_addr)
    msg['Subject'] = Header('自动化测试结果' ,'utf-8').encode()
    '''邮件正文'''
    msg.attach(MIMEText(msg1,'plain','utf-8'))
    #print(msg)
    with open("D:\\python\\Report\\*KW",'rb') as f:
        mime = MIMEBase('hello , this is just a send test' , 'html' , filename = 'test.html')
        mime.add_header('Content-Disposition', 'attachment', filename ='test.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        msg.attach(mime)
        #print(msg)
        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr,password)
        server.sendmail(from_addr,[to_addr],msg.as_string())#发送邮件
        #print(server.sendmail())
        server.quit()
if __name__ == '__main__':
    email_sender()

