import React from 'react';
import {Box, Typography, FormControl, InputLabel, Select, MenuItem} from "@mui/material";


const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      width: 250,
    },
  },
};

function LogDateBox(props) {
    const boxType = props.type
    const value = props.value

    const handleChange = props.handle

    if (boxType === 'Detail') {
        return (
        <Box>
            <Typography variant="h6" sx={{color: 'text.darker'}}>발생일시 : {props.date}</Typography>
            <br />
            <FormControl fullWidth sx={{color: 'text.darker', borderRadius: 5}} >
                <InputLabel id="demo-simple-select-label" sx={{color: 'text.darker'}}>Time</InputLabel>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={value}
                    label="Time"
                    onChange={handleChange}
                    sx={{color: 'text.darker'}}
                    MenuProps={MenuProps}
                >
                    {props.datetime.map((dt) =>
                        <MenuItem key={dt.id} value={dt.datetime} sx={{pl: 4, color: 'text.darker', borderColor: 'text.darker'}}>
                            {dt.datetime}
                        </MenuItem>
                    )}

                </Select>
            </FormControl>
        </Box>
    );
    } else if (boxType === 'Image') {
        return (
        <Box>
            <Typography variant="h6" sx={{color: 'text.darker'}}>발생일시 : {props.date}</Typography>
            <br />
            <FormControl fullWidth sx={{color: 'text.darker', borderRadius: 5}} >
                <InputLabel id="demo-simple-select-label" sx={{color: 'text.darker'}}>Time</InputLabel>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={value}
                    label="Time"
                    onChange={handleChange}
                    sx={{color: 'text.darker'}}
                    MenuProps={MenuProps}
                >
                    {props.datetime.map((dt) =>
                        <MenuItem key={dt.id} value={dt.image_url} sx={{pl: 4, color: 'text.darker', borderColor: 'text.darker'}}>
                            {dt.datetime}
                        </MenuItem>
                    )}

                </Select>
            </FormControl>
        </Box>
    );
    }
}

export default LogDateBox;