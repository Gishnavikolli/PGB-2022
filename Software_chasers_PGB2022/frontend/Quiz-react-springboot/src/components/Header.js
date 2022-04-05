import React from 'react';
import "./Header.css";
import { Link } from 'react-router-dom';

export const Header = () => {
  return (
    <div className='header' style={{display: "flex", flexDirection: "column",alignItems: "center"}}>
        <h1 className="title" >
            Quiz
        </h1>
        <h1>Select any Language</h1>
        <hr className="divider"></hr>
        <footer/>
    </div>

  )
}
