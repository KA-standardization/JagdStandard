window = this;
// window.document = {referrer:""};
// window.location = {href:"",protocol:"https:"};
// window.navigator = {userAgent:""};

// 防止检测: 后代理检测不到先代理
// window = new Proxy(window, {
//     set(target,property,value) {
//         console.log("set", target, property, value);
//         return Reflect.set(...arguments);
//     },
//     get(target,property,receiver) {
//         console.log("get", target, property, receiver);
//         return target[property];
//     }
// });

function vmProxy(o) {
    return new Proxy(o, {
        set(target, property, value) {
            console.log("set", target, property, value);
            return Reflect.set(...arguments);
        },
        get(target, property, receiver) {
            console.log("get", target, property, receiver);
            return target[property];
        }
    });
}

Object.defineProperties(window, {
    [Symbol.toStringTag]: {
        value: "window",
        configurable: true
    }
});
window = vmProxy(window);

document = vmProxy({});

location = vmProxy({});

navigator = vmProxy({
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
});

Object.getOwnPropertyDescriptor_ = Object.getOwnPropertyDescriptor;
Object.getOwnPropertyDescriptor = function (o, p) {
    if (o.toLocaleString() == "[object Navigator]") {
        return undefined;
    }
    Object.getOwnPropertyDescriptor_.apply(this, arguments);
};

// 保护伪造函数
!(() => {
    "use strict";
    const $toString = Function.toString;
    const myFunction_toString_symbol = Symbol('('.concat('', ')_', (Math.random() + '').toString(36)));
    const myToString = function () {
        return typeof this == 'function' && this[myFunction_toString_symbol] || $toString.call(this);
    };
    function set_native(func, key, value) {
        Object.defineProperty(func, key, {
            "enumerable": false,
            "configurable": true,
            "writable": true,
            "value":value
        })
    };
    delete Function.prototype['toString'];
    set_native(Function.prototype, "toString", myToString);
    set_native(Function.prototype.toString, myFunction_toString_symbol, "function toString() { [native code] }");
    this.func_set_native = (func) => {
        set_native(func, myFunction_toString_symbol, `function ${myFunction_toString_symbol, func, name || ''}(){ [native code] }`);
    };
}).call(this);

const descriptor_1 = Object.getOwnPropertyDescriptor(navigator, "userAgent");


