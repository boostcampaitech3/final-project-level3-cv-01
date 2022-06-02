import React from 'react';
import {Box, Typography} from "@mui/material";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";
import ExpandMore from "@mui/icons-material/ExpandMore";
import ExpandLess from "@mui/icons-material/ExpandLess";
import Collapse from "@mui/material/Collapse";
import List from "@mui/material/List";


function LogDateBox(props) {
    console.log(props.datetime,'@')
    const [open, setOpen] = React.useState(true);

    const handleClick = () => {
        setOpen(!open);
    }


    return (
        <Box>
            <Typography variant="h6" sx={{color: 'text.darker'}}>발생일시</Typography>
            <ListItemButton onClick={handleClick}>
                <ListItemText primary={props.date}/>
                {open ? <ExpandMore/> : <ExpandLess/>}
            </ListItemButton>
            <Collapse in={!open} timeout="auto" unmountOnExit>
                <List component="div" disablePadding>
                    {props.datetime.map((dt) =>
                        <ListItemButton sx={{pl: 4}} key={dt.id}>
                            <ListItemText primary={dt.datetime}/>
                        </ListItemButton>
                        )}
                </List>
            </Collapse>
        </Box>
    );
}

export default LogDateBox;