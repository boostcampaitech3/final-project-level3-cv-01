import React from 'react';
import WeatherState from "./WeatherState";
import SelectCropBox from "./SelectCropBox";

function CropState(props) {
    return (
        <div>
            <h3>작물관리</h3>
            <WeatherState />
            <br />
            <SelectCropBox />
            <br />
        </div>
    );
}

export default CropState;