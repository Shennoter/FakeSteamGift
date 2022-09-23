import urllib
import emailSender
import fakeGiftGenerator


reciever = input('输入接收人昵称：')
recieverEmail = input('输入接收人邮箱：')
sender = input('输入发送人昵称：')
gameName = input('输入游戏名称：')
gameNameURLcode = urllib.parse.urlencode({'':gameName})[1:]
senderAvatarLink = input('输入发送人头像链接(建议184×184)：')
greeting = input('输入问候语(不填则默认为"祝你好运")：')

gift = fakeGiftGenerator.fakeGift(gameName, sender, senderAvatarLink, reciever, greeting)
mailText, gameOffName = gift.generateGift()
with open('./gift.html','w',encoding='utf-8')as f:
        f.write(mailText)
emailSender.sendEmail(gameOffName, recieverEmail, mailText)