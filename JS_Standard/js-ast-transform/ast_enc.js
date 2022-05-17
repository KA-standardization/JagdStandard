const traverse = require("@babel/traverse").default;
const generator = require("@babel/generator").default;
const t = require("@babel/types");
const fs = require('fs');

class AstEnc{
    constructor(ast){
        this.ast = ast;
    }
    showCode(){
        console.log(generator(this.ast).code);
    }
    saveCode(){
        let code = generator(this.ast).code;
        fs.writeFile('./dist.js',code,{encoding:'utf8'},(err)=>{
            if(err){
                console.log(err);
            }
        });
    }
    

}