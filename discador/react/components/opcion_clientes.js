import React from "react";
import ReactDOM from "react-dom";


import Header from "./Header";

import store from "../store";
import { Provider } from "react-redux";



class App extends React.Component {
    constructor(props) {


        super(props);

        this.state = {
       
        };
    
      }


      componentDidMount() {


      }

    render() {

      const {  } = this.state;

      return (
        <div> 
         <Header/>

         
        </div>
      );
    }

}




  





ReactDOM.render(

    <Provider store={store}>
    <App />
    </Provider>,
    document.getElementById('app')
    );

