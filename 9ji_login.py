from _ast import arguments

from selenium import webdriver
import time
import random

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

option = webdriver.ChromeOptions()
option.binary_location=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
driver = webdriver.Chrome()    # Chrome浏览器

#访问百度首页
# first_url= 'https://www.dev.9ji.com/'
first_url= 'https://www.9ji.com/'
# print("now access dev %s" %(first_url))
print("Attention!!! now access product %s" %(first_url))
driver.get(first_url)

#等待选区弹框加载出来
time.sleep(1)

#随机选择地区
# driver.find_element_by_id('530102').click()
# print(driver.find_element_by_class_name('city-item'))
#0:昆明市区
#1:安宁市
#2:呈贡区
#3:嵩明县
#4:寻甸县
#5:东川区
#6:晋宁区
#7:宜良县
#8:禄劝县
#9:石林县
#10:富民县
random_district=random.randint(0, 10)
print(random_district)
driver.find_elements_by_class_name('city-item')[random_district].click()

#点击登录
driver.find_elements_by_class_name('mr-5')[1].click()
#等待登录页面跳转
time.sleep(1)


#点击”账户登录“
# ActionChains(driver).move_to_element(driver.find_element_by_link_text("账户登录")).perform()
# down_data_click = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[2]/div/div/div/div[1]/a[2]"))
# )
# time.sleep(2)
# down_data_click.click()
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div/div/div[1]/a[2]").click()

#输入登录用户名
driver.find_elements_by_class_name("login-input")[0].clear()
driver.find_elements_by_class_name("login-input")[0].send_keys("14095279999")
#输入登录密码
driver.find_elements_by_class_name("login-input")[1].clear()
driver.find_elements_by_class_name("login-input")[1].send_keys("0721")
#点击登录
driver.find_element_by_class_name('login-button').click()
time.sleep(2)

#点击旧机回收，进入回收首页
driver.find_element_by_link_text("旧机回收").click()
time.sleep(2)

#随机选择一款热门机型
# //*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div[1]/a[1]
# //*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div[1]/a[2]
# //*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div[1]/a[3]
# //*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div[1]/a[15]



# driver.execute_script("arguments[0].scrollIntoView();", target) #拖动到可见的元素去
# # 向下滚动200个像素
# driver.execute_script('window.scrollBy(0,1000)')
# time.sleep(2)
#循环页面句柄，获取非主页句柄，只适用于2个页面窗口的情况下
#driver切换到回收首页
toHandle = driver.window_handles
driver.switch_to.window(toHandle[1])
#下滑页面到热销商品元素能加载出来的地方
page = driver.find_element_by_tag_name('body')
page.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
#随机选取一个热销商品并点击
random_opular_models=random.randint(1, 15)
random_opular_models_xpath="//*[@id='app']/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div[1]/a[" + str(random_opular_models)+']'
print("选取的热销商品xpath： "+ random_opular_models_xpath)
driver.find_element_by_xpath(random_opular_models_xpath).click()
#切换到热销商品估价页面
toHandle = driver.window_handles
driver.switch_to.window(toHandle[2])

#网络制式选择





