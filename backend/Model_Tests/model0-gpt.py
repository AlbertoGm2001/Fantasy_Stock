import pandas as pd
import numpy as np

def update_player_values(df, bid_col='bids', score_col='score', value_col='current_value'):
    """
    Update player values based on scores while maintaining total market value.
    
    Parameters:
    - df: DataFrame containing player data
    - bid_col: Column name for bid amounts
    - score_col: Column name for player scores
    - value_col: Column name for current player values
    
    Returns:
    - DataFrame with updated values
    """
    
    initial_market_value = np.sum(df[bid_col] * df[value_col])
    
#Se calcula una puntuación esperada, de manera que el jugador con el valor más alto tenga un 10(Esto habría que arreglarlo)
    expected_score = df[value_col] / df[value_col].max() * 10  
    
    # Se calcula puntuación - puntuación esperada para cada jugador
    score_diff = df[score_col] - expected_score

    # Se usa la sigmoide para ajustar el valor de cada jugador en función de su puntuación esperada
    adjustment = 1 + (2 / (1 + np.exp(-score_diff))) - 1
    
    new_values = df[value_col] * (1 + adjustment)
    
    # Se escala el ajuste de cada jugador para mantener el valor total del mercado
    scaling_factor = initial_market_value / np.sum(new_values * df[bid_col])
    final_values = new_values * scaling_factor
    
    # Create result DataFrame
    result_df = df.copy()
    result_df[f'new_{value_col}'] = final_values
    
    return result_df

# Example usage:
if __name__ == "__main__":
    # Create sample data
    data = {
        'player': ['Player1', 'Player2', 'Player3', 'Player4'],
        'bids': [100, 200, 150, 300],
        'score': [9.0, 7.5, 6.0, 8.5],
        'current_value': [10, 20, 5, 30]
    }
    
    df = pd.DataFrame(data)
    updated_df = update_player_values(df)
    print(updated_df)