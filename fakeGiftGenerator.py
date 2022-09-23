from tkinter import W
import urllib
import requests
from lxml import etree

class fakeGift:
    def __init__(self, gameName, sender, senderAvatarLink, reciever, greeting):
        self.__gameName = gameName
        self.__sender = sender
        self.__senderAvatarLink = senderAvatarLink
        self.__reciever = reciever
        if greeting == '':
            self.__greeting = '祝你好运'
        else:
            self.__greeting = greeting
        self.__headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'}
        self.__cookies = {'birthtime':'943977601','steamCountry':'TW%7C6a19e09c7e361488a00ffc68b545c5ce','timezoneOffset':'28800,0','lastagecheckage':'1-0-2000', 'wants_mature_content':'1'}
    def generateGift(self):
        url = 'https://store.steampowered.com/search/?term={0}'.format(self.__gameName)
        gameLinkPath = '//*[@id="search_resultsRows"]/a[1]//@href'
        # 获取商店页面链接
        res = requests.get(url=url, headers=self.__headers, cookies=self.__cookies).text
        html = etree.HTML(res)
        gameLinkObj = html.xpath(gameLinkPath)
        for i in gameLinkObj:
            gameLink = i
        print('商店页面链接:', gameLink)

        # 获取头图链接
        res2 = requests.get(url=gameLink, headers=self.__headers, cookies=self.__cookies).text
        html2 = etree.HTML(res2)
        gamePicLinkObj = html2.xpath("//img[@class='game_header_image_full']//@src")
        for j in gamePicLinkObj:
            gamePicLink = j
        print('头图链接:', gamePicLink)
        # 获取正式名称
        gameOffNameObj = html2.xpath("//div[@id='appHubAppName']")
        for k in gameOffNameObj:
            gameOffName = k
        print('游戏正式名称:', gameOffName.text)

        mail = '''
        <html>
            <center>
                <table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin: 0; padding: 0; width: 100%; height: 100%;" bgcolor="#ffffff" class="gwfw">
                    <tbody><tr>
                        <td style="margin: 0; padding: 0; width: 100%; height: 100%;" align="center" valign="top">
                            <table width="775" border="0" cellspacing="0" cellpadding="0" class="m-shell">
                                <tbody><tr>
                                    <td class="td" style="width:775px; min-width:775px; font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal;">
                                        <table width="100%" border="0" cellspacing="0" cellpadding="0">

                                            <tbody><tr>
                                                <td class="p-80 mpy-35 mpx-15" bgcolor="#212429" style="padding: 80px;">
                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0">


                                                        <tbody><tr>
                                                            <td class="img pb-45" style="font-size:0pt; line-height:0pt; text-align:left; padding-bottom: 45px;">
                                                                <a href="https://store.steampowered.com/" target="_blank" rel="noopener">
                                                                    <img src="https://store.cloudflare.steamstatic.com/public/shared/images/email/logo.png" width="615" height="88" border="0">
                                                                </a>

                                                            </td>
                                                        </tr>



                                                        <tr>
                                                            <td>


                                                                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                    <tbody><tr>
                                                                        <td class="title-36 pb-30 c-grey6 fw-b" style="font-size:36px; line-height:42px; font-family:&#39;Motiva Sans&#39;, Helvetica, Arial, sans-serif; text-align:left; padding-bottom: 30px; color:#bfbfbf; font-weight:bold;">您收到了一件礼物</td>
                                                                    </tr>
                                                                    </tbody></table>



                                                                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                    <tbody><tr>
                                                                        <td class="text-18 c-white pb-20" style="font-size:18px; line-height:25px; font-family:&#39;Motiva Sans&#39;, Helvetica, Arial, sans-serif; text-align:left; color:#dbdbdb; padding-bottom: 20px;">您的好友 {0} 在 Steam 上赠送了您一份游戏<br><i>{1} </i>的礼物订阅。</td>
                                                                    </tr>
                                                                    </tbody></table>




                                                                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                    <tbody><tr>
                                                                        <td class="pb-56" style="padding-bottom: 56px;">
                                                                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                                <tbody><tr>
                                                                                    <td class="fluid-img pb-28" style="font-size:0pt; line-height:0pt; text-align:left; padding-bottom: 28px;">
                                                                                        <a href="{2}" target="_blank" rel="noopener"><img src="{3}" width="616" height="288" border="0"></a>S
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td>
                                                                                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                                            <tbody><tr>
                                                                                                <td class="img" width="3" bgcolor="#727a83" style="font-size:0pt; line-height:0pt; text-align:left;"></td>
                                                                                                <td class="img" width="34" style="font-size:0pt; line-height:0pt; text-align:left;"></td>
                                                                                                <td>
                                                                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                                                        <tbody><tr>
                                                                                                            <td class="text-18 c-grey4 pb-30" style="font-size:18px; line-height:25px; font-family:&#39;Motiva Sans&#39;, Arial, sans-serif; text-align:left; color:#f1f1f1; padding-bottom: 30px;">
                                                                                                                {4}，您好！<br><br>
                                                                                                                {5}                                        </td>
                                                                                                        </tr>
                                                                                                        <tr>
                                                                                                            <td class="text-18 c-white fw-b pb-14" style="font-size:18px; line-height:25px; font-family:&#39;Motiva Sans&#39;, Arial, sans-serif; text-align:left; color:#ffffff; font-weight:bold; padding-bottom: 14px;">祝你好运,</td>
                                                                                                        </tr>
                                                                                                        <tr>
                                                                                                            <td>
                                                                                                                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                                                                    <tbody><tr>
                                                                                                                        <td class="img" width="45" style="font-size:0pt; line-height:0pt; text-align:left;">
                                                                                                                            <img src="{6}" width="32" height="32" border="0"> 
                                                                                                                        </td>
                                                                                                                        <td class="text-18 c-white fw-b" style="font-size:18px; line-height:25px; font-family:&#39;Motiva Sans&#39;, Arial, sans-serif; text-align:left; color:#ffffff; font-weight:bold;">
                                                                                                                            {7}                                                     </td>
                                                                                                                    </tr>
                                                                                                                    </tbody></table>
                                                                                                            </td>
                                                                                                        </tr>
                                                                                                        </tbody></table>
                                                                                                </td>
                                                                                            </tr>
                                                                                            </tbody></table>
                                                                                    </td>
                                                                                </tr>
                                                                                </tbody></table>
                                                                        </td>
                                                                    </tr>
                                                                    </tbody></table>





                                                                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                    <tbody><tr>
                                                                        <td class="pb-20" style="padding-bottom: 20px;">
                                                                            <table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#17191c">
                                                                                <tbody><tr>
                                                                                    <td class="py-35 px-56 mpx-20" align="center" style="padding-top: 35px; padding-bottom: 35px; padding-left: 56px; padding-right: 56px;">
                                                                                        <table width="400" border="0" cellspacing="0" cellpadding="0" class="mw-auto">
                                                                                            <tbody><tr>
                                                                                                <td class="btn-18 c-grey4 l-grey4 tt-u" bgcolor="#235ecf" style="font-size:18px; line-height:22px; mso-padding-alt:14px 35px; font-family:&#39;Motiva Sans&#39;, Helvetica, Arial, sans-serif; text-align:center; border-radius:5px; letter-spacing:1px; background:linear-gradient(90deg, #3A9BED 0%, #235ECF 100%); color:#f1f1f1; text-transform:uppercase;">
                                                                                                    <a href="https://store.steampowered.com/account/ackgift/3FDB98C9D7C1BB16?client=1&amp;redeemer=name%40qq.com" target="_blank" class="link c-grey4" style="display: block; padding: 13px 35px; text-decoration:none; color:#f1f1f1;" rel="noopener">
                                                                                                        <span class="link c-grey4" style="text-decoration:none; color:#f1f1f1;">接收礼物&nbsp;&nbsp; </span>
                                                                                                    </a>
                                                                                                </td>
                                                                                            </tr>
                                                                                            </tbody></table>
                                                                                    </td>
                                                                                </tr>
                                                                                </tbody></table>
                                                                        </td>
                                                                    </tr>
                                                                    </tbody></table>



                                                                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                    <tbody><tr>
                                                                        <td class="text-18 c-grey4 pb-30" style="font-size:18px; line-height:25px; font-family:&#39;Motiva Sans&#39;, Helvetica, Arial, sans-serif; text-align:left; color:#dbdbdb; padding-bottom: 30px;">    如果以上按钮不起作用，可使用此链接接收您的礼物：    <br>
                                                                            <a href="https://store.steampowered.com/account/ackgift/3FDB98C9D7C1BB16?redeemer=name%40qq.com" target="_blank" class="link-u c-white" style="text-decoration:underline; color:#ffffff;" rel="noopener">
                    <span class="link-u c-white" style="text-decoration:underline; color:#ffffff;">
                        https://store.steampowered.com/account/ackgift/3FDB98C9D7C1BB16?redeemer=name%40qq.com        </span>
                                                                            </a>
                                                                        </td>
                                                                    </tr>
                                                                    </tbody></table>



                                                                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                    <tbody><tr>
                                                                        <td class="pt-30" style="padding-top: 30px;">
                                                                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                                <tbody><tr>
                                                                                    <td class="img" width="3" bgcolor="#3a9aed" style="font-size:0pt; line-height:0pt; text-align:left;"></td>
                                                                                    <td class="img" width="37" style="font-size:0pt; line-height:0pt; text-align:left;"></td>
                                                                                    <td>
                                                                                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                                            <tbody><tr>
                                                                                                <td class="text-16 py-20 c-grey4 fallback-font" style="font-size:16px; line-height:22px; font-family:&#39;Motiva Sans&#39;, Helvetica, Arial, sans-serif; text-align:left; padding-top: 20px; padding-bottom: 20px; color:#f1f1f1;">
                                                                                                    祝您愉快，<br>
                                                                                                    Steam团队                                                                                    </td>
                                                                                            </tr>
                                                                                            </tbody></table>
                                                                                    </td>
                                                                                </tr>
                                                                                </tbody></table>
                                                                        </td>
                                                                    </tr>
                                                                    </tbody></table>


                                                            </td>
                                                        </tr>

                                                        </tbody></table>
                                                </td>
                                            </tr>



                                            <tr>
                                                <td class="py-60 px-90 mpy-40 mpx-15" style="padding-top: 60px; padding-bottom: 60px; padding-left: 90px; padding-right: 90px;">
                                                    <table width="100%" border="0" cellspacing="0" cellpadding="0">

                                                        <tbody><tr>
                                                            <td class="text-18 pb-60 mpb-40 fallback-font" style="font-size:18px; line-height:25px; color:#000001; font-family:&#39;Motiva Sans&#39;, Helvetica, Arial, sans-serif; text-align:left; padding-bottom: 60px;">
                                                                此通知已发送至与您的 Steam 帐户关联的电子邮件地址。                                                    <br><br>
                                                                这封电子邮件由系统自动生成，请勿回复。如果您需要额外帮助，请访问 Steam 客服。                                                    <br><br>
                                                            </td>
                                                        </tr>


                                                        <tr>
                                                            <td class="pb-60" style="padding-bottom: 60px;">
                                                                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                    <tbody><tr>
                                                                        <th class="column" width="270" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal;">
                                                                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                                <tbody><tr>
                                                                                    <td class="text-18 mpb-40 fallback-font" style="font-size:18px; line-height:25px; color:#000001; font-family:&#39;Motiva Sans&#39;, Helvetica, Arial, sans-serif; text-align:left;">
                                                                                        <a href="https://help.steampowered.com/" target="_blank" class="link-u c-black" style="text-decoration:underline; color:#000001;" rel="noopener">
                                                                                            <span class="link-u c-black" style="text-decoration:underline; color:#000001;">https://help.steampowered.com</span>
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                                </tbody></table>
                                                                        </th>
                                                                    </tr>
                                                                    </tbody></table>
                                                            </td>
                                                        </tr>



                                                        <tr>
                                                            <td class="pb-80" style="padding-bottom: 80px;">
                                                                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                    <tbody><tr>
                                                                        <th class="column" width="270" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal;">
                                                                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                                <tbody><tr>
                                                                                    <td class="img mpt-0" style="font-size:0pt; line-height:0pt; text-align:left;">
                                                                                        <a href="https://store.steampowered.com/" target="_blank" rel="noopener"><img src="https://store.cloudflare.steamstatic.com/public/shared/images/email/logo_footer.png" width="165" height="50" border="0"></a>
                                                                                    </td>
                                                                                </tr>
                                                                                </tbody></table>
                                                                        </th>
                                                                        <th class="column-top mpb-40" width="15" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; vertical-align:top;"></th>
                                                                        <th class="column" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal;">
                                                                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                                <tbody><tr>
                                                                                    <td class="text-12 fallback-font" style="font-size:12px; line-height:18px; color:#000001; font-family:&#39;Motiva Sans&#39;, Helvetica, Arial, sans-serif; text-align:left;">
                                                                                        若要下载 Steam 桌面客户端并进一步了解 Steam，请访问“关于Steam”。                                                                                    <br><br>
                                                                                        <a href="https://store.steampowered.com/about/" target="_blank" class="link-u c-black" style="text-decoration:underline; color:#000001;" rel="noopener">
                                                                                                    <span class="link-u c-black" style="text-decoration:underline; color:#000001;"><strong>关于 Steam</strong>
                                                                                                    </span>
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                                </tbody></table>
                                                                        </th>
                                                                    </tr>
                                                                    </tbody></table>
                                                            </td>
                                                        </tr>



                                                        <tr>
                                                            <td>
                                                                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                    <tbody><tr>
                                                                        <th class="column-top" valign="top" width="270" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; vertical-align:top;">
                                                                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                                <tbody><tr>
                                                                                    <td class="img" style="font-size:0pt; line-height:0pt; text-align:left;">
                                                                                        <a href="https://www.valvesoftware.com/en/" target="_blank" rel="noopener">
                                                                                            <img src="https://store.cloudflare.steamstatic.com/public/shared/images/email/logo_valve.jpg" width="165" height="48" border="0">
                                                                                        </a>
                                                                                    </td>
                                                                                </tr>
                                                                                </tbody></table>
                                                                        </th>
                                                                        <th class="column-top mpb-40" valign="top" width="15" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; vertical-align:top;"></th>
                                                                        <th class="column-top" valign="top" style="font-size:0pt; line-height:0pt; padding:0; margin:0; font-weight:normal; vertical-align:top;">
                                                                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                                                <tbody><tr>
                                                                                    <td class="text-12 pb-30 fallback-font" style="font-size:12px; line-height:18px; color:#000001; font-family:&#39;Motiva Sans&#39;, Helvetica, Arial, sans-serif; text-align:left; padding-bottom: 30px;">
                                                                                        <strong>�0�8 Valve Corporation</strong>
                                                                                        <br>
                                                                                        <strong>PO Box 1688 Bellevue, WA 98009</strong>
                                                                                        <br><br>
                                                                                        保留所有权利。所有商标均为其在美国及其他国家/地区的各自持有者所有。	                                                                                                                                                </td>
                                                                                </tr>
                                                                                </tbody></table>
                                                                        </th>
                                                                    </tr>
                                                                    </tbody></table>
                                                            </td>
                                                        </tr>
                                                        </tbody></table>
                                                </td>
                                            </tr>

                                            </tbody></table>
                                    </td>
                                </tr>
                                </tbody></table>
                        </td>
                    </tr>
                    </tbody></table>
            </center>

            <center style="font-family:&#39;Motiva Sans&#39;, Helvetica, Arial, sans-serif; color: #000000; font-size: 11px; margin-bottom: 4px;">
                查看此消息时遇到问题？        <a href="https://store.steampowered.com/" style="font-family:&#39;Motiva Sans&#39;, Helvetica, Arial, sans-serif; color: #000000; font-size: 11px; margin-bottom: 4px;" rel="noopener" target="_blank">
                    点击此处        </a>
            </center>
        </html>
        '''.format(self.__sender, gameOffName.text, gameLink, gamePicLink, self.__reciever, self.__greeting, self.__senderAvatarLink, self.__sender)
        return mail, gameOffName.text


if __name__ == '__main__':
    reciever = ''
    recieverEmail = ''
    sender = ''
    gameName = 'call of duty'
    gameNameURLcode = urllib.parse.urlencode({'':gameName})[1:]
    senderAvatarLink = ''
    greeting = ''
    gift = fakeGift(gameName, sender, senderAvatarLink, reciever, greeting)
    mailText, gameOffName = gift.generateGift()
    with open('./gift.html','w',encoding='utf-8')as f:
        f.write(mailText)
 