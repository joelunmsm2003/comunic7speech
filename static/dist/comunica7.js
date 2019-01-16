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
/******/ 	return __webpack_require__(__webpack_require__.s = 0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports) {

throw new Error("Module build failed: SyntaxError: /Users/xiencias/code/comunica7/discador/react/comunica7.js: Unexpected token (8:10)\n\n\u001b[0m \u001b[90m  6 | \u001b[39m      \u001b[36mreturn\u001b[39m (\u001b[0m\n\u001b[0m \u001b[90m  7 | \u001b[39m\u001b[0m\n\u001b[0m\u001b[31m\u001b[1m>\u001b[22m\u001b[39m\u001b[90m  8 | \u001b[39m          \u001b[33m<\u001b[39m\u001b[33mnav\u001b[39m \u001b[36mclass\u001b[39m\u001b[33m=\u001b[39m\u001b[32m\"navbar navbar-expand-lg navbar-light bg-light\"\u001b[39m\u001b[33m>\u001b[39m\u001b[0m\n\u001b[0m \u001b[90m    | \u001b[39m          \u001b[31m\u001b[1m^\u001b[22m\u001b[39m\u001b[0m\n\u001b[0m \u001b[90m  9 | \u001b[39m\u001b[0m\n\u001b[0m \u001b[90m 10 | \u001b[39m            \u001b[33m<\u001b[39m\u001b[33mbutton\u001b[39m \u001b[36mclass\u001b[39m\u001b[33m=\u001b[39m\u001b[32m\"navbar-toggler\"\u001b[39m type\u001b[33m=\u001b[39m\u001b[32m\"button\"\u001b[39m data\u001b[33m-\u001b[39mtoggle\u001b[33m=\u001b[39m\u001b[32m\"collapse\"\u001b[39m data\u001b[33m-\u001b[39mtarget\u001b[33m=\u001b[39m\u001b[32m\"#navbarTogglerDemo01\"\u001b[39m aria\u001b[33m-\u001b[39mcontrols\u001b[33m=\u001b[39m\u001b[32m\"navbarTogglerDemo01\"\u001b[39m aria\u001b[33m-\u001b[39mexpanded\u001b[33m=\u001b[39m\u001b[32m\"false\"\u001b[39m aria\u001b[33m-\u001b[39mlabel\u001b[33m=\u001b[39m\u001b[32m\"Toggle navigation\"\u001b[39m\u001b[33m>\u001b[39m\u001b[0m\n\u001b[0m \u001b[90m 11 | \u001b[39m                \u001b[33m<\u001b[39m\u001b[33mspan\u001b[39m \u001b[36mclass\u001b[39m\u001b[33m=\u001b[39m\u001b[32m\"navbar-toggler-icon\"\u001b[39m\u001b[33m>\u001b[39m\u001b[33m<\u001b[39m\u001b[33m/\u001b[39m\u001b[33mspan\u001b[39m\u001b[33m>\u001b[39m\u001b[0m\n    at Parser.raise (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:4051:15)\n    at Parser.unexpected (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:5382:16)\n    at Parser.parseExprAtom (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:6541:20)\n    at Parser.parseExprSubscripts (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:6104:21)\n    at Parser.parseMaybeUnary (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:6083:21)\n    at Parser.parseExprOps (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:5968:21)\n    at Parser.parseMaybeConditional (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:5940:21)\n    at Parser.parseMaybeAssign (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:5887:21)\n    at Parser.parseParenAndDistinguishExpression (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:6699:28)\n    at Parser.parseExprAtom (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:6473:21)\n    at Parser.parseExprSubscripts (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:6104:21)\n    at Parser.parseMaybeUnary (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:6083:21)\n    at Parser.parseExprOps (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:5968:21)\n    at Parser.parseMaybeConditional (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:5940:21)\n    at Parser.parseMaybeAssign (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:5887:21)\n    at Parser.parseExpression (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:5840:21)\n    at Parser.parseReturnStatement (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:7863:28)\n    at Parser.parseStatementContent (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:7539:21)\n    at Parser.parseStatement (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:7505:17)\n    at Parser.parseBlockOrModuleBlockBody (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:8073:23)\n    at Parser.parseBlockBody (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:8060:10)\n    at Parser.parseBlock (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:8049:10)\n    at Parser.parseFunctionBody (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:7157:24)\n    at Parser.parseArrowExpression (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:7110:10)\n    at Parser.parseParenAndDistinguishExpression (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:6718:12)\n    at Parser.parseExprAtom (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:6473:21)\n    at Parser.parseExprSubscripts (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:6104:21)\n    at Parser.parseMaybeUnary (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:6083:21)\n    at Parser.parseExprOps (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:5968:21)\n    at Parser.parseMaybeConditional (/Users/xiencias/code/comunica7/node_modules/@babel/parser/lib/index.js:5940:21)");

/***/ })
/******/ ]);