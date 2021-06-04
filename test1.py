from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10) #等待的最大时间
url = 'http://www.baidu.com?tn=baiduhome'
browser.get(url)
try:
    # 获取输入框
    input = wait.until(
        #判断该元素是否加载完成
        EC.presence_of_element_located((By.CSS_SELECTOR, '#kw'))
    )
    # 输入查询关键字
    input.send_keys("python")

    # 获取搜索点击按钮
    submit = wait.until(
        #判断该元素是否可以点击
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#su'))
    )
    submit.click()
except TimeoutException:
    print('exception')