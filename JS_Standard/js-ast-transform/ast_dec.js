const traverse = require("@babel/traverse").default;
const generator = require("@babel/generator").default;
const t = require("@babel/types");
const fs = require('fs');

const gloArr = ['console','eval','parseInt','encodeURIComponent','Object','Function','Boolean','Number','Math','Date','String','RegExp','Array'];
var _ac = ["getAttribute", "ActiveXObject", "doact", "bat:", "-1,2,-94,-126,", "getforminfo", "Java Applet Plug-in", "me_cnt", "onLine", "Avenir Next", "Papyrus", "pointerType", "mn_mc_lmt", "hpd", ",s7:", "getFloatVal", "getContext", "data", "Corsiva Hebrew", "hn", "persistent-storage", "non:", "=", "Silverlight Plug-In", "ab", "sf4", "bm", "Unity Player", "Widevine Content Decryption Module", "keyup", "childNodes", "do_dis", "Birch Std", "is not a valid enum value of type PermissionName", "vcact", "\\\\\"", "spawn", "-1,2,-94,-109,", "cns", "click", "hvc", "ce_js_post", "touchend", "toFixed", "gyroscope", "x", "mozConnection", "WebKit-integrierte PDF", "cc", "\"}", "mozHidden", "Open Sans", "PI", "send", "get_stop_signals", "font", "d2", "sendBeacon", "onload", "mme_cnt_lmt", "requestMediaKeySystemAccess", "isTrusted", "fillText", "display", "{\"session_id\" : \"", "aj_ss", "mouseup", "Roboto", "~", "Ubuntu Regular", "doa_throttle", "ke_vel", "js_post", "shift", "chrome", "-1,2,-94,-102,", "Ubuntu Medium", "id", "Avenir", "-", "rve", "sort", "credentials", "POST", "mn_s", "map", "prevfid", "onmousedown", "message", "/", "mozRTCPeerConnection", "storeWebWideTrackingException", "query", "bd", "pi", "cookieEnabled", "accelerometer", "==", "gbrv", "hasOwnProperty", "vc", "plen", "mmmmmmmmlli", "event", "prompt", "90px", "ver", "Constructor", "hkd", "//", "appendChild", "6pt Arial", "; ", "Windows Media Player Plug-in Dynamic Link Library", "mn_w", "Quicksand", "mact", "\",\"sensor_data\" : \"", "mn_ct", "hts", "ArialHebrew-Light", "onkeypress", "iPhotoPhotocast", "mn_init", "off", "<init/>", "aj_lmt_tact", "pme_cnt_lmt", "z1", "Apple Gothic", "div", "startTracking", "ins", "-1,2,-94,-111,", "enGetLoc", "screen", "bc", "Wingdings 2", "dcs", "mn_tcl", "_", "serviceWorker", "pme_cnt", "fpValCalculated", "pageX", "encode", "-1,2,-94,-100,", "email", "pointerup", "hmd", ";", "alpha", "Damascus", "mn_update_challenge_details", "bmisc", "pointerdown", "defaultValue", "Gill Sans MT", "aj_lmt_dmact", "plugins", "span", "arc", "fidcnt", "vib:", "default", "enReadDocUrl", "splice", "driver", "apicall_bm", "x12:", "pduce_cnt_lmt", "getVoices", "registerProtocolHandler", "mn_abck", "sc:", "msHidden", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", "hpu", "onkeyup", "uar", "exp", "cma", "startdoadma", "Times", "fm", "fpcf", "psub", "touchstart", "runFonts", "timezoneOffsetKey", "calc_fp", "emit", "cdoa", "slice", "camera", "dm_dis", "opc:", "x11:", "AdobeAAMDetect", "cf_url", "touchmove", "getmr", "-1,2,-94,-108,", "Monaco", "length", "keydown", "outerWidth", "acos", "rgb(102, 204, 0)", "fsp", "od", "getStorageUpdates", "afSbep8yjnZUjq3aL010jO15Sawj2VZfdYK8uY90uxq", "Calibri", "then", "-1,2,-94,-103,", "FileReader", "hf", "Chrome PDF Viewer", "device-info", "wgl", "Default Browser Helper", ":", "aj_lmt_doact", "MSIE", "isIgn", "XMLHttpRequest", "callPhantom", "Native Client", "msvisibilitychange", "denied", "text", "mn_lcl", "y", "cs", "webstore", "enAddHidden", "toString", "-1,2,-94,-121,", "rVal", "hc", "mn_rts", "RealPlayer Version Plugin", "Courier New", "-1,2,-94,-114,", "Geneva", "appMinorVersion", "dma_throttle", ",loc:", "Shree Devanagari 714", "wl", "search", "loc", "webrtcKey", "np", "altKey", "tst", "</bpd>", "get_cf_date", "mediaDevices", "aj_indx_tact", "clientY", "Palatino", "params_url", "RealPlayer(tm) G2 LiveConnect-Enabled Plug-In (32-bit)", "fillRect", "dm:", "bdm", "informinfo", "substring", "button", "aj_indx_dmact", "Serif", "webkitTemporaryStorage", "<setSDFN>", "background-sync", "doNotTrack", "getdurl", "ckie", "ambient-light-sensor", "Menlo", "-1,2,-94,-105,", "replace", "mozIsLocallyAvailable", ",", "Lobster", "aj_indx_doact", "webkitRTCPeerConnection", "forEach", "document", "selenium", "now", "-1,2,-94,-119,", "aj_indx", "hte", "acceleration", "ta", "string", "body", "function", "shiftKey", "floor", "to", "rgb(120, 186, 176)", "_abck", "nav_perm", "session_id", "mn_lc", ",s1:", "auth", "Helvetica Neue", "wv", "mn_il", ",s2:", "innerHeight", "te_cnt", "Version/4.0", "PointerEvent", "type", "doadma_en", "doe_vel", "chknull", "Nimbus Roman No 9 L", "Palatino-Bold", "clientX", "fc:", "Cantarell", "language", "hkp", "Source Sans Pro", "fas", "{\"sensor_data\":\"", "https://", "withCredentials", "pixelDepth", "getElementsByTagName", "DeviceOrientationEvent", "mr", "charCode", "toDataURL", "xagg", "mn_cd", "Century Gothic", "-1,2,-94,-115,", "getBattery", "clientWidth", "Lato", "ceil", "Microsoft.XMLHTTP", "createElement", "Google Talk Plugin Video Renderer", "innerHTML", "mn_pr", "stroke", "tduce_cnt_lmt", "mn_stout", ",cpen:", "kact", "mduce_cnt", "clipboard", "wen", "mn_cc", "parse", "documentMode", "pd", "m,Ev!xV67BaU> eh2m<f3AG3@", "get_type", "mn_tout", "brave", "-1,2,-94,-112,", "pluginInfo", "parse_gp", "required", "\\'", "mn_al", "Fantasque Sans Mono", "webkitvisibilitychange", "removeChild", "mousedown", "n_ck", "Mozilla Default Plug-in", "mn_rt", "touchcancel", "Batang", "-1,2,-94,-124,", "productSub", "Century", "hardwareConcurrency", "ke_cnt", "Monospace", "fillStyle", "tel", "#f60", "-1,2,-94,-118,", "hasIndexedDB", "clipboard-write", "t_en", "toElement", "tme_cnt", "htc", "updatet", "api_public_key", "random", "Cambria", "isBrave", "Shockwave Flash", "granted", "join", ",\"auth\" : \"", "width", "mn_lg", "altFonts", "Java Plug-in 2 for NPAPI Browsers", "firstLoad", "Bell MT", "default_session", "round", "mn_wt", ",it0", "cka", "msManipulationViewsEnabled", "<@nv45. F1n63r,Pr1n71n6!", "$cdc_asdjflasutopfhvcZLmcfl_", "cdma", "</setSDFN>", ",0", "offsetWidth", "application/json", "t_dis", "mduce_cnt_lmt", "fonts", "gd", "z", "16pt Arial", "navigator", "-1,2,-94,-106,", "Authorization", "cache", "sed", "start_ts", "dme_cnt", "deviceorientation", "strokeStyle", "onfocus", "mozInnerScreenY", "/get_params", "mn_mc_indx", "clearCache", "onmousemove", ",setSDFN:", "lvc", "vibrate", "rir", "doe_cnt_lmt", "fpVal", "Microsoft Tai Le", "readyState", "userAgent", "geolocation", "den", "offsetHeight", "lang", "Buffer", "sensor_data", "; path=/; expires=Fri, 01 Feb 2025 08:00:00 GMT;", "devicePixelRatio", "loap", "<bpd>", "rCFP", "\"", "-1", "td", "Comic Neue", "pageY", "dme_cnt_lmt", "pduce_cnt", "catch", "activeElement", "mousemove", "https:", "localStorage", "url", ",mn_w:", "-1,2,-94,-70,", "password", "", "sdfn", "192px", "-1,2,-94,-80,", "midi", "mozAlarms", "ctrlKey", "-1,2,-94,-101,", "rotate_right", "atanh", "magnetometer", "domAutomation", "brv", "hasSessionStorage", "visibilitychange", "sessionStorageKey", "mn_r", "rotationRate", "sans-serif", "on", "DeviceMotionEvent", "Oswald", "x1", "Bodoni 72", "YouTube Plug-in", "documentElement", "split", "keypress", "Microsoft Sans Serif", "ke_cnt_lmt", "localStorageKey", "charCodeAt", "hbCalc", "-1,2,-94,-122,", "hb", "onreadystatechange", "gf", "Edge PDF Viewer", "innerWidth", "ir", "state", "webdriver", "XPathResult", "value", "none", "aj_type", "clipboard-read", "applyFunc", "opera", "input", "te_vel", "autocomplete", "x2", "mn_psn", "Shockwave for Director", "monospace", "get_browser", "pe_vel", "storage", "position: relative; left: -9999px; visibility: hidden; display: block !important", "cta", "||", "Waseem", "payment-handler", ",s3:", "y1", "hmm", "rst", "bpd", "Adobe Braille", "Noto", "cwen:", "mme_cnt", "number", "fromCharCode", "-1,2,-94,-117,", "height", "mn_ts", "d3", "2", "New York", "product", "stack", "imul", "hmu", "cbrt", "0a46G5m17Vrp4o4c", "metaKey", "dm_en", "listFunctions", "PLUGINS", "beta", "undef", "mn_get_new_challenge_params", "cookie", "iPad;", "gamma", "appVersion", "-1,2,-94,-129,", "init_time", "getGamepads", "gb", "push", "-1,2,-94,-123,", "fontSize", "Basic ", "addEventListener", "hku", "pact", "mn_state", "speechSynthesis", "me_vel", "exception", "name", "dis", ",uaend,", "clientHeight", "-1,2,-94,-127,", "cssText", "cookie_chk_read", "availHeight", "Mac OS X 10_5", "tact", "Adobe Hebrew", "i1:", "Apple LiGothic", "csh", "permissions", "0", "Futura", "pow", "sd_debug", "vc_cnt", "dme_vel", "protocol", "cpa", "Content-type", "Droid Serif", "prod", "hidden", "toLowerCase", "setRequestHeader", "mouse", "voiceURI", "3", "call", "GET", "which", "webkitGetGamepads", "mn_ld", "onblur", "onclick", "fmh", "patp", "webkitHidden", "-1,2,-94,-110,", "isc:", "get_cookie", "prototype", "javaEnabled", "indexedDB", "style", "TouchEvent", "pen", "wrc:", "Candara", "accessibility-events", "bluetooth", "pe_cnt", "check_stop_protocol", "apply", "sessionStorage", "WebEx64 General Plugin Container", "location", "bm-telemetry", "asin", "ITC Bodoni 72 Bold", "serif", "all", "availWidth", "getElementsByName", "ats", "hostname", "do_en", "ff", "target", "attachEvent", "_phantom", "Minion Pro", "tduce_cnt", "requestWakeLock", "disFpCalOnTimeout", "onpointerup", "AlNile", "canvas", "Courier", "notifications", "HTMLElement", "hypot", "wr", "speaker", "Google Earth Plug-in", "sqrt", "RTCPeerConnection", "mozPhoneNumberService", "indexOf", "tme_cnt_lmt", "parseInt", "bind", "jrs", "keyCode", "charAt", "fmz", "2d", "o9", "mn_poll", "Lucida Sans", "fpValstr", "Chrome Remote Desktop Viewer", "QuickTime Plug-in", "Press Start 2P", "mozvisibilitychange", "doe_cnt", "/_bm/_data", "devicemotion", "Microsoft Office Live Plug-in", "abs", "fontFamily", "indexedDbKey", "TI-Nspire", "dmact", "accelerationIncludingGravity", "onpointerdown", "microphone", "unk", "getElementById", "set_cookie", "get_mn_params_from_abck", "undefined", "colorDepth", "-1,2,-94,-120,", "getTimezoneOffset", "SharePoint Browser Plug-in", "encode_utf8", "lastIndexOf", "cal_dis", "mn_sen", "-1,2,-94,-116,", "weh", "hasLocalStorage", "vc_cnt_lmt", "XDomainRequest", "Adobe Acrobat", "mn_get_current_challenges", "onkeydown", "http://", "ssh", "fonts_optm", "n", "}", "t_tst", "pstate", "URL", "htm", "open", "1", "iPhone", "abcdefhijklmnopqrstuvxyz1234567890;+-.", "onmouseup"];
class AstDec{
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
        let code = generator(this.ast, {jsescOption:{"minimal":true}}).code;
        fs.writeFile('./dist.js',code,{encoding:'utf8'},(err)=>{
            if(err){
                console.log(err);
            }
        });
    }
    transformMemberExpression(){
        traverse(this.ast,{
            MemberExpression(path){
                if(t.isStringLiteral(path.node.property) && path.node.computed){
                    let name = path.node.property.value;
                    path.node.property = t.identifier(name);
                    path.node.computed = false;
                }
            }
        })
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
    //字符串转义
    transformStringRaw(){
        traverse(this.ast,{
            StringLiteral(path){
                if(path.node.value.length + 2 != path.node.extra.raw.length){
                    path.replaceWith(t.stringLiteral(path.node.value));
                    path.skip();
                }
            }
        })
    }
    /***
     * fromCharCode
     */
    transformStringFromCharCode(){
        traverse(this.ast,{
            CallExpression(path){
                if(t.isMemberExpression(path.node.callee)){
                    let {object,property} = path.node.callee;
                    if(t.isIdentifier(object) && object.name == 'String' && t.isIdentifier(property) && property.name == 'fromCharCode'){
                        let arr = path.node.arguments;
                        let isAllNum = arr.every(n=>t.isNumericLiteral(n));
                        if(isAllNum){
                            let allNum = arr.map(n=>n.value);
                            let c = String.fromCharCode.apply(null,allNum);
                            path.replaceWith(t.stringLiteral(c));
                        }
                    }
                }
            }
        })
    }
    /***
     * 进制转换
     */
    rawValue(){
        traverse(this.ast,{
            'NumericLiteral|StringLiteral'(path){
                path.node.extra = undefined;
            }
        })
    }
    test(){
        traverse(this.ast,{
            MemberExpression(path){
                let {object,property} = path.node;
                if(!t.isIdentifier(object,{name:'_ac'})) return;
                if(!t.isNumericLiteral(property)) return;
                let index = property.value;
                let value = _ac[index];
                path.replaceWith(t.valueToNode(value));
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
                    let new_consequent = t.blockStatement([t.expressionStatement(consequent)]);
                    let new_alternate = t.blockStatement([t.expressionStatement(alternate)]);
                    let if_node = t.ifStatement(test,new_consequent,new_alternate);
                    path.replaceWithMultiple(if_node);
                }
            }
        })
    }
    /***
     * 单独语句加大括号
     */
    standardLoop(){
        //单独语句加大括号
        traverse(this.ast,{
            'ForStatement|WhileStatement'({node}){
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
                let {operator} = path.node;
                if(operator == "!" || operator == "void"){
                    let {confident,value} = path.evaluate();
                    if(confident){
                        path.replaceInline(t.valueToNode(value));
                    }
                }
            }
        })
    }
    calcValue(){
        traverse(this.ast,{
            // 'BinaryExpression|Identifier|UnaryExpression'(path){
            'UnaryExpression'(path){
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
}

module.exports = AstDec