ChatGPT

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
ChatGPT
Para asegurarte de que cada función en excRep13() se ejecute secuencialmente y no comience la siguiente hasta que la anterior haya terminado, puedes utilizar el operador await en las llamadas de función asíncronas. Aquí tienes una versión actualizada de excRep13() usando async y await en combinación con asyncio para la ejecución secuencial:

python
Copiar código
import asyncio

async def cleanPath_async(folder_path):
    cleanPath(folder_path)  # Llamada sincrónica a cleanPath

async def get_mail13_async(pathSave):
    get_mail13(pathSave)  # Llamada sincrónica a get_mail13

async def activate_eutChrome_async(typeData, typeDownload, chromeTab, btndwc):
    activate_eutChrome(typeData, typeDownload, chromeTab, btndwc)  # Llamada sincrónica a activate_eutChrome

async def open_excel_file_async(file_path):
    open_excel_file(file_path)  # Llamada sincrónica a open_excel_file

async def excRep13():
    await cleanPath_async(saveSF)
    await get_mail13_async(saveSF)
    await activate_eutChrome_async(inc, btndwInc, chromeTabInc, btndwInc2)
    await open_excel_file_async(rep13)

def run_excRep13():
    asyncio.run(excRep13())

# Utiliza run_excRep13() para ejecutar excRep13
En este ejemplo, asyncio.run() se utiliza para ejecutar excRep13() de manera asíncrona, asegurando que cada tarea se complete antes de comenzar la siguiente.

Si tienes funciones de larga duración que no son realmente asíncronas pero necesitas esperar su finalización, puedes utilizar await asyncio.sleep(<duration>) para emular un comportamiento similar, pero recuerda que asyncio se aprovecha mejor con funciones realmente asíncronas o cuando estás esperando por operaciones I/O.

Finalmente, si estás trabajando en un entorno donde asyncio no es necesario y prefieres mantenerlo todo sincrónico, puedes simplemente llamar a cada función de manera secuencial como se hacía anteriormente, ya que en Python las funciones no avanzan hasta que la función llamada previamente ha terminado.


2/2





Si no tengo la posibilidad de instalar asyncio 
ChatGPT
Si no puedes utilizar asyncio o cualquier otra biblioteca asíncrona, puedes simplemente asegurarte de que cada función se ejecute secuencialmente llamándolas una tras otra de manera sincrónica. Aquí tienes una versión actualizada de excRep13() y excRep04() para que cada función se ejecute en secuencia, como ya hacen las funciones regulares en Python:

python
Copiar código
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
        print(f'Horario: {baseService} - {title} {current_hour}:{current_minute}')
        if title == 'Macro_Report13 - Excel':
            excRep13()
        else:
            excRep04()

        time.sleep(60)  # Espera un minuto antes de seguir
    else:
        time.sleep(5)  # Espera 5 segundos antes de revisar nuevamente
        print(f'Fuera de horario {current_hour}:{current_minute}')
        mouse.move(35, 120, absolute=True, duration=1)
        mouse.click('left')
        time.sleep(15)
        mouse.move(100, 160, absolute=True, duration=1)
        mouse.click('left')
        time.sleep(20)
        mouse.move(35, 240, absolute=True, duration=1)
        mouse.click('left')
        time.sleep(20)
En este código, cada función en excRep13() y excRep04() se ejecuta secuencialmente. Python ejecutará cada línea en el orden en que están escritas, esperando a que cada función termine antes de continuar con la siguiente. De esta forma, activate_eutChrome no comenzará hasta que get_mail13 haya terminado, y open_excel_file no comenzará hasta que activate_eutChrome haya terminado, asegurando así la ejecución secuencial que necesitas.





Lo tengo así pero no está pasando como indicas hay un momento donde se ejecutan activate_eutChrome y open_excel_file
ChatGPT
Si las funciones activate_eutChrome y open_excel_file están ejecutándose simultáneamente, es posible que alguna función esté devolviendo el control al programa principal antes de que haya terminado completamente su trabajo. Esto puede suceder si las funciones realizan operaciones que son asíncronas por naturaleza o si estás utilizando threading en algún lugar que no has mostrado aquí.

Para asegurarte de que las funciones se ejecuten secuencialmente, puedes agregar mensajes de depuración (prints) antes y después de cada función para confirmar el orden de ejecución y asegurarte de que no haya comportamientos inesperados.

