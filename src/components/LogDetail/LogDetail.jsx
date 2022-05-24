import React from 'react';
import LogDetailBox from "./LogDetailBox";
import Memo from "./Memo";
import {Link} from "react-router-dom";


const LogDetail = () => {
    return (
        <div>
            <LogDetailBox title='발생일시' content='1111-11-11' />
            <br />
            <LogDetailBox title='피해작물' content='배추' />
            <br />
            <LogDetailBox title='병해충명' content='ㅠㅠ' />
            <br />
            <Memo title='일지' />

        </div>

    );
}

export default LogDetail;