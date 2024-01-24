import { useState } from 'react';

const products = [
  { title: 'Cabbage', isFruit: false, id: 1 },
  { title: 'Garlic', isFruit: false, id: 2 },
  { title: 'Apple', isFruit: true, id: 3 },
];
export function ShoppingList() {

  const listItems = products.map(product =>
    <li key={product.id}> 
      {product.title}
    </li>
  );

  const [count, setCount] = useState(0);
  function handleClick() {
    setCount(count + 1);
    //alert('You clicked me!');
  }
  return (
    <div>
    <h1>{listItems}
    <MyButton count={count} onClick={handleClick} />
    <MyButton count={count} onClick={handleClick} />
    </h1> 
    </div>
    
  );
}
function MyButton({ count, onClick }) {
  return (
    <button onClick={onClick}>
      Clicked {count} times
    </button>
  );
}
function Square({ value }) {
  const [valuue, setValuue] = useState(null);
  function handleClick() {
    setValuue('X');
  }

  return (
    <button
      className="square"
      onClick={handleClick}
    >
      {valuue}
    </button>
  );
}
export default function Board() {
  return (
    <>
      <div className="board-row">
        <Square />
        <Square />
        <Square />
      </div>
      <div className="board-row">
        <Square />
        <Square />
        <Square />
      </div>
      <div className="board-row">
        <Square />
        <Square />
        <Square />
      </div>
    </>
  );
}