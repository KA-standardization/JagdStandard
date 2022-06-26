# Frida-hook

> 1.Objection定位

```
# objection连接程序
objection -g com.xxx.xxx explore
# objection遍历APP的所有activity
android hooking list activities
# 启动目标活动
android intent launch_activity com.xxx.xxx.XXXActivity
# 验证源码和真实运行的代码,是否存在某个函数
android hooking list class_methods com.xxx.xxx.XXXActivity
# 确认函数被调用
android hooking watch class_method com.xxx.xxx.XXXActivity.func --dump-args --dump-return --dump-backtrace
# 获取一个应用内存中的所有类,防止冲刷保存替换原有的 ~/.objection目录中objection.log
android hooking list classes
# 退出objection注入模式,查看保存的日志
cat ~/.objection/objection.log|grep com.xxx.xxx.xxx.class
# 确定目标class存在后,通过objection判断class是否存在目标func
android hooking list class_methods com.xxx.xxx.xxx.class
# 确定存在目标func,对该函数hook
android hooking watch class_method com.xxx.xxx.xxx.class.func --dump-args --dump-return --dump-backtrace
# 最终确定func通过func(java.lang.String,java.lang.Long)实现
```



> 2.frida脚本修改参数,主动调用

```
# 取消objection的hook,frida注入APP
frida -UF -l hook.js # -UF: 使用USB模式,并注入手机最前台应用
  function main(){
    Java.perform(function (){
      var Arith =Java.use('com.example.junior.util.Arith')
      Arith.sub.implementation=function(str,str2){
        var result=this.sub(str,str2)
        console.log('str,str2,result ->',str,str2,result)
        // java调用栈 
        // 将Android开发中获取调用栈的函数Log.getStackTraceString(Throwable e)翻译为JS
       console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()))
        return result
      }
    })
  }
  setImmediate(main)
# 使用frida对参数和返回值进行进一步修改
  function main(){
      Java.perform(function (){
        var Arith =Java.use('com.example.junior.util.Arith')
        Arith.sub.overload('java.lang.String','java.lang.String').implementation=function(str,str2){
        var result=this.sub(str,"111")
        // 复杂类型
        // var JavaString=Java.use('java.lang.String')
        // var result=this.sub(str,JavaString.$new('111'))
    	 console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()))
    		return result
        }
      })
   }
  setImmediate(main)
# 使用frida对函数进行调用
frida -UF -l call.js
	function call(){
	Java.perform(function(){
		var Arith=Java.use('com.xxx.xxx.xxx.Arith')
		var JavaString=Java.use('java.lang.String')
		var result=Arith.sub(JavaString.$new('123'),JavaString.$new('111'))
		console.log(result)
		})
	}
# call()
```

> Python规模化利用

```
# 修改call.js为可以多次调用,并将完成主动调用的函数修改为导出的rpc函数
# loader.py
```

