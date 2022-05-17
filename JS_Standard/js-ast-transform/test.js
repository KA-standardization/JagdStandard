function func67(p1) {
  let v278 = p1 || "";
  const v279 = v278["match"](/[?](\w+=.*&?)*/);
  v278 = v279 ? v279[0]["substr"](1) : "";
  const v280 = v278 ? v278["split"]("&") : null,
        v281 = {};

  if (v280) {
    for (let v453 = 0; v453 < v280["length"]; v453++) {
      v281[v280[v453]["split"]("=")[0]] = v280[v453]["split"]("=")[1];
    }
  }

  return v281;
}



function func66(p1) {
  let v277 = p1 || "";
  v277 = v277.replace(/(http:\/\/|https:\/\/|\/\/)?[^\/]*/, "");
  v277 = -1 !== v277.indexOf("?") ? v277.substr(0, v277.indexOf("?")) : v277; 
  v277 = v277 || "/";
  return v277;
}


function func62(p1) {
  let keys = Object.keys(p1),
      result = 0;

  for (let index = keys.length - 1; index >= 0; index--) {
    let roll = keys.length - index - 1;
    let num = p1[keys[index]] ? 1 : 0;
    let num1 = num << roll;
    result = num1 | result;
  }

  return result;
}

// var url = '/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7031856229676862733&cursor=0&count=20&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+WOW64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F86.0.4240.198+Safari%2F537.36&browser_online=true&msToken=-eLfuHEpZry1sZmuuzpieZvkPmrreigylHyEXKGtfr5y43MyMPw-hPJbxLENJN7Jif_P_8sn-8jJ5AP3FqMFN-ZWDEgMPFVUSdBUsdaDr33qKPNiXTNtOw==&X-Bogus=DFSzsdVLLUGANn3hS7Yn3N4ELVcg'
// var result = func67(url)

// var url = "/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7031856229676862733&cursor=0&count=20&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+WOW64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F86.0.4240.198+Safari%2F537.36&browser_online=true&msToken=-eLfuHEpZry1sZmuuzpieZvkPmrreigylHyEXKGtfr5y43MyMPw-hPJbxLENJN7Jif_P_8sn-8jJ5AP3FqMFN-ZWDEgMPFVUSdBUsdaDr33qKPNiXTNtOw==&X-Bogus=DFSzsdVLLUGANn3hS7Yn3N4ELVcg"
// result = func66(url)

var dir1 = {"directSign": false,"consistent": false, "location": false, "switch": false, "dom": false, "debugger": true, "node": false, "phantom": false, "webdriver": false, "incognito": false, "hook": false, "test": true}

var result = func62(dir1);

console.log(result)