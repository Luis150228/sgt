requiero que excRep13() cada funcion se vaya ejecutando solo si termina la anterior por ejemplo activate_eutChrome se puede tardar 1 min o 10 min en ejecutarse o puede ser variado, pero quiero que hasta que termine ejecute la siguiente linea open_excel_file() y no antes 

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
saveSF = r'Y:\dev\santecReportsAPI\dataUpdate'
saveTxtT = 'Y:\\dev\\santecReportsAPI'
saveTxt = 'Y:\\dev\\santecReportsAPI\\dataUpdate\\'

# Botones Chrome
btnActualizarData = r'C:\Temp\imgAuto\btnActualizarData.png'
btndwInc = r'C:\Temp\imgAuto\btnDownLoadInc.png'
btndwSol = r'C:\Temp\imgAuto\btnDownLoadSol.png'
btndwUnl = r'C:\Temp\imgAuto\btnDownLoadUnl.png'
btndwInc2 = r'C:\Temp\imgAuto\btnDownLoadInc2.png'
btndwSol2 = r'C:\Temp\imgAuto\btnDownLoadSol2.png'
btnUpdate = r'C:\Temp\imgAuto\btnActualizarBase.PNG'
btndwNumRigth = r'C:\Temp\imgAuto\btnNumeroDownload.PNG'
btndwNumRigthExport = r'C:\Temp\imgAuto\btnNumeroExport.PNG'
btndwNumRigthExportCSV = r'C:\Temp\imgAuto\btnNumeroExportCSV.PNG'
btndwNumRigthExportDescargar = r'C:\Temp\imgAuto\btnNumeroExportCSVDescargar.PNG'

inc = 'incident'
sol = 'sc_task'
unlock = 'interaction'
title_rep13 = 'Macro_Report13 - Excel'
title_rep04 = 'Macro_Report04 - Excel'
chromeReportes = 'EUT Reportes'
mail_rep13 = 'Seguimiento Sucursales - Mensaje (HTML)'
mail_rep04 = 'Backlog de incidentes CAU-MTF - Mensaje (HTML)'
chromeTabInc = 'Incidentes | ServiceNow - Google Chrome'
chromeTabTask = 'Tareas del catálogo | ServiceNow - Google Chrome'

reportsExc = {
    (10,39): (inc, rep13, title_rep13, mail_rep13, btndwInc, chromeTabInc, btndwInc2),
    (10,45): (sol, rep04, title_rep04, mail_rep04, btndwSol, chromeTabTask, btndwSol2),
    (10,50): (inc, rep13, title_rep13, mail_rep13, btndwInc, chromeTabInc, btndwInc2),
    (10,56): (inc, rep04, title_rep04, mail_rep04, btndwSol, chromeTabTask, btndwSol2),
}


def open_excel_file(file_path):
    os.startfile(file_path)
    time.sleep(5)

def activate_window(window_title):
    window = gw.getWindowsWithTitle(window_title)
    if window:
        window[0].activate()
        print(f'Ventana Activa "{window[0].title}"')
    else:
        print(f'Ventana de "{window_title}" no esta disponible')

def cleanPath(folder_path):
    if os.path.exists(folder_path):
        # Iterar sobre todos los archivos en la carpeta
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                # Verificar si es un archivo (no un directorio)
                if os.path.isfile(file_path):
                    os.remove(file_path)  # Eliminar el archivo
                    print(f'Archivo eliminado: {file_path}')
            except Exception as e:
                print(f'Error al eliminar {file_path}: {e}')
    else:
        print(f'La carpeta {folder_path} no existe.')

