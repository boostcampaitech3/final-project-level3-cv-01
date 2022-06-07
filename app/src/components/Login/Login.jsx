import * as React from 'react';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import axios from "axios"
import { useNavigate } from 'react-router';
const theme = createTheme({
  status: {
    danger: '#064635',
  },
  palette: {
    primary: {
      main: '#064635',
      darker: '#000000',
    },
    neutral: {
      main: '#64748B',
      contrastText: '#fff',
    },
  },
});

export default function Login() {
  
  const [id, setId] = React.useState("");
  const [password, setPassword] = React.useState("")

  const onChangeId = (e) => {
    setId(e.target.value)
  }
  const onChangePassword = (e) => {
    setPassword(e.target.value)
  }
  const navigation = useNavigate()
  React.useEffect(() => {
    console.log(localStorage.getItem('isLoggedIn'))
    if (localStorage.getItem('isLoggedIn') === "true") {
      navigation('/')
    }
  }, [])


  const handleSubmit = (event) => {
    event.preventDefault();
    try {
      axios.post("http://localhost:8000/api/v1/login", {
        id: id,
        password: password,
      }).then((res) => {
        if (res.data.Authorization) {
          localStorage.setItem('isLoggedIn', true)
          navigation('/')
        } else {
          alert("un-authorized")
        }
      })
    } catch {
      alert("data fetch error")
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 30,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >


          <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="id"
              label="아이디를 입력하세요"
              name="id"
              autoComplete="id"
              autoFocus

              onChange={onChangeId}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="비밀번호를 입력하세요"
              type="password"
              id="password"
              onChange={onChangePassword}
              autoComplete="current-password"
            />

            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
              color='primary'
            >
              로그인
            </Button>
            <Grid container>
              <Grid item xs>
                <Link href="#" variant="body2">
                  비밀번호 찾기
                </Link>
              </Grid>
              <Grid item>
                <Link href="#" variant="body2">
                  회원가입
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
      </Container>
    </ThemeProvider>
  );
}