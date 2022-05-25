import React from 'react';
import StateLog from "./StateLog";
import {Link} from "react-router-dom";
import SimpleBottomNavigation from "../Navigator/Navigator";

function Log(props) {
    return (
        <div>
            피해발생 기록
            <StateLog/>
            <Link to='/'>
                <button>Home page 이동</button>
            </Link>
            <SimpleBottomNavigation />
        </div>

    );
}
export default Log;