# sgt

const recordsPerPage = 10;
const records = /* Aquí debes poner el array con los 50000 registros */;
const totalPages = Math.ceil(records.length / recordsPerPage);

function createTablePage(records) {
  let html = '<table>';
  html += '<tr><th>IMEI</th><th>Nombre del Plan</th><th>Asignado a</th><th>Expediente</th><th>Semaforo Enrollment</th></tr>';
  for (const record of records) {
    html += `<tr><td><button onclick="showDetails('${record.imei}')">${record.imei}</button></td><td>${record.nombre_plan}</td><td>${record.asignado_a}</td><td>${record.expediente}</td><td>${record.semaforo_enrollment}</td></tr>`;
  }
  html += '</table>';
  return html;
}

function showTablePage(page) {
  const startIndex = (page - 1) * recordsPerPage;
  const recordsPage = records.slice(startIndex, startIndex + recordsPerPage);
  const tableHtml = createTablePage(recordsPage);
  document.getElementById('table-container').innerHTML = tableHtml;
}

function showDetails(imei) {
  /* Aquí debes poner el código para mostrar los detalles del registro con el IMEI indicado */
}

// Mostrar la primera página al cargar la página
showTablePage(1);

// Agregar botones de paginación
for (let i = 1; i <= totalPages; i++) {
  const button = document.createElement('button');
  button.innerText = i;
  button.onclick = function() {
    showTablePage(i);
  };
  document.getElementById('pagination-container').appendChild(button);
}


/**/
const createData = async (jsonUrl, pag = 1, items = 100000, campo = '', texto = '', columna = 'num_movil', order = 'ASC')=>{
    try {
        let loader = document.createElement('p')
        loader.innerHTML = 'espere... '
        divloader.appendChild(loader)

        let res = await fetch(`${jsonUrl.url}rutes/showData.php?pag=${pag}&reg=${items}&co=${campo}&tx=${texto}&cl=${columna}&or=${order}`, {
            method: "GET"
        }),
        json = await res.json();
            const datas = json['data'];
            divloader.innerHTML = ''
            return datas

    } catch (error) {
        divData.innerHTML = `Error en consulta parametros incorrectos: ${error}`
    }

}


<div class="btn-paginacion" id="paginacion"><div class="control-pag"><button class="btn-pag" data-set-pg="1">1</button><button class="btn-pag" data-set-pg="2">2</button><button class="btn-pag" data-set-pg="3">3</button><button class="btn-pag" data-set-pg="4">4</button><button class="btn-pag" data-set-pg="1094">1094</button></div></div>



const objetosEncontrados = arregloDeObjetos.filter(objeto => {
  const regex = new RegExp("castro", "i"); // "i" indica que la búsqueda no distingue mayúsculas y minúsculas
  for (const propiedad in objeto) {
    if (regex.test(objeto[propiedad])) {
      return true; // Si se encuentra una coincidencia, se devuelve true y se agrega el objeto al arreglo de objetos encontrados
    }
  }
  return false; // Si no se encuentra ninguna coincidencia, se devuelve false y se excluye el objeto del arreglo de objetos encontrados
});
