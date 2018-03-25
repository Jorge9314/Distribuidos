let meanMinutes = (dates) => {
  var meanMinutesVal = 0;
  for (var i = 0; i < dates.length; i++) {
    meanMinutesVal += dates[i].getMinutes();
  }
  return parseInt(meanMinutesVal/dates.length);
}

let meanHours = (dates) => {
  var meanHoursVal = 0;
  for (var i = 0; i < dates.length; i++) {
    meanHoursVal += dates[i].getHours();
  }
  return parseInt(meanHoursVal/dates.length);
}

let meanMonths = (dates) => {
  var meanMonthsVal = 0;
  for (var i = 0; i < dates.length; i++) {
    meanMonthsVal += dates[i].getMonth();
  }
  return parseInt(meanMonthsVal/dates.length);
}

let meanDays = (dates) => {
  var meanDaysVal = 0;
  for (var i = 0; i < dates.length; i++) {
    meanDaysVal += dates[i].getDate();
  }
  return parseInt(meanDaysVal/dates.length);
}

let meanSeconds = (dates) => {
  var meanSecondsVal = 0;
  for (var i = 0; i < dates.length; i++) {
    meanSecondsVal += dates[i].getSeconds();
  }
  return parseInt(meanSecondsVal/dates.length);
}

let meanYear = (dates) => {
  var meanYearVal = 0;
  for (var i = 0; i < dates.length; i++) {
    meanYearVal += dates[i].getFullYear();
  }
  return parseInt(meanYearVal/dates.length);
}

module.exports = {
  meanMinutes,
  meanMonths,
  meanDays,
  meanSeconds,
  meanYear,
  meanHours
};
