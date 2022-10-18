echo '浏览器版本：'
google-chrome --version
echo 'selenium版本：'
pip list |grep selenium
echo '正在打开浏览器：'
chrome --remote-debugging-port=9222 --user-data-dir="/home/pinyihu/dechrome/Default"
python3 main.py
