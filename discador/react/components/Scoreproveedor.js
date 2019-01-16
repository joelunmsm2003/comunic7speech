
import React from "react";
import ReactDOM from "react-dom";
import store from "../store";
import { Provider } from "react-redux";

import axios from 'axios';

var $ = require ('jquery')

const divStyle = {
  height: '12px',

};

class Scoreproveedor extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
        
            mensaje:"",
            gestiones:[]

        };

    
      }

      componentDidMount() {


        axios.get("/discador/api_gestiones")
        .then(response=>{
    
          console.log('oooo',response)

          this.setState({ gestiones:response.data })
    
        });


    

        
      }


    render() {

      const { gestiones } = this.state;

      return (

        <div>

           <ul className='list-group'>

             <li className='list-item'>jsjjsjs</li>
           </ul>

            
        </div>
      );
    }

  }

  




ReactDOM.render(

    <Provider store={store}>
    <Scoreproveedor />
    </Provider>,
    document.getElementById('app')
    );
