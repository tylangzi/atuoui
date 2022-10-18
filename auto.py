import datetime
from _curses import getmouse
import time

import pyautogui as pt


from selenium.webdriver.common.by import By
import pyperclip as pc
import re
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
from selenium.webdriver.chrome.service import Service

from pynput import keyboard
from selenium.webdriver.support.wait import WebDriverWait


def check_date(vehicle='pacifica-cn-159', rtime='20220713'):
    png = {"googleExe": {"imageIcon": "./image/google.png"}, "dingwei": {"imageIcon": "./image/img_8.png"},
           "time": {"imageIcon": "./image/img_9.png"}}
    a = png.get("googleExe").get('imageIcon')
    googleExe = ()  # 存储google坐标相关信息
    googleExe = pt.locateOnScreen(png.get("googleExe").get('imageIcon'))
    x = googleExe[0]
    y = googleExe[1]
    pt.moveTo(x, y, duration=0.5)  # 移动到google图标位置
    pt.leftClick(x, y, duration=0.1)  # 点击google图标

    url = "https://szexa.xray.autox.tech/"

    pt.hotkey('alt', 'd')
    pt.press('backspace')  # 删除原有内容
    time.sleep(0.5)
    pt.typewrite(url, interval=0.01)  # 输入网址
    pt.hotkey('alt', 'd')  # 再次点击地址栏
    pt.hotkey('ctrl', 'c')
    after_url = pc.paste()
    if after_url != url:
        pt.keyDown('shift')  # 切换输入法
        pt.keyUp('shift')

        pt.press('backspace')  # 删除原有内容
        time.sleep(0.5)
        pt.typewrite(url, interval=0.01)  # 输入网址

    # time.sleep(5)
    pt.press('enter')  # 回车

    pt.moveTo(191, 151, duration=0.5)  # 点击remote records
    pt.leftClick(191, 151, duration=0.5)
    time.sleep(0.2)

    pt.moveTo(163, 507, duration=0.5)  # 点击scaexa
    pt.leftClick(163, 507, duration=0.5)
    time.sleep(0.2)

    pt.moveTo(155, 547, duration=0.5)  # 点击remote records
    pt.leftClick(155, 547, duration=0.5)
    time.sleep(0.2)

    pt.hotkey('ctrl', 'f')  # 搜索records
    records = vehicle
    pt.typewrite(records)
    pt.hotkey('ctrl', 'f')  # 再次搜索records
    pt.hotkey('ctrl', 'c')
    after_records = pc.paste()
    if after_records != records:
        pt.hotkey('ctrl', 'f')  # 搜索records
        pt.typewrite(records)
    time.sleep(0.5)

    # im2 = pt.screenshot('./image/my_screenshot.png')
    # print(im2)

    b = png.get("dingwei").get('imageIcon')
    dingwei = ()  # 存储定位图片胡位置
    dingwei = pt.locateOnScreen(png.get("dingwei").get('imageIcon'), region=(125, 184, 250, 1407))
    # dingwei = pt.locateOnScreen(png.get("dingwei").get('imageIcon'), region=(125,184,250,1407),grayscale=True)
    try:
        x = dingwei[0]
        y = dingwei[1]
        pt.moveTo(x, y, duration=0.5)
        pt.leftClick(x, y, duration=0.5)
        time.sleep(2)
    except:
        pt.screenshot("./image/myscrenshot_except1.png")

    pt.hotkey('ctrl', 'f')  # 搜索records
    rtime = rtime
    pt.typewrite(rtime)
    pt.hotkey('ctrl', 'f')  # 再次搜索records
    pt.hotkey('ctrl', 'c')
    after_rtime = pc.paste()
    if after_rtime != rtime:
        pt.hotkey('ctrl', 'f')  # 搜索records
        pt.typewrite(rtime)
    time.sleep(0.5)

    b = png.get("time").get('imageIcon')
    dingwei = ()  # 存储定位图片胡位置
    dingwei = pt.locateOnScreen(png.get("time").get('imageIcon'), region=(125, 184, 250, 1407))
    # dingwei = pt.locateOnScreen(png.get("dingwei").get('imageIcon'), region=(125,184,250,1407),grayscale=True)
    try:
        x = dingwei[0]
        y = dingwei[1]
        pt.moveTo(x, y, duration=0.5)
        time.sleep(0.1)
        pt.leftClick(x, y, duration=0.5)
        time.sleep(2)
        pt.screenshot("./image/myscrenshot1.png")
    except:
        pt.screenshot("./image/myscrenshot1.png")

    pt.moveTo(282, 152, duration=0.5)  # 点击remote records
    pt.leftClick(282, 152, duration=0.5)
    time.sleep(0.5)

    pt.moveTo(2164, 904, duration=0.5)  # 点击remote records
    pt.leftClick(2164, 904, duration=0.5)
    time.sleep(0.4)

    pt.moveTo(2132, 1013, duration=0.5)  # 点击remote records
    pt.leftClick(2132, 1013, duration=0.5)
    time.sleep(0.2)

    pt.hotkey('ctrl', 'f')  # 搜索records
    pt.typewrite(records)
    pt.hotkey('ctrl', 'f')  # 再次搜索records
    pt.hotkey('ctrl', 'c')
    after_records = pc.paste()
    if after_records != records:
        pt.hotkey('ctrl', 'f')  # 搜索records
        pt.typewrite(records)
    time.sleep(0.5)
    pt.screenshot("./image/myscrenshot2.png")


def open_url():
    png = {"googleExe": {"imageIcon": "./image/google.png"}, "dingwei": {"imageIcon": "./image/img_8.png"},
           "time": {"imageIcon": "./image/img_9.png"}}
    a = png.get("googleExe").get('imageIcon')
    googleExe = ()  # 存储google坐标相关信息
    googleExe = pt.locateOnScreen(png.get("googleExe").get('imageIcon'))
    x = googleExe[0]
    y = googleExe[1]
    pt.moveTo(x, y, duration=0.5)  # 移动到google图标位置
    pt.leftClick(x, y, duration=0.1)  # 点击google图标

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)

    main_windows = driver.current_window_handle
    all_windows = driver.window_handles

    # 切换页面
    for handle in all_windows:
        if handle != main_windows:
            driver.switch_to.window(handle)

    driver.get("https://szexa.xray.autox.tech/")
    time.sleep(0.5)
    return driver


def anocheone(vehicle, rtime):
    driver = open_url()
    time.sleep(5)
    driver.find_element_by_xpath("//*[starts-with(text(),'Remote Records')]").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("//*[starts-with(text(),'szexa.xray.autox.tech')]").click()

    playback = driver.find_element_by_xpath('//*/a[contains(text(),"playback")]')
    action = ActionChains(driver)
    action.click(playback).perform()
    # pt.hotkey('ctrl', 'f')
    # pt.typewrite(vehicle)
    # translate = islang(vehicle)
    # if translate:
    #     pt.hotkey('shift')
    #     pt.hotkey('ctrl', 'f')
    #     pt.typewrite(vehicle)

    # veh = driver.find_element_by_xpath("//*[text()='" + vehicle + "']")
    veh = driver.find_element_by_xpath("//*[contains(text(),'" + vehicle + "')]")

    js = "arguments[0].scrollIntoView({behaviour:'smooth'})"
    driver.execute_script(js, veh)

    driver.find_element_by_xpath("//*[contains(text(),'" + vehicle + "')]").click()
    time.sleep(0.5)
    pt.hotkey('ctrl', 'f')
    pt.typewrite(rtime)
    translate = islang(rtime)
    if translate:
        pt.hotkey('shift')
        pt.hotkey('ctrl', 'f')
        pt.typewrite(rtime)

    target = driver.find_element_by_xpath("//*[starts-with(text(),'" + rtime + "')]")
    target.click()
    # js = 'arguments[0].scrollIntoView()'
    # driver.execute_script(js, target)

    print(driver.title)


def islang(moment, a='ctrl', b='f'):
    translate = False
    a = a
    b = b
    pt.hotkey(a, b)
    pt.hotkey('ctrl', 'c')
    aftermoment = pc.paste()
    if aftermoment != moment:
        translate = True
    return translate


def open_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    return driver


