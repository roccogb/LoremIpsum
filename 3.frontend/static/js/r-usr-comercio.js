const list_input_consumidor=document.getElementsByClassName("usr-consumidor");                              // Todos los input que sean de la clase 'usr-consumidor' van a estar almacenados en 'list_input'. Estos van a ser aquellos utilizados para crear un usuario 'consumidor'
const check_usr_comercio=document.getElementById("check-usr-comercio");
const check_usr_consumidor=document.getElementById("check-usr-consumidor");

// Si el usuario selecciona la casilla para crear una cuenta del tipo comercio
check_usr_comercio.addEventListener("change", ()=>{
    // Aplico una transformación que va a desplazar todos los 'input' de 'usr-consumidor' hacia la izquierda
    for(let i=0; i<list_input_consumidor.length; i++)
    {
        list_input_consumidor[i].style.transform="translateX(-1000px)";
    }
});

// Si el usuario selecciona la casilla para crear una cuenta del tipo consumidor
check_usr_consumidor.addEventListener("change",()=>{
    // Aplico una transformación que va a desplazar todos los 'input' de 'usr-consumidor' al lugar que estaba previamente
    for(let i=0; i<list_input_consumidor.length; i++)
    {
        list_input_consumidor[i].style.transform="translateX(0px)";
    }
});