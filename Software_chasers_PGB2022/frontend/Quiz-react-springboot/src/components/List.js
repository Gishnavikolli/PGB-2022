import React from "react";
import { Link } from "react-router-dom";
import Python from "./Python"
import '../App.css';
import "./List.css";


function List() {
  return (
    <>
      <ul class="list-group" className='lst'>
        <Link class="list-group-item"to="/PythonQuiz"style={{borderRadius:"12px",backgroundColor: "#909090"}}>Python</Link>
        <Link class="list-group-item"to="/JavaQuiz"style={{borderRadius:"12px",backgroundColor: "#909090"}}>Java</Link>
        <Link class="list-group-item"to="/CQuiz"style={{borderRadius:"12px",backgroundColor: "#909090"}}>C</Link>
        <Link class="list-group-item"to="/JavascriptQuiz"style={{borderRadius:"12px",backgroundColor: "#909090"}}>Javascript</Link>
      </ul>
    </>
  );
}

export default List;