def tag():
    try:
        # png = {"googleExe": {"imageIcon": "./image/google.png"}, "dingwei": {"imageIcon": "./image/img_8.png"},
        #        "time": {"imageIcon": "./image/img_9.png"}}
        # a = png.get("googleExe").get('imageIcon')
        # googleExe = ()  # 存储google坐标相关信息
        # googleExe = pt.locateOnScreen(png.get("googleExe").get('imageIcon'))
        # x = googleExe[0]
        # y = googleExe[1]
        # pt.moveTo(x, y, duration=0.5)  # 移动到google图标位置
        # pt.leftClick(x, y, duration=0.1)  # 点击google图标

        # chrome_options = Options()
        # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # chrome_driver = "/usr/local/bin/chromedriver"
        # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        chrome_driver = "/usr/local/bin/chromedriver"
        # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        s = Service("/usr/local/bin/chromedriver")
        driver = webdriver.Chrome(options=chrome_options, service=s)

        slack = "Slack | Threads | AutoX"
        xray = "xRay"

        # 切换页面
        for window in driver.window_handles:
            if driver.title != xray:
                driver.switch_to.window(window)
            else:
                break
        print("qiehuandao slack")

        # pen = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[6]")
        #
        # action = ActionChains(driver)
        # action.move_to_element(pen).click().perform()
        # time.sleep(6)
        # ok = driver.find_element_by_xpath("/html/body/div[11]/div[3]/div/div/div[3]/button[2]")
        # js = "arguments[0].click()"
        # driver.execute_script(js,ok)
        # action = ActionChains(driver)
        # t
        # ok = driver.find_element_by_xpath("//*[contains(text(),'KeyFrames')]")
        ok = driver.find_element(By.XPATH ,"//*[contains(text(),'KeyFrames')]")
        js = "arguments[0].click()"
        driver.execute_script(js, ok)
        # action = ActionChains(driver)

        display = driver.find_element(By.XPATH,
            "//*[contains(text(),'Timestamp:')]/../following-sibling::div/*[name()='svg'][4]")
        action = ActionChains(driver)
        drive = None
        try:
            drive = driver.find_element(By.XPATH,"//*[contains(text(),'DRIVE')]")
        except:
            pass
        if drive is None:
            action.click(display).perform()
        try:
            select_tags = driver.find_element(By.XPATH,"//*[contains(text(),'Select tags')]")
            action = ActionChains(driver)
            action.click(select_tags).perform()
            pc.copy("Hmi")
            pt.hotkey('ctrl', 'v')
            pt.hotkey('enter')
            HMI = driver.find_element(By.XPATH,"//*[contains(text(),'HMI')]")
            action = ActionChains(driver)
            action.click(HMI).perform()
            time.sleep(0.8)
            pc.copy("Disengag")
            pt.hotkey('ctrl', 'v')
            time.sleep(0.3)
            pt.hotkey('enter')
            HMI = driver.find_element(By.XPATH,"//*[contains(text(),'HMI')]")
            action = ActionChains(driver)
            action.click(HMI).perform()
            pc.copy("hybrid")
            pt.hotkey('ctrl', 'v')
            pt.hotkey('enter')

        except:
            pass

    # except:
    #     pass
    except:
        pass

    def on_press(key):
        '按下按键时执行。'
        try:
            # print('alphanumeric key {0} pressed'.format(
            #     key.char))
            if key == keyboard.Key.pause:
                # chrome_options = Options()
                # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                # chrome_driver = "/usr/local/bin/chromedriver"
                # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
                # current_window = driver.current_window_handle
                # driver.switch_to.window(current_window)
                # driver.execute_script("window.alert('打tag已退出')")
                # time.sleep(1.5)
                # pt.hotkey('enter')
                # pt.hotkey('backspace')
                print("*"*30)
                print("打tag已退出")
                return False

            if key == keyboard.Key.f8:
                try:
                    display = driver.find_element(By.XPATH,
                        "//*[contains(text(),'Timestamp:')]/../following-sibling::div/*[name()='svg'][4]")
                    action = ActionChains(driver)
                    drive = None
                    try:
                        drive = driver.find_element(By.XPATH,"//*[contains(text(),'DRIVE')]")
                    except:
                        pass
                    if drive is None:
                        action.click(display).perform()
                    try:
                        select_tags = driver.find_element(By.XPATH,"//*[contains(text(),'Select tags')]")
                        action = ActionChains(driver)
                        action.click(select_tags).perform()
                        pc.copy("Hmi")
                        pt.hotkey('ctrl','v')
                        pt.hotkey('enter')
                        HMI = driver.find_element(By.XPATH,"//*[contains(text(),'HMI')]")
                        action = ActionChains(driver)
                        action.click(HMI).perform()
                        pc.copy("Disenga")
                        pt.hotkey('ctrl', 'v')
                        pt.hotkey('enter')
                        HMI = driver.find_element(By.XPATH,"//*[contains(text(),'HMI')]")
                        action = ActionChains(driver)
                        action.click(HMI).perform()
                        pc.copy("hybrid")
                        pt.hotkey('ctrl', 'v')
                        pt.hotkey('enter')
                    except:
                        pass
                except:
                    pass
            if key == keyboard.KeyCode.from_char('s'):
                try:
                    a_ok = None
                    print("按下了s")
                    try:
                        a_ok = driver.find_element(By.XPATH,"//*[contains(text(),'OK')]")

                    except:
                        pass

                    if a_ok is None:
                        pen = driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[7]")
                        action = ActionChains(driver)
                        action.move_to_element(pen).click().perform()
                        print("s")
                        # time.sleep(0.2)
                        # investigate = driver.find_element_by_xpath("//*[contains(text(),'To Investigate')]")
                        # action.move_to_element(investigate).click().perform()
                        # js = "arguments[0].click()"
                        # driver.execute_script(js, investigate)
                        # action = ActionChains(driver)
                        # print("mmmm")
                        # loc = pt.locateOnScreen("./image/img_18.png")
                        # pt.moveTo(loc).click()
                except:
                    pass
            if key == keyboard.KeyCode.from_char('2'):

                try:
                    open = driver.find_element(By.XPATH,'//*[@id="hide-icon"]')
                    action = ActionChains(driver)
                    action.move_to_element(open).click().perform()

                    search = driver.find_element(By.XPATH,"//*[contains(text(),'Select observed topics')]")
                    action = ActionChains(driver)
                    action.move_to_element(search).click().perform()
                    pc.copy('planning')
                    pt.hotkey('ctrl','v')
                    time.sleep(0.2)
                    pt.hotkey('down')
                    pt.hotkey('down')
                    pt.hotkey('enter')



                    planning = driver.find_element(By.XPATH,"//*/div[contains(text(),'planning')]")
                    action = ActionChains(driver)
                    action.move_to_element(planning).click().perform()

                    pc.copy('system_stat')
                    pt.hotkey('ctrl', 'v')
                    time.sleep(0.2)
                    pt.hotkey('enter')

                    planning = driver.find_element(By.XPATH,"//*/div[contains(text(),'planning')]")
                    action = ActionChains(driver)
                    action.move_to_element(planning).click().perform()

                    pc.copy('chassis')
                    pt.hotkey('ctrl', 'v')
                    time.sleep(0.2)
                    pt.hotkey('enter')
                #
                #

                except:
                    pass

            if key == keyboard.Key.ctrl:
                try:
                    ok = driver.find_element(By.XPATH,"//*[contains(text(),'OK')]")

                    js = "arguments[0].click()"
                    driver.execute_script(js, ok)
                    keyframes = driver.find_element(By.XPATH,"//*[contains(text(),'KeyFrames')]")
                    js = "arguments[0].click()"
                    driver.execute_script(js, keyframes)
                    # time.sleep(2)
                    tim = driver.find_element(By.XPATH,'//*/div[@class="time-display"]').text
                    str_tim = tim.split(r"/")[0].strip()
                    # target = driver.find_element_by_xpath("//*[starts-with(text(),'" + rtime + "')]")
                    timspan_star = driver.find_element(By.XPATH,
                        "//*/span[contains(text(),'" + str_tim + "')]/../../../div[3]/span")
                    action = ActionChains(driver)
                    action.click(timspan_star).perform()

                    lis_star = []
                    all_stars = driver.find_elements(By.XPATH,
                        '//*/div[@aria-colindex="6"]/div[@class="keyframe-tags frame-list-tags"]')
                    for next_star in all_stars:
                        if "" == next_star.text:
                            lis_star.append(next_star)
                    print("空文本：", lis_star[0].text)
                    for lis_sta in lis_star:
                        star_none = lis_sta.find_element(By.XPATH,"./../../div[3]/span")
                        if "color: rgb(255, 227, 0);" == star_none.get_attribute('style'):
                            action = ActionChains(driver)
                            action.click(star_none).perform()
                    lis_time_click = []
                    for star in lis_star:
                        star_time = star.find_element(By.XPATH,'./../../div[2]/div/span')
                        star_tim = star_time.split(r"s")[0].strip()
                        star_tim = float(star_tim)
                        frame_time = driver.find_element(By.XPATH,'//*/div[@class="time-display"]').text
                        frame_tim = frame_time.split(r"/")[0].strip()
                        frame_tim = float(frame_tim)
                        if star_tim > frame_tim:
                            lis_time_click.append(star)
                    return_to = lis_time_click[0].find_element(By.XPATH,'./../../div[7]/button/span')
                    action = ActionChains(driver)
                    action.click(return_to).perform()


                except:
                    pass
                    try:
                        # lis_star = []
                        # all_stars = driver.find_elements_by_xpath(
                        #     '//*/div[@aria-colindex="6"]/div[@class="keyframe-tags frame-list-tags"]')
                        # for next_star in all_stars:
                        #     if "" == next_star.text:
                        #         lis_star.append(next_star)
                        # print("空文本：", lis_star[0].text)
                        # for lis_sta in lis_star:
                        #     star_none = lis_sta.find_element_by_xpath("./../../div[3]/span")
                        #     if "color: rgb(255, 227, 0);" == star_none.get_attribute('style'):
                        #         action = ActionChains(driver)
                        #         action.click(star_none).perform()

                        lis_star = []
                        all_stars = driver.find_elements(By.XPATH,
                            '//*/div[@aria-colindex="6"]/div[@class="keyframe-tags frame-list-tags"]')
                        for next_star in all_stars:
                            # if "" == next_star.text:
                            lis_star.append(next_star)
                        # print("空文本：", lis_star[0].text)
                        for lis_sta in lis_star:
                            star_none = lis_sta.find_element(By.XPATH,"./../../div[3]/span")
                            if "color: rgb(255, 227, 0);" == star_none.get_attribute('style'):
                                action = ActionChains(driver)
                                action.click(star_none).perform()


                    except:
                        pass

            if key == keyboard.KeyCode.from_char('w'):
                try:
                    ok = driver.find_element(By.XPATH,"//*[contains(text(),'KeyFrames')]")
                    js = "arguments[0].click()"
                    driver.execute_script(js, ok)
                    # action = ActionChains(driver)

                    # display = driver.find_element_by_xpath(
                    #     "//*[contains(text(),'Timestamp:')]/../following-sibling::div/*[name()='svg'][4]")
                    # action = ActionChains(driver)
                    # action.click(display).perform()
                except:
                    pass

            if key == keyboard.KeyCode.from_char('3'):
                # if key == keyboard.KeyCode.from_char('x'):
                # print("3")
                try:

                    # loc = pt.position()
                    # pt.click(2415,977)
                    # time.sleep(0.2)
                    label = driver.find_elements(By.XPATH,"//*[@class='MuiButton-label']")
                    for li in label:
                        if li.text in ("Default", "per", "raw2", "occ2", "tllll"):
                            js = "arguments[0].click()"
                            driver.execute_script(js, li)
                    icon = driver.find_element(By.XPATH,"//*[contains(text(),'occ2')]")
                    js = "arguments[0].click()"
                    driver.execute_script(js, icon)
                    options = driver.find_elements(By.XPATH,"//*[contains(text(),'Options')]")
                    for li in options:
                        if li.text == "Options":
                            js = "arguments[0].click()"
                            driver.execute_script(js, li)
                    # pt.moveTo(loc)







                except:
                    pass
            if key == keyboard.KeyCode.from_char('4'):

                try:
                    options = driver.find_elements(By.XPATH,"//*[contains(text(),'Options')]")
                    for li in options:
                        if li.text == "Options":
                            js = "arguments[0].click()"
                            driver.execute_script(js, li)
                    label = driver.find_elements(By.XPATH,"//*[@class='MuiButton-label']")
                    for li in label:
                        if li.text in ("Default", "per", "raw2", "occ2", "tllll"):
                            js = "arguments[0].click()"
                            driver.execute_script(js, li)
                    icon = driver.find_element(By.XPATH,"//*[contains(text(),'raw2')]")
                    js = "arguments[0].click()"
                    driver.execute_script(js, icon)
                    options = driver.find_elements(By.XPATH,"//*[contains(text(),'Options')]")
                    for li in options:
                        if li.text == "Options":
                            js = "arguments[0].click()"
                            driver.execute_script(js, li)
                    # pt.moveTo(loc)






                except:
                    pass
            if key == keyboard.KeyCode.from_char('5'):

                try:
                    options = driver.find_elements(By.XPATH,"//*[contains(text(),'Options')]")
                    for li in options:
                        if li.text == "Options":
                            js = "arguments[0].click()"
                            driver.execute_script(js, li)
                    label = driver.find_elements(By.XPATH,"//*[@class='MuiButton-label']")
                    for li in label:
                        if li.text in ("Default", "per", "raw2", "occ2", "tllll"):
                            js = "arguments[0].click()"
                            driver.execute_script(js, li)
                    icon = driver.find_element(By.XPATH,"//*[contains(text(),'tllll')]")
                    js = "arguments[0].click()"
                    driver.execute_script(js, icon)
                    options = driver.find_elements(By.XPATH,"//*[contains(text(),'Options')]")
                    for li in options:
                        if li.text == "Options":
                            js = "arguments[0].click()"
                            driver.execute_script(js, li)
                    # pt.moveTo(loc)
                    # loc = pt.position()
                    # pt.moveTo()
                    # pt.rightClick()
                    #// *[contains(text(), 'Switch Camera')]
                    sxt = driver.find_element(By.XPATH,"//*[contains(text(),'left_0_n_12mm @')]")
                    action = ActionChains(driver)
                    action.context_click(sxt).perform()

                    switch_camera = driver.find_element(By.XPATH,"// *[contains(text(), 'Switch Camera')]")
                    action = ActionChains(driver)
                    action.click(switch_camera).perform()
                    traffic_light = driver.find_element(By.XPATH,"//*[contains(text(),'left_0_n_12mm_tflight')]")
                    action = ActionChains(driver)
                    action.click(traffic_light).perform()







                except:
                    pass

            if key == keyboard.Key.alt:
                try:
                    print("alt")
                    switch = driver.find_element(By.XPATH,"//*/span[@class='MuiIconButton-label']/span")

                    action = ActionChains(driver)
                    action.move_to_element(switch).click().perform()

                    control = driver.find_elements(By.XPATH,"//*/div[@class='hide-controller']/*[name()='svg']")
                    # try:


                    for li in control:
                        action = ActionChains(driver)
                        action.move_to_element(li).click().perform()
                        break

                    driver.execute_script("arguments[0].scrollIntoView();", switch)
                    # js = "arguments[0].click()"
                    # driver.execute_script(js, li)
                except:
                    pass
            if key == keyboard.Key.f2:
                print("f2")
                control = driver.find_element(By.XPATH,"//*/li[contains(text(),'Control')]")
                js = "arguments[0].click()"
                driver.execute_script(js, control)

            if key == keyboard.Key.esc:
                print("esc")
                control = driver.find_element(By.XPATH,"//*/li[contains(text(),'Planning')]")
                js = "arguments[0].click()"
                driver.execute_script(js, control)





        except AttributeError:
            print('special key {0} pressed'.format(
                key))
        # 通过属性判断按键类型。

    def on_release(key):
        # '松开按键时执行。'
        # print('{0} released'.format(
        #     key))
        # if key == keyboard.Key.esc:
        # Stop listener
        # return False
        pass

    # Collect events until released

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def copymodule():
    png = {"googleExe": {"imageIcon": "./image/google.png"}, "dingwei": {"imageIcon": "./image/img_8.png"},
           "time": {"imageIcon": "./image/img_9.png"}}
    a = png.get("googleExe").get('imageIcon')
    googleExe = ()  # 存储google坐标相关信息
    googleExe = pt.locateOnScreen(png.get("googleExe").get('imageIcon'))
    x = googleExe[0]
    y = googleExe[1]
    pt.moveTo(x, y, duration=0.5)  # 移动到google图标位置
    pt.leftClick(x, y, duration=0.1)  # 点击google图标

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    # driver.get("https://app.slack.com/client/T1WN8GREJ/D02KY11QA05/thread/GCZMAJ2SV-1640863585.181900")
    report = driver.find_element_by_xpath("//*/div[@class='ql-editor']")
    js = "return arguments[0].innerHTML"
    report_html = driver.execute_script(js, report)

    report_blank_html = r"""<div class="ql-editor ql-blank" data-gramm="false" contenteditable="true" dir="auto" role="textbox" tabindex="0" data-team-id="T1WN8GREJ" aria-label="Message to xray" aria-describedby="context_bar_text-a7893561" aria-multiline="true" aria-autocomplete="list" aria-expanded="false" aria-owns="chat_input_tab_ui" spellcheck="true"><p><br></p></div>"""

    def on_press(key):
        '按下按键时执行。'
        try:
            if key == keyboard.Key.f2:
                lis_header = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/div")
                for li in lis_header:
                    print(li.text)

                lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")

                lls_body = []
                for li in lis_body:
                    print(li.text)
                    re_compile = re.compile(r'\W\d{1,2}:\d{2}\s+\w{2}\W')
                    if len(re_compile.findall(li.text)):
                        lls_body.append(li)
                index = lis_body.index(lls_body[1])
                for i in range(index):
                    js = 'arguments[0].removeChild(arguments[1])'
                    driver.execute_script(js, report, lis_body[i])

            if key == keyboard.Key.f3:
                lis_header = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/div")
                for li in lis_header:
                    print(li.text)

                lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")

                lls_body = []
                for li in lis_body:
                    print(li.text)
                    re_compile = re.compile(r'\W\d{1,2}:\d{2}\s+\w{2}\W')
                    if len(re_compile.findall(li.text)):
                        lls_body.append(li)
                index = lis_body.index(lls_body[1])
                for i in range(index, len(lis_body)):
                    js = 'arguments[0].removeChild(arguments[1])'
                    driver.execute_script(js, report, lis_body[i])

            if key == keyboard.Key.f4:
                try:
                    lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")

                    for li in lis_body:
                        re_compile = re.compile(r'\W\d{1,2}:\d{2}\s+\w{2}\W')
                        if len(re_compile.findall(li.text)):
                            shurufa = None
                            text = li.text
                            before_time = re_compile.findall(li.text)[0]
                            print(before_time)
                            mokuai_name = text.replace(before_time, "").strip()

                            actions = ActionChains(driver)
                            actions.click(li).perform()
                            pt.press('home')
                            for i in range(len(re_compile.findall(li.text)[0])):
                                pt.hotkey('shift', 'right')
                            pt.hotkey('backspace')
                            pt.hotkey('down')
                            pt.hotkey('shift', 'enter')
                            pt.hotkey('up')
                            pt.typewrite('@')
                            try:
                                shurufa = pt.locateOnScreen("./image/img_21.png", region=(2864, 1226, 3440, 1440))
                            except:
                                print("没有找到输入法图标")
                            if shurufa is not None:
                                pt.hotkey('shift')
                            pt.typewrite(mokuai_name)
                            pt.hotkey('enter')
                            time.sleep(0.5)
                            pt.hotkey('home')
                            pt.hotkey('backspace')
                except:
                    pass
            if key == keyboard.Key.f8:
                js = "arguments[0].innerHTML='" + report_html + "'"
                driver.execute_script(js, report)

            if key == keyboard.Key.f9:
                js = "arguments[0].innerHTML='" + report_blank_html + "'"
                driver.execute_script(js, report)


        except AttributeError:
            print('special key {0} pressed'.format(
                key))
        # 通过属性判断按键类型。

    def on_release(key):
        pass

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def sent():
    def on_press(key):
        '按下按键时执行。'
        try:
            if key == keyboard.Key.alt:
                print("点击alt")
                # pt.hotkey('enter')
                return False
            if key == keyboard.Key.enter:
                return False


        except AttributeError:
            print('special key {0} pressed'.format(
                key))
        # 通过属性判断按键类型。

    def on_release(key):
        pass

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def semi_autoslack():
    png = {"googleExe": {"imageIcon": "./image/google.png"}, "dingwei": {"imageIcon": "./image/img_8.png"},
           "time": {"imageIcon": "./image/img_9.png"}}
    a = png.get("googleExe").get('imageIcon')
    googleExe = ()  # 存储google坐标相关信息
    googleExe = pt.locateOnScreen(png.get("googleExe").get('imageIcon'))
    x = googleExe[0]
    y = googleExe[1]
    pt.moveTo(x, y, duration=0.5)  # 移动到google图标位置
    pt.leftClick(x, y, duration=0.1)  # 点击google图标

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    driver.implicitly_wait(3)
    # driver.get("https://app.slack.com/client/T1WN8GREJ/D02KY11QA05/thread/GCZMAJ2SV-1640863585.181900")

    # channels = ["road_test_shenzhen", "road_test_prediction", "road_test_perception", "road_test_deeplearning", "road_test_traffic_light"]
    channels = {
        "road_test_shenzhen": {"Planning": "Planning", "System": "System", "Routing": "Routing", "XView": "XView",
                               "lidar": "lidar", "Control": "Control"},
        "road_test_prediction": {"Prediction": "Prediction"}, "road_test_perception": {"Perception": "Perception"},
        "road_test_deeplearning": {"Perception": "Perception"}, "road_test_traffic_light": {"Perception": "Perception"}}

    report = driver.find_element_by_xpath("//*/div[@class='ql-editor']")
    js = "return arguments[0].innerHTML"
    # 非空report
    report_html = driver.execute_script(js, report)
    # 空report
    report_blank_html = r"""<div class="ql-editor ql-blank" data-gramm="false" contenteditable="true" dir="auto" role="textbox" tabindex="0" data-team-id="T1WN8GREJ" aria-label="Message to xray" aria-describedby="context_bar_text-f6f9cd4a" aria-multiline="true" aria-autocomplete="list" aria-expanded="false" aria-owns="chat_input_tab_ui" spellcheck="true"><p><br></p></div>"""
    # 清空原有report
    js = "arguments[0].innerHTML='" + report_blank_html + "'"
    driver.execute_script(js, report)
    time.sleep(1)  # 清空后等待2秒去点击channel
    # time.sleep(2)#清空后等待2秒去点击channel
    for channel in channels:
        # 点击channel
        road_test_shenzhen = driver.find_element_by_xpath("//*[contains(text(),'" + channel + "') and @ dir='auto']")
        js = 'arguments[0].click()'
        driver.execute_script(js, road_test_shenzhen)
        # 添加report
        js = "arguments[0].innerHTML='" + report_html + "'"
        driver.execute_script(js, report)
        title_names = {"road_test_perception": "Perception", "road_test_deeplearning": "Deeplearning",
                       "road_test_traffic_light": "Traffic light"}
        remove_text = {
            "Perception": ["Traffic Light", "Frustum", "Connected Components", "Point Pillars", "Occupancy Grid",
                           "Traffic Cone", "Special Object", "Mask RCNN"],
            "Deeplearning": ["Connected Components", "Frustum", "Point Pillars", "Traffic Cone", "Occupancy Grid",
                             "Special Object", "Mask RCNN"], "Traffic light": ["Traffic Light"]}
        # 删除前后内容
        # 装列表
        next_flag = False  # deeplearning、traffic light,perception是否进行后续操作
        for value in channels[channel].values():
            text_lis_body = []
            able_text_lis_body = []
            flag = False
            lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")
            for li in lis_body:
                re_compile = re.compile(r'\W\d{1,2}:\d{2}\s+\w{2}\W')
                if len(re_compile.findall(li.text)):
                    text_lis_body.append(li)
                    if value in li.text:
                        able_text_lis_body.append(li)
            if len(able_text_lis_body):
                flag = True
            if flag:
                # 删除开头
                if able_text_lis_body[0] is not None:
                    before_index = lis_body.index(able_text_lis_body[0])
                    if before_index != 0 and before_index is not None:
                        for j in range(before_index):
                            js = 'arguments[0].removeChild(arguments[1])'
                            driver.execute_script(js, report, lis_body[j])
                # 删除结尾
                a = text_lis_body.index(able_text_lis_body[0])
                if a < len(text_lis_body) - 1:
                    after_content = text_lis_body[a + 1]
                    after_index = lis_body.index(after_content)
                    for j in range(after_index, len(lis_body)):
                        js = 'arguments[0].removeChild(arguments[1])'
                        driver.execute_script(js, report, lis_body[j])

                # 格式整理
                lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")
                for li in lis_body:
                    re_compile = re.compile(r'\W\d{1,2}:\d{2}\s+\w{2}\W')
                    if len(re_compile.findall(li.text)):
                        text = li.text
                        before_time = re_compile.findall(li.text)[0]
                        print(before_time)
                        mokuai_name = text.replace(before_time, "").strip()
                        actions = ActionChains(driver)
                        actions.click(li).perform()
                        pt.press('home')
                        for i in range(len(re_compile.findall(li.text)[0])):
                            pt.hotkey('shift', 'right')
                        pt.hotkey('backspace')
                        pt.hotkey('down')
                        pt.hotkey('shift', 'enter')
                        pt.hotkey('up')
                        pt.typewrite('@')
                        if channel in title_names.keys():
                            pc.copy(title_names[channel])
                            pt.hotkey('ctrl', 'v')
                        else:
                            pc.copy(mokuai_name)
                            pt.hotkey('ctrl', 'v')
                        pt.hotkey('enter')
                        time.sleep(0.5)
                        pt.hotkey('home')
                        pt.hotkey('backspace')

                        next_flag = True

                # 点击发送
                if channel not in title_names.keys():
                    # print("title_names[channel]:", title_names[channel])
                    # time.sleep(1)
                    sent()

                if channel not in title_names.keys():
                    time.sleep(3)
                    # 删除后再次添加report
                    js = "arguments[0].innerHTML='" + report_html + "'"
                    driver.execute_script(js, report)

        time.sleep(1)
        if channel in title_names.keys() and next_flag:
            # 修改模块名
            lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")
            title_text_node = lis_body[0].find_element_by_xpath("./code/strong")
            js = "arguments[0].innerText='" + title_names[channel] + "'"
            driver.execute_script(js, title_text_node)

            # 删除不需要的内容
            # 加载所有文本值到字典data_body中
            data_body = {}
            lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")
            key = None  # 初始化key
            lis = []
            for li in lis_body:
                if lis_body.index(li) > 0:  # 从第2个li开始遍历
                    re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                    if len(re_compile.findall(li.text)):
                        print("re_compile.findall(li.text)", re_compile.findall(li.text)[0])
                        key = re_compile.findall(li.text)[0].strip()
                        lis = []
                        lis.append(li)
                        data_body[key] = lis

                    if len(re_compile.findall(li.text)) == 0:
                        lis.append(li)
                        data_body[key] = lis
                    print("li.text:", li.text)
                    print("data_body:", data_body)
            # for循环，不是的内容删除掉
            for level in data_body.keys():
                for text in data_body[level]:  # text为对象，非文本
                    print("text.text", text.text)
                    able_text_count = 0  # perception和deeplearning,计算text.text中是否所有的字符串都不包含在要删除的列表中的个数
                    for able_text in text.text.split("/"):
                        print("able_text", able_text)
                        # 对able_text进行去除其他信息处理
                        re_compile = re.compile(r'\(.*\)')
                        if len(re_compile.findall(able_text)):
                            str = re_compile.findall(able_text)[0].strip()
                            able_text = able_text.replace(str, "").strip()
                        else:
                            able_text = able_text.strip()
                        modu_name = title_names[channel]
                        if modu_name in ["Perception"]:
                            if able_text in remove_text[modu_name]:
                                js = 'arguments[0].removeChild(arguments[1])'
                                driver.execute_script(js, report, text)

                        if modu_name in ["Deeplearning", "Traffic light"]:
                            re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                            if able_text not in remove_text[modu_name] and len(re_compile.findall(able_text)) == 0:
                                able_text_count = able_text_count + 1  # 没有符合的字符串　able_text_count＋１
                                print("count", able_text_count)

                            if able_text_count == len(text.text.split("/")):
                                js = 'arguments[0].removeChild(arguments[1])'
                                driver.execute_script(js, report, text)
                                print("已删除")
                                # <p>2. <a href="https://szexa.xray.autox.tech?id=playback/pacifica-cn-373/20220802/2022-08-02-14-15-16&amp;t=6406.55#obstacleId=585559" rel="noopener noreferrer" target="_blank">Perception/Detection/FP/Bicycle</a> (电单车误检，急刹) (585559)</p>

            # 排序前重装
            data_body = {}
            lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")
            key = None  # 初始化key
            lis = []
            for li in lis_body:
                if lis_body.index(li) > 0:  # 从第2个li开始遍历
                    re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                    if len(re_compile.findall(li.text)):
                        key = re_compile.findall(li.text)[0].strip()
                        lis = []
                        lis.append(li)
                        data_body[key] = lis

                    if len(re_compile.findall(li.text)) == 0:
                        lis.append(li)
                        data_body[key] = lis
            # 排序开始
            for level in data_body.keys():
                if len(data_body[level]) > 1:
                    i = 1
                    for text in data_body[level]:
                        if data_body[level].index(text) > 0:
                            js = "return arguments[0].innerHTML"
                            text_html = driver.execute_script(js, text)
                            re_compile = re.compile(r'\d{1,2}\.\s*\<')
                            after_text_html = text_html.replace(re_compile.findall(text_html)[0], "{}. <".format(i))
                            js = "arguments[0].innerHTML='" + after_text_html + "'"
                            driver.execute_script(js, text)
                            i = i + 1

            # #删除没有内容的level
            # 删除前重装
            data_body = {}
            lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")
            key = None  # 初始化key
            lis = []
            for li in lis_body:
                if lis_body.index(li) > 0:  # 从第2个li开始遍历
                    re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                    if len(re_compile.findall(li.text)):
                        key = re_compile.findall(li.text)[0].strip()
                        lis = []
                        lis.append(li)
                        data_body[key] = lis

                    if len(re_compile.findall(li.text)) == 0:
                        lis.append(li)
                        data_body[key] = lis
            # 正式删除
            for level in data_body.keys():
                if len(data_body[level]) == 1:
                    js = 'arguments[0].removeChild(arguments[1])'
                    driver.execute_script(js, report, data_body[level][0])
            # #如果所有的level都为空，删除最前面的模块名＠对应的群
            # 删除前重装
            removed_flag = False
            data_body = {}
            lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")
            key = None  # 初始化key
            lis = []
            for li in lis_body:
                if lis_body.index(li) > 0:  # 从第2个li开始遍历
                    re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                    if len(re_compile.findall(li.text)):
                        key = re_compile.findall(li.text)[0].strip()
                        lis = []
                        lis.append(li)
                        data_body[key] = lis

                    if len(re_compile.findall(li.text)) == 0:
                        lis.append(li)
                        data_body[key] = lis
            # #判断level里面空值的个数。如果空值的个数＝date_body的长度，删除最前面的模块名＠对应的群
            data_body_len = len(data_body)
            i = 0
            for level in data_body.keys():
                if len(data_body[level]) == 0:
                    i = i + 1
            if i == data_body_len:
                js = "arguments[0].innerHTML='" + report_blank_html + "'"
                driver.execute_script(js, report)
                removed_flag = True
            time.sleep(1)
            # 发送
            if not removed_flag:
                # print("title_names[channel]:",title_names[channel])
                sent()

            # time.sleep(3)
            # if title_names[channel] == "Deeplearning":
            #     break
            # if title_names[channel] == "Traffic light":
            #     break
            # if title_names[channel] == "Perception":
            #     break

        # channel结束删除report并停止3秒钟缓冲时间
        js = "arguments[0].innerHTML='" + report_blank_html + "'"
        driver.execute_script(js, report)
        time.sleep(1)
        # time.sleep(2)


