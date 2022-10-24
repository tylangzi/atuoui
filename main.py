
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




def main(z_name,my_name,port):
    print("#" * 30)
    print("已进入程序")
    print("--alt-填双表-，--F8-填二级表格-,--F2-发slack-")
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
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:{}".format(port))
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
        # zaitianyifen_element= WebDriverWait(driver, 1).until(lambda x: x.find_element(By.XPATH, '//*[contains(text(),"再填一份")]'))
        zaitianyifen_element = driver.find_element(By.XPATH,'//*[contains(text(),"再填一份")]')
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
    js = "arguments[0].innerHTML='alt双表-F8二级表-F2slack-'"
    tishi_element =driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div/div/button/span[1]")
    driver.execute_script(js,tishi_element)

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
                slack = "Slack"
                if slack not in driver.title:
                    # 切换页面
                    for window in driver.window_handles:
                        driver.switch_to.window(window)
                        if slack in driver.title:
                            break
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
                commit_info = commit_re_compile.findall(element.text)[0].replace("Commit:", "").strip()
                c_info = commit_info
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
            if key == keyboard.Key.f8:
                # chrome_options = Options()
                # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                chrome_driver = "/usr/local/bin/chromedriver"
                # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
                # s = Service("/usr/local/bin/chromedriver")
                # driver = webdriver.Chrome(options=chrome_options, service=s)
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
                lis_head = driver.find_elements(By.XPATH, "//*[starts-with(text(),'Date')]")
                for li in lis_head:
                    if lis_head.index(li) == 0:
                        action = ActionChains(driver)
                        action.scroll_to_element(li).perform()
                        slack_link = pc.paste()

                        # 获取commit
                        commit_re_compile = re.compile(r"Commit:.{8}")
                        commit_info = commit_re_compile.findall(li.text)[0].replace("Commit:", "").strip()
                        # print("commit:",commit)

                        re_compile = re.compile(r'Date:.{10}')
                        print(re_compile.findall(li.text)[0].replace("Date:2022/", "").strip())
                        ceshi_date = re_compile.findall(li.text)[0].replace("Date:2022/", "").strip()
                        # slack_re_compile = re.compile(r"link:.*")
                        # slack_link = slack_re_compile.findall(li.text)[0].replace("link:", "").strip()
                        body_element = li.find_element(By.XPATH, "./../../..")
                        lis_holetext = li.find_elements(By.XPATH, "./../../../p")
                        index = 1
                        for p in lis_holetext:
                            if "@" not in p.text:
                                # print(p.text)
                                # 获取问题描述信息
                                try:
                                    body_element_re_compile = re.compile(r"{}\s+\(.*\)".format(p.text))
                                    anser_descrip = body_element_re_compile.findall(body_element.text)[0].strip()
                                except Exception as e:
                                    print(e)
                                    anser_descrip = p.text
                                # print("问题描述",anser_descrip)

                                # 如果匹配到了多个anser_descrip,就不取括号
                                try:
                                    is_none_anser_descrip = body_element_re_compile.findall(body_element.text)[1].strip()
                                    anser_descrip = p.text
                                except Exception as e:
                                    print(e)
                                    # print("p.text", anser_descrip)

                                # 获取问题xray链接
                                xray_link = p.get_attribute('href')
                                # print("xray链接：",xray_link)

                                xpath = "//*[starts-with(text(),'Date')]/../../../../following-sibling::tr[{}]/td[2]".format(
                                    index)
                                paste_loc = driver.find_element(By.XPATH, xpath)
                                print("长度：",len(lis_holetext))
                                action = ActionChains(driver)
                                action.scroll_to_element(paste_loc).click(paste_loc).perform()
                                html = p.get_attribute("outerHTML")
                                re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
                                try:
                                    level_info = re_compile.findall(html)[0].strip()
                                    after_html = html.replace(level_info, "")
                                except Exception as e:
                                    after_html = html
                                    # 解决链接缺失超链接问题
                                if "</a></p>" in after_html:
                                    after_html = after_html.replace("</a></p>", "</a> </p>")
                                elif "</a><br></p>" in after_html:
                                    after_html = after_html.replace("</a><br></p>", "</a> </p>")
                                # print("#############")
                                # print("html:元素代码", after_html)
                                # print("#############")
                                js = "arguments[0].innerHTML='" + after_html + "'"
                                driver.execute_script(js, paste_loc)

                                index += 1


                            else:
                                pass

                        for i in range(1, index):
                            xpath = "//*[starts-with(text(),'Date')]/../../../../following-sibling::tr[{}]/td[1]".format(
                                index - i)
                            huibaoren_element = driver.find_element(By.XPATH, xpath)

                            genjin_people = "@ "+ my_name
                            # huibaoren_html = """<p><span contenteditable="false" id="617792abb9c549006fd4c154" text="" accesslevel="CONTAINER" usertype="null" class="mentionView-content-wrap inlineNodeView"><span class="inlineNodeViewAddZeroWidthSpace"></span>​<span data-mention-id="617792abb9c549006fd4c154" data-access-level="CONTAINER" spellcheck="false"><span spellcheck="false" class="css-19j4552">{0}</span></span><span class="inlineNodeViewAddZeroWidthSpace"></span></span>  {1} <span class="code" spellcheck="false">{2}</span></p>""".format(genjin_people,ceshi_date,commit_info)
                            huibaoren_html = """<p><span contenteditable="false" id="617792abb9c549006fd4c154" text="" accesslevel="CONTAINER" usertype="null" class="mentionView-content-wrap inlineNodeView"><span class="inlineNodeViewAddZeroWidthSpace"></span>​<span data-mention-id="617792abb9c549006fd4c154" data-access-level="CONTAINER" spellcheck="false"><span spellcheck="false" class="css-19j4552">{0}</span></span><span class="inlineNodeViewAddZeroWidthSpace"></span></span><span class="code" spellcheck="false"> </span></p>""".format(
                                genjin_people)


                            js = "arguments[0].innerHTML='" + huibaoren_html + "'"
                            driver.execute_script(js, huibaoren_element)

                            xpath = "//*[starts-with(text(),'Date')]/../../../../following-sibling::tr[{}]/td[2]".format(
                                index - i)
                            paste_loc = driver.find_element(By.XPATH, xpath)


                            #获取链接url
                            try:
                                paste_loc_click = paste_loc.find_element(By.XPATH, "./p/a")
                                url = paste_loc_click.get_attribute('href')
                                # print('url',url)
                            except Exception as e:
                                print(e)
                                continue

                            #打开链接
                            driver.execute_script(f'window.open("{url}", "_blank");')
                            # 切换到新的标签页
                            driver.switch_to.window(driver.window_handles[-1])
                            time_element = WebDriverWait(driver, 100).until(
                                                lambda x: x.find_element(By.XPATH, "//*/div[2]/div[4]/p[1]"))

                            # print(driver.title)
                            pt.hotkey('r')
                            time.sleep(0.1)
                            pt.hotkey('v')
                            time.sleep(0.1)
                            pt.hotkey('v')
                            time.sleep(0.1)
                            pt.hotkey('v')
                            time.sleep(0.1)
                            pt.hotkey('ctrl', 'r')
                            time.sleep(0.1)
                            pt.hotkey('enter')
                            # 关闭窗口
                            driver.close()
                            # 关闭后切换回来confluence_window
                            print(confluence_window, "confluence_window")
                            driver.switch_to.window(confluence_window)

                            # 复制粘贴截图
                            xpath = "//*[starts-with(text(),'Date')]/../../../../following-sibling::tr[{}]/td[3]".format(
                                index - i)
                            tupian_element = driver.find_element(By.XPATH, xpath)
                            action = ActionChains(driver)
                            action.scroll_to_element(tupian_element).perform()
                            action.click(tupian_element).perform()
                            pt.hotkey('ctrl', 'v')
                            ispicture_element = WebDriverWait(tupian_element, 100).until(
                                            lambda x: x.find_element(By.XPATH, "./div"))

                            xpath = "//*[starts-with(text(),'Date')]/../../../../following-sibling::tr[{}]/td[4]".format(
                                index - i)
                            slack_element = driver.find_element(By.XPATH, xpath)
                            action = ActionChains(driver)
                            action.scroll_to_element(slack_element).perform()
                            action.click(slack_element).perform()
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

                    else:
                        pass

            if key == keyboard.Key.f2:
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
                    "road_test_shenzhen": {"Planning": "Planning", "System": "System", "Routing": "Routing",
                                           "XView": "XView",
                                           "lidar": "lidar", "Control": "Control"},
                    "road_test_prediction": {"Prediction": "Prediction"},
                    "road_test_perception": {"Perception": "Perception"},
                    "road_test_deeplearning": {"Perception": "Perception",
                                               "Perception Scenario": "Perception Scenario"},
                    "road_test_traffic_light": {"Perception": "Perception"}}

                report = driver.find_element(By.XPATH, "//*/div[@class='ql-editor']")
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
                    road_test_shenzhen = driver.find_element(By.XPATH,
                                                             "//*[contains(text(),'" + channel + "') and @ dir='auto']")
                    js = 'arguments[0].click()'
                    driver.execute_script(js, road_test_shenzhen)
                    # 添加report
                    js = "arguments[0].innerHTML='" + report_html + "'"
                    driver.execute_script(js, report)
                    title_names = {"road_test_perception": "Perception", "road_test_deeplearning": "Deeplearning",
                                   "road_test_traffic_light": "Traffic light"}
                    remove_text = {
                        "Perception": ["Traffic Light", "Frustum", "Connected Components", "Point Pillars",
                                       "Occupancy Grid",
                                       "Traffic Cone", "Special Object", "Mask RCNN"],
                        "Deeplearning": ["Connected Components", "Frustum", "Point Pillars", "Traffic Cone",
                                         "Occupancy Grid",
                                         "Special Object", "Mask RCNN", "Water Raindrop"],
                        "Traffic light": ["Traffic Light"]}
                    nothing_flag = False
                    # 删除前后内容
                    # 装列表
                    next_flag = False  # deeplearning、traffic light,perception是否进行后续操作
                    for value in channels[channel].values():
                        print("value:", value)
                        text_lis_body = []
                        able_text_lis_body = []
                        flag = False
                        lis_body = driver.find_elements(By.XPATH, "//*/div[@class='ql-editor']/p")
                        lis_tou = driver.find_elements(By.XPATH, "//*/div[@class='ql-editor']/div")

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
                            lis_body = driver.find_elements(By.XPATH, "//*/div[@class='ql-editor']/p")
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
                                pt.hotkey('enter')

                            if channel not in title_names.keys():
                                time.sleep(2)
                                # 删除后再次添加report
                                js = "arguments[0].innerHTML='" + report_html + "'"
                                driver.execute_script(js, report)

                            time.sleep(1)
                            if channel in title_names.keys() and next_flag:
                                if value != "Perception Scenario":
                                    # 修改模块名
                                    lis_body = driver.find_elements(By.XPATH, "//*/div[@class='ql-editor']/p")
                                    title_text_node = lis_body[0].find_element(By.XPATH, "./code/strong")
                                    js = "arguments[0].innerText='" + title_names[channel] + "'"
                                    driver.execute_script(js, title_text_node)

                                # 删除不需要的内容
                                # 加载所有文本值到字典data_body中
                                data_body = {}
                                lis_body = driver.find_elements(By.XPATH, "//*/div[@class='ql-editor']/p")
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
                                lis_body = driver.find_elements(By.XPATH, "//*/div[@class='ql-editor']/p")
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
                                lis_body = driver.find_elements(By.XPATH, "//*/div[@class='ql-editor']/p")
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
                                lis_body = driver.find_elements(By.XPATH, "//*/div[@class='ql-editor']/p")
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
                                    pt.hotkey('enter')
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

def name_config():
    try:
        with open("name_config.txt",'r') as f:
            for line in f.readlines():
                print(line.strip())
                line = line.split(" ")
                return line[0],line[1],line[2]
    except:
        print("请输入组长的名字")
        z_name = input()
        print("请输入你名字")
        my_name = input()
        print("请输入你浏览器的端口号，建议为9222")
        port = input()
        with open("name_config.txt",'w') as f:
            f.writelines([z_name," ",my_name," ",port])
        return z_name,my_name,port



            # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    z_name,my_name,port =name_config()
    main(z_name,my_name,port)





