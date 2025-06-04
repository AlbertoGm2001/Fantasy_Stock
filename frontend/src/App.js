import './App.css';
import React,{useState,useEffect}from 'react';
import LoginForm from  './LoginForm/LoginForm'
import InvestPage from  './InvestPage/InvestPage'

/*
HECHO:
1.Meter la lógica de Login. Si no me sale, hay una librería que se llama React Auth kit, que lo automatiza 
2. Que se te rediriga a la pg de inversiones después del login
3.Pasar la info de usuario a la página de My Investments
4. Hacer que no haya que logearse cada vez que se refresca la página

POR HACER:
TODO


PASOS:

1. Hacer una página de búsqueda de jugadores


*/



function App() {
    // sessionStorage.clear()
    let [myUser,setMyUser]=useState()//Esto solo se ejecuta en el primer render cuando la variable no existe
    useEffect(()=>{
        
        if (sessionStorage.getItem("myUser")){
            setMyUser(JSON.parse(sessionStorage.getItem("myUser")))
        }
        },[]

    )
    console.log('MyUser:',myUser)
     return (
     
     <div>
         {!myUser ? (

                <LoginForm setMyUser={setMyUser} />
            ) : (
                <InvestPage myUser={myUser}/>
            )}

     </div>
     )
}

export default App;
