import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

current_directory  = os.getcwd()

driver_path = os.path.join(current_directory, 'chromedriver.exe')

# 创建一个 Options 对象
options = Options()


options.binary_location = driver_path

options.add_argument('--headless')

# 创建一个 WebDriver 实例
driver = webdriver.Chrome(options=options)

# 访问一个网页
driver.get('http://www.example.com')

# 获取网页的源代码
html = driver.page_source

# 打印网页源代码
print(html)

# 关闭 WebDriver 实例
driver.quit()