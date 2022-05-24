import React from 'react';
import GrowthInfo from "./GrowthInfo";
import DamageInfo from "./DamageInfo";
import {Link} from "react-router-dom";

function CropInfo(props) {
    return (
        <div>
            <GrowthInfo />
            <br />
            <DamageInfo />
            <Link to='/'>
                <button>작물확인</button>
            </Link>
        </div>
    );
}

export default CropInfo;