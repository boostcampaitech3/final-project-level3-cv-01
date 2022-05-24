import React from 'react';
import Button from '@mui/material/Button';
import Modal from '@mui/material/Modal';
import Box from '@mui/material/Box';
import LogDetail from "../LogDetail/LogDetail";


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


function CropStateLog(props) {

    const [open, setOpen] = React.useState(false);
    const [open2, setOpen2] = React.useState(false)

    const handleOpen = () => setOpen(true);
    const handleOpen2 = () => setOpen2(true);

    const handleClose = () => setOpen(false);
    const handleClose2 = () => setOpen2(false);
    return (
        <div>
            <h5>해충피해발생</h5>
            <p>날짜!!</p>

            <div>

                <Button onClick={handleOpen}>상세정보</Button>
                <Modal
                    open={open}
                    onClose={handleClose}
                    aria-labelledby="modal-modal-title"
                    aria-describedby="modal-modal-description"
                >
                    <Box sx={style}>
                        <LogDetail/>
                    </Box>

                </Modal>

                <Button onClick={handleOpen2}>결과확인</Button>
                <Modal
                    open={open2}
                    onClose={handleClose2}
                    aria-labelledby="modal-modal-title"
                    aria-describedby="modal-modal-description"
                >
                    <Box sx={style}>
                        작물 Detection 결과 Image!!!
                    </Box>

                </Modal>

                <button>삭제</button>
            </div>
        </div>
    );
}

export default CropStateLog;