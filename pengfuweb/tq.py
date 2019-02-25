from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests,json
chrome_options = Options()
chrome_options.add_argument("--headless")

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",'content-type':'application/json'}

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.baidu.com')
elem = driver.find_element_by_name("wd") # 找到输入框的元素
elem.clear() # 清空输入框里的内容
elem.send_keys(u"天气深圳") # 在输入框中输入'Kali Linux'
elem.send_keys(Keys.RETURN) # 在输入框中输入回车键
driver.implicitly_wait(10) # 隐式等待
tqtoday = driver.find_element_by_css_selector('.op_weather4_twoicon_today')
tqelemtitle = driver.find_element_by_css_selector('.c-gap-bottom-small a').text
time = tqtoday.find_element_by_css_selector('.op_weather4_twoicon_date').text
wd = tqtoday.find_element_by_css_selector('.op_weather4_twoicon_temp').text
weath = tqtoday.find_element_by_css_selector('.op_weather4_twoicon_weath').text
wind = tqtoday.find_element_by_css_selector('.op_weather4_twoicon_wind').text


data = { "msgtype": "text",
          "text": {
         "content": tqelemtitle+'\n'+time+'\n'+wd+'\n'+weath+'\n'+wind
            },
         }
url = 'https://oapi.dingtalk.com/robot/send?access_token=684d740d4e1cf126eb24632a8c9d46591f517a4cdf1ea4176a5a4c01ce4f705e'
res = requests.post(url,data=json.dumps(data),headers=headers)
