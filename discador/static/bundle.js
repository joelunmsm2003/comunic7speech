"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Botones = function (_React$Component) {
    _inherits(Botones, _React$Component);

    function Botones(props) {
        _classCallCheck(this, Botones);

        var _this = _possibleConstructorReturn(this, (Botones.__proto__ || Object.getPrototypeOf(Botones)).call(this, props));

        _this.abremodal = _this.abremodal.bind(_this);

        return _this;
    }

    _createClass(Botones, [{
        key: "abremodal",
        value: function abremodal(opcion, e) {

            $("#" + opcion).modal();
        }
    }, {
        key: "editamodal",
        value: function editamodal(opcion, e) {

            $("#" + opcion).modal();
        }
    }, {
        key: "render",
        value: function render() {
            var _this2 = this;

            return React.createElement(
                "div",
                { className: "row" },
                React.createElement(
                    "div",
                    { className: "col-md-2" },
                    React.createElement(
                        "div",
                        { "class": "btn-group btn-group-toggle", "data-toggle": "buttons" },
                        React.createElement(
                            "label",
                            { "class": "btn btn-secondary active" },
                            React.createElement(
                                "button",
                                { type: "button", "data-toggle": "modal", className: "btn btn-sm btn-dark", onClick: function onClick(e) {
                                        return _this2.abremodal(_this2.props.name, e);
                                    } },
                                "Add"
                            )
                        )
                    )
                ),
                React.createElement(
                    "div",
                    { className: "col-md-3" },
                    this.props.name
                )
            );
        }
    }]);

    return Botones;
}(React.Component);

var Select = function (_React$Component2) {
    _inherits(Select, _React$Component2);

    function Select(props) {
        _classCallCheck(this, Select);

        var _this3 = _possibleConstructorReturn(this, (Select.__proto__ || Object.getPrototypeOf(Select)).call(this, props));

        _this3.state = {
            value: "",
            editar: []
        };

        _this3.selecciona = _this3.selecciona.bind(_this3);
        return _this3;
    }

    _createClass(Select, [{
        key: "selecciona",
        value: function selecciona(api, e) {

            console.log(api, e.target.value);
        }
    }, {
        key: "render",
        value: function render() {
            var _this4 = this;

            return React.createElement(
                "div",
                null,
                React.createElement(Botones, { name: this.props.opcion, edit_modal: this.props.edit_modal }),
                React.createElement(AddModal, { name: this.props.opcion, api: this.props.api }),
                React.createElement(
                    "select",
                    { className: "form-control", onChange: function onChange(e) {
                            return _this4.selecciona(_this4.props.name, e);
                        } },
                    this.props.value.map(function (item) {
                        return React.createElement(
                            "option",
                            { value: item.id },
                            item.nombre
                        );
                    })
                )
            );
        }
    }]);

    return Select;
}(React.Component);

var AddModal = function (_React$Component3) {
    _inherits(AddModal, _React$Component3);

    function AddModal(props) {
        _classCallCheck(this, AddModal);

        var _this5 = _possibleConstructorReturn(this, (AddModal.__proto__ || Object.getPrototypeOf(AddModal)).call(this, props));

        _this5.state = {
            value: []
        };

        _this5.guarda = _this5.guarda.bind(_this5);

        return _this5;
    }

    _createClass(AddModal, [{
        key: "handleChange",
        value: function handleChange(event) {
            this.setState({ value: event.target.value });
        }
    }, {
        key: "guarda",
        value: function guarda(event) {
            var _this6 = this;

            fetch('/discador/' + this.props.api + '/', {
                method: 'post',
                headers: {
                    'Accept': 'application/json, text/plain, */*',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ nombre: this.state.value })
            }).then(function (res) {
                return res.json();
            }).then(function (res) {

                $('#' + _this6.props.name).modal('hide');
                $('body').removeClass('modal-open');
                $('.modal-backdrop').remove();
            });

            event.preventDefault();
        }
    }, {
        key: "render",
        value: function render() {
            var _React$createElement;

            return React.createElement(
                "div",
                { className: "modal fade", id: this.props.name, tabindex: "-1", role: "dialog", "aria-labelledby": "exampleModalLabel", "aria-hidden": "true" },
                React.createElement(
                    "div",
                    { className: "modal-dialog", role: "document" },
                    React.createElement(
                        "div",
                        { className: "modal-content" },
                        React.createElement(
                            "form",
                            { onSubmit: this.guarda },
                            React.createElement(
                                "div",
                                { className: "modal-header" },
                                React.createElement(
                                    "h5",
                                    { className: "modal-title", id: "exampleModalLabel" },
                                    "Agregar ",
                                    this.props.name
                                ),
                                React.createElement(
                                    "button",
                                    { type: "button", className: "close", "data-dismiss": "modal", "aria-label": "Close" },
                                    React.createElement(
                                        "span",
                                        { "aria-hidden": "true" },
                                        "\xD7"
                                    )
                                )
                            ),
                            React.createElement(
                                "div",
                                { className: "modal-body" },
                                React.createElement(
                                    "form",
                                    null,
                                    React.createElement(
                                        "div",
                                        { className: "form-group" },
                                        React.createElement(
                                            "label",
                                            { "for": "recipient-name", className: "col-form-label" },
                                            "Nombre:"
                                        ),
                                        React.createElement("input", { type: "text", className: "form-control", onChange: this.handleChange.bind(this) })
                                    )
                                )
                            ),
                            React.createElement(
                                "div",
                                { className: "modal-footer" },
                                React.createElement(
                                    "button",
                                    { type: "button", className: "btn btn-secondary", "data-dismiss": "modal" },
                                    "Cancelar"
                                ),
                                React.createElement(
                                    "button",
                                    (_React$createElement = { type: "button", className: "btn btn-primary" }, _defineProperty(_React$createElement, "type", "submit"), _defineProperty(_React$createElement, "value", "Buscar"), _React$createElement),
                                    "Guardar"
                                )
                            )
                        )
                    )
                )
            );
        }
    }]);

    return AddModal;
}(React.Component);

