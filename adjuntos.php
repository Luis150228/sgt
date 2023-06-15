<?php
require_once '../classes/adjuntos.class.php';
$_admArchivo = new adjuntar;


if ($_SERVER['REQUEST_METHOD'] == 'OPTIONS') {
    http_response_code(200);
    header('Access-Control-Allow-Origin: *');
    header('Access-Control-Allow-Methods: POST, GET, OPTIONS, PUT, DELETE');
    header('Access-Control-Allow-Headers: X-Requested-With, Content-Type, Origin, Authorization, Accept, Client-Security-Token, Accept-Encoding');
    exit;
}


if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $header = getallheaders();
    $archivo = $_FILES['archivo'];
    $tipo = $_POST['type'];
    $id = $_POST['id'];
    $respClass = $_admArchivo->fnAdjuntar($archivo, $tipo, $id, $header);
    echo json_encode($respClass['code']);
    if (isset($respClass['code'])) {
        $code = $respClass['code'];
        http_response_code($code);
        header('Content-Type: application/json; charset=UTF-8');
        echo json_encode($respClass);
    } else {
        $codeTwo = $respClass['message']['code'];
        http_response_code($codeTwo);
    }
}