def autosent():
    # print("点击enter")
    pt.hotkey('enter')


def autoslack_pro():
    try:
        # png = {"googleExe": {"imageIcon": "./image/google.png"}, "dingwei": {"imageIcon": "./image/img_8.png"},
        #        "time": {"imageIcon": "./image/img_9.png"}}
        # a = png.get("googleExe").get('imageIcon')
        # googleExe = ()  # 存储google坐标相关信息
        # googleExe = pt.locateOnScreen(png.get("googleExe").get('imageIcon'))
        # x = googleExe[0]
        # y = googleExe[1]
        # pt.moveTo(x, y, duration=0.5)  # 移动到google图标位置
        # pt.leftClick(x, y, duration=0.1)  # 点击google图标

        # chrome_options = Options()
        # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # chrome_driver = "/usr/local/bin/chromedriver"
        # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        chrome_driver = "/usr/local/bin/chromedriver"
        # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        s = Service("/usr/local/bin/chromedriver")
        driver = webdriver.Chrome(options=chrome_options, service=s)
        driver.implicitly_wait(100)

        slack = "Slack"
        xray = "xRay"
        print(driver.title)

        # 切换页面
        for window in driver.window_handles:
            driver.switch_to.window(window)
            if slack in driver.title:
                break

        # driver.get("https://app.slack.com/client/T1WN8GREJ/D02KY11QA05/thread/GCZMAJ2SV-1640863585.181900")

        # channels = ["road_test_shenzhen", "road_test_prediction", "road_test_perception", "road_test_deeplearning", "road_test_traffic_light"]
        channels = {
            "road_test_shenzhen": {"Planning": "Planning", "System": "System", "Routing": "Routing", "XView": "XView",
                                   "lidar": "lidar", "Control": "Control"},
            "road_test_prediction": {"Prediction": "Prediction"}, "road_test_perception": {"Perception": "Perception"},
            "road_test_deeplearning": {"Perception": "Perception", "Perception Scenario": "Perception Scenario"},
            "road_test_traffic_light": {"Perception": "Perception"}}

        report = driver.find_element(By.XPATH,"//*/div[@class='ql-editor']")
        js = "return arguments[0].innerHTML"
        # 非空report
        report_html = driver.execute_script(js, report)
        time.sleep(1)
        # 空report
        report_blank_html = r"""<div class="ql-editor ql-blank" data-gramm="false" contenteditable="true" dir="auto" role="textbox" tabindex="0" data-team-id="T1WN8GREJ" aria-label="Message to xray" aria-describedby="context_bar_text-f6f9cd4a" aria-multiline="true" aria-autocomplete="list" aria-expanded="false" aria-owns="chat_input_tab_ui" spellcheck="true"><p><br></p></div>"""
        # 清空原有report
        js = "arguments[0].innerHTML='" + report_blank_html + "'"
        driver.execute_script(js, report)
        # time.sleep(1)  # 清空后等待2秒去点击channel
        time.sleep(2)  # 清空后等待2秒去点击channel
        for channel in channels:
            # 点击channel
            road_test_shenzhen = driver.find_element(By.XPATH,"//*[contains(text(),'" + channel + "') and @ dir='auto']")
            js = 'arguments[0].click()'
            driver.execute_script(js, road_test_shenzhen)
            # 添加report
            js = "arguments[0].innerHTML='" + report_html + "'"
            driver.execute_script(js, report)
            title_names = {"road_test_perception": "Perception", "road_test_deeplearning": "Deeplearning",
                           "road_test_traffic_light": "Traffic light"}
            remove_text = {
                "Perception": ["Traffic Light", "Frustum", "Connected Components", "Point Pillars", "Occupancy Grid",
                               "Traffic Cone", "Special Object", "Mask RCNN"],
                "Deeplearning": ["Connected Components", "Frustum", "Point Pillars", "Traffic Cone", "Occupancy Grid",
                                 "Special Object", "Mask RCNN", "Water Raindrop"], "Traffic light": ["Traffic Light"]}
            nothing_flag = False
            # 删除前后内容
            # 装列表
            next_flag = False  # deeplearning、traffic light,perception是否进行后续操作
            for value in channels[channel].values():
                print("value:", value)
                text_lis_body = []
                able_text_lis_body = []
                flag = False
                lis_body = driver.find_elements(By.XPATH,"//*/div[@class='ql-editor']/p")
                lis_tou = driver.find_elements(By.XPATH,"//*/div[@class='ql-editor']/div")



                for li in lis_body:
                    re_compile = re.compile(r'\W\d{1,2}:\d{2}\s+\w{2}\W')
                    if len(re_compile.findall(li.text)):
                        text_lis_body.append(li)
                        if value == li.text.replace(re_compile.findall(li.text)[0], "").strip():
                            # if value in li.text:
                            able_text_lis_body.append(li)
                if len(able_text_lis_body):
                    flag = True
                    nothing_flag = True
                if flag:
                    # 删除开头
                    if able_text_lis_body[0] is not None:
                        before_index = lis_body.index(able_text_lis_body[0])
                        if before_index != 0 and before_index is not None:
                            for j in range(before_index):
                                js = 'arguments[0].removeChild(arguments[1])'
                                driver.execute_script(js, report, lis_body[j])
                    # 删除结尾
                    a = text_lis_body.index(able_text_lis_body[0])
                    if a < len(text_lis_body) - 1:
                        after_content = text_lis_body[a + 1]
                        after_index = lis_body.index(after_content)
                        for j in range(after_index, len(lis_body)):
                            js = 'arguments[0].removeChild(arguments[1])'
                            driver.execute_script(js, report, lis_body[j])

                    # 格式整理
                    lis_body = driver.find_elements(By.XPATH,"//*/div[@class='ql-editor']/p")
                    for li in lis_body:
                        re_compile = re.compile(r'\W\d{1,2}:\d{2}\s+\w{2}\W')
                        if len(re_compile.findall(li.text)):
                            text = li.text
                            before_time = re_compile.findall(li.text)[0]
                            print(before_time)
                            mokuai_name = text.replace(before_time, "").strip()
                            actions = ActionChains(driver)
                            actions.click(li).perform()
                            pt.press('home')
                            for i in range(len(re_compile.findall(li.text)[0])):
                                pt.hotkey('shift', 'right')
                            pt.hotkey('backspace')
                            pt.hotkey('down')
                            pt.hotkey('shift', 'enter')
                            pt.hotkey('up')
                            pt.typewrite('@')
                            if channel in title_names.keys():
                                pc.copy(title_names[channel])
                                pt.hotkey('ctrl', 'v')
                            else:
                                pc.copy(mokuai_name)
                                pt.hotkey('ctrl', 'v')
                            pt.hotkey('enter')
                            time.sleep(0.5)
                            pt.hotkey('home')
                            pt.hotkey('backspace')

                            next_flag = True

                    # 点击发送
                    if channel not in title_names.keys():
                        # print("title_names[channel]:", title_names[channel])
                        time.sleep(2)
                        autosent()

                    if channel not in title_names.keys():
                        time.sleep(2)
                        # 删除后再次添加report
                        js = "arguments[0].innerHTML='" + report_html + "'"
                        driver.execute_script(js, report)

                    time.sleep(1)
                    if channel in title_names.keys() and next_flag:
                        if value != "Perception Scenario":
                            # 修改模块名
                            lis_body = driver.find_elements(By.XPATH,"//*/div[@class='ql-editor']/p")
                            title_text_node = lis_body[0].find_element(By.XPATH,"./code/strong")
                            js = "arguments[0].innerText='" + title_names[channel] + "'"
                            driver.execute_script(js, title_text_node)

                        # 删除不需要的内容
                        # 加载所有文本值到字典data_body中
                        data_body = {}
                        lis_body = driver.find_elements(By.XPATH,"//*/div[@class='ql-editor']/p")
                        key = None  # 初始化key
                        lis = []
                        for li in lis_body:
                            if lis_body.index(li) > 0:  # 从第2个li开始遍历
                                re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                                if len(re_compile.findall(li.text)):
                                    key = re_compile.findall(li.text)[0].strip()
                                    lis = []
                                    lis.append(li)

                                if len(re_compile.findall(li.text)) == 0:
                                    lis.append(li)
                                    data_body[key] = lis

                        # for循环，不是的内容删除掉
                        for level in data_body.keys():
                            for text in data_body[level]:  # text为对象，非文本
                                able_text_count = 0  # perception和deeplearning,计算text.text中是否所有的字符串都不包含在要删除的列表中的个数
                                removeagin_flag = False
                                for able_text in text.text.split("/"):
                                    # 对able_text进行去除其他信息处理
                                    re_compile = re.compile(r'\(.*\)')
                                    if len(re_compile.findall(able_text)):
                                        str = re_compile.findall(able_text)[0].strip()
                                        able_text = able_text.replace(str, "").strip()
                                    else:
                                        able_text = able_text.strip()
                                    modu_name = title_names[channel]
                                    if modu_name in ["Perception"]:
                                        if able_text in remove_text[modu_name] and not removeagin_flag:
                                            js = 'arguments[0].removeChild(arguments[1])'
                                            driver.execute_script(js, report, text)
                                            removeagin_flag = True

                                    if modu_name in ["Deeplearning", "Traffic light"]:
                                        re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                                        if able_text not in remove_text[modu_name] and len(
                                                re_compile.findall(able_text)) == 0:
                                            able_text_count = able_text_count + 1  # 没有符合的字符串　able_text_count＋１

                                        if able_text_count == len(text.text.split("/")):
                                            js = 'arguments[0].removeChild(arguments[1])'
                                            driver.execute_script(js, report, text)
                                            # <p>2. <a href="https://szexa.xray.autox.tech?id=playback/pacifica-cn-373/20220802/2022-08-02-14-15-16&amp;t=6406.55#obstacleId=585559" rel="noopener noreferrer" target="_blank">Perception/Detection/FP/Bicycle</a> (电单车误检，急刹) (585559)</p>

                        # 排序前重装
                        data_body = {}
                        lis_body = driver.find_elements(By.XPATH,"//*/div[@class='ql-editor']/p")
                        key = None  # 初始化key
                        lis = []
                        for li in lis_body:
                            if lis_body.index(li) > 0:  # 从第2个li开始遍历
                                re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                                if len(re_compile.findall(li.text)):
                                    key = re_compile.findall(li.text)[0].strip()
                                    lis = []
                                    lis.append(li)
                                    data_body[key] = lis

                                if len(re_compile.findall(li.text)) == 0:
                                    lis.append(li)
                                    data_body[key] = lis
                        # # 排序开始
                        for level in data_body.keys():
                            if len(data_body[level]) > 1:
                                i = 1
                                for text in data_body[level]:
                                    if data_body[level].index(text) > 0:
                                        js = "return arguments[0].innerHTML"
                                        text_html = driver.execute_script(js, text)
                                        re_compile = re.compile(r'\d{1,2}\.\s*\<')
                                        after_text_html = text_html.replace(re_compile.findall(text_html)[0],
                                                                            "{}. <".format(i))
                                        js = "arguments[0].innerHTML='" + after_text_html + "'"
                                        driver.execute_script(js, text)
                                        i = i + 1

                        # #删除没有内容的level
                        # 删除前重装
                        data_body = {}
                        lis_body = driver.find_elements(By.XPATH,"//*/div[@class='ql-editor']/p")
                        key = None  # 初始化key
                        lis = []
                        for li in lis_body:
                            if lis_body.index(li) > 0:  # 从第2个li开始遍历
                                re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                                if len(re_compile.findall(li.text)):
                                    key = re_compile.findall(li.text)[0].strip()
                                    lis = []
                                    lis.append(li)
                                    data_body[key] = lis

                                if len(re_compile.findall(li.text)) == 0:
                                    lis.append(li)
                                    data_body[key] = lis
                        # # 正式删除
                        for level in data_body.keys():
                            if len(data_body[level]) == 1:
                                js = 'arguments[0].removeChild(arguments[1])'
                                driver.execute_script(js, report, data_body[level][0])
                        # #如果所有的level都为空，删除最前面的模块名＠对应的群
                        # 删除前重装
                        removed_flag = False
                        data_body = {}
                        lis_body = driver.find_elements(By.XPATH,"//*/div[@class='ql-editor']/p")
                        key = None  # 初始化key
                        lis = []
                        for li in lis_body:
                            if lis_body.index(li) > 0:  # 从第2个li开始遍历
                                re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                                if len(re_compile.findall(li.text)):
                                    key = re_compile.findall(li.text)[0].strip()
                                    lis = []
                                    lis.append(li)
                                    data_body[key] = lis

                                if len(re_compile.findall(li.text)) == 0:
                                    lis.append(li)
                                    data_body[key] = lis
                        # # #判断level里面空值的个数。如果空值的个数＝date_body的长度，删除最前面的模块名＠对应的群
                        data_body_len = len(data_body)
                        i = 0
                        for level in data_body.keys():
                            if len(data_body[level]) == 0:
                                i = i + 1
                        if i == data_body_len:
                            js = "arguments[0].innerHTML='" + report_blank_html + "'"
                            driver.execute_script(js, report)
                            removed_flag = True
                        time.sleep(2)
                        # 发送
                        if not removed_flag:
                            # print("title_names[channel]:",title_names[channel])
                            autosent()
                            # 发送后再次添加report
                            time.sleep(1)
                            js = "arguments[0].innerHTML='" + report_html + "'"
                            driver.execute_script(js, report)
                            time.sleep(2)

                        # time.sleep(3)
                        # if title_names[channel] == "Deeplearning":
                        #     break
                        # if title_names[channel] == "Traffic light":
                        #     break
                        # if title_names[channel] == "Perception":
                        #     break

            # channel结束删除report并停止3秒钟缓冲时间
            if not nothing_flag:  # 如果没有匹配到停3秒时间,保证程序不会出错
                time.sleep(2)
            js = "arguments[0].innerHTML='" + report_blank_html + "'"
            driver.execute_script(js, report)
            time.sleep(2)
            # time.sleep(2)
    except:
        pass

