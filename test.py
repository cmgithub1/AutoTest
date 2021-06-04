import time

from selenium import webdriver

option = webdriver.ChromeOptions()
option.binary_location=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
driver = webdriver.Chrome()    # Chrome浏览器

#访问百度首页
first_url= 'https://www.9ji.com/'
print("now access %s" %(first_url))
driver.get(first_url)

#访问新闻页面
second_url='https://www.9ji.com/bargain/'
print("now access %s" %(second_url))
driver.get(second_url)

#返回（后退）到百度首页
print("back to  %s "%(first_url))
driver.back()

#前进到新闻页
print("forward to  %s"%(second_url))
driver.forward()

# 参数数字为像素点
print("设置浏览器宽480、高800显示")
driver.set_window_size(480, 800)

driver.refresh() #刷新当前页面
# driver.quit()

#输入
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()


