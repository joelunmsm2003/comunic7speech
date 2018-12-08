import React from "react";

class Table extends React.Component {
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
                <button type="button" data-toggle="modal" className="btn btn-sm btn-dark">Add</button>
                </label>
                
                </div>
            </div>

            <div className='col-md-3'>
            kjkjkjk
            </div>
  
        </div>
      );
    }
}


export default Table;