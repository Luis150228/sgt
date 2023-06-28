<?php
require_once "../conexion/cnx.php";

class valores extends cnx
{

    public function readDataIncidentes($datos, $dateOrder)
    {
        $json = json_decode($datos, true);
        $typeFolio = $json[0][1];

        if (strpos($typeFolio, "INC") === 0) {
            foreach ($json as $value) {
                $number = $value[0];
                $folio = $value[1];
                $sys_created_on = $value[2];
                $work_end = $value[3];
                $closed_at = $value[4];
                $closed_by = $value[5];
                $assignment_group = $value[6];
                $assigned_to = $value[7];
                $state = $value[8];
                $category = $value[9];
                $subcategory = $value[10];
                $u_short_description_call = $value[11];
                $u_request_type = $value[12];
                $short_description = $value[13];
                $made_sla = $value[14];
                $u_zone = $value[15];
                $location = $value[16];
                $caller_id = $value[17];
                $sys_updated_by = $value[18];
                $calendar_duration = $value[19];
                $business_duration = $value[20];
                $company = $value[21];
                $description = $value[22];
                $comments_and_work_notes = $value[23];
                $opened_by = $value[24];
                $resolved_by = $value[25];
                $close_code = $value[26];
                $parent_incident = $value[27];
                $child_incidents = $value[28];
                $sys_updated_on = $value[29];
                $sys_created_by = $value[30];
                $data = $this->uploadData($number, $folio, $sys_created_on, $work_end, $closed_at, $closed_by, $assignment_group, $assigned_to, $state, $category, $subcategory, $u_short_description_call, $u_request_type, $short_description, $made_sla, $u_zone, $location, $caller_id, $sys_updated_by, $calendar_duration, $business_duration, $company, $description, $comments_and_work_notes, $opened_by, $resolved_by, $close_code, $parent_incident, $child_incidents, $sys_updated_on, $sys_created_by, $dateOrder);
            };
            return $data;
        } else {
            $result = array(
                "code" => "204",
                "mnj" => "Error al subir informacion archivo incorrecto",
                "data" => '',
            );

            return $result;
        }
    }

    private function uploadData($number, $folio, $sys_created_on, $work_end, $closed_at, $closed_by, $assignment_group, $assigned_to, $state, $category, $subcategory, $u_short_description_call, $u_request_type, $short_description, $made_sla, $u_zone, $location, $caller_id, $sys_updated_by, $calendar_duration, $business_duration, $company, $description, $comments_and_work_notes, $opened_by, $resolved_by, $close_code, $parent_incident, $child_incidents, $sys_updated_on, $sys_created_by, $dateOrder)
    {
        $sql = "CALL stp_addIncidents('$number','$folio','$sys_created_on','$work_end','$closed_at','$closed_by','$assignment_group','$assigned_to','$state','$category','$subcategory','$u_short_description_call','$u_request_type','$short_description','$made_sla','$u_zone','$location','$caller_id','$sys_updated_by','$calendar_duration','$business_duration','$company','$description','$comments_and_work_notes','$opened_by','$resolved_by','$close_code','$parent_incident','$child_incidents','$sys_updated_on','$sys_created_by','$dateOrder')";
        // print_r($sql);
        $query = parent::getData($sql);

        if (empty($query)) {
            $result = array(
                "code" => "204",
                "mnj" => "Error al subir informacion archivo incorrecto",
                "data" => "",
            );
        } else {
            $result = array(
                "code" => "200",
                "mnj" => "Importacion correcta",
                "data" => $query
            );
        }

        return $result;
    }
}
