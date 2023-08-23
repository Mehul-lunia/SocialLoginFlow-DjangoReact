import React,{useState,useEffect} from 'react';
import axios from 'axios';

const Home = () => {

    useEffect(() => {
    axios.get('https://localhost:8000',
    {
      method : 'GET',
      withCredentials : true
    })
    .then((data) => console.log(data))
    });
  return (
    <div>Home</div>
  )
}

export default Home