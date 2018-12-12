/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 43);
/******/ })
/************************************************************************/
/******/ ({

/***/ 125:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 126:
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 43:
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(44);
__webpack_require__(125);
module.exports = __webpack_require__(126);


/***/ }),

/***/ 44:
/***/ (function(module, __webpack_exports__) {

"use strict";
throw new Error("Module build failed: SyntaxError: /Users/xiencias/code/comunica7/static/app.js: Legacy octal literals are not allowed in strict mode (12869:10)\n\n\u001b[0m \u001b[90m 12867 | \u001b[39m\u001b[90m// values for the mode field\u001b[39m\u001b[0m\n\u001b[0m \u001b[90m 12868 | \u001b[39m\u001b[36mvar\u001b[39m modes \u001b[33m=\u001b[39m\u001b[0m\n\u001b[0m\u001b[31m\u001b[1m>\u001b[22m\u001b[39m\u001b[90m 12869 | \u001b[39m  { suid\u001b[33m:\u001b[39m \u001b[35m04000\u001b[39m \u001b[90m// set uid on extraction\u001b[39m\u001b[0m\n\u001b[0m \u001b[90m       | \u001b[39m          \u001b[31m\u001b[1m^\u001b[22m\u001b[39m\u001b[0m\n\u001b[0m \u001b[90m 12870 | \u001b[39m  \u001b[33m,\u001b[39m sgid\u001b[33m:\u001b[39m \u001b[35m02000\u001b[39m \u001b[90m// set gid on extraction\u001b[39m\u001b[0m\n\u001b[0m \u001b[90m 12871 | \u001b[39m  \u001b[33m,\u001b[39m svtx\u001b[33m:\u001b[39m \u001b[35m01000\u001b[39m \u001b[90m// set restricted deletion flag on dirs on extraction\u001b[39m\u001b[0m\n\u001b[0m \u001b[90m 12872 | \u001b[39m  \u001b[33m,\u001b[39m uread\u001b[33m:\u001b[39m  \u001b[35m0400\u001b[39m\u001b[0m\n    at _class.raise (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:4028:15)\n    at _class.readNumber (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:4887:14)\n    at _class.getTokenFromCode (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:4679:14)\n    at _class.readToken (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:4243:12)\n    at _class.readToken (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:3756:46)\n    at _class.nextToken (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:4235:12)\n    at _class.next (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:4171:10)\n    at _class.eat (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:4176:12)\n    at _class.parseObjectProperty (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:6984:14)\n    at _class.parseObjPropValue (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:7010:99)\n    at _class.parseObj (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:6921:12)\n    at _class.parseExprAtom (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:6464:21)\n    at _class.parseExprAtom (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:3724:52)\n    at _class.parseExprSubscripts (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:6081:21)\n    at _class.parseMaybeUnary (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:6060:21)\n    at _class.parseExprOps (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:5945:21)\n    at _class.parseMaybeConditional (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:5917:21)\n    at _class.parseMaybeAssign (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:5864:21)\n    at _class.parseVar (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:8123:26)\n    at _class.parseVarStatement (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:7937:10)\n    at _class.parseStatementContent (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:7528:21)\n    at _class.parseStatement (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:7478:17)\n    at _class.parseBlockOrModuleBlockBody (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:8046:23)\n    at _class.parseBlockBody (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:8033:10)\n    at _class.parseBlock (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:8022:10)\n    at _class.parseFunctionBody (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:7130:24)\n    at _class.parseFunctionBodyAndFinish (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:7112:10)\n    at /Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:8186:14\n    at _class.withTopicForbiddingContext (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:7402:14)\n    at _class.parseFunction (/Users/xiencias/code/comunica7/static/node_modules/@babel/parser/lib/index.js:8185:10)");

/***/ })

/******/ });