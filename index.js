/*
<div class="mb-3">
  <label for="formFile" class="form-label">Documentos de ingreso</label>
  <input required class="form-control" type="file" id="formFileDocs" name="adjunto">
</div>
*/

const inputFile = document.getElementById('formFileDocs');
const fetchBeta = async (ruta, datos)=>{
    const data = JSON.stringify(datos);
    const destino = `${api.url}${ruta}.php`
    const fetchConfig = {
        method: "POST",
        headers: $header,
        body: data
    }

    const peticion = new Request(destino, fetchConfig);

    if (data instanceof FormData) {
        const formDataEntries = [...data.entries()];
        console.log(formDataEntries);
    }else{
        console.log(data);
    }
}


inputFile.addEventListener('change', async (e) =>{
        console.log(e);
        const file = e.target.files[0];
        const typFile = e.target.files[0].type;
        const sizFile = ((e.target.files[0].size)/1024)/1024;
        const refFile = numPedido.value
        console.log(file); /*File {name: 'SUBASTA AUTOS  03-2023.pdf', lastModified: 1682434256241, lastModifiedDate: Tue Apr 25 2023 08:50:56 GMT-0600 (hora estándar central), webkitRelativePath: '', size: 350825, …}
lastModified
: 
1682434256241
lastModifiedDate
: 
Tue Apr 25 2023 08:50:56 GMT-0600 (hora estándar central) {}
name
: 
"SUBASTA AUTOS  03-2023.pdf"
size
: 
350825
type
: 
"application/pdf"
webkitRelativePath
: 
""
[[Prototype]]
: 
File*/
        const typeFiles = [
            "application/pdf",
            "image/jpeg",
            "image/png",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ];

        if (typeFiles.includes(typFile) && sizFile <= 5) {
            const data = new FormData();
            data.append('id', refFile);
            data.append('type', typFile);
            data.append('archivo', file);
            console.log([...data]);
          /*Resultado del [...data] = 
          [
              [
                  "id",
                  "c-100151"
              ],
              [
                  "type",
                  "application/pdf"
              ],
              [
                  "archivo",
                  {}
              ]
          ]
          */
            divLoader()
            const attachFile = await fetchBeta('adjuntos', data);
            console.log(attachFile);
            divLoader()

        }else{
            alert('Tipo o tamaño de archivo incorrecto')
            inputFile.value = ''
        }

    })
