const fs = require('fs');
const {parse} = require('@babel/parser');
const traverse = require("@babel/traverse").default;
const generator = require("@babel/generator").default;
const t = require("@babel/types");
const TouTiaoDec = require('./toutiao_dec');

let code = fs.readFileSync('./douyin_22_3_14_source.js',{encoding:'utf8'});

let ast = parse(code);

let dec = new TouTiaoDec(ast);
/**
 * tiktok
 */
dec.calcValue3();//把多个可计算的值转成一个
dec.standardLoop();//for、if语句加大括号
dec.numericKey();//把对象定义的16进制key和value转成十进制
dec.conditionalToIf();//三目运算符转ifelse,但因为有逻辑运算符的转换不了，所以下边需要再转一遍
dec.logicalExpression();//逻辑&&转if
dec.sequenceToStatement();//逗号表达式转语句
dec.conditionalToIf();//
dec.calcValue1();//void 0 转undefined,!0转true,!1转false
dec.undefinedIdentifier();//else语句里的undefined删掉
dec.removeEmptyIf();//删掉空的else
dec.MemberExpressionToComputeed(['window','Date','Math','String','navigator','JSON','document','Object','Array','Reflect'])
dec.Rename();
dec.RenameBlock();


/**
 * 巨量算数 
 * */
// dec.standardLoop();//for、if语句加大括号
// dec.conditionalToIf();//三目运算符转ifelse,但因为有逻辑运算符的转换不了，所以下边需要再转一遍
// dec.logicalExpression();//逻辑&&转if
// dec.sequenceToStatement();//逗号表达式转语句
// dec.conditionalToIf();//
// dec.calcValue1();//void 0 转undefined,!0转true,!1转false
// dec.undefinedIdentifier();//else语句里的undefined删掉
// dec.removeEmptyIf();//删掉空的else
// dec.MemberExpressionToComputeed(['window','Date','Math','String','navigator','JSON','document','Object','Array','Reflect'])



// dec.sequenceToStatement();
// dec.assignmentExpression();
// dec.removeEmpty();
// dec.test1();
// dec.test2();
// dec.transformRemoveWindow();
dec.saveCode();