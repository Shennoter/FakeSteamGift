import smtplib
import email.mime.multipart
import email.mime.text
def sendEmail(gameName, recieverEmail, emailText):
    # 建立邮件对象
    msg = email.mime.multipart.MIMEMultipart()

    # 填写数据
    msg['Subject'] = u'您在 Steam 上收到了游戏 {0} 的礼物副本'.format(gameName)
    msg['From'] = 'noreply@steampowered.com' # 如果不用本地smtp服务器一般会被当作垃圾邮件无法发送
    msg['To'] = recieverEmail
    body = emailText
    msg.attach(email.mime.text.MIMEText(body,'html','utf-8'))

    try:
        smtp = smtplib.SMTP()
        # 连接到服务器
        smtp.connect('smtp.qq.com', '25')
        # 密码为授权码
        smtp.login('sender@example.com', 'AUTHCODE')
        # 发送邮件
        smtp.sendmail('sender@example.com', [recieverEmail], msg.as_bytes())
        smtp.quit()
        print('邮件发送成功!')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    content = """
    <html>
        <h2 style='color:red'>将进酒</h2>
        <p>人生得意须尽欢，莫使金樽空对月。</p>
        <p>天生我材必有用，千金散尽还复来。</p>
    </html>
    """
    sendEmail('DEATH STRANDING','reciever@example.com',content)