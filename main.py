
"""
#第一步：先关闭所有已经打开的chrome浏览器，然后运行脚本
#第二步：终端输入：chrome --remote-debugging-port=9222，然后打开网页版slack,和网页版的《Autox出车问题记录追踪表》
#第三步：鼠标悬停在要发送的消息头部空白区域，按下alt键，即可填写表格
"""
# import datetime
from _curses import getmouse
import time
import pyautogui as pt
import pyperclip as pc
import re
import subprocess as sub
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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import  expected_conditions as EC




def main(z_name):
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
    # 切换到AutoX出车问题记录
    for window in driver.window_handles:
        driver.switch_to.window(window)
        if "AutoX出车问题记录" in driver.title or "倒计时" in driver.title:
            print("&&&&")
            print(driver.title)
            print("&&&&")
            break
    try:
        zaitianyifen_element= WebDriverWait(driver, 1).until(lambda x: x.find_element(By.XPATH, '//*[contains(text(),"再填一份")]'))
        action = ActionChains(driver)
        action.click(zaitianyifen_element).perform()
    except Exception as e:
        print(e)
    # time.sleep(1)



    #切换页面
    slack = "Slack"
    for window in driver.window_handles:
        driver.switch_to.window(window)
        if slack in driver.title:
            break

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
    def on_press(key):
        '按下按键时执行。'

        try:
            if key == keyboard.Key.alt:
                question_category = None  #问题分类
                branch = None #分支
                slack_link = None#slack链接
                anser_descrip = None#问题描述
                xray_link_time = None #问题发生时间
                scene = None #场景
                people = None#流转给哪位同学
                method = None#反馈的渠道
                xray_link = None#xray链接
                module = None#所属模块
                level = None#等级
                zuzhang = None#组长
                commit = None #commit

                #获取问题分类
                question_category = 1 #AI问题
                #获取分支
                element = driver.execute_script("return window.hovered_element")
                branch_re_compile = re.compile(r"Branch:.*")
                branch = branch_re_compile.findall(element.text)[0].replace("Branch:", "").strip()
                # print("Branch:",branch)
                #获取commit
                commit_re_compile = re.compile(r"Commit:.{8}")
                commit = commit_re_compile.findall(element.text)[0].replace("Commit:", "").strip()
                # print("commit:",commit)
                #获取slack链接
                slack_link_element = None
                try:
                    slack_link_element = element.find_element(By.XPATH, "./../../../../../../a")
                    # slack_link_element = WebDriverWait(element,0.3).until(lambda x:x.find_element(By.XPATH, "./../../../../../../a"))
                except Exception as e:
                    print(e)
                if slack_link_element == None:
                    try:
                        slack_link_element = element.find_element(By.XPATH, "./../../../../../../../div/div/a")
                    except Exception as e:
                        print(e)

                slack_link = slack_link_element.get_attribute("href")
                # print("slackL链接:",slack_link)
                #获取流转给哪位同学
                at_people_element = element.find_element(By.XPATH, "./following-sibling::div")
                at_people_re_compile = re.compile(r"@.*")
                people = at_people_re_compile.findall(at_people_element.text)[0].replace("@", "").strip()
                # print("获取流转给哪位同学",people)
                #填写组长名字
                zuzhang = z_name
                #填写场景类型
                if people == "traffic_light_team":
                    scene = "遇到红绿灯时"
                else:
                    scene = "车辆正常运行移动"
                print("场景",scene)

                #获取所属模块
                module_element = element.find_element(By.XPATH, "./following-sibling::div/code")
                module =module_element.text
                print("模块名",module)
                body_element = None
                try:
                    body_element = element.find_element(By.XPATH, "./following-sibling::div")
                except Exception as e:
                    print(e)

                if body_element:
                    # print(f"当前鼠标说在标签：{element.tag_name},其中文本内容：{element.text}")
                    # print(element.find_element(By.XPATH,"./following-sibling::div").text)
                    tags = body_element.find_elements(By.XPATH,"./a")
                    body_text = body_element.text
                    print(body_text)
                    for tag in tags:
                        if tags.index(tag) == 0:
                            continue
                        # 获取反馈渠道
                        if people in ("planning","controls"):
                            method = "road_test_shenzhen"
                        elif people in ("prediction"):
                            method = "road_test_prediction"
                        elif people in ("perception_triage"):
                            method = "road_test_perception"
                        elif people in ("deeplearning"):
                            method = "road_test_deeplearning"
                        elif people in ("traffic_light_team"):
                            method = "road_test_traffic_light"
                        else:
                            method = "slack"
                        # print("tag_text",tag.text)

                        #获取问题描述信息
                        try:
                            body_element_re_compile = re.compile(r"{}\s+\(.*\)".format(tag.text))
                            anser_descrip = body_element_re_compile.findall(body_text)[0].strip()
                        except Exception as e:
                            print(e)
                            anser_descrip = tag.text
                        # print("问题描述",anser_descrip)

                        #如果匹配到了多个anser_descrip,就不取括号
                        try:
                            is_none_anser_descrip = body_element_re_compile.findall(body_text)[1].strip()
                            anser_descrip = tag.text
                        except Exception as e:
                            print(e)
                        print("tag.text",tag.text)

                        # 获取问题严重等级
                        str = body_text
                        re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                        level_list = re_compile.findall(str)
                        body_list = re_compile.split(str)
                        for i in body_list:
                            if anser_descrip in i:
                                anser_descrip_temp = i
                                break
                        temp_index = body_list.index(anser_descrip_temp)
                        level = level_list[temp_index-1]
                        # print("level",level)

                        #获取问题xray链接
                        xray_link = tag.get_attribute('href')
                        # print(xray_link)
                        #点击链接，进入xray,获取时间
                        action = ActionChains(driver)
                        action.click(tag).perform()
                        #切换到新打开的xray窗口
                        handles_list = driver.window_handles
                        if "xRay" not in driver.title:
                            for window in handles_list:
                                driver.switch_to.window(window)
                                # print("driver.title",driver.title)
                                if "xRay" in driver.title:
                                    print("title",driver.title)
                                    # pen = driver.find_element_by_xpath(
                                    #     "/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[6]")
                                    time_element = WebDriverWait(driver, 100).until(lambda x: x.find_element(By.XPATH,"//*/div[2]/div[4]/p[1]"))
                                    #获取xray_link的时间
                                    xray_link_time = time_element.text
                                    # print("time:",xray_link_time)
                                    driver.close()
                                    break
                        #切换到AutoX出车问题记录
                        for window in driver.window_handles:
                            driver.switch_to.window(window)
                            if "AutoX出车问题记录" in driver.title or "倒计时" in driver.title:
                                print("&&&&")
                                print(driver.title)
                                print("&&&&")
                                break
                        #01问题分类
                        quest_00 = driver.find_element(By.XPATH,"//*/div[@class='question'][1]//div/div[2]/div[2]/div/div[1]/div[1]")
                        action = ActionChains(driver)
                        action.click(quest_00).perform()
                        # question_elements = driver.find_elements(By.XPATH,"//*/div[@class='question']/div[1]")
                        ec = EC.visibility_of_any_elements_located((By.XPATH, "//*/div[@class='question']"))
                        question_elements = ec(driver)
                        for question_element in question_elements:
                            index = question_elements.index(question_element)
                            #移动到可见位置
                            action = ActionChains(driver)
                            action.scroll_to_element(question_element).perform()
                            print("index ",question_elements.index(question_element))
                            if index == 1:#04AI问题
                                if module in ("Planning","Control","Routing"):
                                    i = 2
                                elif module in ("Localization"):
                                    i = 3
                                else:
                                    i = 1
                                quest_01 = question_element.find_element(By.XPATH,"./div/div[2]/div[2]/div/div[{}]/div[1]".format(i))
                                action = ActionChains(driver)
                                action.click(quest_01).perform()
                            elif index == 2:#08具体问题内容
                                quest_02 = question_element.find_element(By.XPATH,"./div/div[2]/div[2]/div/div[1]")
                                action = ActionChains(driver)
                                action.click(quest_02).perform()
                                pc.copy(anser_descrip)
                                pt.hotkey('ctrl','v')
                            elif index == 3:#09问题发生时间
                                quest_03 = question_element.find_element(By.XPATH,"./div/div[2]/div[3]/div/div[1]")
                                action = ActionChains(driver)
                                action.click(quest_03).perform()
                                pc.copy(xray_link_time)
                                pt.hotkey('ctrl', 'v')
                            elif index == 4:#10场景（描述具体场景）
                                quest_04 = question_element.find_element(By.XPATH,"./div/div[2]/div[3]/div/div[1]")
                                action = ActionChains(driver)
                                action.click(quest_04).perform()
                                pc.copy(scene)
                                pt.hotkey('ctrl', 'v')
                            elif index == 5:#11 分支名
                                quest_05 = question_element.find_element(By.XPATH,"./div/div[2]/div[3]/div/div[1]")
                                action = ActionChains(driver)
                                action.click(quest_05).perform()
                                pc.copy(branch)
                                pt.hotkey('ctrl', 'v')
                            elif index == 6:#12 【必填】问题xray link / log/ 记录文件link
                                quest_06 = question_element.find_element(By.XPATH,"./div/div[2]/div[3]/div/div[1]")
                                action = ActionChains(driver)
                                action.click(quest_06).perform()
                                pc.copy(xray_link)
                                pt.hotkey('ctrl', 'v')
                            elif index == 7:#13 此问题流转给哪位同学进行处理(人名)
                                quest_07 = question_element.find_element(By.XPATH,"./div/div[2]/div[3]/div/div[1]")
                                action = ActionChains(driver)
                                action.click(quest_07).perform()
                                pc.copy(people)
                                pt.hotkey('ctrl', 'v')
                            elif index == 8:#13 此问题流转给哪位同学进行处理(人名)
                                quest_08 = question_element.find_element(By.XPATH,"./div/div[2]/div[3]/div/div[1]")
                                action = ActionChains(driver)
                                action.click(quest_08).perform()
                                pc.copy(method)
                                pt.hotkey('ctrl', 'v')
                            elif index == 10:#16组长姓名
                                quest_10 = question_element.find_element(By.XPATH,"./div/div[2]/div[3]/div/div[1]")
                                action = ActionChains(driver)
                                action.click(quest_10).perform()
                                pc.copy(zuzhang)
                                pt.hotkey('ctrl', 'v')
                            elif index == 9:#15影响程度
                                if level in ("【Level 4】","【Level 3】"):
                                    i = 2
                                elif level == "【Level 5】":
                                    i = 1
                                print("i值",i)
                                quest_09 = question_element.find_element(By.XPATH,"./div/div[2]/div[2]/div/div[{}]".format(i))#2  严重影响体感 L4/L3
                                action = ActionChains(driver)
                                action.click(quest_09).perform()
                                pc.copy(slack_link)
                                pt.hotkey('ctrl', 'v')
                            elif index == 12:#18 slack链接
                                quest_12 = question_element.find_element(By.XPATH,"./div/div[2]/div[3]/div/div[1]")
                                action = ActionChains(driver)
                                action.click(quest_12).perform()
                                pc.copy(slack_link)
                                pt.hotkey('ctrl', 'v')
                            print(question_element.text)
                        jishi_element = driver.find_element(By.XPATH,"//*/div[3]/input")
                        import random
                        time1 = random.randint(60,150)

                        for i in range(1, time1):
                            print('剩余时间：%s' % (time1 - i))
                            js = "arguments[0].value = '倒计时:{}'".format(time1-i)
                            driver.execute_script(js,jishi_element)
                            time.sleep(1)
                        # input()
                        tijiao = driver.find_element(By.XPATH, "//*[contains(text(),'提交')]")
                        tijiao.click()
                        querentijiao = driver.find_element(By.XPATH,"//*/button[2]")
                        querentijiao.click()
                        #点击再填一份
                        zaitanyifen = WebDriverWait(driver, 100).until(lambda x: x.find_element(By.XPATH,"//*[contains(text(),'再填一份')]"))
                        action = ActionChains(driver)
                        action.click(zaitanyifen).perform()
                        # 点击再填写一份
                        zaitanyifen = WebDriverWait(driver, 100).until(lambda x: x.find_element(By.XPATH, "//*[contains(text(),'再填写一份')]"))
                        action = ActionChains(driver)
                        action.click(zaitanyifen).perform()
                        # driver.refresh()
                        #切换到slak页面
                        slack = "Slack"
                        for window in driver.window_handles:
                            driver.switch_to.window(window)
                            if slack in driver.title:
                                break

                        # break







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




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    z_name = "刘永欢"
    # z_name = "莫世林"
    main(z_name)





