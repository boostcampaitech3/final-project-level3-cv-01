import React from 'react';

function SelectCropBox(props) {
    return (
        <div>
            현재작물상태 :
            <select name="Crop">
                <option value="배추">배추</option>
            </select>
            <br />
        </div>
    );
}

export default SelectCropBox;