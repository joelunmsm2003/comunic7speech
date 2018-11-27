

            class Hello extends React.Component {
                
              constructor(props) {
                  super(props);


                  this.state = {
                      error: null,
                      isLoaded: false,
                      proveedores: [],
                      carteras:[],
                      resultados:[]
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

              render() {


                  const { error, isLoaded, proveedores, carteras } = this.state;

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

                              <h1>Carteras</h1>

                              {carteras.map(item => (
                              <li onClick={(e) => this.sacaresultados(item, e)} key={item.nombre} >
                              {item.nombre}
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

