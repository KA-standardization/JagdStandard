const t = require("@babel/types");
const traverse = require("@babel/traverse").default;
const generator = require("@babel/generator").default;

function convertCond(path){
    let {test,alternate,consequent} = path.node;
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
    return if_node;
}

module.exports = convertCond;