<?php
ini_set('max_execution_time', 800);
require_once "../conexion/cnx.php";
require '../vendor/autoload.php';

use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;
use PhpOffice\PhpSpreadsheet\Style\Fill;
use PhpOffice\PhpSpreadsheet\Style\Alignment;

class valores extends cnx
{
    private function sendWeeklyReports($datos, $semana, $mes)
    {
        // */
        // Crear una instancia de la aplicación Outlook
        $outlook = new COM('Outlook.Application') or die('Outlook no está instalado.');

        // Crear un nuevo objeto de correo electrónico
        $mail = $outlook->CreateItem(0);

        // Configurar el destinatario, asunto y cuerpo del correo
        $mail->Recipients->Add('C356882@produban.com.mx');
        $mail->Subject = 'PRELIMINAR: Seguimiento Sonda y Tablero de Control SDK ' . $mes . ' - SEMANA ' . $semana;

        // Adjuntar archivos desde una carpeta
        $adjuntosDir = $datos['targetFiles']; // Ruta a la carpeta que contiene los archivos
        $adjuntos = scandir($adjuntosDir); // Obtener la lista de archivos en la carpeta

        foreach ($adjuntos as $archivo) {
            if ($archivo !== '.' && $archivo !== '..') {
                $rutaArchivo = $adjuntosDir . '/' . $archivo;
                $attachment = $mail->Attachments->Add($rutaArchivo);
            }
        }

        // Utilizar HTMLBody para dar formato al contenido del correo, incluyendo la imagen de firma
        $mail->HTMLBody = '
                    <html>
                    <head>
                        <meta charset="UTF-8" />
                    </head>
                    <body style="font-family: Verdana, Geneva, Tahoma, sans-serif; font-size:12px;">
                        <p>Buen dia a todos;</p>
                        <br>
                        <p>Favor de enviar sus observaciones a mas tardar el <strong style="color: red;">Martes a las 10:00</strong>, para
                            realizar los ajustes correspondientes.</p>
                        <p style="color: red;">Nota: El reporte de remoto vs sitio se unifico en un solo libro que incluye los incidentes y tareas.</p>
                        <br>
                        <br>
                        <p>Sin mas por el momento, quedo a sus Ordenes.</p>
                        <p style="color: red; font-size:14px;"><strong>Rangel Diaz Luis Fernando.</strong></p>
                        <p>Control y Gestion EUT</p>
                        <p style="color: red;">luirangel@produban.com.mx</p>
                        <img src="../assets/firma.png" alt="Firma">
                    </body>

                    </html>';

        //         $mail->Body = "Buen día a todos;

        // Favor de enviar sus observaciones a más tardar el Martes a las 10:00, para realizar los ajustes correspondientes.
        // Nota: Los folios sombreados en 'gris' en los tiempos de solución de Resolutor y CAU, son las K's consideradas en la métrica por más de 2 días conforme a la ventana de servicio correspondiente.

        // Sin más por el momento, quedo a sus Ordenes

        // ";
        // Enviar el correo
        $mail->Send();
        // */
    }
}