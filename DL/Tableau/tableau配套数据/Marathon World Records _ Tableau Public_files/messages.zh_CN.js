
/*!
 * Globalize Runtime v1.4.0 2018-07-17T20:38Z Released under the MIT license
 * http://git.io/TrdQbw
 */
"undefined"!=typeof process&&"node"===process.release.name?global.localizeGlobalNamespace=global:window.localizeGlobalNamespace=window,localizeGlobalNamespace.TabGlobalize=function(){var n=function(e,a){return e=e.replace(/{[0-9a-zA-Z-_. ]+}/g,function(e){return e=e.replace(/^{([^}]*)}$/,"$1"),"string"==typeof(r=a[e])?r:"number"==typeof r?""+r:JSON.stringify(r);var r})},o=function(e,r,a){var t;return r=e+(r?": "+n(r,a):""),(t=new Error(r)).code=e,function(){var a=arguments[0];[].slice.call(arguments,1).forEach(function(e){var r;for(r in e)a[r]=e[r]})}(t,a),t},l=function(e,r,a,t){if(!a)throw o(e,r,t)},r=function(e,r){l("E_MISSING_PARAMETER","Missing required parameter `{name}`.",void 0!==e,{name:r})},a=function(e,r,a,t){l("E_INVALID_PAR_TYPE","Invalid `{name}` parameter ({value}). {expected} expected.",a,{expected:t,name:r,value:e})},t=function(e,r){a(e,r,void 0===e||"string"==typeof e,"a string")};function i(e){if(!(this instanceof i))return new i(e);r(e,"locale"),t(e,"locale"),this._locale=e}return i.locale=function(e){return t(e,"locale"),arguments.length&&(this._locale=e),this._locale},i._createError=o,i._formatMessage=n,i._regexpEscape=function(e){return e.replace(/([.*+?^=!:${}()|\[\]\/\\])/g,"\\$1")},i._runtimeKey=function(e,r,a,t){var n,o,l;return t=t||(l=a,JSON.stringify(l,function(e,r){return r&&r.runtimeKey?r.runtimeKey:r})),0<(o=e+r+t,n=[].reduce.call(o,function(e,r){var a=r.charCodeAt(0);return 0|(e=(e<<5)-e+a)},0))?"a"+n:"b"+Math.abs(n)},i._stringPad=function(e,r,a){var t;for("string"!=typeof e&&(e=String(e)),t=e.length;t<r;t+=1)e=a?e+"0":"0"+e;return e},i._validateParameterPresence=r,i._validateParameterTypeString=t,i._validateParameterType=a,i}(),function(e,r){var a,t,n,o;a=e.TabGlobalize,t=a._runtimeKey,n=a._validateParameterType,o=function(e,r){var a;n(e,r,void 0===e||null!==(a=e)&&""+a=="[object Object]"||Array.isArray(e),"Array or Plain Object")},a._messageFormatterFn=function(r){return function(e){return"number"!=typeof e&&"string"!=typeof e||(e=[].slice.call(arguments,0)),o(e,"variables"),r(e)}},a._messageFormat={number:function(e,r){if(isNaN(e))throw new Error("'"+e+"' isn't a number.");return e-(r||0)},plural:function(e,r,a,t,n){if({}.hasOwnProperty.call(t,e))return t[e]();r&&(e-=r);var o=a(e,n);return o in t?t[o]():t.other()},select:function(e,r){return{}.hasOwnProperty.call(r,e)?r[e]():r.other()}},a._validateParameterTypeMessageVariables=o,a.messageFormatter=a.prototype.messageFormatter=function(){return a[t("messageFormatter",this._locale,[].slice.call(arguments,0))]},a.formatMessage=a.prototype.formatMessage=function(e){return this.messageFormatter(e).apply({},[].slice.call(arguments,1))}}(localizeGlobalNamespace),function(e,r){var a,t,n,o,l;a=e.TabGlobalize,t=a._runtimeKey,n=a._validateParameterPresence,o=a._validateParameterType,l=function(e,r){o(e,r,void 0===e||"number"==typeof e,"Number")},a._pluralGeneratorFn=function(r){return function(e){return n(e,"value"),l(e,"value"),r(e)}},a._validateParameterTypeNumber=l,a.plural=a.prototype.plural=function(e,r){return n(e,"value"),l(e,"value"),this.pluralGenerator(r)(e)},a.pluralGenerator=a.prototype.pluralGenerator=function(e){return e=e||{},a[t("pluralGenerator",this._locale,[e])]}}(localizeGlobalNamespace);

