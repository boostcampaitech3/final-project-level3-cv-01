import React from 'react';
import SimpleBottomNavigation from "../Navigator/Navigator";
import { Box, Container, Divider, Typography } from "@mui/material";
import {createTheme, ThemeProvider} from "@mui/material/styles";
import 'antd/dist/antd.css'
import { DatePicker } from 'antd';
import LogBox from "./LogBox";

const onChange = (value, dateString) => {
    console.log('Selected Time: ', value);
    console.log('Formatted Selected Time: ', dateString);
};

const onOk = (value) => {
    console.log('onOk: ', value);
};

const theme = createTheme({

    palette: {
        background: {
            main: '#fff',
            primary: '#064635'
        },
        text: {
            primary: '#064635',
            darker: '#000000',
            white: '#fff'
        },
        button_color: {
            main: '#064645',
            contrastText: '#fff',
            darker: '#000000',
            gray: '#C8C8C8'
        }
    },
});


function Log() {

    return (
        <ThemeProvider theme={theme}>

            <Container maxWidth='xs' sx={{bgcolor: 'background.main', marginTop: 2}}>

                <Box>
                    <Typography variant="h5" sx={{color: 'text.primary'}}>피해발생 기록</Typography>
                </Box>

                <Divider sx={{marginTop: 1, marginBottom: 1}}/>

                <Box>
                    <h5>검색기간</h5>

                    <DatePicker.RangePicker
                        showTime={{
                            format: 'HH:mm',
                        }}
                        format="YYYY-MM-DD HH:mm"
                        onChange={onChange}
                        onOk={onOk}
                        style={{width: '100%', alignItems: 'center'}}
                    />
                </Box>

                <Box>
                    <LogBox category='bug' date='2022-05-26' kind='벌레'/>
                    {/* Log 기록은 날짜와 category를 변수로 받게 해둠 */}
                    <LogBox category='disease' date='2022-05-26' kind='병'/>

                </Box>
                <SimpleBottomNavigation/>
            </Container>

        </ThemeProvider>


    )
        ;
}

export default Log;