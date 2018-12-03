

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
                      resultados:[],
                      nombre_proveedor:'',
                      data:[],
                      todosInit: [],
                      todos: [],
                      todoText: ""
                  };

                    this.updateTodoText = this.updateTodoText.bind(this);
                    this.createTodo = this.createTodo.bind(this);
                    this.filterTodo = this.filterTodo.bind(this);

 
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
             



              sacacarteras(item) {


                this.setState({                
                    proveedor:item,
                    nombre_proveedor:item.nombre
                });

                  
                  
                  fetch("/discador/api_cartera/"+item.id)
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

              render() {


                  const { data,nombre_proveedor, error, isLoaded, proveedor, proveedores, carteras,resultados } = this.state;

                   
                    

                      if (!isLoaded) {
                          
                          return <div>Loading...</div>;
                          
                      } 
                      
                      else {
                          
                          return (

                             <div className='container'>

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




