const { VM,VMScript } = require('vm2');
const codefile = `${__dirname}/code_douyin.js`;
const windowfile = `${__dirname}/window.js`;
var fs = require("fs");
const script = new VMScript(fs.readFileSync(windowfile, 'utf-8') + fs.readFileSync(codefile, 'utf-8'), "Kaiser");
// const script = new VMScript(fs.readFileSync(windowfile, 'utf-8') + fs.readFileSync(codefile, 'utf-8'), `${__dirname}/Kaiser.js`);
const vm = new VM();
// debugger
vm.run(script);
// debugger