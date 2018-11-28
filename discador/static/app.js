
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
                              <ul>
                              <h1>Proveedores</h1>


                              {proveedores.map(item => (

                                  <li onClick={(e) => this.sacacarteras(item, e)} key={item.nombre} >
                                  {item.nombre}
                                  </li>

                              ))}

                              <h1>Carteras {nombre_proveedor}</h1>


                              {carteras.map(item => (
                              <li onClick={(e) => this.sacaresultados(item, e)} key={item.cartera.nombre} >
                              {item.cartera.nombre}
                              </li>
                              ))}


                               <h1>Resultados</h1>

                                {resultados.map(item => (
                                <li onClick={(e) => this.sacasubresultados(item, e)} key={item.resultado.nombre} >
                                {item.resultado.nombre}
                                
                                <input type="checkbox" name="vehicle1" value={item.resultado.check}/>
                                </li>
                                

                                ))}

                              
                              
                              </ul>
                          );
                          }
              }


          }





          ReactDOM.render(


              <Hello />,
              document.getElementById('root')


          );

