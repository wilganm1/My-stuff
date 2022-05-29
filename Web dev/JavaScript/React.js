-------------------------------BASICS-------------------------------
How to create a new React app in the terminal
 npx create-react-app my-app
 cd my-app
 npm start


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

--------------------------------EVENTS & STATES--------------------------------
States represent the current situation of a component.;

  First import the useState object;
  Then create an  array variable for the state;
   
   import {useState} from 'react';   //importing states
  
   const [stateName, setStateName] = useState();  //Setting up the State object
//!!! Have the 2nd item in the array use the word 'set' and the name of the state.
   
   
Handinling events is similar in standard HTML;
A function is called when an HTML event happens;
     
     <button onClick={functionName}>  //
       Activate Lasers
     </button>
     





