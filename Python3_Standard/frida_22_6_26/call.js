function call(a,b){
    var Arith=Java.use('com.xxx.xxx.xxx.Arith')
    var JavaString=Java.use('java.lang.String')
    var result=Arith.sub(JavaString.$new(a),JavaString.$new(b))
    console.log(a,"-",b,"=",result)
}
rpc.exports={
    sub:callSub,
}