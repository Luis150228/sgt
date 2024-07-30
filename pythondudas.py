Opción 2: Actualizar el certificado raíz de confianza
Si estás en un entorno corporativo, es posible que necesites actualizar el certificado raíz de confianza. Aquí te explico cómo hacerlo:

Obtener el certificado raíz de confianza:

Puedes obtener el certificado raíz de confianza desde el navegador web. Visita el sitio web que está causando problemas (por ejemplo, https://pypi.org), haz clic en el candado en la barra de direcciones y sigue las opciones para ver el certificado y exportarlo.
Agregar el certificado al entorno Python:

Una vez que tengas el certificado, puedes agregarlo al entorno de Python utilizando las siguientes instrucciones. Guarda el certificado en un archivo, por ejemplo, corporate.pem.
Configurar pip para usar el certificado:

Usa el siguiente comando para instalar paquetes con el certificado:
bash
Copiar código
c:\Users\c356882\Desktop\reportsAuto\.venv\Scripts\python.exe -m pip install --cert <ruta/al/certificado/corporate.pem> selenium
Opción 3: Configurar pip para ignorar los errores SSL
Otra opción es modificar el archivo de configuración de pip para que ignore los errores SSL. Añade o modifica el archivo pip.ini (en Windows) o pip.conf (en Linux/MacOS) con el siguiente contenido:

Windows (pip.ini):

ini
Copiar código
[global]
trusted-host = pypi.org
               files.pythonhosted.org
Guarda este archivo en la ruta C:\Users\<tu-usuario>\AppData\Roaming\pip\pip.ini.

Linux/MacOS (pip.conf):

ini
Copiar código
[global]
trusted-host = pypi.org
               files.pythonhosted.org
Guarda este archivo en ~/.config/pip/pip.conf.

Opción 4: Usar un proxy corporativo
Si estás detrás de un proxy corporativo, asegúrate de que pip esté configurado para usarlo. Añade la configuración del proxy en el archivo de configuración de pip.

Windows (pip.ini):

ini
Copiar código
[global]
proxy = http://proxy.usuario:proxy.contraseña@proxy.dominio:puerto
trusted-host = pypi.org
               files.pythonhosted.org
Linux/MacOS (pip.conf):

ini
Copiar código
[global]
proxy = http://proxy.usuario:proxy.contraseña@proxy.dominio:puerto
trusted-host = pypi.org
               files.pythonhosted.org
Opción 5: Actualizar pip y certifi
A veces, actualizar pip y certifi (el paquete que maneja certificados SSL en Python) puede resolver el problema:

bash
Copiar código
c:\Users\c356882\Desktop\reportsAuto\.venv\Scripts\python.exe -m pip install --upgrade pip
c:\Users\c356882\Desktop\reportsAuto\.venv\Scripts\python.exe -m pip install --upgrade certifi
Resumen
Si el problema persiste después de probar estas soluciones, puede ser útil ponerse en contacto con el equipo de TI de tu organización para obtener más ayuda, ya que los problemas de SSL a menudo están relacionados con configuraciones de red corporativa o políticas de seguridad.










ChatGPT puede cometer errores. Comprueba la información importante.
