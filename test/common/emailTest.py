import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class Email:
    global passwad
    global login
    global server
    global user
    login = 'yuanzhou.zhang@hongfans.cn'
    user =  "zhangyuanzhou"+ "<"+login+">"
    passwad = "Zyz@0408 "
    server ="smtp.exmail.qq.com"
    def send_email(self,to_list,sub,content):
        msg = MIMEMultipart('related')
        msg['Subject'] = sub
        msg['from'] = 'zhangyuaznhou<%s>'%user
        msg["to"] = ";".join(to_list)
        message = MIMEText(content, "plain", 'utf-8')
        msg.attach(message)
        att = MIMEText(open(u"F:\\test\dataconfig\\API.xls","rb").read(),"base64",'utf-8')
        att["Content-Type"] =  'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename ="test.xls"'
        msg.attach(att)
        Server = smtplib.SMTP()
        Server.connect(server,25)
        Server.login(login,passwad)
        Server.sendmail(user,to_list,msg.as_string())
        Server.close()
if __name__ == '__main__':
    cm = Email()
    to_list = ['1026928681@qq.com',"2278680647@qq.com"]
    sub = "后台接口测试结果"
    content = "a:测试通过率80%，b:失败了20%"
    cm.send_email(to_list,sub,content)