import pandas as pd
import numpy as np
import math


#Este modelo es el más sencillo pq llevo haciendo cosas jodidas toda la tarde de ayer y toda la mañana y no llego a nada 
# Te asignan un ranking según tu participación en el mercado(valor*acciones). Si quedas mejor en el ranking de la jornada
# de lo que se esperaba subes, y sino bajas.
#Esto tiene 2 problemas, el que más participación en el mercado tiene nunca sube, y se pueden llegar a valores negativos.
# Lo primero se puede corregir dando bonus al equipo de la semana o algo así, que se puede hacer pq según está programado, el valor del mercado va bajando,
#  así que esa diferencia se puede meter al mejor jugador de la semana /equipo de la semana,...


#Tareas pendientes:

#1. Hacer pruebas con más jugadores


#BACKLOG:
# 1. Capar que pueda haber valores negativos, pero perjudicar el precio del de rnk esperado último si queda último.


def update_player_values(df, bid_col='bids',score_col='score', value_col='current_value'):
    """
    Update player values based on scores while maintaining total market value.
    
    Parameters:
    - df: DataFrame containing player data
    - score_col: Column name for player scores
    - value_col: Column name for current player values
    
    Returns:
    - DataFrame with updated values
    """
    
    initial_market_value = np.sum(df[value_col])
    print("Valor inicial del mercado",initial_market_value)    
    
    print(df)
    
    c_subida=0.045*initial_market_value#Controla cuanto varían los precios de los jugadores e cada iteración
    c_bajada=.05*initial_market_value
    
    df['ranking_esperado']=pd.Series([v*b for v,b in zip(df[value_col],df[bid_col])]).rank(ascending=False)
    df['ranking']=df[score_col].rank(ascending=False)
    

    changes = [c_bajada * (re-r) if r > re else c_subida * ( re-r) for r, re in zip(df['ranking'], df['ranking_esperado'])]
    df['changes']=changes
    
    new_values=[v+c for v,c in zip(df[value_col],changes)]

    df[value_col]=new_values
    
    
    # Create result DataFrame
    
    final_market_value=sum(df[value_col])
    #Si el jugador que se esperaba que quedase primero, queda primero, se le da un bonus tal que el valor de mercado queda constante
    market_value_difference = initial_market_value - final_market_value
    if market_value_difference > 0:  # Only distribute if there's a positive difference
        first_place_bonus = market_value_difference
        # Find players who maintained their expected first position
        first_place_mask = (df['ranking_esperado'] == 1) & (df['ranking'] == 1)
        
        print(first_place_mask.sum())
        if first_place_mask.any():
            # Add the bonus to all players who maintained first place
            df.loc[first_place_mask, value_col] += first_place_bonus / first_place_mask.sum()
            df.loc[first_place_mask,'changes']+=first_place_bonus


    result_df = df.copy()

    print("Valor final del mercado:",df[value_col].sum())
    return result_df

# Example usage:
if __name__ == "__main__":
    
    data = {
        'player': ['Player1', 'Player2', 'Player3', 'Player4'],
        'bids' : [100,100,100,50],
        'score': [2.0, 3.5, 6.0, 10.5],
        'current_value': [1, 0.5, 5, 30]
    }
    
    df = pd.DataFrame(data)
    updated_df = update_player_values(df)
    print(updated_df)