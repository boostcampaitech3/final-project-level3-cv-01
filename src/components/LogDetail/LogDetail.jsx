import React from 'react';
import {Button, FilledInput, Typography, Container} from "@mui/material";
import Grid from "@mui/material/Grid";
import LogDateBox from "../Log/LogDateBox";
import axios from 'axios';


const LogDetail = (props) => {
    // console.log(props.datetime, '@')
    const [values, setValues] = React.useState({
        crop: props.crop,
        bug: props.bug,
        weather: props.weather[0],
        memo: props.dbmemo
    });
    const handleChange = (prop) => (event) => {
        setValues({...values, [prop]: event.target.value});
    };
    const handleClickSave = () => {
        axios.post('http://127.0.0.1:8000/api/v1/postMemo', {idx: props.idx, crop: props.crop, bug: props.bug, weather: props.weather[0], memo: values.memo, datetime: props.datetime[0]})
        // console.log(props.crop)
        // console.log(props.bug)
        // console.log(props.weather[0])
        // console.log(values.memo)
        //    클릭시 일지 저장하는 state Fucntion
    }
    const [open, setOpen] = React.useState(true);

    const handleClick = () => {
        setOpen(!open);
    }

    return (
        <Container>
            <LogDateBox date={props.date} handleClick={handleClick} datetime={props.datetime} />

            <Typography variant="h6" sx={{color: 'text.darker'}}>피해작물</Typography>
            <FilledInput
                readOnly={true}
                fullWidth
                placeholder={props.crop}
                sx={{color: 'text.darker', marginTop: 1, marginBottom: 2}}
            />

            <Typography variant="h6" sx={{color: 'text.darker'}}>병해충명</Typography>
            <FilledInput
                readOnly={true}
                fullWidth
                placeholder={props.bug}
                sx={{color: 'text.darker', marginTop: 1, marginBottom: 2}}
            />

            <Typography variant="h6" sx={{color: 'text.darker'}}>날씨</Typography>
            <FilledInput
                readOnly={true}
                fullWidth
                placeholder={`${props.weather[0].state} / 강수량 - ${props.weather[0].precipitation}mm`}
                sx={{color: 'text.darker', marginTop: 1, marginBottom: 2}}
            />

            <Typography variant="h6" sx={{color: 'text.darker'}}>일지</Typography>
            <FilledInput
                fullWidth
                placeholder="일지를 작성해주세요"
                onChange={handleChange('memo')}
                multiline
                value={values.memo}
                variant="filled"
                sx={{color: 'text.darker', marginBottom: 2}}
            />
            <Grid container>
                <Grid item xs>
                    <Button onClick={handleClickSave} sx={{paddingRight: 5, paddingLeft: 5, color: 'text.white', bgcolor: 'background.primary'}}> 저장 </Button>
                </Grid>
                <Grid item>
                    <Button onClick={props.handleClose} sx={{paddingRight: 5, paddingLeft: 5, color: 'text.white', bgcolor: 'background.primary'}}> 닫기 </Button>
                </Grid>
            </Grid>

        </Container>

    );
}

export default LogDetail;