import * as React from 'react';
import Paper from '@mui/material/Paper';
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import BorderColor from '@mui/icons-material/Restore';
import Home from '@mui/icons-material/Home';
import Person from '@mui/icons-material/Person';

export default function SimpleBottomNavigation() {
  const [value, setValue] = React.useState(0);

  return (
    <Paper sx={{ position: 'fixed', bottom: 0, left: 0, right: 0 }} elevation={3}>
      <BottomNavigation
        showLabels
        value={value}
        onChange={(event, newValue) => {
          setValue(newValue);
        }}
      >
        <BottomNavigationAction label="Log" icon={<BorderColor />} />
        <BottomNavigationAction label="Home" icon={<Home />} />
        <BottomNavigationAction label="MyPage" icon={<Person />} />
      </BottomNavigation>
    </Paper>
  );
}