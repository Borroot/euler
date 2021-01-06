num = 600851475143;
factor = 1;

while (num !== 1) {
  if (num % ++factor === 0) num /= factor;
}

console.log(factor);
