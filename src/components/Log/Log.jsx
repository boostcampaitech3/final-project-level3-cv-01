import React, {useEffect, useState} from 'react';
import SimpleBottomNavigation from "../Navigator/Navigator";
import {Box, Container, Divider, Typography} from "@mui/material";
import {createTheme, ThemeProvider} from "@mui/material/styles";
import 'antd/dist/antd.css'
import {DatePicker} from 'antd';
import LogBox from "./LogBox";
import {useNavigate} from 'react-router';
import axios from 'axios';

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
    const [diseases, setDiseases] = useState([])
    const navigation = useNavigate()
    useEffect(() => {
        if (localStorage.getItem('isLoggedIn') !== "true") {
            navigation('/login')
        } else {
            axios.post("http://localhost:8000/api/v1/postDisease").then((res) => setDiseases(res.data.diseases))
        }
    }, [])
    // useEffect(() => {
    //     console.log(diseases)
    // }, [diseases])
    return (
        <ThemeProvider theme={theme}>

            <Container maxWidth='xs' sx={{bgcolor: 'background.main'}}>
                <br />
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
                    {/* <React.Fragment>
                        <LogBox category={diseases.category} kind={diseases.kind} date={diseases.date} datetime={diseases.datetime}
                                weather={diseases.weather} imageUrl={diseases.image_url} dbmemo={diseases.dbmemo}/>
                    </React.Fragment> */}
                    {diseases && diseases.map((item) => (
                        <React.Fragment>
                            <LogBox category={item.category} kind={item.kind} date={item.date} datetime={item.datetime}
                                    weather={item.weather} imageUrl={item.image_url} dbmemo={item.dbmemo}/>
                        </React.Fragment>
                    ))}
                    {/* {logDate.map((log) => (
                        <React.Fragment key={log.id}>
                            <LogBox category={log.category} date={log.date} kind={log.kind} datetime={log.datetime}
                                    weather={log.weather} imageUrl={log.image_url} />
                        </React.Fragment>
                    ))} */}
                </Box>
                <SimpleBottomNavigation/>
            </Container>

        </ThemeProvider>


    )
        ;
}

export default Log;