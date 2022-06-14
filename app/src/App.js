import React from 'react'
import Home from './components/Home/Home'
import Log from './components/Log/Log'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Login from "./components/Login/Login";

function App() {
    return (
        <Router>
            <Routes>
                <Route path='/login' element={<Login />} />
                <Route path='/' element={<Home />} />
                <Route path='/log' element={<Log />} />
            </Routes>
        </Router>
    );
}

export default App;
