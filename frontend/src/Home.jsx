import React,{useState,useEffect} from 'react';
import axios from 'axios';

const Home = () => {

  const [username,setUsername] = useState(null);

  const instance = axios.create({
    baseURL : 'https://localhost:8000/',
    withCredentials : true
  })
    useEffect(() => {
    instance.get().then((data) => setUsername(data.data.msg))
    });

    const logoutFunc = () => {
      window.location.href = 'https://localhost:8000/accounts/logout/'
    }
  return (
    <>
    <div>Home</div>
    <h2>{username && username}</h2>
    <button onClick={logoutFunc}>Logout</button>
    </>
  )
}

export default Home