
            class Hello extends React.Component {
                
              constructor(props) {
                  super(props);


                  this.state = {
                      error: null,
                      isLoaded: false,
                      proveedor:null,
                      cartera:null,
                      proveedores: [],
                      carteras:[],
                      resultados:[],
                      nombre_proveedor:''
                  };


                  console.log(this.state)

 
              
              }



              componentDidMount() {

                     fetch("http://localhost:8000/discador/api_proveedor/")
                          .then(res => res.json())
                          .then(
                              (result) => {

                              
                              this.setState({
                                  isLoaded: true,
                                  proveedores: result
                              });

                            
                              },

                              (error) => {
                             
                              }
                          )
               

              }


     



              sacacarteras(item) {


                this.setState({                
                    proveedor:item,
                    nombre_proveedor:item.nombre
                });

                  
                  
                  fetch("http://localhost:8000/discador/api_cartera/"+item.id)
                  .then(res => res.json())
                  .then(
                      (result) => {

                      console.log(result)
                      this.setState({
                          isLoaded: true,
                          carteras: result
                      });
                      },
                      // Note: it's important to handle errors here
                      // instead of a catch() block so that we don't swallow
                      // exceptions from actual bugs in components.
                      (error) => {
                      this.setState({
                          isLoaded: true,
                          error
                      });
                      }
                  )

              }


              sacaresultados(item) {

                this.setState({                
                    cartera:item
                });

                const { proveedor } = this.state;

                  fetch("http://localhost:8000/discador/api_resultados/"+proveedor.id+'/'+item.cartera.id)
                  .then(res => res.json())
                  .then(
                      (result) => {

                      console.log('api_resultados',result)
                      this.setState({
                          isLoaded: true,
                          resultados:result
                      });
                      },
                      // Note: it's important to handle errors here
                      // instead of a catch() block so that we don't swallow
                      // exceptions from actual bugs in components.
                      (error) => {
                      this.setState({
                          isLoaded: true,
                          error
                      });
                      }
                  )

              }

              render() {


                  const { nombre_proveedor, error, isLoaded, proveedor, proveedores, carteras,resultados } = this.state;

                   
                    

                      if (!isLoaded) {
                          
                          return <div>Loading...</div>;
                          
                      } 
                      
                      else {
                          
                          return (

                             <div className='container'>
                              
                              <div className="row">
                               <div className="col-3">

                                <h2>Proveedores</h2>
                              {proveedores.map(item => (

                                  

                                  <div className="list-group">
                                  <a className="list-group-item list-group-item-action"   onClick={(e) => this.sacacarteras(item, e)} key={item.nombre}>{item.nombre}</a> 

                                   </div>
                                   



                              ))}
                              </div>

                              <div className="col-3">
                                 
                              <h2>Carteras </h2>
                              <h2>{nombre_proveedor}</h2>


                              {carteras.map(item => (

                                <div className="list-group">
                                <a className="list-group-item list-group-item-action"    onClick={(e) => this.sacaresultados(item, e)} key={item.nombre}>{item.cartera.nombre}</a> 
                                </div>

                            


                              ))}

                              </div>

                              <div className="col-3">



                               <h2>Resultados</h2>


                                {resultados.map(item => (

                                    <div className="list-group">
                                    <a className="list-group-item list-group-item-action"    onClick={(e) => this.sacaresultados(item, e)} key={item.nombre}>{item.resultado.nombre}
                                    <input type='checkbox'></input>
                                    </a> 
                                    
                                    
                                    </div>

                                    ))}

                    

                              
                                
                              
                              </div>
                
                              
                              
                             </div>

                             </div>

                          );

                          }
              }


          }





          ReactDOM.render(


              <Hello />,
              document.getElementById('root')


          );

