const traverse = require("@babel/traverse").default;
const generator = require("@babel/generator").default;
const t = require("@babel/types");
const fs = require('fs');

const roll = require('./calcValue');
const convertCond = require('./conditional');

const gloArr = ['console','eval','parseInt','encodeURIComponent','Object','Function','Boolean','Number','Math','Date','String','RegExp','Array'];

let count = 1;

class TouTiaoDec{
    constructor(ast){
        this.ast = ast;
    }
    showCode(){
        console.log(generator(this.ast).code);
    }
    log(p){
        console.log(generator(p).code)
    }
    saveCode(){
        // let code = generator(this.ast, {jsescOption:{"minimal":true}}).code;
        let code = generator(this.ast).code;
        fs.writeFile('./douyin_dist_22_3_14.js',code,{encoding:'utf8'},(err)=>{
            if(err){
                console.log(err);
            }
        });
    }

    transformRemoveWindow(){
        traverse(this.ast,{
            MemberExpression(path){
                if(path.node.object.name == 'window' && gloArr.indexOf(path.node.property.name)!=-1){
                    path.replaceWith(t.identifier(path.node.property.name));
                }
            }
        })
    }

    /***
     * 三目运算符转if
     */
    conditionalToIf(){
        traverse(this.ast,{
            ConditionalExpression(path){
                let {test,alternate,consequent} = path.node;
                let test_path = path.get("test");
                const evaluateTest = test_path.evaluateTruthy();
                if(evaluateTest === true){
                    path.replaceInline(consequent);
                }
                else if(evaluateTest === false){
                    path.replaceInline(alternate);
                }
                else{
                    let new_consequent;
                    let new_alternate;
                    let if_node;
                    if(t.isConditionalExpression(consequent)){
                        let nodeConsequent = convertCond(path.get('consequent'));
                        new_consequent = t.blockStatement([nodeConsequent]);
                    }else{
                        new_consequent = t.blockStatement([t.expressionStatement(consequent)]);
                    }

                    if(t.isConditionalExpression(alternate)){
                        let nodeAlternate = convertCond(path.get('alternate'));
                        new_alternate = t.blockStatement([nodeAlternate]);
                    }else{
                        new_alternate = t.blockStatement([t.expressionStatement(alternate)]);
                    }

                    let code1 = generator(new_consequent).code;
                    let code2 = generator(new_alternate).code;
                    if_node = t.ifStatement(test,new_consequent,new_alternate);
                    let code3 = generator(if_node).code;
                    path.replaceWithMultiple(if_node);
                }
                path.skip();
            }
        })
    }
    /***
     * 单独语句加大括号
     */
    standardLoop(){
        //单独语句加大括号
        traverse(this.ast,{
            'ForStatement|WhileStatement|ForInStatement'({node}){
                if(!t.isBlockStatement(node.body)){
                    node.body = t.BlockStatement([node.body]);
                }
            },
            IfStatement({node}){
                if(!t.isBlockStatement(node.consequent)){
                    node.consequent = t.BlockStatement([node.consequent]);
                }
                if(node.alternate && !t.isBlockStatement(node.alternate)){
                    node.alternate = t.BlockStatement([node.alternate]);
                }
            }
        })
    }
    calcValue1(){
        traverse(this.ast,{
            UnaryExpression(path){
                let {operator,argument} = path.node;
                if(operator == "!"){
                    let {confident,value} = path.evaluate();
                    if(confident){
                        path.replaceInline(t.valueToNode(value));
                    }
                }
                else if(operator == "void" && argument.type == 'NumericLiteral' && argument.value == 0){
                    let newNode = t.ExpressionStatement(t.Identifier("undefined"))
                    path.replaceWith(newNode);
                }
            }
        })
    }
    calcValue(){
        traverse(this.ast,{
            'BinaryExpression|Identifier|UnaryExpression'(path){
                let {confident,value} = path.evaluate();
                if(confident){
                    path.replaceInline(t.valueToNode(value));
                }
            }
        })
    }
    sequenceToStatement(){
        traverse(this.ast,{
            ExpressionStatement(path){
                let {expression} = path.node;
                if(!t.isSequenceExpression(expression)){
                    return;
                }
                let tmp = [];
                expression.expressions.forEach(express=>{
                    tmp.push(t.ExpressionStatement(express))
                })
                path.replaceWithMultiple(tmp);
            }
        })
    }
    logicalExpression(){
        traverse(this.ast,{
            LogicalExpression(path){
                let {left,operator,right} = path.node;
                if(operator == "&&"){
                    path.replaceWithMultiple(t.IfStatement(left,t.BlockStatement([t.ExpressionStatement(right)]),null))
                }
            }
        })
    }
    assignmentExpression(){
        traverse(this.ast,{
            AssignmentExpression(path){
                if(t.isConditionalExpression(path.node.right)){
                    let {test,consequent,alternate} = path.node.right;
                    let newCon = t.AssignmentExpression("=",path.node.left,consequent);
                    let newAlt = t.AssignmentExpression("=",path.node.left,alternate);
                    path.replaceWithMultiple(t.IfStatement(test,t.BlockStatement([t.ExpressionStatement(newCon)]),t.BlockStatement([t.ExpressionStatement(newAlt)])))
                }
            }
        })
    }
    removeEmpty(){
        traverse(this.ast,{
            EmptyStatement(path){
                path.remove();
            }
        })
    }
    test1(){
        traverse(this.ast,{
            ConditionalExpression(path){
                let {test, consequent, alternate} = path.node;
                const ParentPath = path.parentPath;
                if(t.isAssignmentExpression(ParentPath)){
                    let {operator, left} = ParentPath.node;
                    if (operator === '='){
                        consequent = t.AssignmentExpression('=', left, consequent);
                        alternate = t.AssignmentExpression('=', left, alternate);
                        ParentPath.replaceWith(t.ConditionalExpression(test, consequent, alternate))
                    }
                }
            },
        })
    }
    test2(){
        {
            traverse(this.ast,{
                ConditionalExpression(path) {
                    let { test, consequent, alternate } = path.node;
                    const ParentPath = path.parentPath;
                    if (t.isExpressionStatement(ParentPath)) {
                        if (!t.isExpressionStatement(consequent)) {
                            consequent = t.BlockStatement([t.ExpressionStatement(consequent)]);
                        }
                        if (!t.isExpressionStatement(alternate)) {
                            alternate = t.BlockStatement([t.ExpressionStatement(alternate)]);
                        }
                        ParentPath.replaceInline(t.IfStatement(test, consequent, alternate));
                    }
                }
            })
        }
    }
    calcValue3(){
        traverse(this.ast,{
            BinaryExpression:function(path){
                let result = roll(path.node);
                if(result.canCalc){
                    path.replaceWith(t.numericLiteral(result.value));
                    path.skip();
                }
            }
        })
    }
    numericKey(){
        traverse(this.ast,{
            ObjectProperty(path){
               let {key,value} = path.node;
               if(t.isNumericLiteral(key)){
                    key.extra = undefined;
               } 
               if(t.isNumericLiteral(value)){
                    value.extra = undefined;
                } 
            }
        })
    }
    undefinedIdentifier(){
        traverse(this.ast,{
            ExpressionStatement(path){
                let {expression} = path.node;
                if(t.isIdentifier(expression) && expression.name=='undefined'){
                    if(t.isBlockStatement(path.parentPath.node)){
                        path.parentPath.remove();
                    }
                }
            }
        })
    }
    removeEmptyIf(){
        traverse(this.ast,{
            IfStatement(path){
                let {alternate} = path.node;
                if(t.isBlockStatement(alternate) && alternate.body.length == 0){
                    // delete path.node;
                    path.node.alternate = null;
                }
            }
        })
    }
    MemberExpressionToComputeed(arr){
        traverse(this.ast,{
            MemberExpression(path){
                let {object,property} = path.node;
                if(t.isIdentifier(object) && t.isStringLiteral(property) && arr.indexOf(object.name)!=-1){
                    let name = property.value;
                    path.node.property = t.identifier(name);
                    path.node.computed = false;
                }
            }
        })
    }
    RenameFuncParam(){
        traverse(this.ast,{
            FunctionDeclaration(path){
                let {params} = path.node;
                let scope = path.scope;

                for(var i = 0;i<params.length;i++){
                    var new_name = 'p'+(i+1);
                    var name = params[i].name;
                    scope.rename(name,new_name);
                }
            }
        })
    }
    Rename(){
        traverse(this.ast,{
            'Program|FunctionDeclaration|FunctionExpression'(path){
                let p=1;
                let bindings = path.scope.bindings;
                for(let oldname in bindings){
                    if(!oldname.startsWith('_0x'))
                        continue;
                    let new_name;
                    if(bindings[oldname].kind == 'var' || bindings[oldname].kind == 'let' || bindings[oldname].kind == 'const'){
                        new_name = 'v' + v++;
                    } else if(bindings[oldname].kind == 'param'){
                        new_name = 'p' + p++;
                    } else if(bindings[oldname].kind == 'hoisted'){
                        new_name = 'func' + func++;
                    }
                    path.scope.rename(oldname,new_name);
                }
            }
        })
    }
    RenameBlock(){
        traverse(this.ast,{
                'BlockStatement'(path){
                path.traverse({
                    Identifier(p){
                        let bindings = p.scope.bindings;
                        for(let oldname in bindings){
                            if(!oldname.startsWith('_0x'))
                                continue;
                            let new_name;
                            if(bindings[oldname].kind == 'var' || bindings[oldname].kind == 'let' || bindings[oldname].kind == 'const'){
                                new_name = 'v' + v++;
                            } else if(bindings[oldname].kind == 'param'){
                                new_name = 'p' + p++;
                            } else if(bindings[oldname].kind == 'hoisted'){
                                new_name = 'func' + func++;
                            }
                            p.scope.rename(oldname,new_name);
                        }
                    }
                })
            }
        })
    }
}
let func=1,v=1;
module.exports = TouTiaoDec