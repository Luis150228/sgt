<?php
include_once '../conexion/cnx.php';

class adjuntar extends cnx
{

    public function fnAdjuntar($file, $tipo, $id, $header)
    {
        $data = $this->almacenar($file, $tipo, $id);

        if ($data) {
            return $data;
        } else {
            return $result = array(
                "code" => "416",
                "message" => "Archivo no anexado"
            );
        }
    }

    private function almacenar($file, $type, $id)
    {
        $ruta = '../attach/' . $type;
        $ext = explode('.', $file['name'])[1];
        $nameFile = $id . '.' . $ext;

        if (file_exists($ruta)) {
            chmod($ruta, 0777);
            if (move_uploaded_file($file['tmp_name'], $ruta . '/' . $nameFile)) {
                $saver = array(
                    "code" => "201",
                    "message" => "Archivo Almacenado",
                    "tipo" => $ext,
                    "url" => $ruta . '/' . $nameFile
                );
            }
        } else {
            $saver = array(
                "code" => "202",
                "message" => "Fallo archivo no almacenado",
                "archivo" => $file['name']
            );
        }

        return $saver;
    }
}
