import React from 'react';

import '../App.css';


class Form extends React.Component {

    state = {
        value: ''
    }

    handleSubmit = (e) =>{
        e.preventDefault();
        this.props.submit(this.state.value);
    }


    onChangeText =(e) =>{
        console.log(e); //stampa un oggetto con un attributo chiamato target che contiente l'oggetto input html
        this.setState({
            value: e.target.value
        })
    }
    render(){
        return(
            <form onSubmit={this.handleSubmit}>
                <input type="text" value = {this.state.value} palceHolder="aggiungi todo" onChange={this.onChangeText}/>
            </form>
        )
    }
}

export default Form;