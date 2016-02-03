# -*- coding: utf-8 -*-
import sys
import smtplib
import argparse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:
    def send(self, target, subject, data, attachment):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = target

        if data:
            txt = MIMEText(data)
            msg.attach(txt)

        if attachment:
            file = MIMEText(open(attachment, 'rb').read(), 'base64', 'utf-8')
            file.add_header('Content-Disposition', 'attachment', filename=attachment.split('/')[-1])
            msg.attach(file)

        s = smtplib.SMTP()
        s.connect('smtp.exmail.qq.com')
        s.login(self.username, self.password)
        s.sendmail(self.username, target, msg.as_string())

        s.quit()

    def __init__(self, username, password):
        self.username = username
        self.password = password

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='发送邮件')
    parser.add_argument('-u', '--username', help='发送邮件的邮箱地址', required=True)
    parser.add_argument('-p', '--password', help='发送邮件的邮箱密码', required=True)
    parser.add_argument('-t', '--target', help='目标邮箱地址', required=True)
    parser.add_argument('-s', '--subject', help='邮件主题', required=True)
    parser.add_argument('-d', '--data', help='要发放的邮件文本')
    parser.add_argument('-a', '--attachment', help='附件')

    args = parser.parse_args()

    print(args.username)
    print(args.target)
    print(args.subject)
    print(args.data)
    print(args.attachment)

    sender = EmailSender(args.username, args.password)
    sender.send(args.target, args.subject, args.data, args.attachment)

