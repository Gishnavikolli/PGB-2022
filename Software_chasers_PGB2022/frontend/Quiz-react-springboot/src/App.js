import List from './components/List'
import Home from './components/Home'
import Python from './components/Python'
import Java from './components/Java'
import JavaScript from './components/JavaScript'
import C from './components/C'
import Questionaire from './components/Questionaire'
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import C2 from './components/C2'
import C3 from './components/C3'
import Java2 from './components/Java2'
import Java3 from './components/Java2'
import Python2 from './components/Python2'
import Python3 from './components/Python3'
import JavaScript2 from './components/JavaScript2'
import JavaScript3 from './components/JavaScript3'
function App() {
  return (
    <div className="App" style={{backgroundImage:"url(./quiz-background.png)"}}>
      <BrowserRouter>
      <Routes>
        <Route exact path= "/" element= {<Home/>}/>
        <Route exact path= "/PythonQuiz" element= {<Python/>}/>
        <Route exact path= "/JavaQuiz" element= {<Java/>}/>
        <Route exact path= "/CQuiz" element= {<C/>}/>
        <Route exact path= "/JavaScriptQuiz" element= {<JavaScript/>}/>
        <Route exact path= "/C2Quiz" element= {<C2/>}/>
        <Route exact path= "/C3Quiz" element= {<C3/>}/>
        <Route exact path= "/Java2Quiz" element= {<Java2/>}/>
        <Route exact path= "/Java3Quiz" element= {<Java3/>}/>
        <Route exact path= "/Python2Quiz" element= {<Python2/>}/>
        <Route exact path= "/Python3Quiz" element= {<Python3/>}/>
        <Route exact path= "/JavaScript2Quiz" element= {<JavaScript2/>}/>
        <Route exact path= "/JavaScript3Quiz" element= {<JavaScript3/>}/>
      </Routes>
      </BrowserRouter> 
    </div>
  );
}

export default App;
