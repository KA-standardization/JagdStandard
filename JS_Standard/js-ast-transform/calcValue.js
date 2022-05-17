const t = require("@babel/types");

function roll(path){
    let canCalc = false;
    let leftValue = 0;
    let rightValue = 0;
    let value = 0;
    let operator = path.operator;

    let {left,right} = path;
    if(t.isBinaryExpression(left)){
        let r1 = roll(left);
        if(r1.canCalc){
            leftValue = r1.value;
        }else{
            return {
                canCalc,
                value
            } 
        }
    }else if(t.isNumericLiteral(left) || t.isUnaryExpression(left)){
        let r2 = getValue(left);
        leftValue = r2;
    }else{
        return {
            canCalc,
            value
        } 
    }

    if(t.isBinaryExpression(right)){
        let r1 = roll(right);
        if(r1.canCalc){
            rightValue = r1.value;
        }else{
            return {
                canCalc,
                value
            } 
        }
    }else if(t.isNumericLiteral(right) || t.isUnaryExpression(right)){
        let r2 = getValue(right);
        rightValue = r2;
    }else{
        return {
            canCalc,
            value
        } 
    }

    canCalc = true;
    value = eval(`${leftValue}${operator}${rightValue}`);
    
    return {
        canCalc,
        value
    }
}

function getValue(path){
    if(t.isNumericLiteral(path)){
        return path.value;
    }else if(t.isUnaryExpression(path)){
        let {operator,argument} = path;
        if(operator == '-'){
            return 0-argument.value;
        }
    }
}

module.exports = roll;