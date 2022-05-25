import React from 'react';
import GrowthInfo from "./GrowthInfo";
import DamageInfo from "./DamageInfo";
import Button from "@mui/material/Button";
import Modal from "@mui/material/Modal";
import Box from "@mui/material/Box";

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


function CropInfo(props) {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    return (
        <div>
            <GrowthInfo />
            <br />
            <DamageInfo />
            <Button onClick={handleOpen}>작물확인</Button>
                <Modal
                    open={open}
                    onClose={handleClose}
                    aria-labelledby="modal-modal-title"
                    aria-describedby="modal-modal-description"
                >
                    <Box sx={style}>
                        작물 Image!!!!
                    </Box>

                </Modal>
        </div>
    );
}

export default CropInfo;