(function( root, factory ) {
  root.Localize = root.Localize || {};
  root.Localize.msg = new root.TabGlobalize('zh-Hans');
  factory( root.TabGlobalize, root.Localize );
  if (root.Localize.initFormattersAndParsers) {
    root.Localize.initFormattersAndParsers();
  }
}(localizeGlobalNamespace, function( Globalize ) {
var validateParameterTypeNumber = Globalize._validateParameterTypeNumber;
var validateParameterPresence = Globalize._validateParameterPresence;
var pluralGeneratorFn = Globalize._pluralGeneratorFn;
var validateParameterTypeMessageVariables = Globalize._validateParameterTypeMessageVariables;
var messageFormat = Globalize._messageFormat;
var messageFormatterFn = Globalize._messageFormatterFn;

Globalize.b1234768562 = pluralGeneratorFn(function(n
/*``*/) {
  return 'other';
});
Globalize.b1387185509 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1667125755 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1811075867 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b208180135 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1925736231 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1284813559 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a912921384 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a204327826 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1208696631 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1680728741 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1199436742 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????? Tableau (??????)"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1253248232 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1772590781 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1631956456 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b835876794 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a588545779 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a944794311 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1895643029 = messageFormatterFn((function(  ) {
  return function (d) { return "?????? Tableau"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a425448847 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b552152719 = messageFormatterFn((function(  ) {
  return function (d) { return "average"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1007943133 = messageFormatterFn((function(  ) {
  return function (d) { return "count"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b276606305 = messageFormatterFn((function(  ) {
  return function (d) { return "sum"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1534538714 = messageFormatterFn((function(  ) {
  return function (d) { return "Analyzing Data"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1979053879 = messageFormatterFn((function(  ) {
  return function (d) { return "Explain the Mark"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a575871695 = messageFormatterFn((function(  ) {
  return function (d) { return "Explain the Mark - "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1270542120 = messageFormatterFn((function(  ) {
  return function (d) { return d.fieldCaption + " is "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1467695831 = messageFormatterFn((function(  ) {
  return function (d) { return " Possible explanations:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b864969113 = messageFormatterFn((function(  ) {
  return function (d) { return "Considering the distribution of values in the data, this value is expected to be between " + d.low + " and " + d.high + ". This takes into account the filters set on " + d.fieldCaptions + "."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a739822230 = messageFormatterFn((function(  ) {
  return function (d) { return "Considering the distribution of values in the data, this value is expected to be between " + d.low + " and " + d.high + "."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b509061094 = messageFormatterFn((function(  ) {
  return function (d) { return "Considering the distribution of values in the data, this value is expected to be between " + d.low + " and " + d.high + ". This takes into account the filter set on " + d.fieldCaption + "."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1498692639 = messageFormatterFn((function(  ) {
  return function (d) { return "Expected Range"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b576207989 = messageFormatterFn((function(  ) {
  return function (d) { return "Based on the selected mark, Tableau runs a statistical analysis on the data in the view and in your data source. This page shows possible explanations for the value of the selected mark, considered with other information in the data source."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b470670935 = messageFormatterFn((function(  ) {
  return function (d) { return "higher value"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b259103296 = messageFormatterFn((function(  ) {
  return function (d) { return "Learn More"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b865074913 = messageFormatterFn((function(  ) {
  return function (d) { return "lower value"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1364895251 = messageFormatterFn((function(  ) {
  return function (d) { return "Average value of records"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a491854311 = messageFormatterFn((function(  ) {
  return function (d) { return d.fieldCaption + " is " + d.relativeToExpectedSum + " The average value of the records in this mark is " + d.relativeToExpectedAverage + " while the number of records contributing to this mark is " + d.relativeToExpectedCount; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b736381017 = messageFormatterFn((function(  ) {
  return function (d) { return d.fieldCaption + " is " + d.relativeToExpectedSum; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1135290535 = messageFormatterFn((function(  ) {
  return function (d) { return "Measure of Rows"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2062494945 = messageFormatterFn((function(  ) {
  return function (d) { return d.fieldCaption + " " + d.aggValue + " appears to be high, but no explanation could be found based on the available data."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b62646003 = messageFormatterFn((function(  ) {
  return function (d) { return d.fieldCaption + " " + d.aggValue + " appears to be low, but no explanation could be found based on the available data."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b788232035 = messageFormatterFn((function(  ) {
  return function (d) { return "Based on the data included in the data source, no explanation could be found."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b737579569 = messageFormatterFn((function(  ) {
  return function (d) { return "No explanation found in data"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1117527777 = messageFormatterFn((function(  ) {
  return function (d) { return " The fields " + d.dimensionsListString + " were considered in this analysis, but did not significantly explain the value of this mark."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a378819493 = messageFormatterFn((function(  ) {
  return function (d) { return " " + d.numberOfDimensions + " fields were considered, such as " + d.dimensionName1 + ", " + d.dimensionName2 + " and " + d.dimensionName3 + ", however analysis of this data did not significantly explain the value of this mark."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2028714678 = messageFormatterFn((function(  ) {
  return function (d) { return " Additional fields were not available for consideration in this analysis."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1125139973 = messageFormatterFn((function(  ) {
  return function (d) { return " The field " + d.dimensionName + " was considered in this analysis, but it did not significantly explain the value of this mark."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1972349498 = messageFormatterFn((function(  ) {
  return function (d) { return "Number of records"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1902221492 = messageFormatterFn((function(  ) {
  return function (d) { return d.fieldCaption + " is " + d.relativeToExpectedSum + " The number of records contributing to this mark is " + d.relativeToExpectedCount + " while the average value of the records in this mark is " + d.relativeToExpectedAverage; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a673986164 = messageFormatterFn((function(  ) {
  return function (d) { return d.fieldCaption + " is " + d.relativeToExpectedSum; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b736058010 = messageFormatterFn((function(  ) {
  return function (d) { return "Number of Rows"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b83375861 = messageFormatterFn((function(  ) {
  return function (d) { return "OK"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b11395680 = messageFormatterFn((function(  ) {
  return function (d) { return "decreasing"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1556234432 = messageFormatterFn((function(  ) {
  return function (d) { return "increasing"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b104731695 = messageFormatterFn((function(  ) {
  return function (d) { return "about " + d.percentage + "% higher than expected"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1890511948 = messageFormatterFn((function(  ) {
  return function (d) { return "about " + d.percentage + "% higher than expected,"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1734769448 = messageFormatterFn((function(  ) {
  return function (d) { return "about " + d.percentage + "% higher than expected."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1609224935 = messageFormatterFn((function(  ) {
  return function (d) { return "about " + d.percentage + "% lower than expected"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b645151394 = messageFormatterFn((function(  ) {
  return function (d) { return "about " + d.percentage + "% lower than expected,"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1783297938 = messageFormatterFn((function(  ) {
  return function (d) { return "about " + d.percentage + "% lower than expected."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b40034879 = messageFormatterFn((function(  ) {
  return function (d) { return "The " + d.higherOrLowerValue + " is partially explained by the percentage of records with " + d.dimension + " = " + d.primaryValue + "."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1876181289 = messageFormatterFn((function(  ) {
  return function (d) { return d.fieldCaption + ":"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1358376893 = messageFormatterFn((function(  ) {
  return function (d) { return ", "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b706443435 = messageFormatterFn((function(  ) {
  return function (d) { return "A single value " + d.outlierValue + " out of " + d.numberOfRows + " rows is increasing " + d.fieldCaption + ". Excluding this value, " + d.fieldCaption + " is " + d.measureValueWithoutOutlier + "."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b706214717 = messageFormatterFn((function(  ) {
  return function (d) { return "A single value " + d.outlierValue + " out of " + d.numberOfRows + " rows is decreasing " + d.fieldCaption + ". Excluding this value, " + d.fieldCaption + " is " + d.measureValueWithoutOutlier + "."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a503955712 = messageFormatterFn((function(  ) {
  return function (d) { return "The extreme value of " + d.fieldCaption + " is " + d.outlierValueDiff + " higher than the next highest row value for the mark."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a504184430 = messageFormatterFn((function(  ) {
  return function (d) { return "The extreme value of " + d.fieldCaption + " is " + d.outlierValueDiff + " lower than the next lowest row value for the mark."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1721999884 = messageFormatterFn((function(  ) {
  return function (d) { return "Distribution of row values within " + d.fieldCaption; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1142535314 = messageFormatterFn((function(  ) {
  return function (d) { return "If this value is excluded from " + d.fieldCaption + ", " + d.fieldCaption + " is " + d.measureValueWithoutOutlier + ", which is " + d.measureValueDiff + " lower than the observed value of " + d.measureValue + "."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1142306596 = messageFormatterFn((function(  ) {
  return function (d) { return "If this value is excluded from " + d.fieldCaption + ", " + d.fieldCaption + " is " + d.measureValueWithoutOutlier + ", which is " + d.measureValueDiff + " higher than the observed value of " + d.measureValue + "."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a247057118 = messageFormatterFn((function(  ) {
  return function (d) { return "Visualize the difference"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1303237973 = messageFormatterFn((function(  ) {
  return function (d) { return "Row details"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2056262037 = messageFormatterFn((function(  ) {
  return function (d) { return "A single record with a value of " + d.outlierValue + " is increasing " + d.fieldCaption + "."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2056490755 = messageFormatterFn((function(  ) {
  return function (d) { return "A single record with a value of " + d.outlierValue + " is decreasing " + d.fieldCaption + "."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a283212439 = messageFormatterFn((function(  ) {
  return function (d) { return "A single extreme value"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1840635111 = messageFormatterFn((function(  ) {
  return function (d) { return "The " + d.higherOrLowerValue + " is partially explained by " + d.dimension + " = " + d.singleValue + "."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1218468136 = messageFormatterFn((function(  ) {
  return function (d) { return d.fieldCaption + " " + d.aggValue + " is " + d.relativeToRange + ". The " + d.higherOrLowerValue + " is partially explained by the mix of values for " + d.dimension + ", which is not shown in this visualization."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2085661113 = messageFormatterFn((function(  ) {
  return function (d) { return "This chart shows how " + d.dimension + " contributes to the value " + d.aggValue + " of the selected mark, compared to other marks in the visualization.  Bars that extend right have a higher representation in the selected mark, whereas bars that extend left have a higher representation in the rest of the data."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b69817415 = messageFormatterFn((function(  ) {
  return function (d) { return "Distribution of values"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1848263832 = messageFormatterFn((function(  ) {
  return function (d) { return "The " + d.higherOrLowerValue + " is partially explained by the mix of values for " + d.dimension + "."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1786178453 = messageFormatterFn((function(  ) {
  return function (d) { return "Mix of values for " + d.dimension; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a345749986 = messageFormatterFn((function(  ) {
  return function (d) { return "as expected"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b360740669 = messageFormatterFn((function(  ) {
  return function (d) { return "as expected,"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1556500055 = messageFormatterFn((function(  ) {
  return function (d) { return "as expected."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a818286400 = messageFormatterFn((function(  ) {
  return function (d) { return "higher than expected"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b216244955 = messageFormatterFn((function(  ) {
  return function (d) { return "higher than expected,"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1372100217 = messageFormatterFn((function(  ) {
  return function (d) { return "higher than expected."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1361905048 = messageFormatterFn((function(  ) {
  return function (d) { return "lower than expected"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1902709197 = messageFormatterFn((function(  ) {
  return function (d) { return "lower than expected,"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b109030945 = messageFormatterFn((function(  ) {
  return function (d) { return "lower than expected."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2129899980 = messageFormatterFn((function(  ) {
  return function (d) { return "value"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1201010608 = messageFormatterFn((function(  ) {
  return function (d) { return "within the expected range"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a105074327 = messageFormatterFn((function(  ) {
  return function (d) { return "within the expected range."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1270263219 = messageFormatterFn((function(  ) {
  return function (d) { return "View Full Data"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a23652603 = messageFormatterFn((function(  ) {
  return function (d) { return "This value is within the expected range based on the all values in the data source."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1204582725 = messageFormatterFn((function(  ) {
  return function (d) { return "This value is within the expected range based on the all values in the data source."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a142433133 = messageFormatterFn((function(  ) {
  return function (d) { return "Expected value"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1297815579 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1650432326 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1338311911 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1970506073 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????..."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1419080121 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a387132665 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????/?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1632221504 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2049286305 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a108331147 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b83157047 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b930478443 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1033907719 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2124595451 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b355426435 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1068765966 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1626485420 = messageFormatterFn((function(  ) {
  return function (d) { return "%"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1616243025 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2132257107 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1269451794 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1467693967 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a514096646 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1153163386 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b499729618 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1696374744 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b312310771 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a119014161 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a530899625 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1473795491 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b744733195 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1336835664 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a358938469 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a278681739 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b8205164 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b440203001 = messageFormatterFn((function(  ) {
  return function (d) { return "Cancel"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a755078925 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1983909160 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a670961629 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b253661727 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2102578769 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1142488134 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a849807621 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b141265852 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a904481334 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1071823862 = messageFormatterFn((function(  ) {
  return function (d) { return "Tableau Server ????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a565688152 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a393153905 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a204329520 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1518109615 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b596552511 = messageFormatterFn((function(  ) {
  return function (d) { return "??????..."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1821839786 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b858040306 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a682142000 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????...???????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1417224788 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a643450479 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????? Tableau ????????????????????????????????? Web ???????????????????????????????????????????????????????????????????????? Tableau ??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1260333433 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????..."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b680987400 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1656299675 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b254975565 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1573330108 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????? " + d.fileSize + " MB ?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a146846667 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1840464864 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b789414544 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????? " + d.GALLERY + " ????????????????????????????????? " + d.EXTENSIONS + " ????????????????????????????????????(.trex ??????)???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a614037108 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a194407169 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b711651089 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1642076757 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1440483855 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b294366749 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1297279479 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a232993075 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1218809024 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b786507832 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a300168349 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a237807434 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b940595154 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1632473256 = messageFormatterFn((function(  ) {
  return function (d) { return "?????? " + d.user + " ????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b5876910 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a64548271 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????? URL ???????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1978365462 = messageFormatterFn((function(  ) {
  return function (d) { return "Show template project contributors!"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1707585391 = messageFormatterFn((function(  ) {
  return function (d) { return "Hide template project contributors!"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a987607170 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b518207688 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????@???????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1461859113 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1250827655 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1292312682 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????????????????..."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b760344358 = messageFormatterFn((function(  ) {
  return function (d) { return "????????? " + d.user + " ????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b185765100 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a478362992 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1882459976 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1020947276 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a939091330 = messageFormatterFn((function( plural, pluralFuncs ) {
  return function (d) { return plural(d.itemCount, 0, pluralFuncs["zh-Hans"], { one: function() { return "??????";}, other: function() { return d.formattedItemCount + " ?????????";} }) + "????????????????????? " + d.comment + " ?????????"; }
})(messageFormat.plural, {"zh-Hans": Globalize("zh-Hans").pluralGenerator()}), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1155288418 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1855467552 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????? Internet ??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2116303110 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????? Internet ????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1265970577 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1847329538 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1969056977 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a115461100 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a291619274 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1912141235 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1616100185 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b594275224 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1113356286 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b789662859 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b762256437 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1279395072 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1150896226 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????..."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1919055361 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a652678051 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1438282852 = messageFormatterFn((function(  ) {
  return function (d) { return "@????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1062190308 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a11562361 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a57822842 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2073566798 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1973058227 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1233479252 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b4292259 = messageFormatterFn((function(  ) {
  return function (d) { return d.user + " ??????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a552620708 = messageFormatterFn((function( plural, pluralFuncs ) {
  return function (d) { return plural(d.itemCount, 0, pluralFuncs["zh-Hans"], { one: function() { return d.formattedItemCount + " ?????????";}, other: function() { return d.formattedItemCount + " ?????????";} }) + "?????????????????????"; }
})(messageFormat.plural, {"zh-Hans": Globalize("zh-Hans").pluralGenerator()}), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1701965264 = messageFormatterFn((function(  ) {
  return function (d) { return d.user + " ??? Tableau ?????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a540765293 = messageFormatterFn((function(  ) {
  return function (d) { return d.user + " ???????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1443088850 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1416666777 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1146145651 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a652159400 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b893640974 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1740886133 = messageFormatterFn((function(  ) {
  return function (d) { return "Microsoft Azure HDInsight ??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1067751499 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a950654867 = messageFormatterFn((function(  ) {
  return function (d) { return "Kerberos"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1981425471 = messageFormatterFn((function(  ) {
  return function (d) { return "LDAP"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2079755952 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b916289690 = messageFormatterFn((function(  ) {
  return function (d) { return "SAML IdP"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1749667710 = messageFormatterFn((function(  ) {
  return function (d) { return "Teradata ?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1339135558 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1879666505 = messageFormatterFn((function(  ) {
  return function (d) { return "Active Directory ??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b173690290 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a865536233 = messageFormatterFn((function(  ) {
  return function (d) { return "Windows ????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1050739143 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1370796730 = messageFormatterFn((function(  ) {
  return function (d) { return "HiveServer2"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a369201128 = messageFormatterFn((function(  ) {
  return function (d) { return "Impala"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2111112256 = messageFormatterFn((function(  ) {
  return function (d) { return "SharkServer (Shark 0.8.1 ???????????????)"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1019984136 = messageFormatterFn((function(  ) {
  return function (d) { return "SharkServer2 (Shark 0.9.*)"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1151193288 = messageFormatterFn((function(  ) {
  return function (d) { return "SparkThriftServer (Spark 1.1 ???????????????)"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1091839420 = messageFormatterFn((function(  ) {
  return function (d) { return "ZooKeeper"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1012432248 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2138009107 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b661794681 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????? SQL ??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1031956546 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????..."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a512669177 = messageFormatterFn((function(  ) {
  return function (d) { return "?????? SQL"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2093065660 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b225588273 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a222861110 = messageFormatterFn((function(  ) {
  return function (d) { return "HTTP"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a420365830 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a520201237 = messageFormatterFn((function(  ) {
  return function (d) { return "SASL"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1758400576 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a888186541 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1225332414 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1497161214 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1076021683 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a199985842 = messageFormatterFn((function(  ) {
  return function (d) { return "?????? SSL????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2058540869 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a934650919 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a732304747 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a242323619 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2101853556 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1244674510 = messageFormatterFn((function(  ) {
  return function (d) { return "??????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b625129772 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1614511471 = messageFormatterFn((function(  ) {
  return function (d) { return "??????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1094672770 = messageFormatterFn((function(  ) {
  return function (d) { return "SAML IdP(Okta):"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1252867296 = messageFormatterFn((function(  ) {
  return function (d) { return d.prompt + ":"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b378118403 = messageFormatterFn((function(  ) {
  return function (d) { return "HTTP:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1559351530 = messageFormatterFn((function(  ) {
  return function (d) { return "???:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2107340144 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a276023143 = messageFormatterFn((function(  ) {
  return function (d) { return "?????? FQDN:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1027644889 = messageFormatterFn((function(  ) {
  return function (d) { return "??????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1062656853 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2023476179 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1119247692 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b927636275 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1178918706 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1227988067 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b640887452 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b896898 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1314732059 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b716844524 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1522796719 = messageFormatterFn((function(  ) {
  return function (d) { return "??????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1502514667 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a147383596 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1618385109 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2114568728 = messageFormatterFn((function(  ) {
  return function (d) { return "Show Initial SQL"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a847573619 = messageFormatterFn((function(  ) {
  return function (d) { return "Hide Initial SQL"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b646302358 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????? SQL"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2117839497 = messageFormatterFn((function(  ) {
  return function (d) { return "????????? SQL"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a892072613 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b517273885 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2090076357 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????? SQL ??????????????????SELECT * FROM table_name???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1124472438 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b197459996 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????..."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1317705100 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????..."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1288538505 = messageFormatterFn((function(  ) {
  return function (d) { return "Add Action"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a773825283 = messageFormatterFn((function(  ) {
  return function (d) { return "Name"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a479272418 = messageFormatterFn((function(  ) {
  return function (d) { return "Run On"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a931680597 = messageFormatterFn((function(  ) {
  return function (d) { return "Fields"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b458803405 = messageFormatterFn((function(  ) {
  return function (d) { return "Source"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2055053687 = messageFormatterFn((function(  ) {
  return function (d) { return "Select"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a580661349 = messageFormatterFn((function(  ) {
  return function (d) { return "Hover"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b124678484 = messageFormatterFn((function(  ) {
  return function (d) { return "Menu"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1815766423 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1511896789 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1401971496 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b638321934 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b434275049 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1130572475 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a121645081 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a940347769 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1940516249 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1508771541 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b195724265 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b795984004 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a957121793 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1583581022 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????" + d.alertSubject + "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2123580406 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1976671770 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b959097003 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a47745726 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2125727461 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b702092840 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????(" + d.viewName + ")"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1893568917 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a548137788 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1935883421 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a45592016 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a347174803 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1627312548 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2068221852 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1219872071 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1718216279 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1744070874 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1931160057 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b108371726 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b305483141 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a300303240 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1655457715 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a38819891 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1803072146 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a973519050 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b930873719 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a729639423 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????(????????????)"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a634781070 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1187550620 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a768585906 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1732688450 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????? true ???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1944765243 = messageFormatterFn((function(  ) {
  return function (d) { return d.interval + " ??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a391303874 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a780568779 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????? "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1622482754 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b643933093 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????? " + d.lastTriggeredTime; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1906835796 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b727835769 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1468756594 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a398726816 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????? Internet ???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b413723749 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a32147523 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????..."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2056635287 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1205673209 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1204837717 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a11762191 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1277354549 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2119677220 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1602982127 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1323099066 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b45127533 = messageFormatterFn((function(  ) {
  return function (d) { return d.recipientCount + " ????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a207074150 = messageFormatterFn((function(  ) {
  return function (d) { return d.recipientCount + " ????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2142065736 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a165798908 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2040145261 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1237660594 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1687411439 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1975098850 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1384857757 = messageFormatterFn((function(  ) {
  return function (d) { return "About"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b600728660 = messageFormatterFn((function(  ) {
  return function (d) { return "Author"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1761562816 = messageFormatterFn((function(  ) {
  return function (d) { return "Cancel"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2089424663 = messageFormatterFn((function(  ) {
  return function (d) { return "Catalog"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b858643619 = messageFormatterFn((function(  ) {
  return function (d) { return "Clear"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b845448396 = messageFormatterFn((function(  ) {
  return function (d) { return "Close"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1396490323 = messageFormatterFn((function(  ) {
  return function (d) { return "Columns"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1823198994 = messageFormatterFn((function(  ) {
  return function (d) { return "Columns (" + d.count + ")"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1224378092 = messageFormatterFn((function(  ) {
  return function (d) { return "Couldn't find the table. Do you have the right URL?"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1697599671 = messageFormatterFn((function(  ) {
  return function (d) { return "Database: " + d.databaseName; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b362167768 = messageFormatterFn((function(  ) {
  return function (d) { return "Databases"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1188622053 = messageFormatterFn((function(  ) {
  return function (d) { return "Database Type"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1778871120 = messageFormatterFn((function(  ) {
  return function (d) { return "Author: " + d.name; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1769948397 = messageFormatterFn((function(  ) {
  return function (d) { return "By " + d.displayName + " on " + d.updatedAt; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1240678706 = messageFormatterFn((function(  ) {
  return function (d) { return "Deprecated"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1684799370 = messageFormatterFn((function(  ) {
  return function (d) { return "Maintenance in progress"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b574356592 = messageFormatterFn((function(  ) {
  return function (d) { return "Stale data"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1623491629 = messageFormatterFn((function(  ) {
  return function (d) { return "Warning"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1926865727 = messageFormatterFn((function(  ) {
  return function (d) { return "Data Source Place Page"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b48859682 = messageFormatterFn((function(  ) {
  return function (d) { return "Data Sources"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a161742849 = messageFormatterFn((function(  ) {
  return function (d) { return "Data Sources (" + d.count + ")"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b141873239 = messageFormatterFn((function(  ) {
  return function (d) { return "Modified"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1732464012 = messageFormatterFn((function(  ) {
  return function (d) { return "Description"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1699890117 = messageFormatterFn((function(  ) {
  return function (d) { return "Details Usage"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b354855940 = messageFormatterFn((function(  ) {
  return function (d) { return "Downstream Data Sources"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b959044701 = messageFormatterFn((function(  ) {
  return function (d) { return "Downstream Data Sources (" + d.count + ")"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b901026756 = messageFormatterFn((function(  ) {
  return function (d) { return "Downstream Sheets"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a479941475 = messageFormatterFn((function(  ) {
  return function (d) { return "Downstream Sheets (" + d.count + ")"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1225927279 = messageFormatterFn((function(  ) {
  return function (d) { return "Downstream Usage"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1229962518 = messageFormatterFn((function(  ) {
  return function (d) { return "Users"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1006327753 = messageFormatterFn((function(  ) {
  return function (d) { return "Users (" + d.count + ")"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2090828679 = messageFormatterFn((function(  ) {
  return function (d) { return "Downstream Workbooks"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b210419592 = messageFormatterFn((function(  ) {
  return function (d) { return "Downstream Workbooks (" + d.count + ")"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a885263074 = messageFormatterFn((function(  ) {
  return function (d) { return "Send an email"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1860072798 = messageFormatterFn((function(  ) {
  return function (d) { return "Less"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1897893914 = messageFormatterFn((function(  ) {
  return function (d) { return "More"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1100561496 = messageFormatterFn((function(  ) {
  return function (d) { return "Error"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1727589311 = messageFormatterFn((function(  ) {
  return function (d) { return "Fields"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b482240704 = messageFormatterFn((function(  ) {
  return function (d) { return "Fields (" + d.count + ")"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1724564743 = messageFormatterFn((function(  ) {
  return function (d) { return "Files"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a210526429 = messageFormatterFn((function(  ) {
  return function (d) { return "Filtered"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1399081749 = messageFormatterFn((function(  ) {
  return function (d) { return "Data Sources"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a62131514 = messageFormatterFn((function(  ) {
  return function (d) { return "Columns"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a510535774 = messageFormatterFn((function(  ) {
  return function (d) { return "Connected Data Sources"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1315526330 = messageFormatterFn((function(  ) {
  return function (d) { return "Connected Sheets"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b538426578 = messageFormatterFn((function(  ) {
  return function (d) { return "#" + " of Connections"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1863875409 = messageFormatterFn((function(  ) {
  return function (d) { return "Connection Type"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a382241945 = messageFormatterFn((function(  ) {
  return function (d) { return "Description"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1030269084 = messageFormatterFn((function(  ) {
  return function (d) { return "Name"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1545839938 = messageFormatterFn((function(  ) {
  return function (d) { return "Owned Data Sources"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b269351379 = messageFormatterFn((function(  ) {
  return function (d) { return "Owned Workbooks"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b355226864 = messageFormatterFn((function(  ) {
  return function (d) { return "Owner"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1872945209 = messageFormatterFn((function(  ) {
  return function (d) { return "Owners"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a363337486 = messageFormatterFn((function(  ) {
  return function (d) { return "Popularity"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1588883100 = messageFormatterFn((function(  ) {
  return function (d) { return "Server"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b431004147 = messageFormatterFn((function(  ) {
  return function (d) { return "Sheets"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1860527802 = messageFormatterFn((function(  ) {
  return function (d) { return "#" + " of Tables"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b685621954 = messageFormatterFn((function(  ) {
  return function (d) { return "Tables"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b858659470 = messageFormatterFn((function(  ) {
  return function (d) { return "Tags"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b836240301 = messageFormatterFn((function(  ) {
  return function (d) { return "Type"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b736415853 = messageFormatterFn((function(  ) {
  return function (d) { return "Workbook"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1414646777 = messageFormatterFn((function(  ) {
  return function (d) { return "Hostname"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1263976843 = messageFormatterFn((function(  ) {
  return function (d) { return "Lineage"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2146718388 = messageFormatterFn((function(  ) {
  return function (d) { return "Loading???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1635372884 = messageFormatterFn((function(  ) {
  return function (d) { return "No description available."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2026703500 = messageFormatterFn((function(  ) {
  return function (d) { return "No tables found."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1524817475 = messageFormatterFn((function(  ) {
  return function (d) { return "Owner Information"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1241260864 = messageFormatterFn((function(  ) {
  return function (d) { return "Owner's Display Name"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b324632537 = messageFormatterFn((function(  ) {
  return function (d) { return "Owner's Domain"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a766915262 = messageFormatterFn((function(  ) {
  return function (d) { return "Owner's Id"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a24777574 = messageFormatterFn((function(  ) {
  return function (d) { return "Owners"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a369433465 = messageFormatterFn((function(  ) {
  return function (d) { return "Owners (" + d.count + ")"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1984848897 = messageFormatterFn((function(  ) {
  return function (d) { return "Owner's Site URI"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b57538087 = messageFormatterFn((function(  ) {
  return function (d) { return "Owner's User Name"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1658599211 = messageFormatterFn((function(  ) {
  return function (d) { return "+ " + d.count + " more"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b278225708 = messageFormatterFn((function(  ) {
  return function (d) { return "Project Name"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1154396903 = messageFormatterFn((function(  ) {
  return function (d) { return "Search"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a701266830 = messageFormatterFn((function(  ) {
  return function (d) { return "Send"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1214803396 = messageFormatterFn((function(  ) {
  return function (d) { return "Send Email"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a726612121 = messageFormatterFn((function( plural, pluralFuncs ) {
  return function (d) { return "To: " + plural(d.USER_COUNT, 0, pluralFuncs["zh-Hans"], { one: function() { return d.USER_COUNT_LOC + " recipient";}, other: function() { return d.USER_COUNT_LOC + " recipients";} }); }
})(messageFormat.plural, {"zh-Hans": Globalize("zh-Hans").pluralGenerator()}), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1394817807 = messageFormatterFn((function(  ) {
  return function (d) { return "Fields in Use (" + d.count + ")"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2015795514 = messageFormatterFn((function(  ) {
  return function (d) { return "Sheets"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b714087387 = messageFormatterFn((function(  ) {
  return function (d) { return "Sheets (" + d.count + ")"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1906814584 = messageFormatterFn((function(  ) {
  return function (d) { return "Site Name"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1008198972 = messageFormatterFn((function(  ) {
  return function (d) { return "Subject"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1026641054 = messageFormatterFn((function(  ) {
  return function (d) { return "Table"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1761177707 = messageFormatterFn((function(  ) {
  return function (d) { return "Tables"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a310304845 = messageFormatterFn((function(  ) {
  return function (d) { return "Upstream Databases"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b571809166 = messageFormatterFn((function(  ) {
  return function (d) { return "Upstream Databases (" + d.count + ")"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b338772317 = messageFormatterFn((function(  ) {
  return function (d) { return "Upsteam Data Sources"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1388088422 = messageFormatterFn((function(  ) {
  return function (d) { return "Upstream Tables"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b981810567 = messageFormatterFn((function(  ) {
  return function (d) { return "Upstream Tables (" + d.count + ")"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1585077846 = messageFormatterFn((function(  ) {
  return function (d) { return "Upstream Usage"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b643873605 = messageFormatterFn((function(  ) {
  return function (d) { return "Workbook Id"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1364741577 = messageFormatterFn((function(  ) {
  return function (d) { return "Workbooks"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b605101962 = messageFormatterFn((function(  ) {
  return function (d) { return "Workbooks (" + d.count + ")"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a848610705 = messageFormatterFn((function(  ) {
  return function (d) { return "Loading"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1284870127 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1206197088 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b828386582 = messageFormatterFn((function(  ) {
  return function (d) { return "?????? Tableau ????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1965266179 = messageFormatterFn((function(  ) {
  return function (d) { return "?????? Tableau ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1999743723 = messageFormatterFn((function(  ) {
  return function (d) { return "?????? Tableau"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1460631410 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1210483799 = messageFormatterFn((function(  ) {
  return function (d) { return "Join"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a156329742 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b500458706 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a130261292 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b92606297 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1481171743 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b73449052 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a787034438 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b783314861 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b226436187 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b619019051 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1579396688 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a538129713 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a713390790 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1250177323 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b386043651 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a211425126 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1559945983 = messageFormatterFn((function(  ) {
  return function (d) { return "??????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1049410267 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1552317726 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1835917113 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1435196141 = messageFormatterFn((function(  ) {
  return function (d) { return "Tableau ?????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1849827602 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2018973531 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b310308461 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1803740400 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1010544552 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1624704120 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1133417668 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1437236647 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????: "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1816119763 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1711812418 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1845395898 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b705315078 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1362400676 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2068247092 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b320607509 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1028309814 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1784973880 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1030603982 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1297737491 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1938442750 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1949369837 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1027111782 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b797433806 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1922948785 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1756823984 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1085576390 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a156594937 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a971195483 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b756775331 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1127121768 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1419550332 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1933376065 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1461954368 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a179960239 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a270771846 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1408123414 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1719017226 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b384605678 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b965872161 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a443438281 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b998857842 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b427132323 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1264264466 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1926371441 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1772756504 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b93217691 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1343044479 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b80649765 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1898568978 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1764872365 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b887680558 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1666980033 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1126066138 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????(???)"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1904210208 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a32705314 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b35729832 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a668344062 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b399843073 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b799511846 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1796571841 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b25050026 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1304219663 = messageFormatterFn((function(  ) {
  return function (d) { return "Insert"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b674679252 = messageFormatterFn((function(  ) {
  return function (d) { return "ISO Quarters"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1592870960 = messageFormatterFn((function(  ) {
  return function (d) { return "ISO Weekdays"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1754338352 = messageFormatterFn((function(  ) {
  return function (d) { return "ISO Weeks"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a17183463 = messageFormatterFn((function(  ) {
  return function (d) { return "ISO Years"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1000682103 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a244480280 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1049607093 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1468655685 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a43500562 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a387506392 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1673716800 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????? Tableau ?????? " + d.VERSION + "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1880796633 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????? Tableau ?????? " + d.VERSION + " ????????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1281503599 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????? Tableau ?????? " + d.VERSION + " ????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b274128742 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????? Tableau " + d.VERSION + " ?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b274127781 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????????????? Tableau " + d.VERSION + " ?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b274126820 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????????????? Tableau " + d.VERSION + " ?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b274125859 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????????????? Tableau " + d.VERSION + " ???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b274124898 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????????????? Tableau " + d.VERSION + " ???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b274123937 = messageFormatterFn((function(  ) {
  return function (d) { return "????????? Tableau ?????? " + d.VERSION + " ??????????????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1693124704 = messageFormatterFn((function(  ) {
  return function (d) { return "Cancel"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1235902092 = messageFormatterFn((function(  ) {
  return function (d) { return "Download PowerPoint"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1752702303 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1449886943 = messageFormatterFn((function(  ) {
  return function (d) { return "??????: "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1644565480 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b845155105 = messageFormatterFn((function(  ) {
  return function (d) { return "??????: " + d["0"]; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1401207206 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????? URL: "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2135391110 = messageFormatterFn((function(  ) {
  return function (d) { return "?????? ID: "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1254315719 = messageFormatterFn((function(  ) {
  return function (d) { return "??????: "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1858054693 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a46198341 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b144723805 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a134553850 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????????????????????????? Tableau ????????? Web ????????????????????????????????????????????????????????????????????????????????????????????? "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b795254068 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1431860934 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b422577754 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1102747932 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b131841610 = messageFormatterFn((function(  ) {
  return function (d) { return "URL"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1271342332 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a559446619 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1608747853 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????????????? Tableau ????????? Web ??????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b854539534 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2035249491 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????? URL:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1547786691 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b566547200 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b397850855 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b54697624 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a669086745 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a96778278 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a965147414 = messageFormatterFn((function(  ) {
  return function (d) { return "Go to Sheet"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1077713361 = messageFormatterFn((function(  ) {
  return function (d) { return "Go to Sheet"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1173206086 = messageFormatterFn((function(  ) {
  return function (d) { return "Cancel"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1550829389 = messageFormatterFn((function(  ) {
  return function (d) { return "Enter sheet name"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1195015416 = messageFormatterFn((function(  ) {
  return function (d) { return "Choose sheet from list"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b306782641 = messageFormatterFn((function(  ) {
  return function (d) { return "Type or select sheet to go to"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b594793319 = messageFormatterFn((function(  ) {
  return function (d) { return "that localize/widgets now requires to exist"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b773629124 = messageFormatterFn((function(  ) {
  return function (d) { return "do not localize"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1480513969 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b974431825 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b205597027 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a603163690 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????..."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1982092220 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1698830327 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1403510746 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a299526060 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2033585770 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b169459756 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1911432885 = messageFormatterFn((function(  ) {
  return function (d) { return "?????? URL"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a152530254 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a744720367 = messageFormatterFn((function(  ) {
  return function (d) { return "?????? SQL"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1381385010 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1288402736 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b197154419 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????? SQL ??????????????????CREATE TABLE " + "#" + "TempTable(x varchar(25));???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b650979301 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????? SQL ??????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a316708602 = messageFormatterFn((function(  ) {
  return function (d) { return "??????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b340466574 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1975163595 = messageFormatterFn((function(  ) {
  return function (d) { return "Give your Metric a name"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2114950664 = messageFormatterFn((function(  ) {
  return function (d) { return "Metric Title"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a35081502 = messageFormatterFn((function(  ) {
  return function (d) { return "No Field Selected"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b789688399 = messageFormatterFn((function(  ) {
  return function (d) { return "Successfully created metric: " + d.metricName; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1889458678 = messageFormatterFn((function(  ) {
  return function (d) { return "Error: Failed to create metric"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1472667129 = messageFormatterFn((function(  ) {
  return function (d) { return "_New Metric"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2013828087 = messageFormatterFn((function(  ) {
  return function (d) { return "Error: Can't save Metric with no selected field"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1891152544 = messageFormatterFn((function(  ) {
  return function (d) { return "Error: No datasource id provided"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1970821169 = messageFormatterFn((function(  ) {
  return function (d) { return "Error: Unknown Action Type"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a954970388 = messageFormatterFn((function(  ) {
  return function (d) { return "Error: Tableau Server could not find that Data Source"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a458160017 = messageFormatterFn((function(  ) {
  return function (d) { return "Error: Fetch request failed. This is probably due to a missing API key, or CORS misconfiguration"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a87792784 = messageFormatterFn((function(  ) {
  return function (d) { return "Error: Failed to fetch information for that datasource"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b156043496 = messageFormatterFn((function(  ) {
  return function (d) { return "Error: API Key Cookie Not Found"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1172679822 = messageFormatterFn((function(  ) {
  return function (d) { return "Error: Failed to fetch field list"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b983924402 = messageFormatterFn((function(  ) {
  return function (d) { return "Placeholder for Reference Link"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b685373778 = messageFormatterFn((function(  ) {
  return function (d) { return "PERIOD"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1951641138 = messageFormatterFn((function(  ) {
  return function (d) { return "HOUR"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a335941092 = messageFormatterFn((function(  ) {
  return function (d) { return "DAY"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1923607486 = messageFormatterFn((function(  ) {
  return function (d) { return "WEEK"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a507544712 = messageFormatterFn((function(  ) {
  return function (d) { return "MONTH"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1866461621 = messageFormatterFn((function(  ) {
  return function (d) { return "YEAR"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1710104258 = messageFormatterFn((function(  ) {
  return function (d) { return "Transport Error: Please try again in a moment"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1483658387 = messageFormatterFn((function(  ) {
  return function (d) { return "Updated " + d.lastUpdated; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2062877427 = messageFormatterFn((function(  ) {
  return function (d) { return "PAST"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1916844178 = messageFormatterFn((function(  ) {
  return function (d) { return "AQL Query Failed"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a990908278 = messageFormatterFn((function(  ) {
  return function (d) { return "Unable to make HTTPS request for metric value"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1183735566 = messageFormatterFn((function(  ) {
  return function (d) { return "Error: Unable to query type of column " + d.columnName; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1875139590 = messageFormatterFn((function(  ) {
  return function (d) { return "No Value"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a949793720 = messageFormatterFn((function(  ) {
  return function (d) { return "Error: No metric value"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1844369902 = messageFormatterFn((function(  ) {
  return function (d) { return "loading ..."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1117195080 = messageFormatterFn((function(  ) {
  return function (d) { return "Aggregation: "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a835545524 = messageFormatterFn((function(  ) {
  return function (d) { return "Measure: "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1453360018 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1200470433 = messageFormatterFn((function(  ) {
  return function (d) { return ","; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a438874237 = messageFormatterFn((function(  ) {
  return function (d) { return ", "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b56677863 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b215012916 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1009839158 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b84015473 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a152741404 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1746866784 = messageFormatterFn((function(  ) {
  return function (d) { return "??????(??????)"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b724160980 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1732266970 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1534731559 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b630591975 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a896503119 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a334023434 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????" + d.fieldLabel + "???????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1989673470 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b433075896 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????: " + d.fieldLabel; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1945074067 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1991644132 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b914442681 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1584870025 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1605857896 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1504514048 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2072075567 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a92120589 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a25146607 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a211211187 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1423438830 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b932121140 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1991527877 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b885756687 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2037892330 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b906732881 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2016916136 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a797075809 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b574242470 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1877454351 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1046194666 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1001456963 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1922192054 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1014784032 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1652125257 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1069132208 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1336171085 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2056564912 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a642275912 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????? 50 ?????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b784657548 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a154199494 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????? 1 ????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a695014453 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b328993280 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a122168472 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a173105584 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1667687581 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1438681846 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a381616721 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b984688567 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1695955426 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1761749846 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b531562445 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a900392619 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b596183924 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a860101956 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2072635088 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b817458200 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1936692946 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b319600208 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a659841524 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1866174290 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1773213058 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1198589825 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1922209695 = messageFormatterFn((function( plural, pluralFuncs ) {
  return function (d) { return d.rowCount + " " + plural(d.rowCounter, 0, pluralFuncs["zh-Hans"], { one: function() { return "???";}, other: function() { return "???";} }); }
})(messageFormat.plural, {"zh-Hans": Globalize("zh-Hans").pluralGenerator()}), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b541010661 = messageFormatterFn((function( plural, pluralFuncs ) {
  return function (d) { return d.valueCount + " " + plural(d.valueCounter, 0, pluralFuncs["zh-Hans"], { one: function() { return "????????????";}, other: function() { return "????????????";} }); }
})(messageFormat.plural, {"zh-Hans": Globalize("zh-Hans").pluralGenerator()}), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b919943105 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a294970712 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1840993406 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1136109025 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b479192975 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1445229369 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????? 10000 ?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1609422597 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1723148111 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1131659284 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????????????????" + d.Retry + "?????????" + d.Retry; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a160270899 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b220916469 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????" + d.Retry + "?????????" + d.Retry; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a744337642 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b819830942 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b547904255 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b149927967 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b699162304 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1774772303 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a429096238 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1021477878 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1715461781 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b252769188 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????" + d.Retry + "?????????" + d.Retry; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1400944517 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1505390585 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a912833254 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1620769321 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????..."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b358657263 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????" + d.Retry + "????????????" + d.Retry + ": "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1534029951 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b434494372 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a368489846 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b709977516 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b940704292 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a962645428 = messageFormatterFn((function( plural, pluralFuncs ) {
  return function (d) { return d.fieldCountLoc + " " + plural(d.fieldCount, 0, pluralFuncs["zh-Hans"], { one: function() { return "?????????";}, other: function() { return "?????????";} }); }
})(messageFormat.plural, {"zh-Hans": Globalize("zh-Hans").pluralGenerator()}), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1417312143 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a39256590 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a735819322 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b872384403 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b397080629 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1460046464 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1275230509 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????? UTF-8???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1002494826 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1618825137 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????? " + d.max + " ????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1178938631 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a284896923 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????? 1 ????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b188331155 = messageFormatterFn((function(  ) {
  return function (d) { return "Field Details"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a571364796 = messageFormatterFn((function(  ) {
  return function (d) { return "Min, Max"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1431968181 = messageFormatterFn((function(  ) {
  return function (d) { return "Null"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1740200906 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b409976217 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a108154074 = messageFormatterFn((function(  ) {
  return function (d) { return d.baseTitle + " - ????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1097923210 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b937938048 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b945371777 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2030304167 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2022870438 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1169187585 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1944587413 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1791671656 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b818654672 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1225715835 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1897462833 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b993016587 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a73461332 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b990614770 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1853037093 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1972074600 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a326921425 = messageFormatterFn((function(  ) {
  return function (d) { return "??????(??????)"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b233853027 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b282407329 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1573033092 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1881155599 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1050179621 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1137521398 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1992420739 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1914751626 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a639257921 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????!"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1109782403 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1428048371 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b77936693 = messageFormatterFn((function(  ) {
  return function (d) { return " ????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b820268042 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1539616467 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b390106961 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a29576740 = messageFormatterFn((function(  ) {
  return function (d) { return "??????/????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1544486788 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b136616276 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1662594918 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1905732018 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2114637973 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b372409081 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b183502279 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b660257015 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b704303157 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1875933714 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b395682044 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1401291663 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b371695909 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a549137299 = messageFormatterFn((function(  ) {
  return function (d) { return "zh_CN"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b705905559 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b69994303 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b206257346 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a423663452 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1317452695 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a995359890 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1643551492 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????(????????????)"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1535858740 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1998871295 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????..."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a829883359 = messageFormatterFn((function(  ) {
  return function (d) { return "??????(??????)"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b483195123 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a206939821 = messageFormatterFn((function(  ) {
  return function (d) { return "??????..."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a866656453 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b184464383 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a454215813 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1196370565 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1687336270 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1661874575 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b831330036 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a280047488 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1284210017 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b220835589 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1628280388 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a772695412 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a856322124 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a300378189 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b907541141 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b207680460 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1094139977 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b926600972 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a594939046 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a538015325 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b334899065 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a631929749 = messageFormatterFn((function(  ) {
  return function (d) { return "Feedback"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1013516353 = messageFormatterFn((function(  ) {
  return function (d) { return "Learn More"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1027098360 = messageFormatterFn((function(  ) {
  return function (d) { return "Restore " + d.numberOfSheets + " sheets from your previous session?"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b516782515 = messageFormatterFn((function(  ) {
  return function (d) { return "We???ve restored your previous session"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1803892726 = messageFormatterFn((function(  ) {
  return function (d) { return "No"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a96036584 = messageFormatterFn((function(  ) {
  return function (d) { return "Yes"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1466468149 = messageFormatterFn((function(  ) {
  return function (d) { return "Usage Analytics"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a291494287 = messageFormatterFn((function(  ) {
  return function (d) { return "No marks appear on this map because geographic data is either missing or incorrectly structured."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a939888392 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b723446761 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1767154667 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b80515203 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2076335313 = messageFormatterFn((function(  ) {
  return function (d) { return "zh_CN"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1258491440 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1359189212 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1581630710 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1652533710 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2086837911 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1519922550 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1051102681 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a367583561 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????????????????????????????????????????????????????<br />??????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a405996856 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1383552439 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b693097322 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1214959443 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1965467749 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1064196033 = messageFormatterFn((function(  ) {
  return function (d) { return d.PROJECT_NAME; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1073236515 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????" + d.PROJECT_NAME + "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a593600830 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????" + d.PROJECT_NAME + "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1314992155 = messageFormatterFn((function(  ) {
  return function (d) { return d.SITE_NAME + " (???????????????)"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a74436889 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1306353414 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2138842185 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1145321968 = messageFormatterFn((function(  ) {
  return function (d) { return "????????? " + d.DATA_SOURCE; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1688135704 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1085521158 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????? " + d.DATA_SOURCE + " ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b772533073 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????? ServiceNow ??????????????????????????????????????????????????????????????? ServiceNow ??????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1929941990 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????? QuickBooks Online ?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a447831220 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????? Tableau ????????? QuickBooks Online???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b187131655 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a447832181 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????? Tableau ????????? QuickBooks Online??????????????????????????????????????? Tableau???????????????????????????????????? Tableau Online ?????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b501983033 = messageFormatterFn((function(  ) {
  return function (d) { return "????????? " + d.DATA_SOURCE + " ???????????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2054527807 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1755214541 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1288087170 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b790550571 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1579300466 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a653280806 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a672141548 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b589123771 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1523010257 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a976848815 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a273423858 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1704746139 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1814193946 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1594228775 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b144562966 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b125075945 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a511308079 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1529844130 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1233827168 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1302272591 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1867425957 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1255406283 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b840665788 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a133208302 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b158547536 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b651736702 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a172938673 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1803979491 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1871708779 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2145730113 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1745331835 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1916346357 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a392570283 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2004049193 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b893610263 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1542807684 = messageFormatterFn((function(  ) {
  return function (d) { return "??????:"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b53839122 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b613318838 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b841022641 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a663529305 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a30921903 = messageFormatterFn((function(  ) {
  return function (d) { return d.alias + " ??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1431354940 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a229443842 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1955577207 = messageFormatterFn((function(  ) {
  return function (d) { return "Show template project contributors!"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1730373646 = messageFormatterFn((function(  ) {
  return function (d) { return "Hide template project contributors!"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b859231237 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b959355842 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b965539255 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a651155198 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a966793410 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b371496808 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b899298160 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2100198494 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1586462971 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1861113744 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a258672848 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1661786374 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b538781547 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1335485715 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1005796540 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1399071121 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a394930784 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b798498267 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1654658548 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a20617347 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1449218862 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a938727568 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a386407839 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a78746415 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1075341446 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1173188836 = messageFormatterFn((function(  ) {
  return function (d) { return "Show template project contributors!"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a564172393 = messageFormatterFn((function(  ) {
  return function (d) { return "Hide template project contributors!"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2130922068 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a90840016 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1458610853 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a379945275 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1081328821 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b44373905 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a140981840 = messageFormatterFn((function(  ) {
  return function (d) { return "??? " + d["1"] + " ??? " + d["2"]; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1780406466 = messageFormatterFn((function(  ) {
  return function (d) { return "??? " + d["1"]; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b179719524 = messageFormatterFn((function(  ) {
  return function (d) { return d["1"] + " " + d["2"] + " " + d["4"]; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2099607385 = messageFormatterFn((function(  ) {
  return function (d) { return d["1"] + " " + d["2"] + " ?????? " + d["3"] + " " + d["4"]; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1655654071 = messageFormatterFn((function(  ) {
  return function (d) { return d["1"] + " ??? " + d["2"]; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a357970237 = messageFormatterFn((function(  ) {
  return function (d) { return d["1"] + " " + d["2"] + " ?????? " + d["3"] + " ??? " + d["4"] + " ??? " + d["5"]; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a621258397 = messageFormatterFn((function(  ) {
  return function (d) { return d["1"] + " " + d["2"] + " ?????? " + d["3"] + " ??? " + d["4"] + " ??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b505787103 = messageFormatterFn((function(  ) {
  return function (d) { return "???/??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b799052628 = messageFormatterFn((function(  ) {
  return function (d) { return "???/??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1359139566 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1229807629 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1530314744 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1196453979 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1115352366 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1197015203 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b998176439 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1196865287 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1890232159 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1800113592 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1462348546 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1303277231 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1084030760 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1789049599 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b193158812 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1625376216 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1922494149 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1683277915 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1245589365 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1577335080 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b303807938 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b466983751 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a931001337 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1929894618 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a24894755 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b916472125 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b159371128 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b61607710 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1066207321 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2052129049 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a116997848 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1195917871 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b122657649 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a593053162 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a91336144 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2072803884 = messageFormatterFn((function(  ) {
  return function (d) { return d["1"] + " " + d["2"] + " ??? " + d["3"]; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1532903334 = messageFormatterFn((function(  ) {
  return function (d) { return d["1"] + d["2"] + " " + d["3"] + " ??? " + d["4"]; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1892454491 = messageFormatterFn((function(  ) {
  return function (d) { return "???/???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1167593428 = messageFormatterFn((function(  ) {
  return function (d) { return "???/???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a150064533 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2020767846 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1175418710 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b71139258 = messageFormatterFn((function(  ) {
  return function (d) { return "Show template project contributors!"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b680155701 = messageFormatterFn((function(  ) {
  return function (d) { return "Hide template project contributors!"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a118695726 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1225141127 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b595401256 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b554920610 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2054421935 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b670828719 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a881045378 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a616327209 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b27822790 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1639253882 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a730822088 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1132569708 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1596108875 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a960739979 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1887412444 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1985217879 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1383496111 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2052274916 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1917060538 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1084344220 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a710390371 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1991171832 = messageFormatterFn((function(  ) {
  return function (d) { return ","; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a652068916 = messageFormatterFn((function(  ) {
  return function (d) { return "b"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2050060993 = messageFormatterFn((function(  ) {
  return function (d) { return "m"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1611617571 = messageFormatterFn((function(  ) {
  return function (d) { return "p"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b443213152 = messageFormatterFn((function(  ) {
  return function (d) { return "t"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1908964737 = messageFormatterFn((function(  ) {
  return function (d) { return "k"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1594369117 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1373727972 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1448858789 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b541022244 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1580309314 = messageFormatterFn((function(  ) {
  return function (d) { return "The username or password is not valid.  Check the database name and credentials and try again."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a424411568 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a657372504 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1606254058 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a915162855 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1216360693 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2096166184 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1820823856 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b314662847 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1876704443 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a72090235 = messageFormatterFn((function(  ) {
  return function (d) { return "??? " + d.weekNum + " ???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2013978346 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1819957053 = messageFormatterFn((function(  ) {
  return function (d) { return "Info: "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2052323444 = messageFormatterFn((function(  ) {
  return function (d) { return "Success: "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a838691195 = messageFormatterFn((function(  ) {
  return function (d) { return "Warning: "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1418808497 = messageFormatterFn((function(  ) {
  return function (d) { return "Error: "; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1335402452 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1370011705 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2025097092 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2044224521 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b98103942 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a752125968 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1294338898 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1990442357 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1904316047 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1040840588 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????..."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1176818211 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a140514727 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????????????????????????????..."; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1707057514 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a860433390 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????????????????????????????????????????????????????????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a629899337 = messageFormatterFn((function(  ) {
  return function (d) { return "??????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1634501512 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a292553168 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1342777268 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a740120965 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b194759695 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a767963183 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1362925230 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2085518276 = messageFormatterFn((function(  ) {
  return function (d) { return "Clear All"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a200003466 = messageFormatterFn((function(  ) {
  return function (d) { return "Include"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a110386696 = messageFormatterFn((function(  ) {
  return function (d) { return "Sheet Selection"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a241307977 = messageFormatterFn((function(  ) {
  return function (d) { return "Select All"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1039370341 = messageFormatterFn((function(  ) {
  return function (d) { return d.x + " of " + d.y; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b935731969 = messageFormatterFn((function(  ) {
  return function (d) { return "???????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2136748321 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1050297293 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a234851685 = messageFormatterFn((function( plural, pluralFuncs ) {
  return function (d) { return plural(d.count, 0, pluralFuncs["zh-Hans"], { one: function() { return d.formattedCount + " calculation";}, other: function() { return d.formattedCount + " calculations";} }); }
})(messageFormat.plural, {"zh-Hans": Globalize("zh-Hans").pluralGenerator()}), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1768736346 = messageFormatterFn((function( plural, pluralFuncs ) {
  return function (d) { return plural(d.count, 0, pluralFuncs["zh-Hans"], { one: function() { return d.formattedCount + " user";}, other: function() { return d.formattedCount + " users";} }); }
})(messageFormat.plural, {"zh-Hans": Globalize("zh-Hans").pluralGenerator()}), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1931032501 = messageFormatterFn((function( plural, pluralFuncs ) {
  return function (d) { return plural(d.count, 0, pluralFuncs["zh-Hans"], { one: function() { return d.formattedCount + " workbook";}, other: function() { return d.formattedCount + " workbooks";} }); }
})(messageFormat.plural, {"zh-Hans": Globalize("zh-Hans").pluralGenerator()}), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1722849454 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1434689050 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a130582672 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1013340243 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b741174224 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b667607768 = messageFormatterFn((function( plural, pluralFuncs ) {
  return function (d) { return plural(d.count, 0, pluralFuncs["zh-Hans"], { one: function() { return d.formattedCount + " dimension";}, other: function() { return d.formattedCount + " dimensions";} }); }
})(messageFormat.plural, {"zh-Hans": Globalize("zh-Hans").pluralGenerator()}), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1380296020 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1631312508 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1989749820 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a961277204 = messageFormatterFn((function( plural, pluralFuncs ) {
  return function (d) { return plural(d.count, 0, pluralFuncs["zh-Hans"], { one: function() { return d.formattedCount + " field";}, other: function() { return d.formattedCount + " fields";} }); }
})(messageFormat.plural, {"zh-Hans": Globalize("zh-Hans").pluralGenerator()}), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1993588419 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a790006550 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1279524621 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b946158772 = messageFormatterFn((function(  ) {
  return function (d) { return "????????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1665728114 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1944643792 = messageFormatterFn((function( plural, pluralFuncs ) {
  return function (d) { return plural(d.count, 0, pluralFuncs["zh-Hans"], { one: function() { return d.formattedCount + " measure";}, other: function() { return d.formattedCount + " measures";} }); }
})(messageFormat.plural, {"zh-Hans": Globalize("zh-Hans").pluralGenerator()}), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b679831372 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b126551892 = messageFormatterFn((function( plural, pluralFuncs ) {
  return function (d) { return plural(d.count, 0, pluralFuncs["zh-Hans"], { one: function() { return d.formattedCount + " member";}, other: function() { return d.formattedCount + " members";} }); }
})(messageFormat.plural, {"zh-Hans": Globalize("zh-Hans").pluralGenerator()}), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1813813296 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1963968633 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b923464357 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a60432405 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1521439943 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a80078128 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b467212399 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1985415037 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a127045081 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1617392417 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a345428408 = messageFormatterFn((function(  ) {
  return function (d) { return "?????????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a727824723 = messageFormatterFn((function(  ) {
  return function (d) { return "??????"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1798904189 = messageFormatterFn((function(  ) {
  return function (d) { return "Connection"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1142056319 = messageFormatterFn((function(  ) {
  return function (d) { return "Howdy World!"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1925097445 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1854980550 = messageFormatterFn((function(  ) {
  return function (d) { return "Ctrl+"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1098205747 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a267368978 = messageFormatterFn((function(  ) {
  return function (d) { return "Alt+"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2028383936 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2083879125 = messageFormatterFn((function(  ) {
  return function (d) { return "Shift+"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2033077612 = messageFormatterFn((function(  ) {
  return function (d) { return "Win+"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a751335476 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796391914 = messageFormatterFn((function(  ) {
  return function (d) { return "A"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796392875 = messageFormatterFn((function(  ) {
  return function (d) { return "B"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796393836 = messageFormatterFn((function(  ) {
  return function (d) { return "C"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796394797 = messageFormatterFn((function(  ) {
  return function (d) { return "D"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796395758 = messageFormatterFn((function(  ) {
  return function (d) { return "E"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796396719 = messageFormatterFn((function(  ) {
  return function (d) { return "F"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796397680 = messageFormatterFn((function(  ) {
  return function (d) { return "G"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796398641 = messageFormatterFn((function(  ) {
  return function (d) { return "H"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796399602 = messageFormatterFn((function(  ) {
  return function (d) { return "I"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796400563 = messageFormatterFn((function(  ) {
  return function (d) { return "J"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796401524 = messageFormatterFn((function(  ) {
  return function (d) { return "K"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796402485 = messageFormatterFn((function(  ) {
  return function (d) { return "L"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796403446 = messageFormatterFn((function(  ) {
  return function (d) { return "M"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796404407 = messageFormatterFn((function(  ) {
  return function (d) { return "N"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796405368 = messageFormatterFn((function(  ) {
  return function (d) { return "O"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796406329 = messageFormatterFn((function(  ) {
  return function (d) { return "P"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796407290 = messageFormatterFn((function(  ) {
  return function (d) { return "Q"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796408251 = messageFormatterFn((function(  ) {
  return function (d) { return "R"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796409212 = messageFormatterFn((function(  ) {
  return function (d) { return "S"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796410173 = messageFormatterFn((function(  ) {
  return function (d) { return "T"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796411134 = messageFormatterFn((function(  ) {
  return function (d) { return "U"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796412095 = messageFormatterFn((function(  ) {
  return function (d) { return "V"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796413056 = messageFormatterFn((function(  ) {
  return function (d) { return "W"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796414017 = messageFormatterFn((function(  ) {
  return function (d) { return "X"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796414978 = messageFormatterFn((function(  ) {
  return function (d) { return "Y"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1796415939 = messageFormatterFn((function(  ) {
  return function (d) { return "Z"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a516714575 = messageFormatterFn((function(  ) {
  return function (d) { return "Zero"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a976594101 = messageFormatterFn((function(  ) {
  return function (d) { return "One"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a981489435 = messageFormatterFn((function(  ) {
  return function (d) { return "Two"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2106119955 = messageFormatterFn((function(  ) {
  return function (d) { return "Three"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b46540979 = messageFormatterFn((function(  ) {
  return function (d) { return "Four"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b52064807 = messageFormatterFn((function(  ) {
  return function (d) { return "Five"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a980157489 = messageFormatterFn((function(  ) {
  return function (d) { return "Six"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1219158940 = messageFormatterFn((function(  ) {
  return function (d) { return "Seven"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1779768222 = messageFormatterFn((function(  ) {
  return function (d) { return "Eight"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a176730073 = messageFormatterFn((function(  ) {
  return function (d) { return "Nine"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b523015054 = messageFormatterFn((function(  ) {
  return function (d) { return "F1"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b523014093 = messageFormatterFn((function(  ) {
  return function (d) { return "F2"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b523013132 = messageFormatterFn((function(  ) {
  return function (d) { return "F3"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b523012171 = messageFormatterFn((function(  ) {
  return function (d) { return "F4"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b523011210 = messageFormatterFn((function(  ) {
  return function (d) { return "F5"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b523010249 = messageFormatterFn((function(  ) {
  return function (d) { return "F6"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b523009288 = messageFormatterFn((function(  ) {
  return function (d) { return "F7"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b523008327 = messageFormatterFn((function(  ) {
  return function (d) { return "F8"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b523007366 = messageFormatterFn((function(  ) {
  return function (d) { return "F9"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a966414228 = messageFormatterFn((function(  ) {
  return function (d) { return "F10"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a966415189 = messageFormatterFn((function(  ) {
  return function (d) { return "F11"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a966416150 = messageFormatterFn((function(  ) {
  return function (d) { return "F12"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1934828455 = messageFormatterFn((function(  ) {
  return function (d) { return "Enter"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a231596592 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1468896095 = messageFormatterFn((function(  ) {
  return function (d) { return "/"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2051044451 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a801776218 = messageFormatterFn((function(  ) {
  return function (d) { return "Down arrow"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2024625528 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1021073535 = messageFormatterFn((function(  ) {
  return function (d) { return "Left arrow"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1488634735 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1561244294 = messageFormatterFn((function(  ) {
  return function (d) { return "Right arrow"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b940376676 = messageFormatterFn((function(  ) {
  return function (d) { return "???"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b517096109 = messageFormatterFn((function(  ) {
  return function (d) { return "Up arrow"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1292572274 = messageFormatterFn((function(  ) {
  return function (d) { return "Backspace"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a275850835 = messageFormatterFn((function(  ) {
  return function (d) { return "CapsLock"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a182207588 = messageFormatterFn((function(  ) {
  return function (d) { return "Comma"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a144422214 = messageFormatterFn((function(  ) {
  return function (d) { return "Menu"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1519179886 = messageFormatterFn((function(  ) {
  return function (d) { return "Delete"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a967357930 = messageFormatterFn((function(  ) {
  return function (d) { return "End"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1757483866 = messageFormatterFn((function(  ) {
  return function (d) { return "Equals"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a236980929 = messageFormatterFn((function(  ) {
  return function (d) { return "Plus"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b497695512 = messageFormatterFn((function(  ) {
  return function (d) { return "Escape"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a10466502 = messageFormatterFn((function(  ) {
  return function (d) { return "Home"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1797105376 = messageFormatterFn((function(  ) {
  return function (d) { return "Insert"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1400580364 = messageFormatterFn((function(  ) {
  return function (d) { return "Slash"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1876531047 = messageFormatterFn((function(  ) {
  return function (d) { return "Asterisk"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b116797767 = messageFormatterFn((function(  ) {
  return function (d) { return "Dash"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b552832712 = messageFormatterFn((function(  ) {
  return function (d) { return "PageDown"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1479398479 = messageFormatterFn((function(  ) {
  return function (d) { return "PageUp"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1904973272 = messageFormatterFn((function(  ) {
  return function (d) { return "Period"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1514617429 = messageFormatterFn((function(  ) {
  return function (d) { return "Space"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a980821540 = messageFormatterFn((function(  ) {
  return function (d) { return "Tab"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2083061721 = messageFormatterFn((function(  ) {
  return function (d) { return "Tilde"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1920196523 = messageFormatterFn((function(  ) {
  return function (d) { return "Backtick"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1607853527 = messageFormatterFn((function(  ) {
  return function (d) { return "Exclamation mark"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1557563703 = messageFormatterFn((function(  ) {
  return function (d) { return "@"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1157725605 = messageFormatterFn((function(  ) {
  return function (d) { return "Pound"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a248562944 = messageFormatterFn((function(  ) {
  return function (d) { return "$"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b250802447 = messageFormatterFn((function(  ) {
  return function (d) { return "%"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b214202990 = messageFormatterFn((function(  ) {
  return function (d) { return "Caret"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a2045863172 = messageFormatterFn((function(  ) {
  return function (d) { return "&"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1792012923 = messageFormatterFn((function(  ) {
  return function (d) { return "Open parenthesis"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a431105381 = messageFormatterFn((function(  ) {
  return function (d) { return "Close parenthesis"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b2096191775 = messageFormatterFn((function(  ) {
  return function (d) { return "Underscore"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b698065768 = messageFormatterFn((function(  ) {
  return function (d) { return "Open brace"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a469337858 = messageFormatterFn((function(  ) {
  return function (d) { return "Close brace"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1402692400 = messageFormatterFn((function(  ) {
  return function (d) { return "Open square bracket"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b759397478 = messageFormatterFn((function(  ) {
  return function (d) { return "Close square bracket"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a561990054 = messageFormatterFn((function(  ) {
  return function (d) { return "Open angle bracket"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1323529212 = messageFormatterFn((function(  ) {
  return function (d) { return "Close angle bracket"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1398195526 = messageFormatterFn((function(  ) {
  return function (d) { return "Question mark"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1094113821 = messageFormatterFn((function(  ) {
  return function (d) { return "Single quote"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a1075270202 = messageFormatterFn((function(  ) {
  return function (d) { return "Double quote"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a181356142 = messageFormatterFn((function(  ) {
  return function (d) { return "Colon"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.a314348864 = messageFormatterFn((function(  ) {
  return function (d) { return "Semicolon"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b691074740 = messageFormatterFn((function(  ) {
  return function (d) { return "Vertical bar"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
Globalize.b1406609339 = messageFormatterFn((function(  ) {
  return function (d) { return "Backslash"; }
})(), Globalize("zh-Hans").pluralGenerator({}));
}));
