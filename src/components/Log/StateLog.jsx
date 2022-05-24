import React from 'react';
import DateFilterBox from "./DateFilterBox";
import CropStateLog from "./CropStateLog";

function StateLog(props) {
    return (
        <div>
            <DateFilterBox />
            <CropStateLog />
        </div>
    );
}

export default StateLog;