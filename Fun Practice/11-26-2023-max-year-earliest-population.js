// 1854. Maximum Population Year
// Easy
// Topics
// Companies
// Hint
// You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

// The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

// Return the earliest year with the maximum population.

function maximumPopulation(logs) {
  let yearMap = {};

  for (let i = 1950; i <= 2050; i++) {
    yearMap[i] = 0;
  }

  logs.forEach(([birth, death]) => {
    console.log(birth, death);
    yearMap[birth]++;
    yearMap[death]--;
  });

  let maxPopYear;
  let maxPop = 0;
  let currentPop = 0;

  for (year in yearMap) {
    currentPop += yearMap[year];
    if (currentPop > maxPop) {
      maxPop = currentPop;
      maxPopYear = year;
    }
  }

  return maxPopYear;
}

console.log(
  maximumPopulation([
    [1950, 1961],
    [1960, 1971],
    [1970, 1981],
  ])
);