var Opcion = function (_React$Component4) {
    _inherits(Opcion, _React$Component4);

    function Opcion(props) {
        _classCallCheck(this, Opcion);

        var _this7 = _possibleConstructorReturn(this, (Opcion.__proto__ || Object.getPrototypeOf(Opcion)).call(this, props));

        _this7.state = {
            proveedores: [],
            carteras: [],
            gestiones: [],
            resultados: [],
            subresultados: []

        };

        fetch("/discador/api_proveedor/").then(function (res) {
            return res.json();
        }).then(function (result) {
            _this7.setState({
                isLoaded: true,
                proveedores: result
            });
        }, function (error) {});

        fetch("/discador/api_carteras/").then(function (res) {
            return res.json();
        }).then(function (result) {
            _this7.setState({
                isLoaded: true,
                carteras: result
            });
        }, function (error) {});

        fetch("/discador/api_gestiones/").then(function (res) {
            return res.json();
        }).then(function (result) {
            _this7.setState({
                isLoaded: true,
                gestiones: result
            });
        }, function (error) {});

        fetch("/discador/api_resultados/").then(function (res) {
            return res.json();
        }).then(function (result) {
            _this7.setState({
                isLoaded: true,
                resultados: result
            });
        }, function (error) {});

        fetch("/discador/api_subresultados/").then(function (res) {
            return res.json();
        }).then(function (result) {
            _this7.setState({
                isLoaded: true,
                subresultados: result
            });
        }, function (error) {});

        return _this7;
    }

    _createClass(Opcion, [{
        key: "render",
        value: function render() {
            var _state = this.state,
                proveedores = _state.proveedores,
                carteras = _state.carteras,
                gestiones = _state.gestiones,
                resultados = _state.resultados,
                subresultados = _state.subresultados;


            return React.createElement(
                "div",
                { className: "container-fluid" },
                React.createElement(
                    "div",
                    { className: "row" },
                    React.createElement(
                        "a",
                        { "class": "btn btn-sm", href: "/admin/discador/score/" },
                        "Admin"
                    )
                ),
                React.createElement(
                    "div",
                    { className: "row" },
                    React.createElement(
                        "div",
                        { className: "col-md-3" },
                        React.createElement(Select, { edit_modal: "_proveedor", opcion: "Proveedor", api: "api_proveedores", name: "api_proveedor_detalle", value: proveedores })
                    ),
                    React.createElement(
                        "div",
                        { className: "col-md-3" },
                        React.createElement(Select, { edit_modal: "_cartera", opcion: "Cartera", api: "api_carteras", name: "api_detalle_cartera", value: carteras })
                    ),
                    React.createElement(
                        "div",
                        { className: "col-md-3" },
                        React.createElement(Select, { edit_modal: "_gestion", opcion: "Gestion", api: "api_gestiones", name: "api_gestiones", value: gestiones })
                    ),
                    React.createElement(
                        "div",
                        { className: "col-md-3" },
                        React.createElement(Select, { edit_modal: "_gestion", opcion: "Resultados", api: "api_gestiones", name: "api_gestiones", value: resultados })
                    )
                )
            );
        }
    }]);

    return Opcion;
}(React.Component);

ReactDOM.render(React.createElement(Opcion, null), document.getElementById('user'));
