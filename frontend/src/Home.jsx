import React,{useState,useEffect} from 'react';
import axios from 'axios';

const Home = () => {

    const [userdata,setUserdata] = useState(null);

    const instance = axios.create({
    baseURL : 'https://localhost:8000/',
    withCredentials : true
  })

    const getUserData = () => {
    instance.get().then((data) => setUserdata(data.data))
  }

    useEffect(getUserData,[])
  
    const logoutFunc = () => {
      window.location.href = 'https://localhost:8000/accounts/logout/'
    }

    const renderProfileDetails = () => {
      if(userdata.provider == 'github'){
        return (
          <div>
            <div style={{"display":"flex","justifyContent":"space-around","width":"100vw"}}>
          <img src={userdata.avatar_url} alt="Profile Photo" height="250px" width="250px" style={{"borderRadius":"50%"}}/>
          <h2>{userdata.username}</h2>
            </div>
            <div style={{"textAlign":"center"}}>
          <h2>{userdata.email}</h2>
          <h2>{userdata.html_url}</h2>
            </div>
          
        </div>
      )
    }
    else if(userdata.provider == 'google'){
      return (
        <div>
          <div style={{"display":"flex","justifyContent":"space-around","width":"100vw"}}>
          <img src={userdata.picture} alt="Profile Photo" height="250px" width="250px" style={{"borderRadius":"50%"}}/>
          <h2>{userdata.name}</h2>
          </div>
        </div>
      )
    }
    }
  return (
    <>
    
    <h2>{userdata && renderProfileDetails()}</h2>
    <button onClick={logoutFunc}>Logout</button>
    </>
  )
}

export default Home