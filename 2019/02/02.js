function getNextIntCodes(intcodes, index = 0) {
  const command = intcodes[index];
  const first_position = intcodes[index + 1];
  const second_position = intcodes[index + 2];
  const next_position = intcodes[index + 3];
  if (command === 1) {
    intcodes[next_position] =
      intcodes[first_position] + intcodes[second_position];
  } else if (command === 2) {
    intcodes[next_position] =
      intcodes[first_position] * intcodes[second_position];
  } else {
    return intcodes;
  }
  index += 4;
  return getNextIntCodes(intcodes, index);
}

test("1,0,0,0,99 become 2,0,0,0,99", () => {
  expect(getNextIntCodes([1, 0, 0, 0, 99])).toEqual([2, 0, 0, 0, 99]);
});
test("2,3,0,3,99 become 2,3,0,6,99", () => {
  expect(getNextIntCodes([2, 3, 0, 3, 99])).toEqual([2, 3, 0, 6, 99]);
});
test("2,4,4,5,99,0 become 2,4,4,5,99,9801", () => {
  expect(getNextIntCodes([2, 4, 4, 5, 99, 0])).toEqual([2, 4, 4, 5, 99, 9801]);
});
test("1,1,1,4,99,5,6,0,99 become 30,1,1,4,2,5,6,0,99", () => {
  expect(getNextIntCodes([1, 1, 1, 4, 99, 5, 6, 0, 99])).toEqual([
    30,
    1,
    1,
    4,
    2,
    5,
    6,
    0,
    99
  ]);
});
test("result", () => {
  let input = [
    1,
    0,
    0,
    3,
    1,
    1,
    2,
    3,
    1,
    3,
    4,
    3,
    1,
    5,
    0,
    3,
    2,
    10,
    1,
    19,
    1,
    5,
    19,
    23,
    1,
    23,
    5,
    27,
    2,
    27,
    10,
    31,
    1,
    5,
    31,
    35,
    2,
    35,
    6,
    39,
    1,
    6,
    39,
    43,
    2,
    13,
    43,
    47,
    2,
    9,
    47,
    51,
    1,
    6,
    51,
    55,
    1,
    55,
    9,
    59,
    2,
    6,
    59,
    63,
    1,
    5,
    63,
    67,
    2,
    67,
    13,
    71,
    1,
    9,
    71,
    75,
    1,
    75,
    9,
    79,
    2,
    79,
    10,
    83,
    1,
    6,
    83,
    87,
    1,
    5,
    87,
    91,
    1,
    6,
    91,
    95,
    1,
    95,
    13,
    99,
    1,
    10,
    99,
    103,
    2,
    6,
    103,
    107,
    1,
    107,
    5,
    111,
    1,
    111,
    13,
    115,
    1,
    115,
    13,
    119,
    1,
    13,
    119,
    123,
    2,
    123,
    13,
    127,
    1,
    127,
    6,
    131,
    1,
    131,
    9,
    135,
    1,
    5,
    135,
    139,
    2,
    139,
    6,
    143,
    2,
    6,
    143,
    147,
    1,
    5,
    147,
    151,
    1,
    151,
    2,
    155,
    1,
    9,
    155,
    0,
    99,
    2,
    14,
    0,
    0
  ];
  input[1] = 12;
  input[2] = 2;
  expect(getNextIntCodes(input)[0]).toBe(9706670);
});

function randomIntFromInterval(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

test("find noum verb", () => {
  let input = [
    1,
    0,
    0,
    3,
    1,
    1,
    2,
    3,
    1,
    3,
    4,
    3,
    1,
    5,
    0,
    3,
    2,
    10,
    1,
    19,
    1,
    5,
    19,
    23,
    1,
    23,
    5,
    27,
    2,
    27,
    10,
    31,
    1,
    5,
    31,
    35,
    2,
    35,
    6,
    39,
    1,
    6,
    39,
    43,
    2,
    13,
    43,
    47,
    2,
    9,
    47,
    51,
    1,
    6,
    51,
    55,
    1,
    55,
    9,
    59,
    2,
    6,
    59,
    63,
    1,
    5,
    63,
    67,
    2,
    67,
    13,
    71,
    1,
    9,
    71,
    75,
    1,
    75,
    9,
    79,
    2,
    79,
    10,
    83,
    1,
    6,
    83,
    87,
    1,
    5,
    87,
    91,
    1,
    6,
    91,
    95,
    1,
    95,
    13,
    99,
    1,
    10,
    99,
    103,
    2,
    6,
    103,
    107,
    1,
    107,
    5,
    111,
    1,
    111,
    13,
    115,
    1,
    115,
    13,
    119,
    1,
    13,
    119,
    123,
    2,
    123,
    13,
    127,
    1,
    127,
    6,
    131,
    1,
    131,
    9,
    135,
    1,
    5,
    135,
    139,
    2,
    139,
    6,
    143,
    2,
    6,
    143,
    147,
    1,
    5,
    147,
    151,
    1,
    151,
    2,
    155,
    1,
    9,
    155,
    0,
    99,
    2,
    14,
    0,
    0
  ];

  for (let noun = 0; noun < 100; noun++) {
    input[1] = noun;
    for (let verb = 0; verb < 100; verb++) {
      input[2] = verb;
      if (getNextIntCodes([...input])[0] === 19690720) {
        console(`answer ${100 * noun + verb}`);
      }
    }
  }
});
