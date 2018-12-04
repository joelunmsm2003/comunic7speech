'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var User = function (_React$Component) {
  _inherits(User, _React$Component);

  function User(props) {
    _classCallCheck(this, User);

    var _this = _possibleConstructorReturn(this, (User.__proto__ || Object.getPrototypeOf(User)).call(this, props));

    _this.state = {
      agentes: []
    };

    return _this;
  }

  _createClass(User, [{
    key: 'componentDidMount',
    value: function componentDidMount() {
      var _this2 = this;

      console.log('Carge....');

      fetch('/discador/api_agentes').then(function (res) {
        return res.json();
      }).then(function (res) {

        console.log('fetch..', res);

        _this2.setState({
          agentes: res

        });
      });
    }
  }, {
    key: 'render',
    value: function render() {
      var agentes = this.state.agentes;


      console.log('render', agentes);

      return React.createElement(
        'table',
        { className: 'table' },
        React.createElement(
          'thead',
          { className: 'thead-dark' },
          React.createElement(
            'tr',
            null,
            React.createElement(
              'th',
              { scope: 'col' },
              'ID'
            ),
            React.createElement(
              'th',
              { scope: 'col' },
              'Login'
            ),
            React.createElement(
              'th',
              { scope: 'col' },
              'Nivel'
            ),
            React.createElement(
              'th',
              { scope: 'col' },
              'Anexo'
            ),
            React.createElement(
              'th',
              { scope: 'col' },
              'Estado'
            )
          )
        ),
        React.createElement(
          'tbody',
          null,
          this.state.agentes.map(function (todo) {
            return React.createElement(
              'tr',
              null,
              React.createElement(
                'td',
                null,
                todo.id
              ),
              React.createElement(
                'td',
                null,
                todo.nombre
              ),
              ' '
            );
          })
        )
      );
    }
  }]);

  return User;
}(React.Component);

React.createElement(
  'table',
  { 'class': 'table' },
  React.createElement(
    'thead',
    { 'class': 'thead-dark' },
    React.createElement(
      'tr',
      null,
      React.createElement(
        'th',
        { scope: 'col' },
        'ID'
      ),
      React.createElement(
        'th',
        { scope: 'col' },
        'Login'
      ),
      React.createElement(
        'th',
        { scope: 'col' },
        'Nivel'
      ),
      React.createElement(
        'th',
        { scope: 'col' },
        'Anexo'
      ),
      React.createElement(
        'th',
        { scope: 'col' },
        'Estado'
      )
    )
  ),
  React.createElement(
    'tbody',
    null,
    React.createElement(
      'tr',
      null,
      React.createElement(
        'th',
        { scope: 'row' },
        '1'
      ),
      React.createElement(
        'td',
        null,
        'Mark'
      ),
      React.createElement(
        'td',
        null,
        'Otto'
      ),
      React.createElement(
        'td',
        null,
        '@mdo'
      ),
      React.createElement(
        'td',
        null,
        '@fat'
      )
    ),
    React.createElement(
      'tr',
      null,
      React.createElement(
        'th',
        { scope: 'row' },
        '2'
      ),
      React.createElement(
        'td',
        null,
        'Jacob'
      ),
      React.createElement(
        'td',
        null,
        'Thornton'
      ),
      React.createElement(
        'td',
        null,
        '@fat'
      ),
      React.createElement(
        'td',
        null,
        '@twitter'
      )
    ),
    React.createElement(
      'tr',
      null,
      React.createElement(
        'th',
        { scope: 'row' },
        '3'
      ),
      React.createElement(
        'td',
        null,
        'Larry'
      ),
      React.createElement(
        'td',
        null,
        'the Bird'
      ),
      React.createElement(
        'td',
        null,
        '@twitter'
      ),
      React.createElement(
        'td',
        null,
        '@fat'
      )
    )
  )
);

ReactDOM.render(React.createElement(User, null), document.getElementById('user'));
