import { useEffect,useState } from 'react';
import './InvestPage.css';








function InvestPage(
    myUser
) {
    
    let [myPlayers,setMyPlayers]=useState()
    let user=myUser.myUser//Al pasarlo como un argumento de una función pasa de ser un elemento de la clase Player, a ser un objeto {myUser:myUser,type:Object} 
    //Fetch my user data
    useEffect(()=>{//Hay que meter esto en useEffect, pq sino la app se renderiza de nuevo cada vez que el valor de una variable cambai, y se entra en un bucle infinito
        async function fetchData(){
            
            //Fetch players my user has bidded on data
            
            let playersData=await fetch('http://localhost:5000/players')
            let playersResponse=await playersData.json()
            setMyPlayers(playersResponse.filter(
                player => Object.keys(user.players_bids || {}).includes(String(player.player_id))
             ))
        }
        fetchData()
        
       
        

    },[])

    if(myUser && myPlayers){
        console.log("MyUSER:",myUser)
        console.log("MyPlayers:",myPlayers)
    


    
    

    
    return (
        <div className="invest-container">
            <h1 className="invest-header">My Investments</h1>
            <h1 className="money-header">{user.user_name}: {myUser?.money || 0}€</h1>
            <table className="invest-table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Team</th>
                        <th>Previous Scores</th>
                        <th>Invested Money</th>
                        <th>Value</th>
                        <th>Expected Score</th>
                    </tr>
                </thead>
                <tbody>
                    {myPlayers.map((player, index) => (
                    <tr key={player.id || index}>
                        <td>{player.player_name}</td>
                        <td>{player.team}</td>
                        <td>{player.prev_scores}</td>
                        <td>{user.players_bids[player.player_id]}</td>
                        <td>{player.value}</td>
                        <td>{player.expected_score}</td>

                    </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}
}
export default InvestPage;