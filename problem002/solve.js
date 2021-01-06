total = 0;
a = 1;
b = 2;

do {
  if (b % 2 === 0) total += b;
  [a, b] = [b, a + b];
} while (b < 4e6);

console.log(total);
