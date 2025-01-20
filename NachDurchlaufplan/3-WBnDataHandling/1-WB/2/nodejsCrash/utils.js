// utils.js

function grandom() {
    return Math.floor(Math.random() * 100) + 1;
}

function ctof(c){
    return(c*9)/5 + 32;
}

module.exports = {
    grandom,
    ctof,
};

console.log('utils.js is loaded');