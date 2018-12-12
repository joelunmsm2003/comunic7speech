var ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  entry: {
    'app.js': './app.js', 
    'cartera.js': './cartera.js',
    'style':'./scss/main.scss'
  },
  output: {
    filename: './dist/[name]'
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
