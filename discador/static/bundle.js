"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

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
            poetFilter: "",
            isLoaded: false,
            proveedor: null,
            cartera: null,
            proveedores: [],
            carteras: [],
            gestiones: [],
            resultados: [],
            subresultados: [],
            nombre_proveedor: '',
            data: [],
            todosInit: [],
            todos: [],
            todoText: "",
            value: ""
        };

        _this.updateTodoText = _this.updateTodoText.bind(_this);
        _this.createTodo = _this.createTodo.bind(_this);
        _this.filterTodo = _this.filterTodo.bind(_this);
        _this.sacacarteras = _this.sacacarteras.bind(_this);
        _this.handleChange = _this.handleChange.bind(_this);
        _this.handleSubmit = _this.handleSubmit.bind(_this);

        return _this;
    }

    _createClass(Hello, [{
        key: "componentDidMount",
        value: function componentDidMount() {
            var _this2 = this;

            // this.setState({
            //     todos: this.state.todosInit,
            //     });


            fetch('/static/data.json').then(function (res) {
                return res.json();
            }).then(function (res) {

                _this2.setState({
                    todosInit: res,
                    todos: res
                });
            });

            fetch("/discador/api_proveedor/").then(function (res) {
                return res.json();
            }).then(function (result) {
                _this2.setState({
                    isLoaded: true,
                    proveedores: result
                });
            }, function (error) {});

            fetch("/discador/api_carteras/").then(function (res) {
                return res.json();
            }).then(function (result) {
                _this2.setState({
                    isLoaded: true,
                    carteras: result
                });
            }, function (error) {});

            fetch("/discador/api_gestiones/").then(function (res) {
                return res.json();
            }).then(function (result) {
                _this2.setState({
                    isLoaded: true,
                    gestiones: result
                });
            }, function (error) {});

            fetch("/discador/api_resultados/").then(function (res) {
                return res.json();
            }).then(function (result) {
                _this2.setState({
                    isLoaded: true,
                    resultados: result
                });
            }, function (error) {});

            fetch("/discador/api_subresultados/").then(function (res) {
                return res.json();
            }).then(function (result) {
                _this2.setState({
                    isLoaded: true,
                    subresultados: result
                });
            }, function (error) {});
        }
    }, {
        key: "onLoad",
        value: function onLoad(data) {

            this.setState({
                data: this.parseData(data)
            });
        }
    }, {
        key: "updateTodoText",
        value: function updateTodoText(e) {
            this.setState({
                todoText: e.target.value
            });
        }
    }, {
        key: "createTodo",
        value: function createTodo(e) {

            e.preventDefault();

            console.log(e.target.value);

            var obj = { "id": 3, "name": this.state.todoText };

            this.state.todos.push(obj);

            console.log('0000', this.state.todos);

            this.setState({
                todos: this.state.todos,
                todoText: ""
            });
        }
    }, {
        key: "filterTodo",
        value: function filterTodo(e) {

            console.log('filtrando..', e);
            var updatedList = this.state.todosInit;

            updatedList = updatedList.filter(function (item) {
                return item.name.toLowerCase().search(e.target.value.toLowerCase()) !== -1;
            });

            this.setState({
                todos: updatedList
            });
            if (updatedList == 0) {
                this.setState({
                    message: true
                });
            } else {
                this.setState({
                    message: false
                });
            }
        }
    }, {
        key: "parseData",
        value: function parseData(response) {
            console.log('ooo', response.data);
            return response.data;
        }
    }, {
        key: "guardar",
        value: function guardar(nombre) {

            console.log(nombre);
        }
    }, {
        key: "sacaresultados",
        value: function sacaresultados(item) {
            var _this3 = this;

            this.setState({
                cartera: item
            });

            var proveedor = this.state.proveedor;


            fetch("/discador/api_resultados/" + proveedor.id + '/' + item.cartera.id).then(function (res) {
                return res.json();
            }).then(function (result) {

                console.log('api_resultados', result);
                _this3.setState({
                    isLoaded: true,
                    resultados: result
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
        key: "sacacarteras",
        value: function sacacarteras(event) {
            var _this4 = this;

            console.log(event.target.value);

            // this.setState({                
            //     proveedor:item,
            //     nombre_proveedor:item.nombre
            // });

            fetch("/discador/api_cartera/" + event.target.value).then(function (res) {
                return res.json();
            }).then(function (result) {

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
        key: "handleChange",
        value: function handleChange(event) {
            this.setState({ value: event.target.value });
        }
    }, {
        key: "handleSubmit",
        value: function handleSubmit(event) {
            var _this5 = this;

            console.log(this.state.value);

            fetch('/discador/api_proveedor/', {
                method: 'post',
                headers: {
                    'Accept': 'application/json, text/plain, */*',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ nombre: this.state.value })
            }).then(function (res) {
                return res.json();
            }).then(function (res) {

                fetch("/discador/api_proveedor/").then(function (res) {
                    return res.json();
                }).then(function (result) {
                    _this5.setState({
                        isLoaded: true,
                        proveedores: result
                    });

                    $('#proveedor').modal('hide');
                    $('body').removeClass('modal-open');
                    $('.modal-backdrop').remove();
                }, function (error) {});
            });

            event.preventDefault();
        }
    }, {
        key: "render",
        value: function render() {
            var _state = this.state,
                value = _state.value,
                data = _state.data,
                nombre_proveedor = _state.nombre_proveedor,
                error = _state.error,
                isLoaded = _state.isLoaded,
                proveedor = _state.proveedor,
                proveedores = _state.proveedores,
                carteras = _state.carteras,
                gestiones = _state.gestiones,
                resultados = _state.resultados,
                subresultados = _state.subresultados;


            if (!isLoaded) {

                return React.createElement(
                    "div",
                    null,
                    "Loading..."
                );
            } else {
                var _React$createElement, _React$createElement2;

                return React.createElement(
                    "div",
                    { className: "container-fluid" },
                    React.createElement("br", null),
                    React.createElement(
                        "div",
                        { className: "row" },
                        React.createElement(
                            "div",
                            { className: "col-md-2" },
                            React.createElement(
                                "h5",
                                null,
                                "Proveedores"
                            ),
                            React.createElement(
                                "div",
                                { className: "row" },
                                React.createElement(
                                    "div",
                                    { className: "col-10" },
                                    React.createElement(
                                        "select",
                                        { className: "form-control" },
                                        proveedores.map(function (item) {
                                            return (

                                                // <option  onClick={(e) => this.sacacarteras(item, e)} key={item.nombre}>{item.nombre}</option> 
                                                React.createElement(
                                                    "option",
                                                    { value: item.id },
                                                    item.nombre
                                                )
                                            );
                                        })
                                    )
                                ),
                                React.createElement(
                                    "div",
                                    { className: "col-2" },
                                    React.createElement(
                                        "button",
                                        { type: "button", "data-toggle": "modal", "data-target": "#proveedor", className: "btn btn-sm btn-dark" },
                                        "Add"
                                    ),
                                    React.createElement(
                                        "button",
                                        { type: "button", "data-toggle": "modal", "data-target": "#editproveedor", className: "btn btn-sm btn-dark" },
                                        "Edit"
                                    )
                                )
                            )
                        ),
                        React.createElement(
                            "div",
                            { className: "col-md-2" },
                            React.createElement(
                                "h5",
                                null,
                                "Carteras "
                            ),
                            React.createElement(
                                "h5",
                                null,
                                nombre_proveedor
                            ),
                            React.createElement(
                                "select",
                                { className: "form-control" },
                                carteras.map(function (item) {
                                    return React.createElement(
                                        "option",
                                        { value: item.id },
                                        item.nombre
                                    );
                                })
                            )
                        ),
                        React.createElement(
                            "div",
                            { className: "col-md-2" },
                            React.createElement(
                                "h5",
                                null,
                                "Gestion "
                            ),
                            React.createElement(
                                "select",
                                { className: "form-control" },
                                gestiones.map(function (item) {
                                    return (

                                        // <option  onClick={(e) => this.sacacarteras(item, e)} key={item.nombre}>{item.nombre}</option> 
                                        React.createElement(
                                            "option",
                                            { value: item.id },
                                            item.nombre
                                        )
                                    );
                                })
                            )
                        ),
                        React.createElement(
                            "div",
                            { className: "col-md-2" },
                            React.createElement(
                                "h5",
                                null,
                                "Resultados"
                            ),
                            React.createElement(
                                "select",
                                { className: "form-control", onChange: this.sacaresultados },
                                resultados.map(function (item) {
                                    return (

                                        // <option  onClick={(e) => this.sacacarteras(item, e)} key={item.nombre}>{item.nombre}</option> 
                                        React.createElement(
                                            "option",
                                            { value: item.id },
                                            item.nombre
                                        )
                                    );
                                })
                            )
                        ),
                        React.createElement(
                            "div",
                            { className: "col-md-2" },
                            React.createElement(
                                "h5",
                                null,
                                "Subresultados"
                            ),
                            React.createElement(
                                "select",
                                { className: "form-control" },
                                subresultados.map(function (item) {
                                    return (

                                        // <option  onClick={(e) => this.sacacarteras(item, e)} key={item.nombre}>{item.nombre}</option> 
                                        React.createElement(
                                            "option",
                                            { value: item.id },
                                            item.nombre
                                        )
                                    );
                                })
                            )
                        )
                    ),
                    React.createElement(
                        "form",
                        { onSubmit: this.createTodo },
                        React.createElement(
                            "div",
                            { className: "col-lg-12 input-group" },
                            React.createElement("input", { type: "text",
                                className: "center-block",
                                placeholder: "Insert here\u2026",
                                value: this.state.todoText,
                                onChange: this.updateTodoText
                            }),
                            React.createElement(
                                "button",
                                { className: "btn btn-success center-block" },
                                "Creates"
                            )
                        )
                    ),
                    React.createElement(
                        "ul",
                        null,
                        this.state.todos.map(function (todo) {
                            return React.createElement(
                                "li",
                                null,
                                todo.id,
                                " ",
                                todo.name
                            );
                        }),
                        this.state.message ? React.createElement(
                            "li",
                            null,
                            "No search results."
                        ) : ''
                    ),
                    React.createElement("input", { type: "text",
                        className: "center-block",
                        placeholder: "Filter here\u2026"

                    }),
                    React.createElement(
                        "div",
                        null,
                        data.map(function (item) {
                            return React.createElement(
                                "div",
                                { key: item.id },
                                React.createElement(
                                    "a",
                                    { href: 'mailto:${item.email}' },
                                    item.name
                                ),
                                " ",
                                item.company
                            );
                        })
                    ),
                    React.createElement(
                        "div",
                        { className: "modal fade", id: "proveedor", tabindex: "-1", role: "dialog", "aria-labelledby": "exampleModalLabel", "aria-hidden": "true" },
                        React.createElement(
                            "div",
                            { className: "modal-dialog", role: "document" },
                            React.createElement(
                                "div",
                                { className: "modal-content" },
                                React.createElement(
                                    "form",
                                    { onSubmit: this.handleSubmit },
                                    React.createElement(
                                        "div",
                                        { className: "modal-header" },
                                        React.createElement(
                                            "h5",
                                            { className: "modal-title", id: "exampleModalLabel" },
                                            "Nuevo Provedor"
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
                                                React.createElement("input", { type: "text", className: "form-control", value: this.state.value, onChange: this.handleChange, id: "recipient-name" })
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
                    ),
                    React.createElement(
                        "div",
                        { className: "modal fade", id: "editproveedor", tabindex: "-1", role: "dialog", "aria-labelledby": "exampleModalLabel", "aria-hidden": "true" },
                        React.createElement(
                            "div",
                            { className: "modal-dialog", role: "document" },
                            React.createElement(
                                "div",
                                { className: "modal-content" },
                                React.createElement(
                                    "form",
                                    { onSubmit: this.handleSubmit },
                                    React.createElement(
                                        "div",
                                        { className: "modal-header" },
                                        React.createElement(
                                            "h5",
                                            { className: "modal-title", id: "exampleModalLabel" },
                                            "Editar Provedor"
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
                                                React.createElement("input", { type: "text", className: "form-control", value: this.state.value, onChange: this.handleChange, id: "recipient-name" })
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
                                            (_React$createElement2 = { type: "button", className: "btn btn-primary" }, _defineProperty(_React$createElement2, "type", "submit"), _defineProperty(_React$createElement2, "value", "Buscar"), _React$createElement2),
                                            "Actualizar"
                                        )
                                    )
                                )
                            )
                        )
                    )
                );
            }
        }
    }]);

    return Hello;
}(React.Component);

ReactDOM.render(React.createElement(Hello, null), document.getElementById('root'));
