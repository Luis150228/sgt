<?php
include_once "../classes/incImport.class.php";

$_consult = new valores;

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, PUT, DELETE, GET');

$contBody = file_get_contents('php://input');
$bodyJson = json_decode($contBody, true);
$headers = getallheaders();
// foreach ($_GET as $key => $value) {
//     echo $key.'=>'.$value.'<br>';
// }

if ($_SERVER['REQUEST_METHOD'] == 'GET') {
    if (isset($_GET['token']) && isset($_GET['catalogo'])) {
        $dataClass = $_consult->readData($_GET['token'], $_GET['catalogo']);
        // print_r(($_GET['token']));
    } else {
        http_response_code(203);
        header('Content-Type: application/json; charset=UTF-8');
    }
} else if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($headers['time-update'])) {
        $dataClass = $_consult->readDataIncidentes($contBody, $headers['time-update']);
    } elseif (isset($bodyJson['token']) && ($bodyJson['orden'] == 'menu')) {
        // $dataClass = $_consult->createNavOne($contBody);
    }
    http_response_code(200);
} else if ($_SERVER['REQUEST_METHOD'] == 'PUT') {
    http_response_code(200);
} else if ($_SERVER['REQUEST_METHOD'] == 'DELETE') {
    http_response_code(200);
} else {
    http_response_code(400);
}

header('Content-Type: application/json; charset=UTF-8');
echo json_encode($dataClass);