También, puedes revisar las funciones en busca de cualquier operación que pudiera devolver el control prematuramente, especialmente en activate_eutChrome. A continuación, te muestro cómo agregar mensajes de depuración:

python
Copiar código
def excRep13():
    print("Limpiando directorio...")
    cleanPath(saveSF)
    print("Directorio limpiado.")
    
    print("Obteniendo correos...")
    get_mail13(saveSF)
    print("Correos obtenidos.")
    
    print("Activando Chrome para EUT...")
    activate_eutChrome(inc, btndwInc, chromeTabInc, btndwInc2)
    print("Chrome activado para EUT.")
    
    print("Abriendo archivo Excel...")
    open_excel_file(rep13)
    print("Archivo Excel abierto.")

def excRep04():
    print("Activando Chrome para tarea...")
    activate_eutChrome(sol, btndwSol, chromeTabTask, btndwSol2)
    print("Chrome activado para tarea.")
    
    print("Abriendo archivo Excel...")
    open_excel_file(rep04)
    print("Archivo Excel abierto.")

while True:
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    if (current_hour, current_minute) in reportsExc:
        baseService, file_macro, title, mail, btnData, chrTab, btnRepData = reportsExc[(current_hour, current_minute)]
        print(f'Horario: {baseService} - {title} {current_hour}:{current_minute}')
        if title == 'Macro_Report13 - Excel':
            excRep13()
        else:
            excRep04()

        time.sleep(60)  # Espera un minuto antes de seguir
    else:
        time.sleep(5)  # Espera 5 segundos antes de revisar nuevamente
        print(f'Fuera de horario {current_hour}:{current_minute}')
        mouse.move(35, 120, absolute=True, duration=1)
        mouse.click('left')
        time.sleep(15)
        mouse.move(100, 160, absolute=True, duration=1)
        mouse.click('left')
        time.sleep(20)
        mouse.move(35, 240, absolute=True, duration=1)
        mouse.click('left')
        time.sleep(20)
Si después de agregar los mensajes de depuración ves que las funciones siguen ejecutándose simultáneamente, revisa si hay alguna operación asíncrona en activate_eutChrome o cualquier otra función. Algunas bibliotecas pueden estar ejecutando operaciones en segundo plano o lanzando hilos sin que te des cuenta.

Otra posibilidad es asegurar que el uso de time.sleep sea adecuado. Asegúrate de que time.sleep se utilice correctamente para dar suficiente tiempo a las operaciones antes de pasar a la siguiente instrucción. Aquí hay un ejemplo:

python
Copiar código
def open_excel_file(file_path):
    os.startfile(file_path)
    time.sleep(10)  # Asegúrate de esperar lo suficiente para que el archivo se abra completamente

def activate_window(window_title):
    window = gw.getWindowsWithTitle(window_title)
    if window:
        window[0].activate()
        print(f'Ventana Activa "{window[0].title}"')
    else:
        print(f'Ventana de "{window_title}" no está disponible')

def activate_eutChrome(typeData, typeDownload, chromeTab, btndwc):
    print(f'Activando EUT Chrome para {typeData}...')
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
        time.sleep(90)  # Este tiempo de espera es crítico
        try:
            activate_window(chromeReportes)
            time.sleep(1)
            activate_window(chromeTab)
            time.sleep(1)
            location = pyautogui.locateOnScreen(btndwNumRigth)
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
                pyautogui.write(saveTxt + typeData)
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.hotkey('alt', 'F4')
                print('Se descargó la información')
                btndwClick = pyautogui.locateOnScreen(btndwc)
                pyautogui.moveTo(pyautogui.center(btndwClick))
                time.sleep(3)
                btnUpdateClick = pyautogui.locateOnScreen(btnUpdate)
                pyautogui.moveTo(pyautogui.center(btnUpdateClick))
                time.sleep(10)
                print('Se actualiza la información')
        except:
            print('No se localiza la ventana')
    else:
        print(f'Navegador chrome de "{chromeReportes}" no está disponible')
En este ejemplo, se agregan más mensajes de depuración y se aseguran tiempos de espera adecuados. Ajusta los tiempos de espera según sea necesario para tu entorno específico.





Estoy presentando está falla al instalar 
PS C:\Users\c356882\Desktop\reportsAuto> c:\Users\c356882\Desktop\reportsAuto\.venv\Scripts\python.exe -m pip install -U selenium
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:997)'))': /simple/selenium/
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:997)'))': /simple/selenium/
WARNING: Retrying (Retry(total=2, connect=None, read=N
