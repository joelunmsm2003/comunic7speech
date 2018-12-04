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
                      resultados:[],
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


                  const { value,data,nombre_proveedor, error, isLoaded, proveedor, proveedores, carteras,resultados } = this.state;

                   
                    

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
                              
                              <div className="row">

                               <div className="col-3">

                                <h2>Proveedores</h2>
                                <img src="/static/add.png"  height="30" width="30"class="btn btn-primary" data-toggle="modal" data-target="#exampleModal" data-whatever="@mdo">
                                </img><img src="/static/edit.png"  height="30" width="30"></img>
                                <img src="/static/delete.png" height="30" width="30" ></img>


<div className="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div className="modal-dialog" role="document">
    <div className="modal-content">
      <div className="modal-header">
        <h5 className="modal-title" id="exampleModalLabel">Nuevo Provedor</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form>
          <div class="form-group">
            <label for="recipient-name" class="col-form-label">Recipient:</label>
            <input type="text" class="form-control" id="recipient-name"></input>
          </div>
          <div class="form-group">
            <label for="message-text" class="col-form-label">Message:</label>
            <textarea class="form-control" id="message-text"></textarea>
          </div>
        </form>
      </div>

      <div className="modal-footer">
        <button type="button" className="btn btn-secondary" data-dismiss="modal">Calcelar</button>
        <button type="button" className="btn btn-primary">Guardar</button>
      </div>
    </div>
  </div>
</div>




                                <select className='form-control'   onChange={this.sacacarteras}>

                              {proveedores.map(item => (

                                 // <option  onClick={(e) => this.sacacarteras(item, e)} key={item.nombre}>{item.nombre}</option> 
                                 <option  value={item.id} >{item.nombre}</option>

                              ))}

                              </select> 

                              </div>
 

                              <div className="col-3">
                                 
                              <h2>Carteras </h2>
                              <h2>{nombre_proveedor}</h2>
                              <img src="/static/add.png"  height="30" width="30"class="btn btn-primary" data-toggle="modal" data-target="#exampleModal" data-whatever="@mdo">
                                </img><img src="/static/edit.png"  height="30" width="30"></img>
                                <img src="/static/delete.png" height="30" width="30" ></img>


                              <select className='form-control'   onChange={this.sacaresultados}>
                              {carteras.map(item => (


                                <option  value={item.id} >{item.cartera.nombre}</option>
                                // <div className="list-group">
                                // <a className="list-group-item list-group-item-action"    onClick={(e) => this.sacaresultados(item, e)} key={item.nombre}>{item.cartera.nombre}</a> 

                                //</div>

                            


                              ))}

                              </select> 

                              </div>

                              <div className="col-3">



                               <h2>Resultadoss</h2>

                                <select className='form-control'   onChange={this.sacaresultados}>
                                {resultados.map(item => (

                                    //<div className="list-group">
                                    //<a className="list-group-item list-group-item-action"    onClick={(e) => this.sacaresultados(item, e)} key={item.nombre}>{item.resultado.nombre}
                                    //<input type='checkbox'></input>
                                    //</a> 
                                    
                                    
                                    //</div>
                                    <option  value={item.id} >{item.resultado.nombre}</option>

                                    ))}
                                    </select> 
                    

                              
                                
                              
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



