largest = -Infinity;
for (let a = 900; a < 1000; a++) {
  for (let b = 900; b < 1000; b++) {
    normal = a * b;
    reversed = String(normal).split("").reverse().join("");
    if (normal == reversed && normal > largest) {
      largest = normal;
    }
  }
}
console.log(largest);