def chaxunshuju(vehicle, rtime):
    flag = False
    for i in range(2):

        try:
            print(i)
            anocheone(vehicle=vehicle, rtime=rtime)
            flag = True
            print("已打开")

        except:
            time.sleep(2)
            print("未打开")
        if flag:
            break


def autoslack():
    png = {"googleExe": {"imageIcon": "./image/google.png"}, "dingwei": {"imageIcon": "./image/img_8.png"},
           "time": {"imageIcon": "./image/img_9.png"}}
    a = png.get("googleExe").get('imageIcon')
    googleExe = ()  # 存储google坐标相关信息
    googleExe = pt.locateOnScreen(png.get("googleExe").get('imageIcon'))
    x = googleExe[0]
    y = googleExe[1]
    pt.moveTo(x, y, duration=0.5)  # 移动到google图标位置
    pt.leftClick(x, y, duration=0.1)  # 点击google图标

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    driver.implicitly_wait(10)
    # driver.get("https://app.slack.com/client/T1WN8GREJ/D02KY11QA05/thread/GCZMAJ2SV-1640863585.181900")

    # channels = ["road_test_shenzhen", "road_test_prediction", "road_test_perception", "road_test_deeplearning", "road_test_traffic_light"]
    channels = {
        "road_test_shenzhen": {"Planning": "Planning", "System": "System", "Routing": "Routing", "XView": "XView",
                               "lidar": "lidar", "Control": "Control"},
        "road_test_prediction": {"Prediction": "Prediction"}, "road_test_perception": {"Perception": "Perception"},
        "road_test_deeplearning": {"Perception": "Perception"},
        "road_test_traffic_light": {"Perception": "Perception"}}

    report = driver.find_element_by_xpath("//*/div[@class='ql-editor']")
    js = "return arguments[0].innerHTML"
    # 非空report
    report_html = driver.execute_script(js, report)
    # 空report
    report_blank_html = r"""<div class="ql-editor ql-blank" data-gramm="false" contenteditable="true" dir="auto" role="textbox" tabindex="0" data-team-id="T1WN8GREJ" aria-label="Message to xray" aria-describedby="context_bar_text-f6f9cd4a" aria-multiline="true" aria-autocomplete="list" aria-expanded="false" aria-owns="chat_input_tab_ui" spellcheck="true"><p><br></p></div>"""
    # 清空原有report
    js = "arguments[0].innerHTML='" + report_blank_html + "'"
    driver.execute_script(js, report)
    # time.sleep(1)  # 清空后等待2秒去点击channel
    time.sleep(2)  # 清空后等待2秒去点击channel
    for channel in channels:
        # 点击channel
        road_test_shenzhen = driver.find_element_by_xpath("//*[contains(text(),'" + channel + "') and @ dir='auto']")
        js = 'arguments[0].click()'
        driver.execute_script(js, road_test_shenzhen)
        # 添加report
        js = "arguments[0].innerHTML='" + report_html + "'"
        driver.execute_script(js, report)
        title_names = {"road_test_perception": "Perception", "road_test_deeplearning": "Deeplearning",
                       "road_test_traffic_light": "Traffic light"}
        remove_text = {
            "Perception": ["Traffic Light", "Frustum", "Connected Components", "Point Pillars", "Occupancy Grid",
                           "Traffic Cone", "Special Object", "Mask RCNN"],
            "Deeplearning": ["Connected Components", "Frustum", "Point Pillars", "Traffic Cone", "Occupancy Grid",
                             "Special Object", "Mask RCNN"], "Traffic light": ["Traffic Light"]}
        # 删除前后内容
        # 装列表
        next_flag = False  # deeplearning、traffic light,perception是否进行后续操作
        for value in channels[channel].values():
            print("value:", value)
            text_lis_body = []
            able_text_lis_body = []
            flag = False
            lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")
            for li in lis_body:
                re_compile = re.compile(r'\W\d{1,2}:\d{2}\s+\w{2}\W')
                if len(re_compile.findall(li.text)):
                    text_lis_body.append(li)
                    if value == li.text.replace(re_compile.findall(li.text)[0], "").strip():
                        # if value in li.text:
                        able_text_lis_body.append(li)
            if len(able_text_lis_body):
                flag = True
            if flag:
                # 删除开头
                if able_text_lis_body[0] is not None:
                    before_index = lis_body.index(able_text_lis_body[0])
                    if before_index != 0 and before_index is not None:
                        for j in range(before_index):
                            js = 'arguments[0].removeChild(arguments[1])'
                            driver.execute_script(js, report, lis_body[j])
                # 删除结尾
                a = text_lis_body.index(able_text_lis_body[0])
                if a < len(text_lis_body) - 1:
                    after_content = text_lis_body[a + 1]
                    after_index = lis_body.index(after_content)
                    for j in range(after_index, len(lis_body)):
                        js = 'arguments[0].removeChild(arguments[1])'
                        driver.execute_script(js, report, lis_body[j])

                # 格式整理
                lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")
                for li in lis_body:
                    re_compile = re.compile(r'\W\d{1,2}:\d{2}\s+\w{2}\W')
                    if len(re_compile.findall(li.text)):
                        text = li.text
                        before_time = re_compile.findall(li.text)[0]
                        print(before_time)
                        mokuai_name = text.replace(before_time, "").strip()
                        actions = ActionChains(driver)
                        actions.click(li).perform()
                        pt.press('home')
                        for i in range(len(re_compile.findall(li.text)[0])):
                            pt.hotkey('shift', 'right')
                        pt.hotkey('backspace')
                        pt.hotkey('down')
                        pt.hotkey('shift', 'enter')
                        pt.hotkey('up')
                        pt.typewrite('@')
                        if channel in title_names.keys():
                            pc.copy(title_names[channel])
                            pt.hotkey('ctrl', 'v')
                        else:
                            pc.copy(mokuai_name)
                            pt.hotkey('ctrl', 'v')
                        pt.hotkey('enter')
                        time.sleep(0.5)
                        pt.hotkey('home')
                        pt.hotkey('backspace')

                        next_flag = True

                # 点击发送
                if channel not in title_names.keys():
                    # print("title_names[channel]:", title_names[channel])
                    time.sleep(2)
                    autosent()

                if channel not in title_names.keys():
                    time.sleep(2)
                    # 发送后再次添加report
                    js = "arguments[0].innerHTML='" + report_html + "'"
                    driver.execute_script(js, report)

        time.sleep(1)
        if channel in title_names.keys() and next_flag:
            if value != "Perception Scenario":
                # 修改模块名
                lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")
                title_text_node = lis_body[0].find_element_by_xpath("./code/strong")
                js = "arguments[0].innerText='" + title_names[channel] + "'"
                driver.execute_script(js, title_text_node)

            # 删除不需要的内容
            # 加载所有文本值到字典data_body中
            data_body = {}
            lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")
            key = None  # 初始化key
            lis = []
            for li in lis_body:
                if lis_body.index(li) > 0:  # 从第2个li开始遍历
                    re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                    if len(re_compile.findall(li.text)):
                        key = re_compile.findall(li.text)[0].strip()
                        lis = []
                        lis.append(li)

                    if len(re_compile.findall(li.text)) == 0:
                        lis.append(li)
                        data_body[key] = lis
            # for循环，不是的内容删除掉
            for level in data_body.keys():
                for text in data_body[level]:  # text为对象，非文本
                    able_text_count = 0  # perception和deeplearning,计算text.text中是否所有的字符串都不包含在要删除的列表中的个数
                    removeagin_flag = False
                    for able_text in text.text.split("/"):
                        # 对able_text进行去除其他信息处理
                        re_compile = re.compile(r'\(.*\)')
                        if len(re_compile.findall(able_text)):
                            str = re_compile.findall(able_text)[0].strip()
                            able_text = able_text.replace(str, "").strip()
                        else:
                            able_text = able_text.strip()
                        modu_name = title_names[channel]
                        if modu_name in ["Perception"]:
                            if able_text in remove_text[modu_name] and not removeagin_flag:
                                js = 'arguments[0].removeChild(arguments[1])'
                                driver.execute_script(js, report, text)
                                removeagin_flag = True

                        if modu_name in ["Deeplearning", "Traffic light"]:
                            re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                            if able_text not in remove_text[modu_name] and len(
                                    re_compile.findall(able_text)) == 0:
                                able_text_count = able_text_count + 1  # 没有符合的字符串　able_text_count＋１

                            if able_text_count == len(text.text.split("/")):
                                js = 'arguments[0].removeChild(arguments[1])'
                                driver.execute_script(js, report, text)
                                # <p>2. <a href="https://szexa.xray.autox.tech?id=playback/pacifica-cn-373/20220802/2022-08-02-14-15-16&amp;t=6406.55#obstacleId=585559" rel="noopener noreferrer" target="_blank">Perception/Detection/FP/Bicycle</a> (电单车误检，急刹) (585559)</p>

            # 排序前重装
            data_body = {}
            lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")
            key = None  # 初始化key
            lis = []
            for li in lis_body:
                if lis_body.index(li) > 0:  # 从第2个li开始遍历
                    re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                    if len(re_compile.findall(li.text)):
                        key = re_compile.findall(li.text)[0].strip()
                        lis = []
                        lis.append(li)
                        data_body[key] = lis

                    if len(re_compile.findall(li.text)) == 0:
                        lis.append(li)
                        data_body[key] = lis
            # # 排序开始
            for level in data_body.keys():
                if len(data_body[level]) > 1:
                    i = 1
                    for text in data_body[level]:
                        if data_body[level].index(text) > 0:
                            js = "return arguments[0].innerHTML"
                            text_html = driver.execute_script(js, text)
                            re_compile = re.compile(r'\d{1,2}\.\s*\<')
                            after_text_html = text_html.replace(re_compile.findall(text_html)[0],
                                                                "{}. <".format(i))
                            js = "arguments[0].innerHTML='" + after_text_html + "'"
                            driver.execute_script(js, text)
                            i = i + 1

            # #删除没有内容的level
            # 删除前重装
            data_body = {}
            lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")
            key = None  # 初始化key
            lis = []
            for li in lis_body:
                if lis_body.index(li) > 0:  # 从第2个li开始遍历
                    re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                    if len(re_compile.findall(li.text)):
                        key = re_compile.findall(li.text)[0].strip()
                        lis = []
                        lis.append(li)
                        data_body[key] = lis

                    if len(re_compile.findall(li.text)) == 0:
                        lis.append(li)
                        data_body[key] = lis
            # # 正式删除
            for level in data_body.keys():
                if len(data_body[level]) == 1:
                    js = 'arguments[0].removeChild(arguments[1])'
                    driver.execute_script(js, report, data_body[level][0])
            # #如果所有的level都为空，删除最前面的模块名＠对应的群
            # 删除前重装
            removed_flag = False
            data_body = {}
            lis_body = driver.find_elements_by_xpath("//*/div[@class='ql-editor']/p")
            key = None  # 初始化key
            lis = []
            for li in lis_body:
                if lis_body.index(li) > 0:  # 从第2个li开始遍历
                    re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                    if len(re_compile.findall(li.text)):
                        key = re_compile.findall(li.text)[0].strip()
                        lis = []
                        lis.append(li)
                        data_body[key] = lis

                    if len(re_compile.findall(li.text)) == 0:
                        lis.append(li)
                        data_body[key] = lis
            # # #判断level里面空值的个数。如果空值的个数＝date_body的长度，删除最前面的模块名＠对应的群
            data_body_len = len(data_body)
            i = 0
            for level in data_body.keys():
                if len(data_body[level]) == 0:
                    i = i + 1
            if i == data_body_len:
                js = "arguments[0].innerHTML='" + report_blank_html + "'"
                driver.execute_script(js, report)
                removed_flag = True
            time.sleep(2)
            # 发送
            if not removed_flag:
                # print("title_names[channel]:",title_names[channel])
                autosent()

            # time.sleep(3)
            # if title_names[channel] == "Deeplearning":
            #     break
            # if title_names[channel] == "Traffic light":
            #     break
            # if title_names[channel] == "Perception":
            #     break

        # channel结束删除report并停止3秒钟缓冲时间
        js = "arguments[0].innerHTML='" + report_blank_html + "'"
        driver.execute_script(js, report)
        time.sleep(1)
        # time.sleep(2)


