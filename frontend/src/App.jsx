import React from 'react'

const App = () => {

  const facebookLogin = () => {
    window.location.href = 'https://localhost:8000/accounts/login/'
  }
  
  

  return (
    <>
    <button onClick={facebookLogin}>Login</button>
    </>
  )
}

export default App