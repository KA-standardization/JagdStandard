function call(){
Java.perform(function(){
	var Arith=Java.use('com.android.calculator2.Calculator')
	//var JavaString=Java.use('java.lang.Integer')
	//var result=Arith.a(JavaString.$new(643),JavaString.$new(123))
	var result=Arith.a(10,8)
	console.log(result)
	})
}