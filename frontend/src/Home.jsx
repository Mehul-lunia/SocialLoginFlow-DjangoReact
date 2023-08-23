import React,{useState,useEffect} from 'react';
import axios from 'axios';

const Home = () => {
  const instance = axios.create({
    baseURL : 'https://localhost:8000/',
    withCredentials : true
  })
    useEffect(() => {
    instance.get().then((data) => console.log(data))
    });

    const logoutFunc = () => {
      window.location.href = 'https://localhost:8000/accounts/logout/'
    }
  return (
    <>
    <div>Home</div>
    <button onClick={logoutFunc}>Logout</button>
    </>
  )
}

export default Home