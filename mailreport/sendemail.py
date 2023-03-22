import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

# from tests.test_case import Test_py



class SendEmail:
    my_sender = '460330968@qq.com'  # 发件人邮箱账号
    my_pass = 'ckyrhgagruoucage'  # 发件人邮箱密码
    my_user = '1447953727@qq.com'  # 收件人邮箱账号，我这边发送给自己


    def mail(self,report_name):
        ret = True
        try:
            msg = MIMEMultipart()
            msg['From'] = formataddr(["From460330968", self.my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["游戏人生", self.my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "学校平台测试报告"  # 邮件的主题，也可以说是标题

            msg.attach(MIMEText("学校平台自动化测试报告",'plain','utf-8'))
            # 构造一个文件


            att1 = MIMEText(open('../tests/report/'+report_name,'rb').read(),'base64','utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename='+report_name
            msg.attach(att1)

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.my_sender, self.my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.my_sender, [self.my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        return ret


# if __name__ == '__main__':
#     ret = SendEmail().mail('2021-06-08-16-18-56 report.html')
#
#     if ret:
#         print("邮件发送成功")
#     else:
#         print("邮件发送失败")
