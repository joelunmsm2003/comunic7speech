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
            poetFilter: "",
            isLoaded: false,
            proveedor: null,
            cartera: null,
            proveedores: [],
            carteras: [],
            resultados: [],
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
                resultados = _state.resultados;


            if (!isLoaded) {

                return React.createElement(
                    "div",
                    null,
                    "Loading..."
                );
            } else {

                return React.createElement(
                    "div",
                    { className: "container" },
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
                        { className: "row" },
                        React.createElement(
                            "div",
                            { className: "col-3" },
                            React.createElement(
                                "h2",
                                null,
                                "Proveedores"
                            ),
                            React.createElement("img", { src: "/static/add.png", height: "30", width: "30", "class": "btn btn-primary", "data-toggle": "modal", "data-target": "#exampleModal", "data-whatever": "@mdo" }),
                            React.createElement("img", { src: "/static/edit.png", height: "30", width: "30" }),
                            React.createElement("img", { src: "/static/delete.png", height: "30", width: "30" }),
                            React.createElement(
                                "div",
                                { className: "modal fade", id: "exampleModal", tabindex: "-1", role: "dialog", "aria-labelledby": "exampleModalLabel", "aria-hidden": "true" },
                                React.createElement(
                                    "div",
                                    { className: "modal-dialog", role: "document" },
                                    React.createElement(
                                        "div",
                                        { className: "modal-content" },
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
                                                { type: "button", "class": "close", "data-dismiss": "modal", "aria-label": "Close" },
                                                React.createElement(
                                                    "span",
                                                    { "aria-hidden": "true" },
                                                    "\xD7"
                                                )
                                            )
                                        ),
                                        React.createElement(
                                            "div",
                                            { "class": "modal-body" },
                                            React.createElement(
                                                "form",
                                                null,
                                                React.createElement(
                                                    "div",
                                                    { "class": "form-group" },
                                                    React.createElement(
                                                        "label",
                                                        { "for": "recipient-name", "class": "col-form-label" },
                                                        "Recipient:"
                                                    ),
                                                    React.createElement("input", { type: "text", "class": "form-control", id: "recipient-name" })
                                                ),
                                                React.createElement(
                                                    "div",
                                                    { "class": "form-group" },
                                                    React.createElement(
                                                        "label",
                                                        { "for": "message-text", "class": "col-form-label" },
                                                        "Message:"
                                                    ),
                                                    React.createElement("textarea", { "class": "form-control", id: "message-text" })
                                                )
                                            )
                                        ),
                                        React.createElement(
                                            "div",
                                            { className: "modal-footer" },
                                            React.createElement(
                                                "button",
                                                { type: "button", className: "btn btn-secondary", "data-dismiss": "modal" },
                                                "Calcelar"
                                            ),
                                            React.createElement(
                                                "button",
                                                { type: "button", className: "btn btn-primary" },
                                                "Guardar"
                                            )
                                        )
                                    )
                                )
                            ),
                            React.createElement(
                                "select",
                                { className: "form-control", onChange: this.sacacarteras },
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
                            { className: "col-3" },
                            React.createElement(
                                "h2",
                                null,
                                "Carteras "
                            ),
                            React.createElement(
                                "h2",
                                null,
                                nombre_proveedor
                            ),
                            React.createElement("img", { src: "/static/add.png", height: "30", width: "30", "class": "btn btn-primary", "data-toggle": "modal", "data-target": "#exampleModal", "data-whatever": "@mdo" }),
                            React.createElement("img", { src: "/static/edit.png", height: "30", width: "30" }),
                            React.createElement("img", { src: "/static/delete.png", height: "30", width: "30" }),
                            React.createElement(
                                "select",
                                { className: "form-control", onChange: this.sacaresultados },
                                carteras.map(function (item) {
                                    return React.createElement(
                                        "option",
                                        { value: item.id },
                                        item.cartera.nombre
                                    )
                                    // <div className="list-group">
                                    // <a className="list-group-item list-group-item-action"    onClick={(e) => this.sacaresultados(item, e)} key={item.nombre}>{item.cartera.nombre}</a> 

                                    //</div>


                                    ;
                                })
                            )
                        ),
                        React.createElement(
                            "div",
                            { className: "col-3" },
                            React.createElement(
                                "h2",
                                null,
                                "Resultadoss"
                            ),
                            React.createElement(
                                "select",
                                { className: "form-control", onChange: this.sacaresultados },
                                resultados.map(function (item) {
                                    return (

                                        //<div className="list-group">
                                        //<a className="list-group-item list-group-item-action"    onClick={(e) => this.sacaresultados(item, e)} key={item.nombre}>{item.resultado.nombre}
                                        //<input type='checkbox'></input>
                                        //</a> 


                                        //</div>
                                        React.createElement(
                                            "option",
                                            { value: item.id },
                                            item.resultado.nombre
                                        )
                                    );
                                })
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