def autoexcell():
    png = {"googleExe": {"imageIcon": "./image/google.png"}, "dingwei": {"imageIcon": "./image/img_8.png"},
           "time": {"imageIcon": "./image/img_9.png"}}
    a = png.get("googleExe").get('imageIcon')
    googleExe = ()  # 存储google坐标相关信息
    googleExe = pt.locateOnScreen(png.get("googleExe").get('imageIcon'))
    x = googleExe[0]
    y = googleExe[1]
    pt.moveTo(x, y, duration=0.5)  # 移动到google图标位置
    pt.leftClick(x, y, duration=0.1)  # 点击google图标

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    driver.implicitly_wait(10)

    lis_name = driver.find_elements_by_xpath("//*[text()='Pinyi Hu 胡品毅[QA]' and @tabindex='-1']")

    for li in lis_name:
        lis_heads = li.find_elements_by_xpath("./../../../div/div/div/div/div/pre")
        for head in lis_heads:
            if "2022/08/09" in head.text:
                re_compile = re.compile(r'Commit:\w{8}')
                print(re_compile.findall(head.text)[0].replace("Commit:", "").strip())
                print(head.text)


def cptool():
    png = {"googleExe": {"imageIcon": "./image/google.png"}, "dingwei": {"imageIcon": "./image/img_8.png"},
           "time": {"imageIcon": "./image/img_9.png"}}
    a = png.get("googleExe").get('imageIcon')
    googleExe = ()  # 存储google坐标相关信息
    googleExe = pt.locateOnScreen(png.get("googleExe").get('imageIcon'))
    x = googleExe[0]
    y = googleExe[1]
    pt.moveTo(x, y, duration=0.5)  # 移动到google图标位置
    pt.leftClick(x, y, duration=0.1)  # 点击google图标

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    driver.implicitly_wait(10)

    js = '''
    window.hovered_element = null
    function track_mouse(event){
     var x = event.clientX, y = event.clientY
     var element = document.elementFromPoint(x, y)
      if (!element) {
          window.hovered_element = null
      return // 当前位置没有元素
     } 
      window.hovered_element = element
    }
    window.onmousemove = track_mouse
    '''
    driver.execute_script(js)
    while True:
        element = driver.execute_script("return window.hovered_element")
        if element:
            print(f"当前鼠标说在标签：{element.tag_name},其中文本内容：{element.text}")
            actions = ActionChains(driver)

            # actions.click(element).perform()
            # for i in range(len(element.text)):
            #     pt.hotkey('shift,left')
        time.sleep(1)


