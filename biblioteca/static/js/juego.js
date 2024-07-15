//Inicializacion de variables
let tarjetasDestapadas = 0;
let tarjeta1 = null;
let tarjeta2 = null;
let primerResultado = null;
let segundoResultado = null;
let movimientos = 0;
let aciertos = 0;
let temporizador = false;
let timer = 30;
let tiempoRegresivoId  = null;
let timerInicial = 30;
//apuntando a documento HTML
let mostrarMovimientos = document.getElementById('movimientos');
let mostrarAciertos = document.getElementById('aciertos');
let mostrarTiempo = document.getElementById('t-restante');
//audio
let winAudio = new Audio('assets/sounds/Win.mp3');
let correctAudio = new Audio ('assets/sounds/Correct.mp3');
let loseAudio = new Audio ('assets/sounds/Lose.mp3');
//numeros aleatorios
let numeros = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8];
numeros = numeros.sort(()=>{return Math.random()-0.5});
console.log(numeros);
//funciones
function contarTiempo(){
    tiempoRegresivoId = setInterval(()=>{
        timer--;
        mostrarTiempo.innerHTML = `Tiempo: ${timer} segundos`;
        if(timer == 0){
            loseAudio.play();
            clearInterval(tiempoRegresivoId);
            bloquearTarjetas(numeros);
        }
    },1000)
}
function bloquearTarjetas(){
    for (let i = 0; i<=15; i++){
        let tarjetaBloqueada = document.getElementById(i);
        tarjetaBloqueada.innerHTML = `<img id="imagenjuego" src="assets/img/${numeros[i]}.png" alt="">`;
        tarjetaBloqueada.disabled = true;
    }
}
//Funcion Principal
function destapar(id){
    if(temporizador == false){
        contarTiempo();
        temporizador = true;
    }
    tarjetasDestapadas++;
    console.log(tarjetasDestapadas);
    if(tarjetasDestapadas == 1){
        //mostrar primer boton
        tarjeta1 = document.getElementById(id);
        primerResultado = numeros[id]
        tarjeta1.innerHTML = `<img id="imagenjuego" src="assets/img/${primerResultado}.png" alt="">`;
        //deshabilitar primer boton
        tarjeta1.disabled = true;
    }else if(tarjetasDestapadas == 2){
        //mostrar segundo numero
        tarjeta2 = document.getElementById(id);
        segundoResultado = numeros[id];
        tarjeta2.innerHTML = `<img id="imagenjuego" src="assets/img/${segundoResultado}.png" alt="">`;
        //deshabilitar segundo boton
        tarjeta2.disabled = true;
        //incrementar movimientos
        movimientos++;
        mostrarMovimientos.innerHTML = `Movimientos: ${movimientos}`;
        if(primerResultado == segundoResultado){
            //encerar contador tarjetas destapadas
            tarjetasDestapadas = 0;
            //aumentar aciertos
            aciertos++;
            mostrarAciertos.innerHTML = `Aciertos: ${aciertos}`;
            correctAudio.play();
            if (aciertos == 8) {
                winAudio.play();
                clearInterval(tiempoRegresivoId);
                // Generar un número aleatorio de 4 dígitos
                let numeroAleatorio = Math.floor(Math.random() * (9999 - 1000 + 1)) + 1000;
                mostrarAciertos.innerHTML = `Tu código: ${numeroAleatorio}🥳`;
                mostrarTiempo.innerHTML = `Fantastico! Sólo demoraste ${timerInicial - timer} segundos`;
                mostrarMovimientos.innerHTML = `Movimientos: ${movimientos}😎`;
            }
        }else{
            //mostrar momentaneamente valores y volver a tapar
            setTimeout(()=>{
                tarjeta1.innerHTML = ' ';
                tarjeta2.innerHTML = ' ';
                tarjeta1.disabled = false;
                tarjeta2.disabled = false;
                tarjetasDestapadas = 0;
            },600);
        }
    }
}