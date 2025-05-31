/* Script de JS encargado de la animación del cambio de fondo del template del login*/
const div_fade=document.getElementById("bg-fade");               // El objeto 'div_fade' va a representar el elemento 'div' que me va a permitir realizar la animacion del fondo
const list_img=[ 
                    "../static/media/img/planetario.jpg",
                    "../static/media/img/puente_palermo.jpg",
                    "../static/media/img/puente_mujer.jpg", 
                    "../static/media/img/caminito_boca_essi.jpeg",
                    "../static/media/img/santelmo.jpg",
                    "../static/media/img/obelisco_recortado.jpeg"
                ];


let i = 0;

function cambiarFondo(){
    div_fade.style.backgroundImage=`url('${list_img[i]}')`;             // Cargo la aquella imagen que se encuentren en la posición i de 'list_img' en el objeto div_fade
    div_fade.style.opacity=0.5                                          // Simulo el efecto de un fadein con la opacidad de la imagen
    div_fade.style.opacity=0.75
    div_fade.style.opacity=1;                                           

    // Agrego una demora de 5s antes de la siguiente imagen para asi el cliente puede ver la imagen mejor
    setTimeout(()=>{
        div_fade.style.opacity=0.75;                                    // Simulo el efecto de un fadeout con la opacidad de la imagen
        div_fade.style.opacity=0.5;                                       
        div_fade.style.opacity=0.25;

        // Agrego una demora de 650ms antes de que se incremente el contador y que se vuelva a ejecutar la funcion para así el cambio de imagen no es instantaneo.
        setTimeout(()=>{
            // Aumento i para poder mostrar la siguiente imagen. Si la variable llega a ser igual al tamaño de 'list_img', vuelve a 0 y se reinicia el ciclo
            // Ej: i=2%2 -> i=0
            i=(i+1)%list_img.length;  
            cambiarFondo();
        },650);
    },5000);
}

cambiarFondo()