"""
#第一步：先关闭所有已经打开的chrome浏览器，然后运行脚本
#第二步：终端输入：chrome --remote-debugging-port=9222，然后打开网页版slack,和网页版的《Autox出车问题记录追踪表》
#第三步：鼠标悬停在要发送的消息头部空白区域，按下alt键，即可填写表格
"""
# import datetime
import pyautogui as pt
from selenium.webdriver import ActionChains
import re
import pyperclip as pc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
def autocon1(driver,name):
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
    # pt.hotkey('f11')
    # time.sleep(10)
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
                    xpath1 = "//*[starts-with(text(),'Date')]/../../../../following-sibling::tr[{}]/td[1]".format(
                        index)
                    paste_loc1 = driver.find_element(By.XPATH, xpath1)
                    print("长度：",len(lis_holetext))
                    # 解决滑动问题
                    try:
                        if index % 3 == 0:
                            action = ActionChains(driver)
                            action.scroll_to_element(paste_loc1).click(paste_loc1).perform()
                    except Exception as e:
                        print(e)
                        xpath_before = "//*[starts-with(text(),'Date')]/../../../../following-sibling::tr[{}]/td[1]".format(
                            index - 1)
                        paste_loc1 = driver.find_element(By.XPATH, xpath_before)
                        try:
                            action = ActionChains(driver)
                            action.scroll_to_element(paste_loc1).click(paste_loc1).perform()
                        except Exception as e:
                            print(e)
                            xpath_before_before = "//*[starts-with(text(),'Date')]/../../../../following-sibling::tr[{}]/td[1]".format(
                                index - 2)
                            paste_loc1 = driver.find_element(By.XPATH, xpath_before_before)
                            action = ActionChains(driver)
                            action.scroll_to_element(paste_loc1).click(paste_loc1).perform()
                            paste_loc1 = driver.find_element(By.XPATH, xpath_before)
                            action.scroll_to_element(paste_loc1).click(paste_loc1).perform()

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

                genjin_people = "@ "+ name
                huibaoren_html = """<p><span contenteditable="false" id="617792abb9c549006fd4c154" text="" accesslevel="CONTAINER" usertype="null" class="mentionView-content-wrap inlineNodeView"><span class="inlineNodeViewAddZeroWidthSpace"></span>​<span data-mention-id="617792abb9c549006fd4c154" data-access-level="CONTAINER" spellcheck="false"><span spellcheck="false" class="css-19j4552">{0}</span></span><span class="inlineNodeViewAddZeroWidthSpace"></span></span>  {1} <span class="code" spellcheck="false">{2}</span></p>""".format(genjin_people,ceshi_date,commit_info)
                # huibaoren_html = """<p><span contenteditable="false" id="617792abb9c549006fd4c154" text="" accesslevel="CONTAINER" usertype="null" class="mentionView-content-wrap inlineNodeView"><span class="inlineNodeViewAddZeroWidthSpace"></span>​<span data-mention-id="617792abb9c549006fd4c154" data-access-level="CONTAINER" spellcheck="false"><span spellcheck="false" class="css-19j4552">{0}</span></span><span class="inlineNodeViewAddZeroWidthSpace"></span></span><span class="code" spellcheck="false"> </span></p>""".format(
                #     genjin_people)


                js = "arguments[0].innerHTML='" + huibaoren_html + "'"
                driver.execute_script(js, huibaoren_element)

                xpath = "//*[starts-with(text(),'Date')]/../../../../following-sibling::tr[{}]/td[2]".format(
                    index - i)
                paste_loc = driver.find_element(By.XPATH, xpath)

                # 获取链接url
                try:
                    paste_loc_click = paste_loc.find_element(By.XPATH, "./p/a")
                    url = paste_loc_click.get_attribute('href')
                    print('url', url)
                except Exception as e:
                    print(e)
                    continue
                #获取当前句柄
                current_handle = driver.current_window_handle
                # 打开链接
                last_handle = driver.window_handles[-1]
                driver.execute_script(f'window.open("{url}", "_blank");')
                if last_handle != driver.window_handles[-1]:
                    driver.switch_to.window(driver.window_handles[-1])
                    time_element = WebDriverWait(driver, 100).until(
                        lambda x: x.find_element(By.XPATH, "//*/div[2]/div[4]/p[1]"))
                else:
                    driver.switch_to.window(current_handle)
                    # 点击链接
                    try:
                        driver.switch_to.window(current_handle)
                        paste_loc_click = paste_loc.find_element(By.XPATH, "./p/a")
                        paste_loc_click.click()
                    except Exception as e:
                        print(e)
                        continue
                    try:
                        element = driver.find_element(By.XPATH, "//*/span[@aria-label='在新选项卡打开链接']")
                    except Exception as e:
                        print(e)
                        element = driver.find_element(By.XPATH,
                                                      "//*/span[@aria-label='Open link in a new tab']")
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
                # time.sleep(1)
                # 关闭后切换回来confluence_window
                print(confluence_window, "confluence_window")
                driver.switch_to.window(confluence_window)
                # break

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


        # except:
        #     pass
        else:
            pass

                