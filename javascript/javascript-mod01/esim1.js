/**
Tässä tiedostossa on ensimmäisiä JavaScript-esimerkkejä
*/
'use strict'; // muista käyttää aina tiedoston alussa

// Käytä const-avainsanaa muuttujan esittelyyn, paitsi jos sen arvoa
// tarttee myöhemmin muuttaa
let teksti = 'Moi maailma!'

console.log(teksti);
teksti = 'Moi Joku';
// Selaimen oma alert-ikkuna (popup)
//alert('Kukkuu!!');
document.querySelector('.output').textContent = teksti;

let name = 'Matti';
let age = 23;
let greeting = `Moi ${name}, ${age} v!`;
console.log(greeting);

// syötteen lukeminen
name = prompt('Anna nimesi:');
//console.log('käyttäjän syöte', userInput);
age = parseInt(prompt('Anna ikäsi:'));

if (10 < age && age < 100) {
    greeting = `Moi ${name}, ikäsi vuoden päästä ${age + 1} v!`;
    document.querySelector('.output').textContent = greeting;
} else {
    console.log('Olet liian nuori tälle sivulle.');
}

// Math-luokka
// noppaesimerkki 1-6
const result =  Math.ceil(Math.random()*6);
console.log('nopanheitto', result);

switch (result) {
    case 6:
        console.log('Voitit 100 e');
        break;
    case 5:
        console.log('Voitit 50 e');
        break;
    case 4:
        console.log('voitit 20 e');
        break;
    default:
        console.log('et voittanut mitään');
}

// while, käytä kun et tiedä täysin monta kertaa toteutetaan
// toistetaan aina kun ehto on tosi
// eroaa do while sillä että ei välttämättä tuteuteta kertaakaan
// meillä on aina alkuehto joka tsekataan

let count = 0;

while (count < 5) {

    console.log('Laskuri:', count)
    count++;
}


// do-while
// looppi halutaan suorittaa ainakin kerran ennen ehtoa
let result2 = 0;

do {
    console.log('Tämä tulostuu ainakin kerran vaikka ehto ei täyttyisi');
    count++;
} while (count < 5);


let result = 3;

do {

    result2 = Math.floor(Math.random()*6)+1;
    console.log(result);
}   while (result < 6);

let numero = 3;

do {
    console.log('Tämä tulostuu ainakin kerran vaikka ehto ei täyttyisi');
    numero++;
}   while (numero < 6);

// Tilanteisiin jossa haluat toistaa loopin x määrä kertoja
// esimerkiksi kun käydään taulukon indeksit läpi

for (let i = 1; i <= 10 ; i++) {     //miten kauan 1 on pienempi kuin 10
    console.log('Luku on', i);
}

for (let i = 10; i >= 1 ; i--) {     // miten kauan 10 on isompi kuin 1
    console.log(1);
}