# Test Case Description
# 1. Open the browser
# 2. Go to python.org
# 3. Web page title cointains word python

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://python.org')

assert 'python' in driver.title.lower()
driver.close()