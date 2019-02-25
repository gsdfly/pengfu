import requests,json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument("--headless")       # define headless
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Firefox()
driver.get('https://tianqi.qq.com/')
# data= {
#     "actionCard": {
#         "title": "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身",
#         "text": "![screenshot](@lADOpwk3K80C0M0FoA) \n\n #### 乔布斯 20 年前想打造的苹果咖啡厅 \n\n Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划",
#         "hideAvatar": "0",
#         "btnOrientation": "0",
#         "btns": [
#             {
#                 "title": "内容不错",
#                 "actionURL": "https://www.dingtalk.com/"
#             },
#             {
#                 "title": "不感兴趣",
#                 "actionURL": "https://www.dingtalk.com/"
#             }
#         ]
#     },
#     "msgtype": "actionCard"
# }
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",'content-type':'application/json'}

# res = requests.post('https://oapi.dingtalk.com/robot/send?access_token=684d740d4e1cf126eb24632a8c9d46591f517a4cdf1ea4176a5a4c01ce4f705e',data=json.dumps(data),headers=headers)
# print(res.content)


# res = requests.get('https://tianqi.qq.com/',headers=headers)
# print(res.content.decode('gbk'))