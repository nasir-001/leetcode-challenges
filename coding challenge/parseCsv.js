function parseCSV(input, separator, quote) {
  separator = separator || ',';
  quote = quote || '"';

  var data = [];
  var row = [];
  var value = [];
  var inString = false;

  function pushValue() {
    row.push(value.join(""));
    value = [];
  }

  function pushRow() {
    pushValue();
    data.push(row);
    row = [];
  }

  for(var i=0; i<input.length; i++) {
    var ch = input[i];
    if(inString) {
      if(ch === quote) {
        if(input[i+1] === quote) {
          value.push(quote);
          i++;
        } else {
          inString = false;
        }
      } else {
        value.push(ch);
      }
    } else {
      if(ch === '\n') {
        pushRow();
      } else if(ch === separator) {
        pushValue();
      } else if(ch === quote) {
        inString = true;
      } else {
        value.push(ch);
      }
    }
  }
  pushRow()
  return data
}