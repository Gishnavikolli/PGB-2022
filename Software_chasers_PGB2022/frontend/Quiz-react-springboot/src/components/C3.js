import React, { useState, useEffect } from "react";
import "../App.css"
import Questionaire from "./Questionaire";
import Axious from "axios"; 
import { Link } from "react-router-dom";
// const API_URL = "https://opentdb.com/api.php?amount=10&type=multiple";
const API_URL = "http://localhost:8086/quiz/CategoryAndDifficulty?Category=JAVA&Difficulty=Level-1";
function C3() {
  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [showAnswers, setShowAnswers] = useState(false);
  
  useEffect(() => {
    Axious.get(API_URL)
      .then((res) => res.data)
      .then((data) => {
       
        //to hide the json data
      // console.log = function (data) {
      //     var tempObj;
      
      //     if (typeof data === 'object' && !data.length) {
      //         tempObj = JSON.parse(JSON.stringify(data));
      //         tempObj = null;
      //         return tempObj;
      //     }
      
      //     return data;
      // };
        const questions = data.map((question) => ({
          ...question,
          answers: [
            question.correct_answers,
            ...question.incorrect_answers,
          ].sort(() => Math.random() - 0.5),
        }));
            console.log(questions)
        setQuestions(questions);
      });
  }, []);

  const handleAnswer = (answer) => {
    if (!showAnswers) {
      if (answer.target.value === questions[currentIndex].correct_answers) {
        setScore(score + 1);
        
      }
    }
    // if(currentIndex==questions.length-1)
      setShowAnswers(true);
  };

  const handleNextQuestion = () => {

    setCurrentIndex(currentIndex + 1);
    setShowAnswers(false);
  };

  const SameLevel=()=>window.history.go="/C3Quiz";
  return questions.length > 0 ? (
    <div
      className="container"
      style={{ backgroundImage: "url(./quiz-background.png)" }}
    >
      {currentIndex >= questions.length ? (
        <>
        <h1>Game Ended, your Score is {score}</h1>
        {score>=9?
          <>
          <div><h1>Congratulations! You have qualified the Quiz </h1></div> 
          </>
        :
        <>
        <div><h1>Sorry,You are not qualified to NextLevel</h1></div>
        <Link to="/C3Quiz"><button style={{marginLeft:"5%",backgroundColor:"white",width:"200px",padding:"8px",fontWeight:"bolder",borderRadius:"10px"}} type= "button" className='btn-next' onClick={SameLevel}>Try Again</button></Link>
        </>
        }
        </>
      ) : (
        <Questionaire
          handleAnswer={handleAnswer}
          showAnswers={showAnswers}
          handleNextQuestion={handleNextQuestion}
          data={questions[currentIndex]}
        />
      )}
    </div>
  ) : (
    "loading..."
  );
}

export default C3;
