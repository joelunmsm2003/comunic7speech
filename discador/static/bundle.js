"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

//Proveedore

var Hello = function (_React$Component) {
    _inherits(Hello, _React$Component);

    function Hello(props) {
        _classCallCheck(this, Hello);

        var _this = _possibleConstructorReturn(this, (Hello.__proto__ || Object.getPrototypeOf(Hello)).call(this, props));

        _this.state = {
            error: null,
            isLoaded: false,
            proveedores: [],
            carteras: [],
            resultados: []
        };

        console.log(_this.state);

        return _this;
    }

    _createClass(Hello, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            var _this2 = this;

            fetch("http://localhost:8000/discador/api_proveedor/").then(function (res) {
                return res.json();
            }).then(function (result) {

                _this2.setState({
                    isLoaded: true,
                    proveedores: result
                });
            }, function (error) {});
        }
    }, {
        key: "sacacarteras",
        value: function sacacarteras(item) {
            var _this3 = this;

            fetch("http://localhost:8000/discador/api_cartera/" + item.id).then(function (res) {
                return res.json();
            }).then(function (result) {

                console.log(result);
                _this3.setState({
                    isLoaded: true,
                    carteras: result
                });
            },
            // Note: it's important to handle errors here
            // instead of a catch() block so that we don't swallow
            // exceptions from actual bugs in components.
            function (error) {
                _this3.setState({
                    isLoaded: true,
                    error: error
                });
            });
        }
    }, {
        key: "sacaresultados",
        value: function sacaresultados(item) {
            var _this4 = this;

            fetch("http://localhost:8000/discador/api_cartera/" + item.id).then(function (res) {
                return res.json();
            }).then(function (result) {

                console.log(result);
                _this4.setState({
                    isLoaded: true,
                    carteras: result
                });
            },
            // Note: it's important to handle errors here
            // instead of a catch() block so that we don't swallow
            // exceptions from actual bugs in components.
            function (error) {
                _this4.setState({
                    isLoaded: true,
                    error: error
                });
            });
        }
    }, {
        key: "render",
        value: function render() {
            var _this5 = this;

            var _state = this.state,
                error = _state.error,
                isLoaded = _state.isLoaded,
                proveedores = _state.proveedores,
                carteras = _state.carteras;


            if (!isLoaded) {

                return React.createElement(
                    "div",
                    null,
                    "Loading..."
                );
            } else {

                return React.createElement(
                    "div",
                    { className: "row" },
                    React.createElement(
                        "div",
                        { className: "col-2" },
                        proveedores.map(function (item) {
                            return React.createElement(
                                "div",
                                { className: "list-group" },
                                React.createElement(
                                    "a",
                                    { className: "list-group-item list-group-item-action active", id: "list-home-list", "data-toggle": "list", href: "#list-home", role: "tab", "aria-controls": "home", onClick: function onClick(e) {
                                            return _this5.sacacarteras(item, e);
                                        }, key: item.nombre },
                                    item.nombre
                                )
                            );
                        })
                    ),
                    React.createElement(
                        "div",
                        { className: "col-3" },
                        carteras.map(function (item) {
                            return React.createElement(
                                "div",
                                { className: "tab-content", id: "nav-tabContent" },
                                React.createElement(
                                    "div",
                                    { className: "list-group-item list-group-item-action active", id: "list-home", role: "tabpanel", "aria-labelledby": "list-home-list", onClick: function onClick(e) {
                                            return _this5.sacaresultados(item, e);
                                        }, key: item.nombre },
                                    item.nombre
                                )
                            );
                        })
                    )
                );
            }
        }
    }]);

    return Hello;
}(React.Component);

ReactDOM.render(React.createElement(Hello, null), document.getElementById('root'));

//// Usuarios


var User = function (_React$Component2) {
    _inherits(User, _React$Component2);

    function User() {
        _classCallCheck(this, User);

        return _possibleConstructorReturn(this, (User.__proto__ || Object.getPrototypeOf(User)).apply(this, arguments));
    }

    _createClass(User, [{
        key: "render",
        value: function render() {

            React.createElement(
                "h1",
                null,
                "Hola"
            );
        }
    }]);

    return User;
}(React.Component);

ReactDOM.render(React.createElement(User, null), document.getElementById('user'));
