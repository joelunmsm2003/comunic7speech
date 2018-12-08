import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";


const App = () => (
  <DataProvider endpoint="api/lead/" 
                render={data => <Table data={data} />} />
);
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;

    render() {
    
     const { proveedores,carteras,gestiones,resultados,subresultados} = this.state;

      return (
        <div className='container-fluid'>
        <div className='row'>
           <div className='col-md-4'><Select edit_modal='_proveedor' opcion='proveedor' api='api_proveedores' name='api_proveedor_detalle' value={proveedores}/></div>
           <div className='col-md-4'><Select edit_modal='_cartera' opcion='cartera' api='api_carteras' name='api_detalle_cartera' value={carteras}/></div>
           <div className='col-md-4'><Select edit_modal='_gestion' opcion='gestion' api='api_gestiones' name='api_gestiones' value={gestiones}/></div>
        </div>
        </div>
      );
    }
  }
  


ReactDOM.render(
<Opcion />,
document.getElementById('user')
);
