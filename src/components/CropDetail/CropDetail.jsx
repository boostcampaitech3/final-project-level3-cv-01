import React from 'react';
import SelectImageBox from './SelectImageBox'
import ImageBlock from "./ImageBlock";

function CropDetail(props) {
    return (
        <div>
            <SelectImageBox />
            <ImageBlock />
            <button>닫기</button>
        </div>
    );
}

export default CropDetail;