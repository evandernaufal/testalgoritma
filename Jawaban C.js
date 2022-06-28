// EVANDER NAUFAL LASMANTO
// JAWABAN SOAL C

const words = 'Helloh World';
const countWords = [];

for (const element of words) {
    if (countWords[element]) {
        countWords[element] += 1;
    } else {
        countWords[element] = 1;
    }
}

console.log(countWords);
