var ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {

  entry: {
    'discador.index.js': './discador/react/components/App.js',
    'discador.cartera.js': './discador/react/components/Cartera.js', 
    'discador.score.js':'./discador/react/components/Scoreproveedor.js',
    'discador.traeAgentes.js': './discador/react/components/traeAgentes.js', 
    'discador.proveedorscore.js':'./discador/react/components/ProveedorScore.js',
    'discador.agentes.js':'./discador/react/components/Agentes.js',
    'discador.marcador.js':'./discador/react/components/Agentes.js',
    'discador.asignascore.js':'./discador/react/components/AsignaScoreProveedor.js',
    'discador.opcion_clientes.js':'./discador/react/components/opcion_clientes.js',
    'style':'./scss/main.scss'
  },
  output: {
    filename: './static/dist/[name]'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      /*
      your other rules for JavaScript transpiling go in here
      */
      { // css / sass / scss loader for webpack
        test: /\.(css|sass|scss)$/,
        use: ExtractTextPlugin.extract({
          use: ['css-loader', 'sass-loader'],
        })
      }
    ]
  },
  plugins: [
    new ExtractTextPlugin({ // define where to save the file
      filename: 'dist/[name].bundle.css',
      allChunks: true,
    }),
  ],
};