def kuaijiejian():
    def on_press(key):
        '按下按键时执行。'

        try:
            if key == keyboard.Key.alt:

                pt.hotkey('enter')
                # loc = pt.position()
                # pt.click(2833,210)
                # pt.moveTo(loc)


        except AttributeError:
            print('special key {0} pressed'.format(
                key))
        # 通过属性判断按键类型。


    def on_release(key):
        pass

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def tianbiaoge():
    png = {"googleExe": {"imageIcon": "./image/google.png"}, "dingwei": {"imageIcon": "./image/img_8.png"},
           "time": {"imageIcon": "./image/img_9.png"}}
    a = png.get("googleExe").get('imageIcon')
    googleExe = ()  # 存储google坐标相关信息
    googleExe = pt.locateOnScreen(png.get("googleExe").get('imageIcon'))
    x = googleExe[0]
    y = googleExe[1]
    pt.moveTo(x, y, duration=0.5)  # 移动到google图标位置
    pt.leftClick(x, y, duration=0.1)  # 点击google图标

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    driver.implicitly_wait(100)

    def on_press(key):
        '按下按键时执行。'

        try:
            if key == keyboard.Key.esc:
                pt.hotkey('home')
                pt.hotkey('right')
                pt.hotkey('right')
                pt.hotkey('shift', 'end')

                pt.hotkey('ctrl','c')
            if key == keyboard.Key.f2:
                pt.hotkey('ctrl','v')

            if key == keyboard.Key.f4:
                pt.typewrite("@")
                pc.copy("pinyihu")
                pt.hotkey('ctrl','v')
                loc_dt = datetime.datetime.today()
                time_del = datetime.timedelta(hours=3)
                new_dt = loc_dt + time_del
                datetime_format = new_dt.strftime("%m/%d")
                loc_dt_format = loc_dt.strftime("%m/%d")
                print(loc_dt_format)
                print(datetime_format)
                # pc.copy(loc_dt_format)
                # pt.typewrite(" ")
                # pt.hotkey('ctrl','v')
            if key == keyboard.Key.f8:
                driver = webdriver.Chrome(chrome_driver, options=chrome_options)
                driver.implicitly_wait(10)
                handles_list = driver.window_handles
                print(driver.title)
                if "Confluence" not in driver.title:
                    for window in handles_list:
                        driver.switch_to.window(window)
                        if "Confluence" in driver.title:
                            break
                element = driver.find_element_by_xpath("//*/span[@aria-label='Open link in a new tab']")
                js = "arguments[0].click()"
                driver.execute_script(js,element)
                print(driver.title)

                handles_list = driver.window_handles
                if "xRay" not in driver.title:
                    for window in handles_list:
                        driver.switch_to.window(window)
                        if "xRay" in driver.title:
                            pen = driver.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[6]")
                            break
                print(driver.title)
                pt.hotkey('r')
                time.sleep(0.3)
                pt.hotkey('v')
                time.sleep(0.3)
                pt.hotkey('v')
                time.sleep(0.3)
                pt.hotkey('v')
                time.sleep(0.3)
                pt.hotkey('ctrl','r')
                time.sleep(0.5)
                pt.hotkey('enter')
                pt.hotkey('ctrl','w')
                pt.hotkey('tab')
                pt.hotkey('ctrl','v')
            if key == keyboard.Key.f9:
                pt.hotkey('ctrl','v')
            if key == keyboard.Key.f10:
                pt.hotkey('ctrl','c')






        except AttributeError:
            print('special key {0} pressed'.format(
                key))
        # 通过属性判断按键类型。


    def on_release(key):
        pass

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def jietu():
    pass


# #点击链接
# paste_loc_click = paste_loc.find_element_by_xpath("./p/a")
# paste_loc_click.click()
# #截图
# element = driver.find_element_by_xpath("//*/span[@aria-label='Open link in a new tab']")
# js = "arguments[0].click()"
# driver.execute_script(js, element)
# print(driver.title)
# #点击链接后重新获取handlelist
# handles_list = driver.window_handles
# if "xRay" not in driver.title:
#     for window in handles_list:
#         driver.switch_to.window(window)
#         if "xRay" in driver.title:
#             pen = driver.find_element_by_xpath(
#                 "/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[6]")
#             break
# print(driver.title)
# pt.hotkey('r')
# pt.hotkey('v')
# pt.hotkey('v')
# pt.hotkey('v')
# pt.hotkey('ctrl', 'r')
# time.sleep(0.5)
# pt.hotkey('enter')
# #关闭窗口
# driver.close()
# #关闭后切换回来confluence_window
# driver.switch_to.window(confluence_window)
#
# #复制粘贴截图
# time.sleep(0.5)
# pt.hotkey('tab')
# pt.hotkey('ctrl', 'v')
#

