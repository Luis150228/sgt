[Running] python -u "c:\Users\c356882\Desktop\reportsAuto\testSel.py"
Traceback (most recent call last):
  File "c:\Users\c356882\Desktop\reportsAuto\testSel.py", line 4, in <module>
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