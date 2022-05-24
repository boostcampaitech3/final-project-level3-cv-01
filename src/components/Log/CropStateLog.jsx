import React from 'react';
import {Link} from "react-router-dom";


function CropStateLog(props) {
    return (
        <div>
            <h5>해충피해발생</h5>
            <p>날짜!!</p>
            <div>
                <Link to='/logdetail'>
                    <button>상세정보</button>
                </Link>
                <button>결과확인</button>
                <button>삭제</button>
            </div>
        </div>
    );
}

export default CropStateLog;