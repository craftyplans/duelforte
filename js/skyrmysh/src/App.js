import React from 'react';
import logo from './skyrmysh-logo.png';
import './App.css';

const cards = [
    "Quick Attack",
    "Hard Attack",
    "Precise Attack",
    "Quick Defend",
    "Hard Defend",
    "Precise Defend",
    "Move",
    "Cast Spell",
    "Focus",
    "Other",
    "Full"
]

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
            className={this.state.selected ? "card-selected" : "card"}
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
            <p>Select up to 2 cards.</p>
            {cards.map(c => <Card content={c} />)}
            </div>
        </div>
  );
}

export default App;
