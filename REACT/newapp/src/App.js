import React from 'react';
import './App.css';
import Todo from './components/todo';
import Form from './components/form';


class App extends React.Component {
  state = {
    todos: [
      {name: 'imparare React' , completato: true},
      {name: 'imparare gli state' , completato: false},
      {name: 'imparare i component' , completato: true},
    ]
  }
  
  addTodo = (text) => {
    
    this.setState({
      todos : [...this.state.todos, {name: text , completato: false}]
    })
  }

  render(){
    return(
      <div className="app">
        <div className="todo-list">
          {this.state.todos.map((item, index) => (
            <Todo todo={item} key = {index}/>
          ))}
          <Form submit={this.addTodo} />
        </div>
      </div>
    )
  }
}

export default App;