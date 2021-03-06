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
        if (prop.state === '???') {
            <Icon path={mdiWeatherRainy}
                  title="???"
                  size={3}
                  sx={{margin: 0.5}}
            />
        } else if (prop.state === '???/???') {
            <Icon path={mdiWeatherSnowyRainy}
                  title="???/???"
                  size={3}
                  sx={{margin: 0.5}}
            />
        } else if (prop.state === '???') {
            <Icon path={mdiWeatherSnowyHeavy}
                  title="???"
                  size={3}
                  sx={{margin: 0.5}}
            />
        } else if (prop.state === '?????????') {
            <Icon path={mdiWeatherPouring}
                  title="?????????"
                  size={3}
                  sx={{margin: 0.5}}
            />
        } else {
            <Icon path={mdiWhiteBalanceSunny}
                  title="??????"
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
                    {/*    Logo ?????? ??????*/}
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
                                sx={{color: 'text.darker', textAlign: 'center', p: 1, marginBottom: 1.5}}>????????????
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
                                                    sx={{color: 'text.darker'}}> {weather.temperature}???

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
                                      title="??????"
                                      size={3}
                                      sx={{margin: 0.5}}
                                />
                                <br/>
                                <Typography variant="h5"
                                            sx={{color: 'text.darker'}}> {weather.state}
                                </Typography>
                            </Box>
                        </Stack>
                        {/*  ?????? API ??????  */}
                    </Box>

                    <Box sx={{p: 2, textAlign: 'center'}}>
                        <Typography variant='h5'>?????????????????? : ??????</Typography>
                    </Box>

                    <Divider variant="middle"/>

                    <Box sx={{p: 0.5}}>
                        <Box sx={{width: '100%'}}>
                            <Stack>
                                <Typography variant="p"
                                            sx={{color: 'text.darker', p: 1}}>???????????? ??????
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
                                                        sx={{color: 'text.darker'}}>??????
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
                                                        sx={{color: 'text.darker'}}>??????
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
                                        onClick={handleOpen}>????????? ?????? ??????</Button>
                            </Stack>

                        </Box>

                        {/* ????????? ?????? ?????? ?????? ?????? ??? ???????????? ?????? Modal???????????? ??????*/}
                        <Modal
                            open={open}
                            onClose={handleClose}
                            aria-labelledby="modal-modal-title"
                            aria-describedby="modal-modal-description"
                        >
                            <Container sx={style}>
                                <Box sx={{textAlign: 'center'}}>
                                    <h1>???????????????</h1>
                                    <Box>
                                        <FormControl>
                                            <InputLabel id="demo-simple-select-label">Camera</InputLabel>
                                            <Stack direction="row" spacing={2}>
                                                {/* ?????? ?????? Select Box ?????? */}
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
                                                    {/* ???????????? ????????? ?????? */}
                                                    <Button>
                                                        <CachedOutlinedIcon fontSize='large'/>
                                                    </Button>
                                                </Box>
                                            </Stack>
                                        </FormControl>
                                    </Box>
                                </Box>
                                {/* ?????? ????????? ???????????? ?????? */}
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
                                    ?????? ?????? ?????????
                                </Box>
                                {/* ?????? ?????? ?????? ??? window ??? ???????????? ?????? ?????? */}
                                <Box>
                                    <Button variant='contained' color='button_color' onClick={handleClose}
                                            sx={{minWidth: 350, p: 1, marginTop: 1, alignItems: 'center'}}>??????</Button>
                                </Box>
                            </Container>
                        </Modal>
                    </Box>
                </Box>

            </Container>
            {/* ?????? ?????? ??? box */}

            {/* Navigation */}
            <SimpleBottomNavigation/>
        </ThemeProvider>
    );
};

export default Home;