from selenium import webdriver

"""
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
http://d.hatena.ne.jp/rougeref/20161014

selenium.common.exceptions.WebDriverException: Message: Unable to find a matching set of capabilities
https://stackoverflow.com/questions/43713445/selenium-unable-to-find-a-matching-set-of-capabilities-despite-driver-being-in
"""

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
