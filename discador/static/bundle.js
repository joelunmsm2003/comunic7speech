"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Hello = function (_React$Component) {
    _inherits(Hello, _React$Component);

    function Hello(props) {
        _classCallCheck(this, Hello);

        var _this = _possibleConstructorReturn(this, (Hello.__proto__ || Object.getPrototypeOf(Hello)).call(this, props));

        _this.state = {
            error: null,
            isLoaded: false,
            proveedor: null,
            cartera: null,
            proveedores: [],
            carteras: [],
            resultados: [],
            nombre_proveedor: ''
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

            this.setState({
                proveedor: item,
                nombre_proveedor: item.nombre
            });

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

            this.setState({
                cartera: item
            });

            var proveedor = this.state.proveedor;


            fetch("http://localhost:8000/discador/api_resultados/" + proveedor.id + '/' + item.cartera.id).then(function (res) {
                return res.json();
            }).then(function (result) {

                console.log('api_resultados', result);
                _this4.setState({
                    isLoaded: true,
                    resultados: result
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
                nombre_proveedor = _state.nombre_proveedor,
                error = _state.error,
                isLoaded = _state.isLoaded,
                proveedor = _state.proveedor,
                proveedores = _state.proveedores,
                carteras = _state.carteras,
                resultados = _state.resultados;


            if (!isLoaded) {

                return React.createElement(
                    "div",
                    null,
                    "Loading..."
                );
            } else {

                return React.createElement(
                    "ul",
                    null,
                    React.createElement(
                        "h1",
                        null,
                        "Proveedores"
                    ),
                    proveedores.map(function (item) {
                        return React.createElement(
                            "li",
                            { onClick: function onClick(e) {
                                    return _this5.sacacarteras(item, e);
                                }, key: item.nombre },
                            item.nombre
                        );
                    }),
                    React.createElement(
                        "h1",
                        null,
                        "Carteras ",
                        nombre_proveedor
                    ),
                    carteras.map(function (item) {
                        return React.createElement(
                            "li",
                            { onClick: function onClick(e) {
                                    return _this5.sacaresultados(item, e);
                                }, key: item.cartera.nombre },
                            item.cartera.nombre
                        );
                    }),
                    React.createElement(
                        "h1",
                        null,
                        "Resultados"
                    ),
                    resultados.map(function (item) {
                        return React.createElement(
                            "li",
                            { onClick: function onClick(e) {
                                    return _this5.sacasubresultados(item, e);
                                }, key: item.resultado.nombre },
                            item.resultado.nombre,
                            React.createElement("input", { type: "checkbox", name: "vehicle1", value: item.resultado.check })
                        );
                    })
                );
            }
        }
    }]);

    return Hello;
}(React.Component);

ReactDOM.render(React.createElement(Hello, null), document.getElementById('root'));
