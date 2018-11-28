

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

                              
                              <div className="row">
                               <div className="col-6">
                              {proveedores.map(item => (

                                  

                                  <div className="list-group" id="myList" role="tablist">
                                  <a className="list-group-item list-group-item-action active" id="list-home-list" data-toggle="list" href="#list-home" role="tab" aria-controls="home" onClick={(e) => this.sacacarteras(item, e)} key={item.nombre}>{item.nombre}</a> 

                                   </div>
                                   


                              ))}
                              </div>

                              <h1>Carteras</h1>
                              <div className="col-6">

                              {carteras.map(item => (

                              
                                <div className="tab-content" id="nav-tabContent">
                                  <div className="tab-pane fade show active" id="list-home" role="tabpanel" aria-labelledby="list-home-list" onClick={(e) => this.sacaresultados(item, e)} key={item.nombre} >{item.nombre}</div>
                                </div>
                              
                              ))}
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

