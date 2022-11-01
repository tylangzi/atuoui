"""
#第一步：先关闭所有已经打开的chrome浏览器，然后运行脚本
#第二步：终端输入：chrome --remote-debugging-port=9222，然后打开网页版slack,和网页版的《Autox出车问题记录追踪表》
#第三步：鼠标悬停在要发送的消息头部空白区域，按下alt键，即可填写表格
"""
# import datetime
import pyautogui as pt
from pynput import keyboard
from selenium.webdriver import ActionChains, Keys
import re
import pyperclip as pc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pandas import Series,DataFrame
import pandas as pd
import time
def autocollection(driver,z_name):
    slack = "Slack"
    if slack not in driver.title:
        # 切换页面
        for window in driver.window_handles:
            driver.switch_to.window(window)
            if slack in driver.title:
                break
    js = "arguments[0].innerHTML='正在录入'"
    tishi_element = driver.find_element(By.XPATH,
                                        "/html/body/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div/div/button/span[1]")
    driver.execute_script(js, tishi_element)

    element = driver.execute_script("return window.hovered_element")


    data = []
    question_category = None  # 问题分类
    branch = None  # 分支
    slack_link = None  # slack链接
    anser_descrip = None  # 问题描述
    xray_link_time = None  # 问题发生时间
    scene = None  # 场景
    people = None  # 流转给哪位同学
    method = None  # 反馈的渠道
    xray_link = None  # xray链接
    module = None  # 所属模块
    level = None  # 等级
    zuzhang = None  # 组长
    commit = None  # commit
    ceshi_date = None  # 测试日期
    upload_people = None  # 发slack的同学
    after_morning = None #上下午

    # 获取问题分类
    question_category = 1  # AI问题
    # # 获取分支
    branch_re_compile = re.compile(r"Branch:.*")
    branch = branch_re_compile.findall(element.text)[0].replace("Branch:", "").strip()
    # print("Branch:",branch)
    # 获取commit
    commit_re_compile = re.compile(r"Commit:.{8}")
    commit = commit_re_compile.findall(element.text)[0].replace("Commit:", "").strip()
    # print("commit:",commit)
    # 获取日期
    re_compile = re.compile(r'Date:.{10}')
    print(re_compile.findall(element.text)[0].replace("Date:2022/", "").strip())
    ceshi_date = re_compile.findall(element.text)[0].replace("Date:2022/", "").strip()
    # 获取车辆
    vehicle_re_compile = re.compile(r"Vehicle:.*")
    vehicle = vehicle_re_compile.findall(element.text)[0].replace("Vehicle:", "").strip()
    # print("vehicle:",commit)
    # 获取slack链接
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
    # 获取处理人
    upload_people_element = None
    try:
        upload_people_element = element.find_element(By.XPATH, "./../../../../../../span")
    except Exception as e:
        print(e)
    if upload_people_element == None:
        try:
            upload_people_element = element.find_element(By.XPATH,
                                                         "./../../../../../../../div/div/span")
        except Exception as e:
            print(e)

    upload_people = upload_people_element.text.replace("[QA]", "").strip().split(" ")[-1]
    print("upload_people:", upload_people)
    # 获取流转给哪位同学
    at_people_element = element.find_element(By.XPATH, "./following-sibling::div")
    at_people_re_compile = re.compile(r"@.*")
    people = at_people_re_compile.findall(at_people_element.text)[0].replace("@", "").strip()
    # print("获取流转给哪位同学",people)
    # 填写组长名字
    zuzhang = z_name
    # 填写场景类型
    if people == "traffic_light_team":
        scene = "遇到红绿灯时"
    else:
        scene = "车辆正常运行移动"
    # print("场景",scene)

    # 获取所属模块
    module_element = element.find_element(By.XPATH, "./following-sibling::div/code")
    module = module_element.text
    print("模块名", module)
    body_element = None
    try:
        body_element = element.find_element(By.XPATH, "./following-sibling::div")
    except Exception as e:
        print(e)

    if body_element:
        # print(f"当前鼠标说在标签：{element.tag_name},其中文本内容：{element.text}")
        # print(element.find_element(By.XPATH,"./following-sibling::div").text)
        tags = body_element.find_elements(By.XPATH, "./a")
        body_text = body_element.text
        # print(body_text)
        for tag in tags:
            if tags.index(tag) == 0:
                continue
            # 获取反馈渠道
            if people in ("planning", "controls"):
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

            # 获取问题描述信息
            # try:
            #     body_element_re_compile = re.compile(r"{}\s+\(.*\)".format(tag.text))
            #     anser_descrip = body_element_re_compile.findall(body_text)[0].strip()
            # except Exception as e:
            #     # print(e)
            #     anser_descrip = tag.text
            # # print("问题描述",anser_descrip)
            #
            # # 如果匹配到了多个anser_descrip,就不取括号
            # try:
            #     is_none_anser_descrip = body_element_re_compile.findall(body_text)[1].strip()
            #     anser_descrip = tag.text
            # except Exception as e:
            #     print(e)
            # # print("tag.text",tag.text)
            anser_descrip = tag.text
            # 获取问题严重等级
            str = body_text
            re_compile = re.compile(r'\W\w{5}\s+\d{1}\W')
            level_list = re_compile.findall(str)
            body_list = re_compile.split(str)
            for i in body_list:
                if anser_descrip in i:
                    # print('##########')
                    # print('[%s]'%i)
                    anser_descrip_temp = i
                    break
            temp_index = body_list.index(anser_descrip_temp)
            level = level_list[temp_index - 1]
            print("level", level)

            # 获取问题xray链接
            xray_link = tag.get_attribute('href')
            # print(xray_link)
            #获取上下午
            time_re_compile = re.compile(r'\d{4}-.{14}')
            print(time_re_compile.findall(xray_link)[0][11:])
            if int(time_re_compile.findall(xray_link)[0][11:].split("-")[0].strip()) < 13:
                after_morning = "上午"
            else:
                after_morning = "下午"


            info_list = [ceshi_date,after_morning,branch, commit, vehicle, upload_people, anser_descrip, xray_link,
                         module, level]
            data.append(info_list)

        df = pd.DataFrame(data=data,
                          columns=["测试日期","时间段", "分支名", "commit", "车辆", "triager", "tag", "xray链接", "模块名",
                                   "所在等级"])

        df.to_csv('data.csv', mode="a+", header=False, index=False)
        js = "arguments[0].innerHTML='已录入'"
        tishi_element = driver.find_element(By.XPATH,
                                            "/html/body/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div/div/button/span[1]")
        driver.execute_script(js, tishi_element)

