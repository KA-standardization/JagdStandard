function _0x3c12a5(_0x250bcb, _0x48874f, _0x219868) {
  return (_0x3c12a5 = Reflect.construct).apply(null, arguments);
}

function _0x1bf51e(_0x22460d) {
  return function (_0xa2fadf) {
    if (Array.isArray(_0xa2fadf)) {
      for (var _0x30c434 = 0, _0x30cc3e = new Array(_0xa2fadf.length); _0x30c434 < _0xa2fadf.length; _0x30c434++) {
        _0x30cc3e[_0x30c434] = _0xa2fadf[_0x30c434];
      }

      return _0x30cc3e;
    }
  }(_0x22460d) || function (_0x55867f) {
    if (Symbol['iterator'] in Object(_0x55867f) || '[object Arguments]' === Object.prototype.toString.call(_0x55867f)) {
      return Array.from(_0x55867f);
    }
  }(_0x22460d) || function () {
    throw new TypeError('Invalid attempt to spread non-iterable instance');
  }();
}

for (var _0x56d547 = [], _0x3f8ebe = 0, _0x288cfa = [], _0x23c513 = 0, _0x27bbfc = function (_0x32cb0c, _0x3ff0d7) {
  var _0x3d4b1b = _0x32cb0c[_0x3ff0d7++],
      _0x21f0fb = _0x32cb0c[_0x3ff0d7],
      _0x2d0997 = parseInt('' + _0x3d4b1b + _0x21f0fb, 16);

  if (_0x2d0997 >> 7 == 0) {
    return [1, _0x2d0997];
  }

  if (_0x2d0997 >> 6 == 2) {
    var _0x246c85 = parseInt('' + _0x32cb0c[++_0x3ff0d7] + _0x32cb0c[++_0x3ff0d7], 16);

    return _0x2d0997 &= 63, [2, _0x246c85 = (_0x2d0997 <<= 8) + _0x246c85];
  }

  if (_0x2d0997 >> 6 == 3) {
    var _0x1529ee = parseInt('' + _0x32cb0c[++_0x3ff0d7] + _0x32cb0c[++_0x3ff0d7], 16),
        _0x411aeb = parseInt('' + _0x32cb0c[++_0x3ff0d7] + _0x32cb0c[++_0x3ff0d7], 16);

    return _0x2d0997 &= 63, [3, _0x411aeb = (_0x2d0997 <<= 16) + (_0x1529ee <<= 8) + _0x411aeb];
  }
}, _0x40ca1a = function (_0x50dc77, _0x409020) {
  var _0x494409 = parseInt('' + _0x50dc77[_0x409020] + _0x50dc77[_0x409020 + 1], 16);

  return _0x494409 = _0x494409 > 127 ? -256 + _0x494409 : _0x494409;
}