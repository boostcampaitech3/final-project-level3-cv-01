import {Box, Button, ButtonGroup, Stack, Typography} from "@mui/material";
import BugReportOutlinedIcon from "@mui/icons-material/BugReportOutlined";
import CoronavirusOutlinedIcon from "@mui/icons-material/CoronavirusOutlined";
import React from "react";
import {createTheme, ThemeProvider} from "@mui/material/styles";
import {Grid} from "@mui/material"
import LogDetail from "../LogDetail/LogDetail";
import Modal from "@mui/material/Modal";

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

const style = {
    position: 'absolute',
    alignItems: "center",
    justifyContent: "center",
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
};


function LogBox(prop) {

    const date2 = prop.date
    const kind2 = prop.kind

    const [open, setOpen] = React.useState(false);
    const [open2, setOpen2] = React.useState(false)

    const handleOpen = () => setOpen(true);
    const handleOpen2 = () => setOpen2(true);

    const handleClose = () => setOpen(false);
    const handleClose2 = () => setOpen2(false);

    const categoryType = prop.category;
    const buttonBlock = (
        <ButtonGroup variant="outlined" aria-label="outlined button group"
                     sx={{width: '101%', marginLeft: -0.1, marginRight: -0.1}}>
            <Button sx={{
                width: '100%',
                color: 'text.darker',
                borderColor: 'button_color.gray',
                borderRadius: 0,
                borderWidth: 2
            }} onClick={handleOpen}>상세정보</Button>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={style}>
                    <LogDetail date={date2} crop='배추' bug={kind2} handleClose={handleClose}/>
                </Box>
            </Modal>

            <Button sx={{
                width: '100%',
                color: 'text.darker',
                borderColor: 'button_color.gray',
                borderWidth: 2
            }} onClick={handleOpen2}>결과확인</Button>
            <Modal
                open={open2}
                onClose={handleClose2}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={style}>
                    <img src={prop.imageUrl} alt="결과 이미지"/>
                </Box>

            </Modal>

            <Button sx={{
                width: '100%',
                color: 'text.darker',
                borderColor: 'button_color.gray',
                borderRadius: 0,
                borderWidth: 2
            }}>삭제</Button>
        </ButtonGroup>
    );
    if (categoryType === 'bug') {
        return (
            <ThemeProvider theme={theme}>
                <Box sx={{borderColor: 'button_color.gray', borderStyle: 'solid', borderWidth: 4, marginTop: 2}}>
                    <Stack direction='row' spacing={3} sx={{margin: 1}}>
                        <Box>
                            <BugReportOutlinedIcon fontSize='large'
                                                   sx={{textAlign: 'center', marginTop: 1.5, marginLeft: 2}}/>
                        </Box>
                        <Grid container spacing={1}>
                            <Grid item xs={12} sx={{textAlign: 'left', marginLeft: 2}}>
                                <Typography>해충 피해 발생</Typography>
                            </Grid>
                            <Grid item xs={12} sx={{textAlign: 'left', marginLeft: 2}}>
                                <Typography>{date2}</Typography>
                            </Grid>
                        </Grid>
                    </Stack>
                    {buttonBlock}
                </Box>

            </ThemeProvider>
        );
    } else {
        return (
            <ThemeProvider theme={theme}>
                <Box sx={{borderColor: 'button_color.gray', borderStyle: 'solid', borderWidth: 4, marginTop: 2}}>
                    <Stack direction='row' spacing={5} sx={{margin: 1}}>
                        <Box>
                            <CoronavirusOutlinedIcon fontSize='large'
                                                     sx={{textAlign: 'center', marginTop: 1.5, marginLeft: 2}}/>
                        </Box>
                        <Grid container spacing={1}>
                            <Grid item xs={12} sx={{textAlign: 'left', marginLeft: 2}}>
                                <Typography>질병 피해 발생</Typography>
                            </Grid>
                            <Grid item xs={12} sx={{textAlign: 'left', marginLeft: 2}}>
                                <Typography>{date2}</Typography>
                            </Grid>
                        </Grid>
                    </Stack>
                    {buttonBlock}
                </Box>
            </ThemeProvider>
        )
    }
};
export default LogBox;
