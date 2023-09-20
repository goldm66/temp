from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time, localtime, strftime
from json import load, dumps
from re import S, sub
from os import path

time3c = 2681096446.4125874
# 转换成localtime
time_local = localtime(time3c)
# 转换成新的时间格式(2016-05-05 20:28:54)
time3 = strftime("%Y年%m月%d日 %H点", time_local)
print("\033[1;32m::::::::::试用截止时间:::::::::: \033[0m",
      time3, "\033[1;32m::::::::::使用截止时间:::::::::: \033[0m", time3)
print(f"\033[1;32m::::::::::✨✨✨试用截止时间  {time3}✨✨✨:::::::::: \033[0m",
      f"\033[1;32m::::::::::✨✨✨试用截止时间  {time3}✨✨✨:::::::::: \033[0m")

# from selenium.common.exceptions import NoSuchElementException
chrome_options = webdriver.ChromeOptions()
options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])  # 禁止打印日志
# # INFO = 0 WARNING = 1 LOG_ERROR = 2 LOG_FATAL = 3 default is 0
chrome_options.add_argument('log-level=3')
# 去除浏览器被控制字样
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


chrome_options.add_experimental_option(
    "excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

chrome_options.add_experimental_option('detach', True)  # 关闭自动关闭浏览器
chrome_options.add_argument('--ignore-certificate-errors')

chrome_options.add_argument('--disable-gpu')

chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')  # 沙箱机制
# chrome_options.add_argument('--headless')  # 无界面模式

# chrome_options.add_argument('handshake-errors')
chrome_driver = r"E:\xxqg\chromedriver_113.0.5672.63.exe"
browser = webdriver.Chrome(chrome_driver, options=chrome_options)
# browser = webdriver.Chrome(options=chrome_options)
# 在请求网页之前就定义浏览器navigator.webdriver的值为undefined，真正的避免被识别
# addScriptToEvaluateOnNewDocument 添加一段js脚本，在打开新的document时执行
with open('./stealth.min.js')as f:
    js = f.read()
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": js
})


def img_src_val():
    # 获取学习强国网页登陆二维码

    frame = browser.find_element(By.ID, "ddlogin-iframe")
    browser.implicitly_wait(3)
    browser.switch_to.frame(frame)

    browser.implicitly_wait(3)
    img = browser.find_element(
        By.XPATH, "//div[@class='login_qrcode_content']/img")
    browser.implicitly_wait(3)
    return img.get_attribute('src')


def rcsplit(imgsrc):
    # 替换xuexiqg.html二维码
    with open("xuexiqg_rc.html", "r", encoding="utf-8") as f:
        htmlurl = f.readlines()
    htmlurlstr = ''.join(htmlurl)
    x = imgsrc
    val = sub(r'src=(.*) alt=""', fr'src={x} alt=""', htmlurlstr, S)
    a2 = val
    with open("xuexiqg_rc.html", "w", encoding="utf-8") as f:
        f.writelines(a2)


def fun0():  # 打开网页并拿Cookes
    browser.implicitly_wait(25)
    browser.get('https://pc.xuexi.cn/points/my-points.html')
    browser.implicitly_wait(15)
    with open('xuexiqg.json', 'r', encoding='utf-8') as f:
        listcookies = load(f)

    for i in listcookies:
        browser.add_cookie(i)
    browser.implicitly_wait(15)
    browser.get('https://pc.xuexi.cn/points/my-points.html')
    browser.implicitly_wait(15)


def coolies0():
    # coolies替换
    browser.implicitly_wait(5)
    cookie = browser.get_cookies()
    # print("\033[1;43m==>> :::::cookie::::: \033[0m", cookie)
    jsonCookies = dumps(cookie)
    with open('xuexiqg.json', 'w') as f:
        f.write(jsonCookies)
    browser.implicitly_wait(20)
    # print("\033[1;43m==>> :::::登录信息已更新::::: \033[0m")


