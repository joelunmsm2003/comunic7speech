
import React from "react";
import { connect , Provider} from 'react-redux';
import { load_Agentes} from "../actionCreators"
import ReactDOM from "react-dom";

import Header from "./Header";

import store from "../store";


import axios from "axios"

console.log("kkkkkkmm")
class App extends React.Component {
    
    constructor(props) {
        console.log("kkkkkkm")
        super(props);

        this.state = {
          traeAgentes:[{id:1}],
          todoAgentes:[],

        };

  
      }


      componentDidMount() {

      store.dispatch(load_Agentes())

      this.listaagentes()
      }

  

      listaagentes(){
        axios.get("/discador/api_agentes ")
        .then(response=>{
    
          console.log('bienbenido,',response.data)

          this.setState({
            todoAgentes:response.data,
          })


          store.dispatch(cargaagentes(response.data))

  

    
        });
      }


    render() {


      const {todoAgentes} = this.state


      return (

        <div>
        <Header/>

        <div className="container">

            <table className="table">
  <thead className="thead-dark">
    <tr>
      <th scope="col">ID</th>
      <th scope="col">Nombre</th>
      <th scope="col">Anexo</th>
      <th scope="col">Usuario</th>
      <th scope="col">Estado</th>
      <th scope="col">Usuario</th>
    </tr>
  </thead>
  <tbody>
    
    {todoAgentes.map(item => (
      <tr >
    <th value={item.id} scope="row">{item.id}</th>
    <td>{item.nombre}</td>
    <td>{item.supervisor}</td>
    <td>{item.anexo}</td>
    <td>{item.estado}</td>
    <td>{item.user}</td>

  </tr>
 
    
          
          


          ))}

   
  </tbody>
</table>


        </div>



   
        </div>

      );
    }


  }

 
  




  






const Trae = ({traeAgentes}) =>{
  console.log("kkkkkkm_locaso_hola_mundo..")
  console.log("probando   q me traes..",traeAgentes)
  return (
    <div className='row'>
        <h1>Todos los Agentes</h1>
        {traeAgentes.map(data=>
        <li>{data.anexo}</li>
        
        )}
    </div>
  );

}
   

const  mapStateToProps = state =>{

      return{
        traeAgentes:state.traeAgentes,
      }
  
  }
  

ReactDOM.render(

  <Provider store={store}>
    <App />
   
    </Provider>,
  

    document.getElementById('root')
    );
  
  export default connect(mapStateToProps)(Trae);  

   