import React from 'react';
import GrowthInfo from "./GrowthInfo";
import DamageInfo from "./DamageInfo";

function CropInfo(props) {
    return (
        <div>
            <GrowthInfo />
            <br />
            <DamageInfo />
            <button>작물확인</button>
        </div>
    );
}

export default CropInfo;