# 挂机函数
def guaji():
    browser.implicitly_wait(5)

    browser.get(
        'https://www.xuexi.cn/98d5ae483720f701144e4dabf99a4a34/5957f69bffab66811b99940516ec8784.html')
    handleA = browser.current_window_handle  # 锁定起始页
    print("\033[1;32m==>>当前网址: \033[0m:", browser.current_url)
    browser.implicitly_wait(20)

    def fun1(handleA):

        x = 0
        y = 0
        for i in range(1, 7):
            if time() < time3c or y < 1:
                while y < 30:
                    try:
                        browser.implicitly_wait(20)
                        handles = browser.window_handles  # 获取所有网页
                        for newhandle in handles:  # 遍历所有打开网页
                            if newhandle != handleA:
                                browser.switch_to.window(newhandle)
                                browser.close()  # 关闭当前网页

                        y += 1
                        print(y)
                        browser.find_element(
                            by=By.XPATH, value=f'//*[@id = "page-main"]/section/div/div/div/div/div/section/div/div/div/div[1]/div/section/div/div/div/div/div/section/div/div/div/div/div[3]/section/div/div/div/div/div/section/div/div/div[1]/div/div[{i+x}]/div/div/div[1]').click()  # 点击新闻标签浏览新闻

                        browser.implicitly_wait(15)
                        handles = browser.window_handles  # 获取所有网页
                        for newhandle in handles:  # 遍历所有打开网页
                            if newhandle != handleA:
                                browser.switch_to.window(newhandle)
                        browser.implicitly_wait(5)
                        try:
                            browser.find_element(
                                by=By.XPATH, value=f'//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[2]/div/span[4]/div/span').click()

                            print(
                                "\033[1;32m==>>阅读文章中(1分钟)-------------- \033[0m")

                            sleep(60)
                            browser.close()
                            browser.switch_to.window(handleA)
                            browser.implicitly_wait(20)
                            break
                        except:
                            browser.implicitly_wait(5)
                            handles = browser.window_handles  # 获取所有网页
                            for newhandle in handles:  # 遍历所有打开网页
                                if newhandle != handleA:
                                    browser.switch_to.window(newhandle)
                                    browser.close()  # 关闭当前网页
                                    browser.switch_to.window(handleA)
                            x += 1
                            browser.implicitly_wait(5)
                            # print("\033[1;32m==>>:::::这个是视频::::: \033[0m:")

                    except:
                        print("网络好像不佳，请检查你的网络，请手机自己阅读文章吧✨✨✨")
                else:
                    # print("##########✨✨✨试用期已过，请下载新的试用版，没有长期版，学习交流用✨✨✨#########",)
                    # print(f"\033[1;32m::::::::::✨✨✨试用截止时间  {time3}✨✨✨:::::::::: \033[0m",
                    #       f"\033[1;32m::::::::::✨✨✨试用截止时间  {time3}✨✨✨:::::::::: \033[0m")
                    pass

    fun1(handleA)

    browser.implicitly_wait(5)  # 进入百灵首页
    print("\033[1;32m==>>进入百灵首页: \033[0m:")
    browser.get(
        'https://www.xuexi.cn/xxqg.html?id=c7c3b74e1887422c9733b0d22bf25498')

    browser.implicitly_wait(20)

    def fun1(i, p):
        print("i", i, "p", p)
        if time() < time3c:
            browser.implicitly_wait(5)
            handles = browser.window_handles  # 获取所有网页
            for newhandle in handles:  # 遍历所有打开网页
                if newhandle != handleA:
                    browser.switch_to.window(newhandle)
                    browser.close()  # 关闭当前网页
            browser.implicitly_wait(5)
            browser.find_element(
                by=By.XPATH, value=f'//*[@id="6231cc81a4"]/div/div/div/div/div/div/section/div/div/div/div[{i}]/div[{p}]/div/div[1]/div[1]/span/div').click()
            
            browser.implicitly_wait(5)
            handles = browser.window_handles  # 获取所有网页
            for newhandle in handles:  # 遍历所有打开网页
                if newhandle != handleA:
                    browser.switch_to.window(newhandle)

            browser.implicitly_wait(5)
            browser.find_element(
                by=By.XPATH, value=f'//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[2]').click()
            print("\033[1; 43m == >>视频播放中(30秒)-------------- \033[0m")
            sleep(30)
            browser.close()
            browser.switch_to.window(handleA)
            browser.implicitly_wait(20)
        else:
            print("##########✨✨✨试用期已过，请下载新的试用版，没有长期版，学习交流用✨✨✨#########",)
            print(f"\033[1;32m::::::::::✨✨✨试用截止时间  {time3}✨✨✨:::::::::: \033[0m",
                  f"\033[1;32m::::::::::✨✨✨试用截止时间  {time3}✨✨✨:::::::::: \033[0m")
            print("出了点小问题，我再查查怎么改进")

    for i in range(1, 5):
        for p in range(1, 4):
            fun1(i, p)


# 更换二维码
try:

    fun0()

    browser.find_element(
        by=By.XPATH, value=f'//*[@id="app"]/div/div[2]/div/div[3]/div[1]/span[1]')
    browser.implicitly_wait(25)
    print("开始挂机")
    guaji()


except:
    browser.implicitly_wait(5)
    img1 = img_src_val()  # 获取学习强国网页登陆二维码
    img2 = rcsplit(img1)  # 替换xuexiqg.html二维码
    print("登录信息过期重新扫码")
    try:
        chrome_driver2 = r"E:\xxqg\chromedriver_113.0.5672.63.exe"
        browser2 = webdriver.Chrome(chrome_driver2, options=options)
        # browser2 = webdriver.Chrome(options=options)
        browser2.get('file:///'+path.abspath('xuexiqg_rc.html'))
        browser.implicitly_wait(5)
        try:
            z = 0
            while z < 40:
                browser.implicitly_wait(5)
                browser.find_element(
                    By.XPATH, "//div[@class='login_qrcode_content']/img")
                browser.implicitly_wait(5)
                z += 1

                print("\033[1;32m==>> 扫描二维码(两分钟内完成):::: \033[0m")
                sleep(1)

        except:
            browser2.quit()
            print("扫码完成")
            coolies0()  # coolies替换
            print("开始挂机")
            guaji()
    except:
        print("What's going on?出了点小问题，我再查查怎么改进")


sleep(3)
browser.quit()
