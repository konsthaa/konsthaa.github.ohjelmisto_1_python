'use strict';

function out(s){document.getElementById('out').innerHTML=s;}
const task=[];

/* 1 */
task[1]=function(){
  console.log("I'm printing to console!");
  out('<p>Check console (F12)</p>');
};

/* 2 */
task[2]=function(){
  const name=prompt('What is your name?')||'';
  out('<h3>Hello, '+name+'!</h3>');
};

/* 3 */
task[3]=function(){
  const a=+prompt('First integer:');
  const b=+prompt('Second integer:');
  const c=+prompt('Third integer:');
  if(isNaN(a)||isNaN(b)||isNaN(c)) return out('<p>Enter numbers!</p>');
  const sum=a+b+c, prod=a*b*c, avg=sum/3;
  out('<p>Sum: <b>'+sum+'</b></p><p>Product: <b>'+prod+'</b></p><p>Average: <b>'+(avg).toFixed(2)+'</b></p>');
};

/* 4 */
task[4]=function(){
  const name=prompt('Student name:')||'';
  const r=Math.floor(Math.random()*4)+1;
  const h=['Gryffindor','Slytherin','Hufflepuff','Ravenclaw'];
  out('<h3>'+name+', you are '+h[r-1]+'.</h3>');
};

/* 5 */
task[5]=function(){
  const y=+prompt('Year:');
  const leap=(y%4===0 && y%100!==0)||(y%400===0);
  out('<h3>'+y+' '+(leap?'is':'is not')+' a leap year.</h3>');
};

/* 6 */
task[6]=function(){
  if(!confirm('Calculate square root?')) return out('<h3>The square root is not calculated.</h3>');
  const n=+prompt('Number:');
  if(isNaN(n)) return out('<p>Invalid!</p>');
  if(n<0) return out('<p>Square root of negative is not defined.</p>');
  out('<h3>Square root of '+n+' = '+Math.sqrt(n).toFixed(4)+'</h3>');
};

/* 7 */
task[7]=function(){
  const d=+prompt('How many dice?');
  if(isNaN(d)||d<1) return out('<p>Invalid!</p>');
  let s=0;
  for(let i=0;i<d;i++) s+=Math.floor(Math.random()*6)+1;
  out('<h3>Sum of '+d+' dice: <b>'+s+'</b></h3>');
};

/* 8 */
task[8]=function(){
  const s=+prompt('Start year:'), e=+prompt('End year:');
  if(isNaN(s)||isNaN(e)||s>e) return out('<p>Invalid range!</p>');
  let list='';
  for(let y=s;y<=e;y++){
    if((y%4===0 && y%100!==0)||(y%400===0)) list+='<li>'+y+'</li>';
  }
  out(list?'<ul>'+list+'</ul>':'<p>No leap years.</p>');
};

/* 9 */
task[9]=function(){
  const n=+prompt('Integer:');
  if(isNaN(n)||n<=1) return out('<h3>'+n+' is not prime.</h3>');
  let p=true;
  for(let i=2;i*i<=n;i++) if(n%i===0){p=false;break;}
  out('<h3>'+n+' '+(p?'is':'is not')+' a prime number.</h3>');
};

/* 10 */
task[10]=function(){
  const dice=+prompt('Number of dice:');
  const target=+prompt('Target sum:');
  if(isNaN(dice)||isNaN(target)||dice<1||target<dice||target>6*dice) return out('<p>Invalid!</p>');
  const tries=10000;
  let ok=0;
  for(let i=0;i<tries;i++){
    let sum=0;
    for(let j=0;j<dice;j++) sum+=Math.floor(Math.random()*6)+1;
    if(sum===target) ok++;
  }
  const prob=(ok/tries*100).toFixed(2);
  out('<h3>Probability to get sum '+target+' with '+dice+' dice is <b>'+prob+'%</b></h3>');
};