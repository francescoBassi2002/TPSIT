import React from 'react';

import '../App.css';

const Todo = function(props){
    return (
        <div className="todo">
            {props.todo.name}
        </div>
    )
}


export default Todo;