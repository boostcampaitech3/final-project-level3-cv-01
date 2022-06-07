import React, {useEffect, useState} from 'react';
import SimpleBottomNavigation from "../Navigator/Navigator";
import {createTheme, ThemeProvider} from "@mui/material/styles";
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import {Button, Divider, Modal, Stack, Typography} from "@mui/material";
import CachedOutlinedIcon from '@mui/icons-material/CachedOutlined';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import {useNavigate} from 'react-router';
import Logo from './logo.png'
import axios from 'axios';

import {
    mdiWeatherSnowyRainy,
    mdiWeatherPouring,
    mdiWeatherSnowyHeavy,
    mdiWeatherRainy,
    mdiWhiteBalanceSunny
} from '@mdi/js';
import Icon from '@mdi/react'

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
};

const theme = createTheme({
    status: {
        danger: '#064635',
    },
    palette: {
        background: {
            main: '#fff',
            primary: '#064635',
            logo: '#274437'
        },
        text: {
            primary: '#064635',
            darker: '#000000',
            white: '#fff'
        },
        button_color: {
            main: '#064645',
            contrastText: '#fff',
        }
    },
});


const Home = () => {
    const [weather, setWeather] = useState([])
    const navigation = useNavigate()
    const [open, setOpen] = useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    const [camera, setCamera] = useState('');
    const handleChange = (event) => {
        setCamera(event.target.value);
    };
    useEffect(() => {
        if (localStorage.getItem('isLoggedIn') !== "true") {
            navigation('/login')
        } else {
            axios.post("http://localhost:8000/api/v1/postWeather").then((res) => setWeather(res.data.weather))
        }
    }, [])
    const weatherBox = (prop) => {
        if (prop.state === '비') {
            <Icon path={mdiWeatherRainy}
                  title="비"
                  size={3}
                  sx={{margin: 0.5}}
            />
        } else if (prop.state === '비/눈') {
            <Icon path={mdiWeatherSnowyRainy}
                  title="비/눈"
                  size={3}
                  sx={{margin: 0.5}}
            />
        } else if (prop.state === '눈') {
            <Icon path={mdiWeatherSnowyHeavy}
                  title="눈"
                  size={3}
                  sx={{margin: 0.5}}
            />
        } else if (prop.state === '소나기') {
            <Icon path={mdiWeatherPouring}
                  title="소나기"
                  size={3}
                  sx={{margin: 0.5}}
            />
        } else {
            <Icon path={mdiWhiteBalanceSunny}
                  title="맑음"
                  size={3}
                  sx={{margin: 0.5}}
            />
        }
    }
    return (
        <ThemeProvider theme={theme}>

            <Container maxWidth='xs'
                       sx={{alignItems: 'center', bgcolor: 'background.logo', minHeight: 790, minWidth: '100%'}}>

                <Box sx={{color: 'text.white', minHeight: '100%', minWidth: '100%', alignItems: 'center', p: '5%'}}>
                    <img src={Logo}/>
                    {/*    Logo 삽입 예정*/}
                </Box>

                <Box sx={{
                    color: 'text.darker',
                    // borderTopLeftRadius: 50,
                    // borderTopRightRadius: 50,
                    borderRadius: 10,
                    p: 2,
                    margin: 0,
                    minHeight: 580,
                    bgcolor: 'background.paper',
                }}>
                    <Typography variant="h5"
                                sx={{color: 'text.darker', textAlign: 'center', p: 1, marginBottom: 1.5}}>작물관리
                    </Typography>

                    <Box
                        sx={{
                            bgcolor: 'background.paper',
                            boxShadow: 2,
                            borderRadius: 8,
                            p: 2,
                            minWidth: 80,
                            minHeight: 160,
                            alignItems: 'center'
                        }}
                    >
                        <Stack direction="row" spacing={1}>
                            <Box>
                                <Stack spacing={2}>
                                    <Box sx={{textAlign: 'center', alignItems: 'center'}}>
                                        <Typography variant="h6"
                                                    sx={{color: 'text.darker'}}> {weather.date}
                                        </Typography>
                                    </Box>
                                    <Box sx={{textAlign: 'center', alignItems: 'center'}}>
                                        <Typography variant="h4"
                                                    sx={{color: 'text.darker'}}> {weather.temperature}℃

                                        </Typography>
                                    </Box>
                                    <Box sx={{textAlign: 'center', alignItems: 'center'}}>
                                        <Typography variant="h6"
                                                    sx={{color: 'text.darker'}}> {weather.precipitation}mm
                                        </Typography>
                                    </Box>
                                </Stack>
                            </Box>

                            <Box sx={{
                                textAlign: 'center',
                                alignItems: 'center',
                                minWidth: 180,
                                p: 2
                            }}>
                                {weatherBox(weather)}
                                <Icon path={mdiWhiteBalanceSunny}
                                      title="맑음"
                                      size={3}
                                      sx={{margin: 0.5}}
                                />
                                <br/>
                                <Typography variant="h5"
                                            sx={{color: 'text.darker'}}> {weather.state}
                                </Typography>
                            </Box>
                        </Stack>
                        {/*  날씨 API 입력  */}
                    </Box>

                    <Box sx={{p: 2, textAlign: 'center'}}>
                        <Typography variant='h5'>현재작물상태 : 배추</Typography>
                    </Box>

                    <Divider variant="middle"/>

                    <Box sx={{p: 0.5}}>
                        <Box sx={{width: '100%'}}>
                            <Stack>
                                <Typography variant="p"
                                            sx={{color: 'text.darker', p: 1}}>피해발생 정보
                                </Typography>
                                <Box>
                                    <Stack direction="row" spacing={2} sx={{
                                        bgcolor: '#F2F2F2',
                                        borderTopLeftRadius: 6,
                                        borderTopRightRadius: 6,
                                        p: 1.5
                                    }}>
                                        <Box>
                                            <Typography variant="h8"
                                                        sx={{color: 'text.darker'}}>해충
                                            </Typography>
                                        </Box>
                                        <Box>
                                            <Typography variant="p"
                                                        sx={{color: 'text.darker'}}>Description
                                            </Typography>
                                        </Box>
                                    </Stack>
                                </Box>
                                <br/>
                                <Box>
                                    <Stack direction="row" spacing={2}
                                           sx={{
                                               bgcolor: '#F2F2F2',
                                               borderBottomRightRadius: 6,
                                               borderBottomLeftRadius: 6,
                                               p: 1.5
                                           }}>
                                        <Box>
                                            <Typography variant="h8"
                                                        sx={{color: 'text.darker'}}>질병
                                            </Typography>
                                        </Box>
                                        <Box sx={{textAlign: 'center'}}>
                                            <Typography variant="p"
                                                        sx={{color: 'text.darker'}}>Description
                                            </Typography>
                                        </Box>
                                    </Stack>
                                </Box>
                                <br/>
                                <Button variant='contained' color='button_color' sx={{p: 1}}
                                        onClick={handleOpen}>실시간 작물 확인</Button>
                            </Stack>

                        </Box>

                        {/* 실시간 작물 확인 버튼 클릭 시 나타나는 화면 Modal기능으로 구현*/}
                        <Modal
                            open={open}
                            onClose={handleClose}
                            aria-labelledby="modal-modal-title"
                            aria-describedby="modal-modal-description"
                        >
                            <Container sx={style}>
                                <Box sx={{textAlign: 'center'}}>
                                    <h1>배추하우스</h1>
                                    <Box>
                                        <FormControl>
                                            <InputLabel id="demo-simple-select-label">Camera</InputLabel>
                                            <Stack direction="row" spacing={2}>
                                                {/* 사진 선택 Select Box 코딩 */}
                                                <Select
                                                    labelId="demo-simple-select-label"
                                                    id="demo-simple-select"
                                                    value={camera}
                                                    label="Camera"
                                                    onChange={handleChange}
                                                    sx={{minWidth: 120, color: '#000000'}}
                                                >
                                                    <MenuItem value={10} sx={{color: '#000000'}}>Camera1</MenuItem>
                                                    <MenuItem value={20} sx={{color: '#000000'}}>Camera2</MenuItem>
                                                    <MenuItem value={30} sx={{color: '#000000'}}>Camera3</MenuItem>
                                                </Select>

                                                <Box sx={{alignItems: 'center', textAlign: 'center'}}>
                                                    {/* 새로고침 아이콘 부분 */}
                                                    <Button>
                                                        <CachedOutlinedIcon fontSize='large'/>
                                                    </Button>
                                                </Box>
                                            </Stack>
                                        </FormControl>
                                    </Box>
                                </Box>
                                {/* 원본 이미지 보여지는 부분 */}
                                <Box sx={{
                                    bgcolor: 'background.paper',
                                    boxShadow: 2,
                                    borderRadius: 8,
                                    p: 2,
                                    minWidth: 80,
                                    minHeight: 160,
                                    alignItems: 'center',
                                    textAlign: 'center'
                                }}>
                                    작물 원본 이미지
                                </Box>
                                {/* 확인 버튼 클릭 시 window 창 닫아주는 확인 버튼 */}
                                <Box>
                                    <Button variant='contained' color='button_color' onClick={handleClose}
                                            sx={{minWidth: 350, p: 1, marginTop: 1, alignItems: 'center'}}>확인</Button>
                                </Box>
                            </Container>
                        </Modal>
                    </Box>
                </Box>

            </Container>
            {/* 아래 여백 용 box */}

            {/* Navigation */}
            <SimpleBottomNavigation/>
        </ThemeProvider>
    );
};

export default Home;