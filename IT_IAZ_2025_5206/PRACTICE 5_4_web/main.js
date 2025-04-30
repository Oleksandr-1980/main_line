const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

ctx.beginPath();
ctx.arc(50, 50, 15, 0, Math.PI * 2); // Outer circle
ctx.stroke (); 