import React from 'react';

function LoginBlock(props) {
    return (
        <div>
            <input placeholder='아이디' type='text' />
            <br />
            <input placeholder='비밀번호' type='password' />
            <br />
            <button>로그인</button>
        </div>
    );
}

export default LoginBlock;