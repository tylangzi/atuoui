
"""
#第一步：先关闭所有已经打开的chrome浏览器，然后运行脚本
#第二步：终端输入：chrome --remote-debugging-port=9222，然后打开网页版slack,和网页版的《Autox出车问题记录追踪表》
#第三步：鼠标悬停在要发送的消息头部空白区域，按下alt键，即可填写表格
"""
# import datetime
from _curses import getmouse
import pyautogui as pt
import pyperclip as pc
import subprocess as sub
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
from selenium.webdriver.chrome.service import Service
from pynput import keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import  expected_conditions as EC
import autocon
import autowx
import autoslack
def init(port):
    print("#" * 30)
    print("已进入程序")
    print("--alt-填双表-，--F8-填二级表格-,--F2-发slack-")
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:{}".format(port))
    chrome_driver = "/usr/local/bin/chromedriver"
    # driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    s = Service(chrome_driver)
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
        pass
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
    return driver


def main(z_name,name,port):
    driver=init(port)#chushihua


    def on_press(key):
        '按下按键时执行。'

        
        try:
            if key == keyboard.Key.alt:
                autowx.autowx1(driver,z_name)

                        # break
            if key == keyboard.Key.f8:
                autocon.autocon1(driver,name)
                # except:
                #     pass

            if key == keyboard.Key.f2:
                autoslack.autoslack1(driver)
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
    z_name,name,port=name_config()
    # z_name = "莫世林"
    main(z_name,name,port)





