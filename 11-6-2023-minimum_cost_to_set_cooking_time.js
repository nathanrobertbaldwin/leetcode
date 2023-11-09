function genMinuteMoreCombos(secs) {
  let combos = [];

  // Represented as 1 more minute and 60 fewer seconds.

  let minutes = Math.floor(secs / 60);
  let seconds = secs % 60;
  if (minutes === 0) minutes = "";
  else minutes = minutes.toString();
  if (seconds < 10) seconds = "0" + seconds.toString();
  else seconds = seconds.toString();

  let time = minutes + seconds;
  console.log(time);
  while (time.length <= 4) {
    combos.push(time);
    time = "0" + time;
  }

  return combos;
}

function genMinuteLessCombos(secs) {
  let combos = [];

  let minutes = Math.floor(secs / 60);
  let seconds = secs % 60;

  if (seconds <= 39) {
    if (minutes > 0) {
      minutes = (minutes - 1).toString();
      seconds = ((secs % 60) + 60).toString();
      if (minutes === "0") combos.push(seconds);
    } else {
      minutes = "";
      seconds = seconds.toString();
    }

    let time = minutes + seconds;

    while (time.length <= 4) {
      combos.push(time);
      time = "0" + time;
    }
  }

  return combos;
}

function minCostSetTime(startAt, moveCost, pushCost, targetSeconds) {
  let combos = [
    ...genMinuteMoreCombos(targetSeconds),
    ...genMinuteLessCombos(targetSeconds),
  ];
  console.log(combos);
  let minCost = Infinity;

  for (let i = 0; i < combos.length; i++) {
    let currCombo = combos[i];
    let currCost = 0;
    let priorNum = startAt;

    for (let j = 0; j < currCombo.length; j++) {
      let currNum = parseInt(currCombo[j]);
      if (currNum === priorNum) currCost += pushCost;
      else currCost += moveCost + pushCost;
      priorNum = currNum;
    }

    if (currCost <= minCost) minCost = currCost;
    currCost = 0;
  }

  return minCost;
}

// startAt =
// 0
// moveCost =
// 9985
// pushCost =
// 9986
// targetSeconds =
// 41

console.log(minCostSetTime(0, 9985, 9986, 41));
