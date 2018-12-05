//Proveedore

            class Hello extends React.Component {
                
              constructor(props) {
                  super(props);


                  this.state = {
                      error: null,
                      poetFilter: "",
                      isLoaded: false,
                      proveedor:null,
                      cartera:null,
                      proveedores: [],
                      carteras:[],
                      gestiones:[],
                      resultados:[],
                      subresultados:[],
                      nombre_proveedor:'',
                      data:[],
                      todosInit: [],
                      todos: [],
                      todoText: "",
                      value:""
                  };

                    this.updateTodoText = this.updateTodoText.bind(this);
                    this.createTodo = this.createTodo.bind(this);
                    this.filterTodo = this.filterTodo.bind(this);
                    this.sacacarteras = this.sacacarteras.bind(this);
                    this.handleChange = this.handleChange.bind(this);
                    this.handleChange1 = this.handleChange1.bind(this);
                    this.handleSubmit = this.handleSubmit.bind(this);
                    this.handleSubmit1 = this.handleSubmit1.bind(this);

 
              }

              componentDidMount() {



                // this.setState({
                //     todos: this.state.todosInit,
                //     });


                    fetch('/static/data.json')
                    .then(res => res.json())
                    .then(res => {

                        this.setState({
                            todosInit:res,
                            todos: res
                          });

                    })
                   
                    fetch("/discador/api_proveedor/")
                          .then(res => res.json())
                          .then((result) => {
                              this.setState({
                                  isLoaded: true,
                                  proveedores: result
                              });
                              },
                              (error) => {
                              }
                          )

                    fetch("/discador/api_carteras/")
                    .then(res => res.json())
                    .then((result) => {
                        this.setState({
                            isLoaded: true,
                            carteras: result
                        });
                        },
                        (error) => {
                        }
                    )

                    fetch("/discador/api_gestiones/")
                    .then(res => res.json())
                    .then((result) => {
                        this.setState({
                            isLoaded: true,
                            gestiones: result
                        });
                        },
                        (error) => {
                        }
                    )

                    fetch("/discador/api_resultados/")
                    .then(res => res.json())
                    .then((result) => {
                        this.setState({
                            isLoaded: true,
                            resultados: result
                        });
                        },
                        (error) => {
                        }
                    )

                    fetch("/discador/api_subresultados/")
                    .then(res => res.json())
                    .then((result) => {
                        this.setState({
                            isLoaded: true,
                            subresultados: result
                        });
                        },
                        (error) => {
                        }
                    )
               

              }


              onLoad(data){

                this.setState({
                  data: this.parseData(data)
                });

            }



            updateTodoText (e)
            {
            this.setState({
            todoText: e.target.value
            });
            }
            
            createTodo (e)
            {

            e.preventDefault();


            console.log(e.target.value)

            var obj = { "id":3, "name": this.state.todoText };

            this.state.todos.push(obj)

            console.log('0000',this.state.todos)


            this.setState({ 
            todos: this.state.todos,
            todoText: "",
            });
            }
            
            filterTodo(e)
            { 

            console.log('filtrando..',e)
            var updatedList = this.state.todosInit;

            updatedList = updatedList.filter((item =>{
                return item.name.toLowerCase().search(
                e.target.value.toLowerCase()) !== -1;
            }) );

            this.setState({ 
                todos: updatedList,
            });
            if (updatedList == 0 ) {
            this.setState({ 
            message: true,
            });
            } else {
            this.setState({ 
            message: false,
            });
            
            
            }
            
            }

            parseData (response) {
                console.log('ooo',response.data)
                return response.data;
              }
             
            guardar(nombre) {

                console.log(nombre)

               
              }




              sacaresultados(item) {

                this.setState({                
                    cartera:item
                });

                const { proveedor } = this.state;

                  fetch("/discador/api_resultados/"+proveedor.id+'/'+item.cartera.id)
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

              sacacarteras(event) {


                console.log(event.target.value)
                
                // this.setState({                
                //     proveedor:item,
                //     nombre_proveedor:item.nombre
                // });
                
                fetch("/discador/api_carteras/"+event.target.value)
                .then(res => res.json())
                .then(
                    (result) => {

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


              handleChange(event) {
                this.setState({value: event.target.value});
              }
            
              handleSubmit(event) {

                console.log(this.state.value)
                
                fetch('/discador/api_proveedor/', {
                    method: 'post',
                    headers: {
                        'Accept': 'application/json, text/plain, */*',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({nombre: this.state.value})
                    }).then(res=>res.json())
                    .then(res => {

                          fetch("/discador/api_proveedor/")
                          .then(res => res.json())
                          .then((result) => {
                              this.setState({
                                  isLoaded: true,
                                  proveedores: result
                              });

                                $('#proveedor').modal('hide'); 
                                $('body').removeClass('modal-open'); 
                                $('.modal-backdrop').remove();

                              },
                              (error) => {
                              }
                          )



                        
                    });
                
                    
                event.preventDefault();
              }

              handleChange1(event) {
                this.setState({value: event.target.value});
              }

              handleSubmit1(event) {

                console.log(this.state.value)
                
                fetch('/discador/api_carteras/', {
                    method: 'post',
                    headers: {
                        'Accept': 'application/json, text/plain, */*',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({nombre: this.state.value})
                    }).then(res=>res.json())
                    .then(res => {
                        

                          fetch("/discador/api_carteras/")
                          .then(res => res.json())
                          .then((result) => {
                              this.setState({
                                  isLoaded: true,
                                  carteras: result
                              });

                                $('#cartera').modal('hide'); 
                                $('body').removeClass('modal-open'); 
                                $('.modal-backdrop').remove();

                              },
                              (error) => {
                              }
                          )



                        
                    });
                
                    
                event.preventDefault();
              }



              render() {


                  const { value,data,nombre_proveedor, error, isLoaded, proveedor, proveedores,carteras,gestiones,resultados,subresultados } = this.state;

                   
                    

                      if (!isLoaded) {
                          
                          return <div>Loading...</div>;
                          
                      } 
                      
                      else {
                          
                          return (

                             <div className='container-fluid'>

                            
                            <br></br>

                             <div className="row">

                              

                                <div className="col-md-2">

                                
                                  
                                <h5>Proveedores</h5>
                               
                                
                                    <div className='row'>
                                            <div className='col-10'>
                                            <select className='form-control'>
                                            

                                            {proveedores.map(item => (

                                            // <option  onClick={(e) => this.sacacarteras(item, e)} key={item.nombre}>{item.nombre}</option> 
                                            <option  value={item.id} >{item.nombre}</option>

                                            ))}

                                            </select> 
                                            </div>

                                            <div className='col-2'>
                                            <button type="button" data-toggle="modal" data-target="#proveedor" className="btn btn-sm btn-dark">Add</button>
                                            <button type="button" data-toggle="modal" data-target="#editproveedor" className="btn btn-sm btn-dark">Edit</button>
                                            </div>
                                    </div>
                                </div>



                                <div className="col-md-2">
                                
                                <h5>Carteras </h5>
                                <div className='row'>
                                <div className='col-10'>
                                <h5>{nombre_proveedor}</h5>



                                <select className='form-control'>

                                {carteras.map(item => (

                                <option  value={item.id} >{item.nombre}</option>

                                ))}

                                </select> 
                                    </div>


                                    </div>

                                     <div className='col-2'>
                                            <button type="button" data-toggle="modal" data-target="#cartera" className="btn btn-sm btn-dark">Add</button>
                                            <button type="button" data-toggle="modal" data-target="#editcartera" className="btn btn-sm btn-dark">Edit</button>
                                            </div>
                                </div>




                                <div className="col-md-2">
                                
                                <h5>Gestion </h5>
                                


                                <select className='form-control'>

                                {gestiones.map(item => (

                                    // <option  onClick={(e) => this.sacacarteras(item, e)} key={item.nombre}>{item.nombre}</option> 
                                    <option  value={item.id} >{item.nombre}</option>

                                ))}

                                </select>

                                </div>

                                <div className="col-md-2">



                                <h5>Resultadoss</h5>


                                <select className='form-control'   onChange={this.sacaresultados}>

                                {resultados.map(item => (

                                    // <option  onClick={(e) => this.sacacarteras(item, e)} key={item.nombre}>{item.nombre}</option> 
                                    <option  value={item.id} >{item.nombre}</option>

                                ))}

                                </select>

                                </div>

                                <div className="col-md-2">



                                <h5>Subresultados</h5>


                                <select className='form-control'>

                                {subresultados.map(item => (

                                    // <option  onClick={(e) => this.sacacarteras(item, e)} key={item.nombre}>{item.nombre}</option> 
                                    <option  value={item.id} >{item.nombre}</option>

                                ))}

                                </select>

                                </div>



                                </div>

                                <form onSubmit={this.createTodo}>
                                    <div className='col-lg-12 input-group'>
                                    <input type='text'
                                    className='center-block'
                                    placeholder='Insert here…'
                                    value={this.state.todoText}
                                    onChange={this.updateTodoText}
                                    />
                                    <button className='btn btn-success center-block'>Creates</button>
                                    </div>
                                </form>

                                <ul>

                                    

                                {this.state.todos.map((todo) => 
                                {
                                return (<li>{todo.id} {todo.name}</li>)
                                }
                                )} 
                                {this.state.message ? <li>No search results.</li> : '' }
                                </ul>

                                <input type='text'
                                className='center-block'
                                placeholder='Filter here…'
                               



                                />

                               <div>
                                {
                                    data.map(item => (
                                    <div key={item.id}>
                                        <a href={'mailto:${item.email}'}>{item.name}</a> {item.company}
                                    </div>
                                    ))
                                }
                                </div>
                              


                                <div className="modal fade" id="proveedor" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                <div className="modal-dialog" role="document">
                                    <div className="modal-content">

                                    <form onSubmit={this.handleSubmit}>
                                    <div className="modal-header">
                                        <h5 className="modal-title" id="exampleModalLabel">Nuevo Provedor</h5>
                                        <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">&times;</span>
                                        </button>
                                    </div>
                                    <div className="modal-body">
                                        <form>
                                        <div className="form-group">
                                            <label for="recipient-name" className="col-form-label">Nombre:</label>
                                            <input type="text"  className="form-control" value={this.state.value} onChange={this.handleChange} id="recipient-name"></input>
                                        </div>
                                        </form>
                                    </div>

                                    <div className="modal-footer">
                                        <button type="button" className="btn btn-secondary" data-dismiss="modal">Cancelar</button>
                                        <button type="button" className="btn btn-primary" type="submit" value="Buscar">Guardar</button>
                                    </div>
                                    </form>
                                    </div>
                                </div>

                                </div> 

                                <div className="modal fade" id="editproveedor" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                <div className="modal-dialog" role="document">
                                    <div className="modal-content">

                                    <form onSubmit={this.handleSubmit}>
                                    <div className="modal-header">
                                        <h5 className="modal-title" id="exampleModalLabel">Editar Provedor</h5>
                                        <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">&times;</span>
                                        </button>
                                    </div>
                                    <div className="modal-body">
                                        <form>
                                        <div className="form-group">
                                            <label for="recipient-name" className="col-form-label">Nombre:</label>
                                            <input type="text"  className="form-control" value={this.state.value} onChange={this.handleChange} id="recipient-name"></input>
                                        </div>
                                        </form>
                                    </div>

                                    <div className="modal-footer">
                                        <button type="button" className="btn btn-secondary" data-dismiss="modal">Cancelar</button>
                                        <button type="button" className="btn btn-primary" type="submit" value="Buscar">Actualizar</button>
                                    </div>
                                    </form>
                                    </div>
                                </div>
                                </div>

                          

                            <div className="modal fade" id="cartera" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                <div className="modal-dialog" role="document">
                                    <div className="modal-content">

                                    <form onSubmit={this.handleSubmit1}>
                                    <div className="modal-header">
                                        <h5 className="modal-title" id="exampleModalLabel">Nueva Cartera</h5>
                                        <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">&times;</span>
                                        </button>
                                    </div>
                                    <div className="modal-body">
                                        <form>
                                        <div className="form-group">
                                            <label for="recipient-name" className="col-form-label">Nombre:</label>
                                            <input type="text"  className="form-control" value={this.state.value} onChange={this.handleChange1} id="recipient-name"></input>
                                        </div>
                                        </form>
                                    </div>

                                    <div className="modal-footer">
                                        <button type="button" className="btn btn-secondary" data-dismiss="modal">Cancelar</button>
                                        <button type="button" className="btn btn-primary" type="submit" value="Buscar">Guardar</button>
                                    </div>
                                    </form>
                                    </div>
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



