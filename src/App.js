import React from 'react'
import Home from './components/Home/Home'
import Log from './components/Log/Log'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import LogDetail from "./components/LogDetail/LogDetail";
import Login from "./components/Login/Login";

function App() {
    return (
        <Router>
            <Routes>
                <Route path='/login' element={<Login />} />
                <Route path='/' element={<Home />} />
                <Route path='/log' element={<Log />} />
                <Route path='/logdetail' element={<LogDetail />} />
            </Routes>
        </Router>
    );
}

export default App;
