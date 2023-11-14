#!/usr/bin/node

exports.callMeMoby = function callMeMoby (x, theFunction) {
  for (let k = 0; k < x; k++) {
    theFunction();
  }
};
