import React from 'react';
import { Button, FilledInput, Typography, Container } from "@mui/material";


const LogDetail = (props) => {
    const [values, setValues] = React.useState({
        memo: '',
    });
    const handleChange = (prop) => (event) => {
        setValues({...values, [prop]: event.target.value});
    };
    const handleClickSave = () => {
        console.log(values.memo)
        //    클릭시 일지 저장하는 state Fucntion
    }

    return (
        <Container>
            <Typography variant="h6" sx={{color: 'text.darker'}}>발생일시</Typography>
            <FilledInput
                readOnly={true}
                fullWidth
                placeholder={props.date}
                sx={{color: 'text.darker', marginTop: 1}}
            />
            <br/>
            <Typography variant="h6" sx={{color: 'text.darker'}}>피해작물</Typography>
            <FilledInput
                readOnly={true}
                fullWidth
                placeholder={props.crop}
                sx={{color: 'text.darker', marginTop: 1}}
            />
            <br/>
            <Typography variant="h6" sx={{color: 'text.darker'}}>병해충명</Typography>
            <FilledInput
                readOnly={true}
                fullWidth
                placeholder={props.bug}
                sx={{color: 'text.darker', marginTop: 1}}
            />
            <br/>
            <Typography variant="h6" sx={{color: 'text.darker'}}>일지</Typography>
            <FilledInput
                fullWidth
                placeholder="일지를 작성해주세요"
                onChange={handleChange('memo')}
                multiline
                value={values.memo}
                variant="filled"
                sx={{color: 'text.darker'}}
            />
            <Button onClick={handleClickSave}> 저장 </Button>
            <Button onClick={props.handleClose}> 닫기 </Button>

        </Container>

    );
}

export default LogDetail;