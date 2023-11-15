#!/usr/bin/node
exports.esrever = function (list) {
  const reversedVer = [];
  for (let k = list.length - 1; k >= 0; k--) {
    reversedVer.push(list[k]);
  }
  return reversedVer;
};
