import React from 'react';
import logo from './skyrmysh-logo.png';
import './App.css';
import cards from './cards.json'
import character from './character.json'

class Card extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            selected: false,
        };
    }

    render() {
        return (
                <div
            className={this.state.selected ? "card selected" : "card"}
            onClick={() => this.setState({selected: ! this.state.selected })}
                >
                {this.props.content}
            </div>
        );
    }
}

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="logo" alt="logo" />
            </header>    
            <div className="body">
            <p>{character.name}, select up to {character.actions} cards.</p>
            <div className="card-list">
            {cards.map(c => <Card content={c} />)}
        </div>
            </div>
        </div>
  );
}

export default App;
