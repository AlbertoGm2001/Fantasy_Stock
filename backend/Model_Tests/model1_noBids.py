import pandas as pd
import numpy as np
import math


#Este modelo no contempla que el nº de acciones compradas para cada jugador puede ser distinto.
# Asume que solo se puede comprar un nº n de acciones para cada jugador, y que todas esas acciones están compradas. 
# 
# Lo que se hace es calcular una variable que sea la puntuación de cada jugador por su valor
# (tanto puntuaciones como valores en % de lo que ocupan en el mercado)
# Se calcula la media de esa variable, y los jugadores con el valor de esa variable por encima de la media 
# subirán su precio más cuanto más alejados de la media estén, y multplicado por una constante.

# ESTE MODELO NO FUNCIONA COMO QUERRÍA CON LAS FÓRMULAS PARA CALCULAR Z QUE HE PROBADO.

def update_player_values(df, score_col='score', value_col='current_value'):
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
    
    c=0.05*initial_market_value#Controla cuanto varían los precios de los jugadores e cada iteración

    scaled_scores=[elem/sum(df[score_col]) for elem in df[score_col]]

    scaled_values=[elem/sum(df[value_col]) for elem in df[value_col]]
    
    Z=[p*(v) for p,v in zip(scaled_scores,scaled_values)]
    
    avg_Z=sum(Z)/len(Z)

    changes=[c*(z-avg_Z) for z in Z]

    new_values=[v+c for v,c in zip(df[value_col],changes)]

    df[value_col]=new_values
    
    
    # Create result DataFrame
    result_df = df.copy()
    
    final_market_value=sum(df[value_col])
    print("Valor final del mercado:",final_market_value)
    

    return result_df

# Example usage:
if __name__ == "__main__":
    # Create sample data
    data = {
        'player': ['Player1', 'Player2', 'Player3', 'Player4'],
        'score': [9.0, 7.5, 6.0, 10.5],
        'current_value': [10, 20, 5, 30]
    }
    
    df = pd.DataFrame(data)
    updated_df = update_player_values(df)
    print(updated_df)