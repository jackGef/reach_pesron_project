import Home from "./pages/Home"
import Check from "./pages/Check"
import Header from "./components/Header"
import './App.css'
import { BrowserRouter, Route, Routes } from "react-router-dom" 
import LinearRegression from "./pages/LinearRegression"
import LogisticRegerssion from "./pages/LogisticRegerssion"

function App() {

  return (
    <div className="app">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home/>}/>
          <Route path="/ai/linearRegression" element={<LinearRegression/>}/>
          <Route path="/ai/logisticRegression" element={<LogisticRegerssion/>}/>
        </Routes>
      </BrowserRouter>
      {/* <Header/> */}
      {/* <Check/> */}
    </div>
  )
}

export default App
