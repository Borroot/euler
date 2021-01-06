console.log(
  Array.from(Array(999), (_, index) => index + 1)
    .filter((x) => x % 3 === 0 || x % 5 === 0)
    .reduce((a, b) => a + b)
);
