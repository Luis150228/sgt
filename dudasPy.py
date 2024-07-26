[Running] python -u "c:\Users\c356882\Desktop\reportsAuto\reportsAuto001.py"
Traceback (most recent call last):
  File "c:\Users\c356882\Desktop\reportsAuto\reportsAuto001.py", line 90, in <module>
    report013()
  File "c:\Users\c356882\Desktop\reportsAuto\reportsAuto001.py", line 80, in report013
    messages = suc_fuera.Items()
  File "C:\Users\c356882\AppData\Local\Programs\Python\Python310\lib\site-packages\win32com\client\dynamic.py", line 226, in __call__
    self._oleobj_.Invoke(*allArgs), self._olerepr_.defaultDispatchName, None
pywintypes.com_error: (-2147024809, 'El par�metro no es correcto.', None, None)


import os
import pyautogui
import pygetwindow as gw
import win32com.client
import mouse, time
from datetime import datetime

# Ruta de los Archivos
rep13 = r'C:\Temp\repAuto\Macro_Report13.xlsm'
rep04 = r'C:\Temp\repAuto\Macro_Report04.xlsm'
btnSendMail = r'C:\Temp\imgAuto\btnSendMail.png'
excelImg13 = r'C:\Temp\imgAuto\mouseClickExcelApp13.png'
excelImg04 = r'C:\Temp\imgAuto\mouseClickExcelApp04.png'
saveSF = r'C:\Temp\filesAuto'

title_rep13 = 'Macro_Report13 - Excel'
title_rep04 = 'Macro_Report04 - Excel'
chromeReportes = 'EUT Reportes - Google Chrome'
mail_rep13 = 'Seguimiento Sucursales - Mensaje (HTML)'
mail_rep04 = 'Backlog de incidentes CAU-MTF - Mensaje (HTML)'

# reportsExc = {
#     (8,30): (rep13, title_rep13, mail_rep13),
#     (8,50): (rep04, title_rep04, mail_rep04),
#     (15,50): (rep13, title_rep13, mail_rep13),
#     (15,55): (rep04, title_rep04, mail_rep04)
# }

reportsExc = {
    (10,20): (rep13, title_rep13, mail_rep13),
    (10,22): (rep04, title_rep04, mail_rep04),
    (10,26): (rep13, title_rep13, mail_rep13),
    (10,40): (rep04, title_rep04, mail_rep04),
    (10,45): (rep13, title_rep13, mail_rep13),
    (10,50): (rep04, title_rep04, mail_rep04),
}


def open_excel_file(file_path):
    os.startfile(file_path)
    time.sleep(5)

def activate_window(window_title):
    window = gw.getWindowsWithTitle(window_title)
    if window:
        window[0].activate()
    else:
        print(f'Ventana de "{window_title}" no esta disponible')

def activate_mail(window_title):
    window = gw.getWindowsWithTitle(window_title)
    if window:
        window[0].activate()
        time.sleep(3)
        center = pyautogui.locateOnScreen(btnSendMail)
        pyautogui.click(center)
    else:
        print(f'Correo de "{window_title}" no esta disponible busque ventana de forma Manual')

def excMacro(img_button):
    center = pyautogui.locateOnScreen(img_button)
    pyautogui.click(center)
    print('Ejecutar Macro')

def get_new_file(fileName):
    base, extension = os.path.splitext(fileName)
    tiemstamp = datetime.now().strftime('%Y%m%d%H%M%S')
    return f"{base}_{tiemstamp}{extension}"

def report013():
    if not os.path.exists(saveSF):
        os.makedirs(saveSF)
    outlook = win32com.client.Dispatch('outlook.Application').GetNamespace('MAPI')
    inbox = outlook.Folders.Item('Bandeja de entrada')
    suc_fuera = inbox.Folders.Item('Suc Fuera')
    messages = suc_fuera.Items()
    
    for message in messages:
     if message.Unread:
         for attachment in message.Attachments:
             new_file = get_new_file(attachment.FileName)
             attachment.SaveAsFile(os.path.join(saveSF, new_file))
             print(f"Se guardo el archivo con el nombre {new_file}")


report013()
# open_excel_file(rep13)
# open_excel_file(rep04)

# activate_window(title_rep13)
# time.sleep(1)
# excMacro(excelImg13)
# time.sleep(30)
# activate_mail(mail_rep13)


# activate_window(title_rep04)
# time.sleep(10)

# while True:
#     now = datetime.now()
#     current_hour = now.hour
#     current_minute = now.minute
#     if (current_hour, current_minute) in reportsExc:
#         file_path, title, mail = reportsExc[(current_hour, current_minute)]
#         print(f'horario {title} {current_hour}:{current_minute}')
#         mouse.move(20, 120, absolute=True, duration=2)
#         mouse.move(35, 120, absolute=True, duration=1)
#         time.sleep(60)
#     else:
#         time.sleep(5)
#         print(f'fuera de horario {current_hour}:{current_minute}')
#         mouse.move(35, 120, absolute=True, duration=1)
#         mouse.click('left')
#         time.sleep(15)
#         mouse.move(100, 160, absolute=True, duration=1)
#         mouse.click('left')
#         time.sleep(20)
#         mouse.move(35, 240, absolute=True, duration=1)
#         mouse.click('left')
#         time.sleep(20)