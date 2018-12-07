

            class User extends React.Component {
               
                constructor(props) {
                    super(props);

                    this.state = {
                        agentes: []
                    };
  
   
                }

                componentDidMount() {

                console.log('Carge....')

                fetch('/discador/api_agentes')
                    .then(res => res.json())
                    .then(res => {


                        console.log('fetch..',res)

                        this.setState({
                            agentes:res,
                            
                          });

                    })


                }


                
      
               render(){

                            const { agentes } = this.state;

                            
                            console.log('render',agentes)

                            return(<table className="table">

                                            <thead className="thead-dark">
                                              <tr>
                                                <th scope="col">ID</th>
                                                <th scope="col">Login</th>
                                                <th scope="col">Nivel</th>
                                                <th scope="col">Anexo</th>
                                                <th scope="col">Estado</th>
                                              </tr>
                                            </thead>
                                            <tbody>
                                    {this.state.agentes.map((todo) => 
                                        {
                                        return (
                                        
                                            
                                            
                                            
                                            <tr><td>{todo.id}</td><td>{todo.nombre}</td> </tr>
                                            
                                            )
                                        }
                                    )} 
                                    </tbody>
                            </table>)


                        } 
               
  
  
            
                    }



                    <table className="table">
                    <thead className="thead-dark">
                      <tr>
                        <th scope="col">ID</th>
                        <th scope="col">Login</th>
                        <th scope="col">Nivel</th>
                        <th scope="col">Anexo</th>
                        <th scope="col">Estado</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <th scope="row">1</th>
                        <td>Mark</td>
                        <td>Otto</td>
                        <td>@mdo</td>
                        <td>@fat</td>
                      </tr>
                      <tr>
                        <th scope="row">2</th>
                        <td>Jacob</td>
                        <td>Thornton</td>
                        <td>@fat</td>
                        <td>@twitter</td>
                      </tr>
                      <tr>
                        <th scope="row">3</th>
                        <td>Larry</td>
                        <td>the Bird</td>
                        <td>@twitter</td>
                        <td>@fat</td>
                      </tr>
                  
                  
                    </tbody>
                  
                  
                  </table>
  
  
        
  
            
  

  
           ReactDOM.render(
            <User />,
            document.getElementById('user')
            );

  
  