def tianbiaoge_pro():
    # png = {"googleExe": {"imageIcon": "./image/google.png"}, "dingwei": {"imageIcon": "./image/img_8.png"},
    #        "time": {"imageIcon": "./image/img_9.png"}}
    # a = png.get("googleExe").get('imageIcon')
    # googleExe = ()  # 存储google坐标相关信息
    # googleExe = pt.locateOnScreen(png.get("googleExe").get('imageIcon'))
    # x = googleExe[0]
    # y = googleExe[1]
    # pt.moveTo(x, y, duration=0.5)  # 移动到google图标位置
    # pt.leftClick(x, y, duration=0.1)  # 点击google图标
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "/usr/local/bin/chromedriver"
    # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    s = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(options=chrome_options, service=s)
    driver.implicitly_wait(100)
    def on_press(key):
        '按下按键时执行。'

        # global driver
        try:
            # if key == keyboard.Key.pause:
            #     # chrome_options = Options()
            #     # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            #     # chrome_driver = "/usr/local/bin/chromedriver"
            #     driver = webdriver.Chrome(chrome_driver, options=chrome_options)
            #     current_window = driver.current_window_handle
            #     driver.switch_to.window(current_window)
            #     driver.execute_script("window.alert('填写表格已退出')")
            #     time.sleep(1.5)
            #     pt.hotkey('enter')
            #     pt.hotkey('backspace')
            #     print("*" * 30)
            #     print("填写表格已退出")
            #     return False
            if key == keyboard.Key.esc:
                # pt.typewrite("@")
                pc.copy("@pinyihu")
                pt.hotkey('ctrl', 'v')

            if key == keyboard.Key.f2:
                pt.hotkey('ctrl','v')
            if key == keyboard.Key.f8:
                # try:
                chrome_options = Options()
                chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                chrome_driver = "/usr/local/bin/chromedriver"
                # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
                s = Service("/usr/local/bin/chromedriver")
                driver = webdriver.Chrome(options=chrome_options, service=s)
                driver.implicitly_wait(100)
                confluence_window = None
                handles_list = driver.window_handles
                print(driver.title)
                if "Confluence" not in driver.title:
                    for window in handles_list:
                        driver.switch_to.window(window)
                        if "Confluence" in driver.title:
                            confluence_window = window
                            break

                else:
                    main_windows = driver.current_window_handle
                    confluence_window = main_windows
                    driver.switch_to.window(confluence_window)
                # time.sleep(0.5)


                lis_head = driver.find_elements(By.XPATH,"//*[starts-with(text(),'Date')]")
                pt.hotkey('f11')
                # time.sleep(10)
                for li in lis_head:


                    # loc = li.location_once_scrolled_into_view
                    # print(loc)
                    action = ActionChains(driver)
                    action.move_to_element(li).click().perform()
                    time.sleep(0.3)
                    pt.hotkey('end')
                    time.sleep(0.3)
                    pt.hotkey('down')
                    time.sleep(0.3)
                    pt.hotkey('down')
                    pt.hotkey('enter')
                    link = pc.paste()
                    time.sleep(0.1)

                    pc.copy("link:")
                    time.sleep(0.1)
                    pt.hotkey('ctrl', 'v')
                    pc.copy(link)
                    pt.hotkey('ctrl', 'v')



                    re_compile = re.compile(r'Date:.{10}')
                    print(re_compile.findall(li.text)[0].replace("Date:2022/", "").strip())

                    ceshi_date = re_compile.findall(li.text)[0].replace("Date:2022/", "").strip()
                    slack_re_compile = re.compile(r"link:.*")
                    slack_link = slack_re_compile.findall(li.text)[0].replace("link:", "").strip()
                    lis_holetext = li.find_elements(By.XPATH,"./../../../p/a")
                    lis_holetext = li.find_elements(By.XPATH,"./../../../p")
                    index = 1
                    for p in lis_holetext:
                        if "@" not in p.text:
                            # time.sleep(0.5)
                            action = ActionChains(driver)
                            action.click(p).perform()
                            pt.hotkey('end')
                            pt.hotkey('shift','home')
                            #复制
                            pt.hotkey('ctrl','c')
                            #站到下一个格子 格子加一
                            print(index)
                            xpath = "//*[starts-with(text(),'Date')]/../../../../following-sibling::tr[{}]/td[2]".format(index)
                            paste_loc = driver.find_element(By.XPATH,xpath)
                            # time.sleep(0.5)
                            action = ActionChains(driver)
                            driver.execute_script("arguments[0].scrollIntoView();", paste_loc)
                            action.click(paste_loc).perform()
                            pt.hotkey('ctrl','v')
                            jietu()
                            #填写日期
                            pt.hotkey('shift','tab')
                            pt.typewrite("@")
                            pc.copy("pinyihu")
                            pt.hotkey('ctrl','v')
                            # pc.copy(ceshi_date)
                            # pt.hotkey('ctrl','v')
                            index += 1

                            # time.sleep(0.5)
                            #回到原始位置
                            #复制
                            #
                    for i in range(1,index):
                        print(index - i ,"index")
                        xpath = "//*[starts-with(text(),'Date')]/../../../../following-sibling::tr[{}]/td[2]".format(
                            index - i)
                        paste_loc = driver.find_element(By.XPATH,xpath)


                        #点击链接
                        paste_loc_click = paste_loc.find_element(By.XPATH,"./p/a")
                        paste_loc_click.click()
                        #截图
                        element = driver.find_element(By.XPATH,"//*/span[@aria-label='Open link in a new tab']")
                        js = "arguments[0].click()"
                        driver.execute_script(js, element)
                        print(driver.title)
                        #点击链接后重新获取handlelist
                        handles_list = driver.window_handles
                        if "xRay" not in driver.title:
                            for window in handles_list:
                                driver.switch_to.window(window)
                                if "xRay" in driver.title:
                                    pen = driver.find_element(By.XPATH,
                                        "/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[6]")
                                    break
                        print(driver.title)
                        # time.sleep(0.4)
                        pt.hotkey('r')
                        time.sleep(0.2)
                        pt.hotkey('v')
                        time.sleep(0.2)
                        pt.hotkey('v')
                        time.sleep(0.2)
                        pt.hotkey('v')
                        time.sleep(0.2)
                        pt.hotkey('ctrl', 'r')
                        time.sleep(0.2)
                        pt.hotkey('enter')
                        #关闭窗口
                        driver.close()
                        # time.sleep(1)
                        #关闭后切换回来confluence_window
                        print(confluence_window,"confluence_window")
                        driver.switch_to.window(confluence_window)
                        # break

                        #复制粘贴截图
                        time.sleep(0.8)

                        pt.hotkey('tab')
                        time.sleep(0.5)

                        pt.hotkey('ctrl', 'v')
                        time.sleep(0.8)
                        pt.hotkey('right')
                        pc.copy(slack_link)
                        pt.hotkey('ctrl','v')

                        i += 1
                    #清空表格
                    source = driver.find_element(By.XPATH,"//*[starts-with(text(),'Date')]/../../../following-sibling::td[1]")
                    target = driver.find_element(By.XPATH,"//*[starts-with(text(),'Date')]/../../../preceding-sibling::td[1]")

                    actions = ActionChains(driver)
                    actions.drag_and_drop(source, target)
                    actions.perform()
                    pt.hotkey('backspace')
                    pt.hotkey('f11')
                    break
                # except:
                #     pass


            if key == keyboard.Key.f4:
                try:
                    chrome_options = Options()
                    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                    chrome_driver = "/usr/local/bin/chromedriver"
                    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
                    driver.implicitly_wait(100)
                    handles_list = driver.window_handles
                    print(driver.title)
                    if "Confluence" not in driver.title:
                        for window in handles_list:
                            driver.switch_to.window(window)
                            if "Confluence" in driver.title:
                                break
                    element = driver.find_element(By.XPATH,"//*/span[@aria-label='Open link in a new tab']")
                    js = "arguments[0].click()"
                    driver.execute_script(js, element)
                    print(driver.title)

                    handles_list = driver.window_handles
                    if "xRay" not in driver.title:
                        for window in handles_list:
                            driver.switch_to.window(window)
                            if "xRay" in driver.title:
                                pen = driver.find_element(By.XPATH,
                                    "/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[6]")
                                break
                    print(driver.title)
                    pt.hotkey('r')
                    time.sleep(0.3)
                    pt.hotkey('v')
                    time.sleep(0.3)
                    pt.hotkey('v')
                    time.sleep(0.3)
                    pt.hotkey('v')
                    time.sleep(0.3)
                    pt.hotkey('ctrl', 'r')
                    time.sleep(0.5)
                    pt.hotkey('enter')
                    pt.hotkey('ctrl', 'w')
                    pt.hotkey('tab')
                    pt.hotkey('ctrl', 'v')
                except:
                    pass
            if key == keyboard.Key.pause:
                # chrome_options = Options()
                # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                # chrome_driver = "/usr/local/bin/chromedriver"
                # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
                # current_window = driver.current_window_handle
                # driver.switch_to.window(current_window)
                # driver.execute_script("window.alert('填表格已退出')")
                # time.sleep(1.5)
                # pt.hotkey('enter')
                # pt.hotkey('backspace')
                print("*" * 30)
                print("填表格已退出")
                return False


        except AttributeError:
            print('special key {0} pressed'.format(
                key))
        # 通过属性判断按键类型。


    def on_release(key):
        pass

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def huizong():
    try:
        # png = {"googleExe": {"imageIcon": "./image/google.png"}, "dingwei": {"imageIcon": "./image/img_8.png"},
        #        "time": {"imageIcon": "./image/img_9.png"}}
        # a = png.get("googleExe").get('imageIcon')
        # googleExe = ()  # 存储google坐标相关信息
        # googleExe = pt.locateOnScreen(png.get("googleExe").get('imageIcon'))
        # x = googleExe[0]
        # y = googleExe[1]
        # pt.moveTo(x, y, duration=0.5)  # 移动到google图标位置
        # pt.leftClick(x, y, duration=0.1)  # 点击google图标
        # print("#" * 30)
        # print("已进入程序，可以尝试快捷键进行操作啦(*_*)")
        def on_press(key):
            '按下按键时执行。'


            try:
                if key == keyboard.KeyCode.from_char('6'):
                    # chrome_options = Options()
                    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                    # chrome_driver = "/usr/local/bin/chromedriver"
                    # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
                    # current_window = driver.current_window_handle
                    # driver.switch_to.window(current_window)
                    # driver.execute_script("window.alert('打tag已进入')")
                    # time.sleep(1)
                    # pt.hotkey('enter')
                    print("*"*30)
                    print("打tag已进入")
                    pt.hotkey('backspace')
                    tag()
                if key == keyboard.KeyCode.from_char('7'):
                    # chrome_options = Options()
                    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                    # chrome_driver = "/usr/local/bin/chromedriver"
                    # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
                    # current_window = driver.current_window_handle
                    # driver.switch_to.window(current_window)
                    # driver.execute_script("window.alert('开始发送slack报告')")
                    # time.sleep(0.5)
                    # pt.hotkey('enter')
                    pt.hotkey('backspace')
                    autoslack_pro()

                if key == keyboard.KeyCode.from_char('8'):
                    # chrome_options = Options()
                    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                    # chrome_driver = "/usr/local/bin/chromedriver"
                    # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
                    # current_window = driver.current_window_handle
                    # driver.switch_to.window(current_window)
                    # driver.execute_script("window.alert('填写表格已进入')")
                    # time.sleep(0.5)
                    # pt.hotkey('enter')
                    print("*" * 30)
                    print("填写表格已进入")
                    pt.hotkey('backspace')
                    execell_pro()
                if key == keyboard.Key.scroll_lock:
                    # chrome_options = Options()
                    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                    # chrome_driver = "/usr/local/bin/chromedriver"
                    # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
                    # current_window = driver.current_window_handle
                    # driver.switch_to.window(current_window)
                    # driver.execute_script("window.alert('已退出程序，感谢您的使用(*_*)')")
                    # time.sleep(0.5)
                    # pt.hotkey('enter')
                    print("-" * 30)
                    print("已退出程序，感谢您的使用(*_*)")
                    return False


            except AttributeError:
                print('special key {0} pressed'.format(
                    key))
            # 通过属性判断按键类型。

        def on_release(key):
            pass
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
    except:
        pass


