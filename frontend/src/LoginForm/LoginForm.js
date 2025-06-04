import './LoginForm.css';
import{ useState} from 'react';







function LoginForm({setMyUser}) {
    let [errorMessage,setErrorMessage]=useState();
    let [userName,setUserName]=useState();
    let [password,setPassword]=useState();

    
    async function loginRequest(e){

        e.preventDefault()
        let data= await fetch('http://127.0.0.1:5000/users')

        let response=await data.json()
        let userFound=response.some(user=>(user.user_name===userName && user.password===password))
        
        setErrorMessage(undefined)
        if(!password || !userName){

            setErrorMessage("You must include userName and password")
        }
        
        else if(!userFound){
            setErrorMessage("User not Found")
        }
        else{
            let foundUser=response.find(user=>(user.user_name===userName && user.password===password))

            console.log("MyUser",foundUser)
            setMyUser(foundUser)
            sessionStorage.setItem('myUser',JSON.stringify(foundUser))
            

        }
    }


    return (
        
        
        <div className="login-container">
            {errorMessage && <div className="error-message">{errorMessage}</div>}
            <form className="login-form" onSubmit= {loginRequest}>
                <input 
                    type='text' 
                    name="userName"
                    placeholder='User Name'
                    className="login-input"
                    onChange={(e)=>setUserName(e.target.value)}
                />
                <input 
                    type='password'
                    name="password" 
                    placeholder='Password'
                    className="login-input"
                    onChange={(e)=>setPassword(e.target.value)}
                />     
                <button className="login-button" >Submit</button>
            </form>
        </div>
    );
}

export default LoginForm;