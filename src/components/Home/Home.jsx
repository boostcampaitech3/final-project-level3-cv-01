import React from 'react';
import CropState from "./CropState";
import CropInfo from "./CropInfo";
import {Link} from "react-router-dom";


const Home = () => {

    return (
        <>
            <CropState/>
            <CropInfo/>
            <Link to='/log'>
                <button>Log page 이동</button>
            </Link>

        </>
    );
};

export default Home;