class Botones extends React.Component {
    constructor(props) {
        super(props);
        this.abremodal = this.abremodal.bind(this);

      }


    abremodal (opcion,e) {

        $("#"+opcion).modal()
    
    }

    editamodal (opcion,e) {

        $("#"+opcion).modal()
    
    }

    render() {
      return (
        <div className='row'>

            

            <div className='col-md-2'>
                <div class="btn-group btn-group-toggle" data-toggle="buttons">
                <label class="btn btn-secondary active">
                <button type="button" data-toggle="modal" className="btn btn-sm btn-dark" onClick={e => this.abremodal(this.props.name,e)}>Add</button>
                </label>
                
                </div>
            </div>

            <div className='col-md-3'>
            {this.props.name}
            </div>
  
        </div>
      );
    }
}


class Select extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            value: "",
            editar:[]
        };

       

        this.selecciona = this.selecciona.bind(this);
      }

    

      selecciona(api,e){


        console.log(api,e.target.value)
        

      }


    render() {
      return (
        <div>
            <Botones name={this.props.opcion} edit_modal={this.props.edit_modal}/>

            <AddModal name={this.props.opcion} api={this.props.api}/>


            <select className='form-control'  onChange={e => this.selecciona(this.props.name,e)}>
                                            
                {this.props.value.map(item => (

                 <option  value={item.id} >{item.nombre}</option>

                ))}

            </select>

        </div>
      );
    }
  }

 

  class AddModal extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: []
        };

        this.guarda = this.guarda.bind(this);
        
      }


      handleChange(event) {
        this.setState({value: event.target.value});
      }

      


      guarda(event) {

        
        fetch('/discador/'+this.props.api+'/', {
            method: 'post',
            headers: {
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({nombre: this.state.value})
            }).then(res=>res.json())
            .then(res => {
                
                $('#'+this.props.name).modal('hide'); 
                $('body').removeClass('modal-open'); 
                $('.modal-backdrop').remove();
                
            });
        
            
        event.preventDefault();
      }

    render() {
      return (
       

            <div className="modal fade" id={this.props.name} tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div className="modal-dialog" role="document">
                    <div className="modal-content">

                    <form onSubmit={this.guarda}>
                    <div className="modal-header">
                        <h5 className="modal-title" id="exampleModalLabel">Agregar {this.props.name }</h5>
                        <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div className="modal-body">
                        <form>
                        

                        <div className="form-group">
                            <label for="recipient-name" className="col-form-label">Nombre:</label>
                            <input type="text"  className="form-control" onChange={this.handleChange.bind(this)} ></input>
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
             
      
      );
    }
  }

class Opcion extends React.Component {


    constructor(props) {
        super(props);

        this.state = {
            proveedores: [],
            carteras:[],
            gestiones:[],
            resultados:[],
            subresultados:[]

        };

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


    render() {

    
     const { proveedores,carteras,gestiones,resultados,subresultados} = this.state;

      return (
        <div className='container-fluid'>
        <div className='row'><a class='btn btn-sm' href='/admin/discador/score/'>Admin</a></div>
        <div className='row'>

            
           <div className='col-md-3'><Select edit_modal='_proveedor' opcion='Proveedor' api='api_proveedores' name='api_proveedor_detalle' value={proveedores}/></div>
           <div className='col-md-3'><Select edit_modal='_cartera' opcion='Cartera' api='api_carteras' name='api_detalle_cartera' value={carteras}/></div>
           <div className='col-md-3'><Select edit_modal='_gestion' opcion='Gestion' api='api_gestiones' name='api_gestiones' value={gestiones} /></div>
           <div className='col-md-3'><Select edit_modal='_gestion' opcion='Resultados' api='api_gestiones' name='api_gestiones' value={resultados}/></div>
        
        
        </div>
        </div>
      );
    }
  }
  


ReactDOM.render(
<Opcion />,
document.getElementById('user')
);
