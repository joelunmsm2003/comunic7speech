

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
                
                fetch("/discador/api_cartera/"+event.target.value)
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

              render() {


                  const { value,data,nombre_proveedor, error, isLoaded, proveedor, proveedores,carteras,gestiones,resultados,subresultados } = this.state;

                   
                    

                      if (!isLoaded) {
                          
                          return <div>Loading...</div>;
                          
                      } 
                      
                      else {
                          
                          return (

                             <div className='container'>

                            

                             <div className="row">

                              

                                <div className="col-2">

                                <h4>Proveedores</h4>

                                <select className='form-control'>
                                

                                {proveedores.map(item => (

                                // <option  onClick={(e) => this.sacacarteras(item, e)} key={item.nombre}>{item.nombre}</option> 
                                <option  value={item.id} >{item.nombre}</option>

                                ))}

                                </select> 
                                </div>


                                <div className="col-2">
                                
                                <h4>Carteras </h4>
                                <h4>{nombre_proveedor}</h4>



                                <select className='form-control'>

                                {carteras.map(item => (

                                <option  value={item.id} >{item.nombre}</option>

                                ))}

                                </select> 

                                </div>

                                <div className="col-2">
                                
                                <h4>Gestion </h4>
                                


                                <select className='form-control'>

                                {gestiones.map(item => (

                                    // <option  onClick={(e) => this.sacacarteras(item, e)} key={item.nombre}>{item.nombre}</option> 
                                    <option  value={item.id} >{item.nombre}</option>

                                ))}

                                </select>

                                </div>

                                <div className="col-2">



                                <h4>Resultados</h4>


                                <select className='form-control'   onChange={this.sacaresultados}>

                                {resultados.map(item => (

                                    // <option  onClick={(e) => this.sacacarteras(item, e)} key={item.nombre}>{item.nombre}</option> 
                                    <option  value={item.id} >{item.nombre}</option>

                                ))}

                                </select>

                                </div>

                                <div className="col-2">



                                <h4>Subresultados</h4>


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
                                    <button className='btn btn-success center-block'>Create</button>
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
                                onChange={this.filterTodo}
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
                              
                              

                             </div>

                          );

                          }
              }


          }







          ReactDOM.render(


              <Hello />,
              document.getElementById('root')


          );




