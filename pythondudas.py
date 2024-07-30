import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Temp\chrome-win64')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()


[Running] python -u "c:\Users\c356882\Desktop\autoEUT\test001.py"
Traceback (most recent call last):
  File "c:\Users\c356882\Desktop\autoEUT\test001.py", line 4, in <module>
    driver = webdriver.Chrome('C:\Temp\chrome-win64')  # Optional argument, if not specified will search path.
  File "C:\Users\c356882\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\chrome\webdriver.py", line 45, in __init__
    super().__init__(
  File "C:\Users\c356882\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\chromium\webdriver.py", line 50, in __init__
    if finder.get_browser_path():
  File "C:\Users\c356882\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\common\driver_finder.py", line 47, in get_browser_path
    return self._binary_paths()["browser_path"]
  File "C:\Users\c356882\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\common\driver_finder.py", line 56, in _binary_paths
    browser = self._options.capabilities["browserName"]
AttributeError: 'str' object has no attribute 'capabilities'
