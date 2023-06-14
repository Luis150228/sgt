const frmOdc = document.getElementById('frm-odc');

const fetchPOST = async (ruta, datos)=>{
    const data = JSON.stringify(datos);
    const destino = `${api.url}${ruta}.php`
    const fetchConfig = {
        method: "POST",
        headers: $header,
        body: data
    }

    const peticion = new Request(destino, fetchConfig);
    try {
        const resp = await fetch(peticion);
        const result = await resp.json();
        return result
    } catch (error) {
        throw new Error(`Peticion Fecht con problemas de servidor: ${error}`);
    }
}


const attachDocs = async (data)=>{
    const resultado = await fetchPOST('adjuntos', data);
     return resultado;
}

inputFile.addEventListener('change', async (e) =>{
        console.log(e);
        const typFile = e.target.files[0].type;
        const sizFile = ((e.target.files[0].size)/1024)/1024;
        const refFile = numPedido.value
        console.log(inputFile.type);
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
            data.append('archivo', inputFile);
            console.log([...data]);
            divLoader()
            const attachFile = await attachDocs(data);
            console.log(attachFile);
            divLoader()

        }else{
            alert('Tipo o tamaño de archivo incorrecto')
            inputFile.value = ''
        }

    })
