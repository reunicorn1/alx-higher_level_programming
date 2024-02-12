#!/usr/bin/node

const argv = process.argv;
if (argv.length < 4) {
  console.log(0);
} else {
  let max = Number(argv[2]);
  let secondMax = Number(argv[3]);
  for (let i = 2; argv[i] !== undefined; i++) {
    if (max < Number(argv[i])) {
      secondMax = max;
      max = Number(argv[i]);
    } else if ((Number(argv[i]) > secondMax) && (Number(argv[i]) !== max)) {
      secondMax = Number(argv[i]);
    }
  }
  console.log(secondMax);
}
