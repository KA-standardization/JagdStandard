function unicodeEnc(str) {
  for (var value = "", i = 0; i < str.length; i++) {
    value += "\\u" + ("0000" + parseInt(str.charCodeAt(i)).toString(16)).substr(-4);
  }
  return value;
}
function hexEnc(str) {
    for(var value = "",i=0;i<str.length;i++){
        value+= "\\x" + str.charCodeAt(i).toString(16)
    }
    return value;
}
function stringToByte(str){
  for(var value=[],i=0;i<str.length;i++){
    value.push(str.charCodeAt(i));
  }
  return value;
}
module.exports = {
    unicodeEnc,
    hexEnc,
    stringToByte
}