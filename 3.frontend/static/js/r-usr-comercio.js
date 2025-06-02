const block_input_consumidor=document.getElementById("data-usr-consumidor")
const block_input_comercio=document.getElementById("data-usr-comercio")
const check_usr_comercio=document.getElementById("check-usr-comercio");
const check_usr_consumidor=document.getElementById("check-usr-consumidor");

// Si el usuario selecciona la casilla para crear una cuenta del tipo comercio
check_usr_comercio.addEventListener("change", ()=>{
    // Aplico una transformación que va a desplazar todo el bloque del usuario comercio hacia la izquierda haciendolos "aparecer" en pantalla
    block_input_comercio.style.transform="translateX(0px)";

    // Aplico una transformación que va a desplazar todo el bloque del usuario consumidor hacia la izquierda haciendolo "desaparecer" de la pantalla
    block_input_consumidor.style.transform="translateX(-1000px)";
});

// Si el usuario selecciona la casilla para crear una cuenta del tipo consumidor
check_usr_consumidor.addEventListener("change",()=>{
    // Aplico una transformación que va a desplazar todo el bloque del usuario consumidor hacia la derecha haciendolo "aparecer" en la pantalla
    block_input_consumidor.style.transform="translateX(0px)";
    
    // Aplico una transformación que va a desplazar todo el bloque del usuario comercio hacia la derecha haciendolo "desaparecer" de la pantalla
    block_input_comercio.style.transform="translateX(2000px)";
});