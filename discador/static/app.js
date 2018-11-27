

class Prueba extends React.Component{
  constructor(){
     super();
     this.state= {title: 'Click text'}
  }
  
  render(){
     return <div onClick= {() => this.setState({title:'New text'})}>{this.state.title}</div>
  } 
}

ReactDOM.render(<Prueba/>, document.getElementById('carteras'))


class Agentes extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: []
    };

    this.state= {title: 'Click text'}
   
  }

  componentDidMount() {
    fetch("http://138.68.230.137:8000/distrito")
      .then(res => res.json())
      .then(
        (result) => {

          console.log(result)
          this.setState({
            isLoaded: true,
            items: result
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



  sacacarteras(e) {

      fetch("http://138.68.230.137:8000/distrito")
      .then(res => res.json())
      .then(
        (result) => {

          console.log(result)
          this.setState({
            isLoaded: true,
            items: result
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
    const { error, isLoaded, items } = this.state;

 
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <ul>
          {items.map(item => (
            <li onClick={(e) => this.sacacarteras(item, e)} key={item.nombre} >
              {item.nombre}
            </li>
          ))}
        </ul>
      );
    }
  }






}






ReactDOM.render(
    <Agentes />,
    document.getElementById('root')
);

ReactDOM.render(
    <Title />,
    document.getElementById('carteras')
);

