import pyautogui as pt
from selenium.webdriver import ActionChains
import re
import pyperclip as pc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
def autoslack1(driver):
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