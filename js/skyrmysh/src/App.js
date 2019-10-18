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

//function cardDOM(card){
//    return <div>{card}<div>
//}

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="logo" alt="logo" />
            </header>    
            <div className="body">
            <p>Select up to 2 cards.</p>
            <select size={cards.length} multiple>
            {cards.map(c => <option>{c}</option>)}
            </select>
            </div>
        </div>
  );
}

export default App;
