-------------------------------BASICS-------------------------------;
Use Visual Studio Code for an IDE;
  
Type the following in windows terminal to create a new React app.;
  npx create-react-app app-name    ;  //starts react setup
  cd app-name                     ;   //goes into the app directory
  code .            ;                 //opens Visual Studio Code
  

  


React is a JavaScript package used to create user interfaces.;

React uses a JavaScript extension called JSX which combines HTML and JavaScript;
 
  const name = <h1>"Joseph Smith"</h1>;
  
 *****Attributes use camelCase*****;
  
These variables can be called in other elements using {name};

    const name = 'Josh Perez';
    const element = <h1>Hello, {name}</h1>;

Functions & objects can also be passed through;

    function formatName(x) {
    return x.firstName + ' ' + x.lastName;}

    const user = {
      firstName: 'Harper',
      lastName: 'Perez'};

    const element = (
      <h1>
        Hello, {formatName(user)}!
      </h1>);

JSX can contain children;
  const element = (
    <div>
      <h1>Hello!</h1>
      <h2>Good to see you here.</h2>
    </div>);

Rendering elements;
  React usually has a <div> with id = 'root';

The DOM renders this div;
   const root = ReactDOM.createRoot(document.getElementById('root'));
   root.render(element); //element is a javascript code that is passed;

---------------------------COMPONENTS & PROPS---------------------------;
Components are pieces of the UI that act like functions.;
They are created as a function and take in "props" (short for;
properties) which are then rendered by the ReactDOM;

An easy way to use props is by destructuring it with {} so you dont need;
to use the word 'prop';

  const Header = ({ title }) => {  //This uses the function shortcut () => {}
  return (
    <header>
        <h1>title</h1>;
    </header>)};
                 **************************
  The Header function is called by using <Header title = "~~";>
                 **************************
  function App() {
    return (
      <div className="container">
         <Header title = {'Hello'} /> //the Header variables is called and the prop is set in the tag.
      </div>);};

-------------------------------------LISTS-------------------------------------
Lists use map() to loop through their contents.;
    
    map() works like for (a in aa){} but this syntax:  ; //
     aa.map(a);

  function Car(props) {
    return <li>I am a { props.brand }</li>;} ; /// This puts every element in list tag <li>

  function Garage() {
    const cars = ['Ford', 'BMW', 'Audi'];  //This is the array used.
    return (
      <>
        <h1>Who lives in my garage?</h1>
        <ul> // *** This starts the list in HTML
          {cars.map((car) => <Car brand={car} />)}  //** Explained below
        </ul>
      </>);}

-Keys. Used to keep track of list elements. reserved keyword.;
 There are many ways to do this;
      const cars = [                        //object
        {id: 1, brand: 'Ford'},
        {id: 1, brand: 'Ford'},
        {id: 1, brand: 'Ford'}]

    {cars.map((car) => <Car key={car.id} brand={car.brand} />)};

------------------------------FORMS------------------------------
Information in forms in handled by form states in components

import { useState } from 'react';
import ReactDOM from 'react-dom/client';

function MyForm() {
  const [name, setName] = useState(""); //sets default at ""

  return (
    <form>
      <label>Enter your name:
        <input
          type="text" //type of the form
          value={name}  //
          onChange={(e) => setName(e.target.value)} //e is an event
        />
      </label>
    </form>)}


--------------------------------EVENTS---------------------------------
Handinling events is similar in standard HTML;
A function is called when an HTML event happens;
     
     <button onClick={() => {}}>  //function
       Activate Lasers
     </button>
  
-------------------------------HOOKS-------------------------------
Hooks allow function components to have access to state and other React features. 
State generally refers to data or properties that need to be tracked in an application.

 -useState
   *** useState accepts an initial state and returns two values: ***;
      -The current state.
      -A function that updates the state.

1) import { useState} from "react";

2) function FavoriteColor(){
      const [color, setColor] = useState("");}
       //  current,  function that updates

 Example:
    function FavoriteColor() {
      const [color, setColor] = useState("red");  //default color is red
      return <h1>My favorite color is {color}!</h1>};

To update the state call the updater function;
Use a callback function to access it;
    
      <button   //button to change color to blue
        type="button"
        onClick={() => setColor("blue")}  //This is the updater function
      >Blue</button>
      
 -useEffect. 
    The useEffect Hook allows you to perform side effects in your components.
    The second argument is optional
       *** useEffect(<function>, <dependency>)
   
Example: counting every second after rendering
      useEffect(() => {
        setTimeout(() => {
          setCount((count) => count + 1);
        }, 1000);
      }, []); // <- add empty brackets here to stop after 1 time