def qidong():
    try:
        print("*" * 30)
        print("按下Pause进入程序")

        def on_press(key):
            '按下按键时执行。'

            try:
                if key == keyboard.Key.pause:
                    time.sleep(0.8)
                    # chrome_options = Options()
                    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                    # chrome_driver = "/usr/local/bin/chromedriver"
                    # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
                    # current_window = driver.current_window_handle
                    # driver.switch_to.window(current_window)
                    # driver.execute_script("window.alert('已进入程序，可以尝试快捷键进行操作啦(*_*)')")
                    # time.sleep(0.8)
                    # pt.hotkey('enter')
                    print("#" * 30)
                    print("已进入程序")
                    print("--6-看数据-，--7-发slack-,--8-填表格-")

                    huizong()


            except AttributeError:
                print('special key {0} pressed'.format(
                    key))
            # 通过属性判断按键类型。
        def on_release(key):
            pass
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
    except:
        pass


def execell_pro():
    # png = {"googleExe": {"imageIcon": "./image/google.png"}, "dingwei": {"imageIcon": "./image/img_8.png"},
    #        "time": {"imageIcon": "./image/img_9.png"}}
    # a = png.get("googleExe").get('imageIcon')
    # googleExe = ()  # 存储google坐标相关信息
    # googleExe = pt.locateOnScreen(png.get("googleExe").get('imageIcon'))
    # x = googleExe[0]
    # y = googleExe[1]
    # pt.moveTo(x, y, duration=0.5)  # 移动到google图标位置
    # pt.leftClick(x, y, duration=0.1)  # 点击google图标
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "/usr/local/bin/chromedriver"
    # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    s = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(options=chrome_options, service=s)
    driver.implicitly_wait(100)

    def on_press(key):
        '按下按键时执行。'

        # global driver
        try:
            # if key == keyboard.Key.pause:
            #     # chrome_options = Options()
            #     # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            #     # chrome_driver = "/usr/local/bin/chromedriver"
            #     driver = webdriver.Chrome(chrome_driver, options=chrome_options)
            #     current_window = driver.current_window_handle
            #     driver.switch_to.window(current_window)
            #     driver.execute_script("window.alert('填写表格已退出')")
            #     time.sleep(1.5)
            #     pt.hotkey('enter')
            #     pt.hotkey('backspace')
            #     print("*" * 30)
            #     print("填写表格已退出")
            #     return False
            if key == keyboard.Key.esc:
                # pt.typewrite("@")
                pc.copy("@pinyihu")
                pt.hotkey('ctrl', 'v')

            if key == keyboard.Key.f2:
                pt.hotkey('ctrl', 'v')
            if key == keyboard.Key.f8:
                # try:
                chrome_options = Options()
                chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                chrome_driver = "/usr/local/bin/chromedriver"
                # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
                s = Service("/usr/local/bin/chromedriver")
                driver = webdriver.Chrome(options=chrome_options, service=s)
                # driver.implicitly_wait(100)
                confluence_window = None
                handles_list = driver.window_handles
                print(driver.title)
                if "Confluence" not in driver.title:
                    for window in handles_list:
                        driver.switch_to.window(window)
                        if "Confluence" in driver.title:
                            confluence_window = window
                            break

                else:
                    main_windows = driver.current_window_handle
                    confluence_window = main_windows
                    driver.switch_to.window(confluence_window)
                # time.sleep(0.5)

                lis_head = driver.find_elements(By.XPATH, "//*[starts-with(text(),'Date')]")
                pt.hotkey('f11')
                # time.sleep(10)
                for li in lis_head:
                    action = ActionChains(driver)
                    action.scroll_to_element(li).perform()

                    slack_link = pc.paste()


                    re_compile = re.compile(r'Date:.{10}')
                    print(re_compile.findall(li.text)[0].replace("Date:2022/", "").strip())

                    ceshi_date = re_compile.findall(li.text)[0].replace("Date:2022/", "").strip()
                    # slack_re_compile = re.compile(r"link:.*")
                    # slack_link = slack_re_compile.findall(li.text)[0].replace("link:", "").strip()
                    lis_holetext = li.find_elements(By.XPATH, "./../../../p/a")
                    lis_holetext = li.find_elements(By.XPATH, "./../../../p")
                    index = 1
                    for p in lis_holetext:
                        if "@" not in p.text:
                            # time.sleep(0.5)
                            action = ActionChains(driver)
                            action.scroll_to_element(p).perform()
                            action.click(p).perform()
                            # time.sleep(0.5)
                            pt.hotkey('end')
                            # time.sleep(0.5)
                            pt.hotkey('shift', 'home')
                            # 复制
                            # time.sleep(0.3)
                            pt.hotkey('ctrl', 'c')
                            # 站到下一个格子 格子加一
                            print(index)
                            xpath = "//*[starts-with(text(),'Date')]/../../../../following-sibling::tr[{}]/td[2]".format(
                                index)
                            paste_loc = driver.find_element(By.XPATH, xpath)
                            # time.sleep(0.5)
                            action = ActionChains(driver)
                            action.scroll_to_element(paste_loc).perform()
                            action.click(paste_loc).perform()
                            pt.hotkey('ctrl', 'v')
                            jietu()
                            # 填写日期
                            # pt.hotkey('shift', 'tab')
                            xpath = "//*[starts-with(text(),'Date')]/../../../../following-sibling::tr[{}]/td[1]".format(
                                index)
                            huibaoren_element = driver.find_element(By.XPATH,xpath)
                            action = ActionChains(driver)
                            action.click(huibaoren_element).perform()
                            pc.copy("@pinyihu")
                            pt.hotkey('ctrl', 'v')
                            # pc.copy(ceshi_date)
                            # pt.hotkey('ctrl','v')
                            index += 1

                            # time.sleep(0.5)
                            # 回到原始位置
                            # 复制
                            #
                    for i in range(1, index):
                        print(index - i, "index")
                        xpath = "//*[starts-with(text(),'Date')]/../../../../following-sibling::tr[{}]/td[2]".format(
                            index - i)
                        paste_loc = driver.find_element(By.XPATH, xpath)

                        # 点击链接
                        paste_loc_click = paste_loc.find_element(By.XPATH, "./p/a")
                        paste_loc_click.click()
                        # 截图
                        element = driver.find_element(By.XPATH, "//*/span[@aria-label='Open link in a new tab']")
                        js = "arguments[0].click()"
                        driver.execute_script(js, element)
                        print(driver.title)
                        # 点击链接后重新获取handlelist
                        handles_list = driver.window_handles
                        if "xRay" not in driver.title:
                            for window in handles_list:
                                driver.switch_to.window(window)
                                if "xRay" in driver.title:
                                    # pen = driver.find_element(By.XPATH,
                                    #                           "/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[6]")
                                    time_element = WebDriverWait(driver, 100).until(
                                        lambda x: x.find_element(By.XPATH, "//*/div[2]/div[4]/p[1]"))
                                    break
                        print(driver.title)
                        # time.sleep(0.4)
                        pt.hotkey('r')
                        time.sleep(0.2)
                        pt.hotkey('v')
                        time.sleep(0.2)
                        pt.hotkey('v')
                        time.sleep(0.2)
                        pt.hotkey('v')
                        time.sleep(0.2)
                        pt.hotkey('ctrl', 'r')
                        time.sleep(0.2)
                        pt.hotkey('enter')
                        # 关闭窗口
                        driver.close()
                        # time.sleep(1)
                        # 关闭后切换回来confluence_window
                        print(confluence_window, "confluence_window")
                        driver.switch_to.window(confluence_window)
                        # break

                        # 复制粘贴截图
                        # time.sleep(0.8)

                        # pt.hotkey('tab')
                        # time.sleep(0.5)
                        xpath = "//*[starts-with(text(),'Date')]/../../../../following-sibling::tr[{}]/td[3]".format(
                            index - i)
                        tupian_element = driver.find_element(By.XPATH,xpath)
                        action = ActionChains(driver)
                        action.scroll_to_element(tupian_element).perform()
                        action.click(tupian_element).perform()

                        pt.hotkey('ctrl', 'v')
                        # time.sleep(0.8)
                        # pt.hotkey('right')
                        xpath = "//*[starts-with(text(),'Date')]/../../../../following-sibling::tr[{}]/td[4]".format(
                            index - i)
                        tupian_element = driver.find_element(By.XPATH, xpath)
                        action = ActionChains(driver)
                        action.scroll_to_element(tupian_element).perform()
                        action.click(tupian_element).perform()
                        pc.copy(slack_link)
                        pt.hotkey('ctrl', 'v')

                        i += 1
                    # 清空表格
                    source = driver.find_element(By.XPATH,
                                                 "//*[starts-with(text(),'Date')]/../../../following-sibling::td[1]")
                    target = driver.find_element(By.XPATH,
                                                 "//*[starts-with(text(),'Date')]/../../../preceding-sibling::td[1]")

                    actions = ActionChains(driver)
                    actions.drag_and_drop(source, target)
                    actions.perform()
                    pt.hotkey('backspace')
                    pt.hotkey('f11')
                    break
                # except:
                #     pass

            if key == keyboard.Key.f4:
                try:
                    chrome_options = Options()
                    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                    chrome_driver = "/usr/local/bin/chromedriver"
                    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
                    driver.implicitly_wait(100)
                    handles_list = driver.window_handles
                    print(driver.title)
                    if "Confluence" not in driver.title:
                        for window in handles_list:
                            driver.switch_to.window(window)
                            if "Confluence" in driver.title:
                                break
                    element = driver.find_element(By.XPATH, "//*/span[@aria-label='Open link in a new tab']")
                    js = "arguments[0].click()"
                    driver.execute_script(js, element)
                    print(driver.title)

                    handles_list = driver.window_handles
                    if "xRay" not in driver.title:
                        for window in handles_list:
                            driver.switch_to.window(window)
                            if "xRay" in driver.title:
                                # pen = driver.find_element(By.XPATH,
                                #                           "/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[6]")
                                time_element = WebDriverWait(driver, 100).until(lambda x: x.find_element(By.XPATH, "//*/div[2]/div[4]/p[1]"))
                                break
                    print(driver.title)
                    pt.hotkey('r')
                    time.sleep(0.3)
                    pt.hotkey('v')
                    time.sleep(0.3)
                    pt.hotkey('v')
                    time.sleep(0.3)
                    pt.hotkey('v')
                    time.sleep(0.3)
                    pt.hotkey('ctrl', 'r')
                    time.sleep(0.5)
                    pt.hotkey('enter')
                    handles_list = driver.window_handles
                    if "xRay" not in driver.title:
                        for window in handles_list:
                            driver.switch_to.window(window)
                            if "xRay" in driver.title:

                                break
                    driver.close()
                    handles_list = driver.window_handles
                    print(driver.title)
                    if "Confluence" not in driver.title:
                        for window in handles_list:
                            driver.switch_to.window(window)
                            if "Confluence" in driver.title:

                                break

                    pt.hotkey('tab')
                    pt.hotkey('ctrl', 'v')
                except:
                    pass
            if key == keyboard.Key.pause:
                # chrome_options = Options()
                # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                # chrome_driver = "/usr/local/bin/chromedriver"
                # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
                # current_window = driver.current_window_handle
                # driver.switch_to.window(current_window)
                # driver.execute_script("window.alert('填表格已退出')")
                # time.sleep(1.5)
                # pt.hotkey('enter')
                # pt.hotkey('backspace')
                print("*" * 30)
                print("填表格已退出")
                return False


        except AttributeError:
            print('special key {0} pressed'.format(
                key))
        # 通过属性判断按键类型。

    def on_release(key):
        pass

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    # check_date(vehicle='pacifica-cn-47', rtime='20220721')#已弃用Hmi

    # chaxunshuju(vehicle='pacifica-cn-37', rtime='20220914')
    # tag()
    # autoslack_pro() # 发报告_pro
    # tianbiaoge_pro()#表格填写_pro
    # huizong()
    qidong()
    execell_pro()
    # copy-module()#已弃用
    # semi_autoslack()#发报告
    # autoslack()#自动发报告
    # print(time.strftime('%Y/%m/%d', time.localtime()))
    # autoexcell()
    # cptool()
    # kuaijiejian()
    # tianbiaoge()