############################### odenes de Chrome para actualizar bases de datos
def activate_eutChrome(typeData, typeDownload, chromeTab, btndwc):
    if typeData == 'sc_task':
        minData = 120
    else:
        minData = 20

    window = gw.getWindowsWithTitle(chromeReportes)
    if window:
        window[0].activate()
        time.sleep(1)
        center = pyautogui.locateOnScreen(btnActualizarData)
        pyautogui.click(center)
        time.sleep(1)
        btnLink = pyautogui.locateOnScreen(typeDownload)
        pyautogui.click(btnLink)
        time.sleep(90)
        try:
            activate_window(chromeReportes)
            time.sleep(1)
            activate_window(chromeTab)
            time.sleep(1)
            location = pyautogui.locateOnScreen(btndwNumRigth)
            # pyautogui.click(location)
            # print('Clik Izquierdo')
            if location is not None:
                pyautogui.rightClick(pyautogui.center(location))
                time.sleep(3)
                exportar = pyautogui.locateOnScreen(btndwNumRigthExport)
                pyautogui.moveTo(pyautogui.center(exportar))
                time.sleep(1)
                exportarCSV = pyautogui.locateOnScreen(btndwNumRigthExportCSV)
                pyautogui.moveTo(pyautogui.center(exportarCSV))
                pyautogui.click()
                print('Esperando btn de descarga...')
                time.sleep(90)
                exportarBtnDescargar = pyautogui.locateOnScreen(btndwNumRigthExportDescargar)
                pyautogui.moveTo(pyautogui.center(exportarBtnDescargar))
                pyautogui.click()
                time.sleep(10)
                pyautogui.write(saveTxtT)
                time.sleep(3)
                pyautogui.press('enter')
                pyautogui.write(saveTxt+typeData)
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.hotkey('alt', 'F4')
                print('Se descargo la informacion')
                btndwClick = pyautogui.locateOnScreen(btndwc)
                pyautogui.moveTo(pyautogui.center(btndwClick))
                time.sleep(3)
                btnUpdateClick = pyautogui.locateOnScreen(btnUpdate)
                pyautogui.moveTo(pyautogui.center(btnUpdateClick))
                time.sleep(10)
                print('Se Actualiza la informacion')

        except:
            print('No se localiza la ventana')
            # allwins = gw.getAllWindows()
            # for allwin in allwins:
            #     print(f'Titulos:{allwin.title}')

    else:
        print(f'Navegador chrome de "{chromeReportes}" no esta disponible')
############################### odenes de Chrome para actualizar bases de datos



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
    textName = f"{base}_{tiemstamp}{extension}"
    return 'Comunicaciones.xlsx'

def get_mail13(pathSave):
    if not os.path.exists(pathSave):
        os.makedirs(pathSave)
    outlook = win32com.client.Dispatch('outlook.Application').GetNamespace('MAPI')
    try:
      inbox = outlook.Folders.Item('Bandeja de entrada')
    except:
      inbox = outlook.GetDefaultFolder(6)

    suc_fuera = inbox.Folders.Item('Suc Fuera')
    messages = suc_fuera.items

    for message in messages:
     if message.Unread:
         for attachment in message.Attachments:
             if attachment.FileName.endswith('.XLSX'):
                new_file = get_new_file(attachment.FileName)
                attachment.SaveAsFile(os.path.join(pathSave, new_file))
                print(f"Se guardo el archivo con el nombre {new_file}")


def excRep13():
    cleanPath(saveSF)
    get_mail13(saveSF)
    activate_eutChrome(inc, btndwInc, chromeTabInc, btndwInc2)
    open_excel_file(rep13)

def excRep04():
    activate_eutChrome(sol, btndwSol, chromeTabTask, btndwSol2)
    open_excel_file(rep04)


while True:
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    if (current_hour, current_minute) in reportsExc:
        baseService, file_macro, title, mail, btnData, chrTab, btnRepData = reportsExc[(current_hour, current_minute)]
        print(f'horario: {baseService} - {title} {current_hour}:{current_minute}')
        if title == 'Macro_Report13 - Excel':
            excRep13()
        else:
            excRep04()

        time.sleep(60)
    else:
        time.sleep(5)
        print(f'fuera de horario {current_hour}:{current_minute}')
        mouse.move(35, 120, absolute=True, duration=1)
        mouse.click('left')
        time.sleep(15)
        mouse.move(100, 160, absolute=True, duration=1)
        mouse.click('left')
        time.sleep(20)
        mouse.move(35, 240, absolute=True, duration=1)
        mouse.click('left')
        time.sleep(20)