let headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)"
}

let bodyContent = new FormData();
bodyContent.append("id", "c-100151");
bodyContent.append("type", "application/pdf");
bodyContent.append("archivo", "c:\Users\c356882\Downloads\21001234_acn1.pdf");

let response = await fetch("http://180.176.105.244/santec_hardware_api/rutes/adjuntos.php", { 
  method: "POST",
  body: bodyContent,
  headers: headersList
});

let data = await response.text();
console.log(data);
