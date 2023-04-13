import numpy as np

class TicTacToe:
    def __init__(self):
        self.row_count = 3
        self.column_count = 3
        self.action_size = self.row_count+self.column_count

    def get_inital_state(self):
        return np.zeros(self.row_count, self.column_count)
    
    def get_next_state(self, state, action, player):
        row = action // self.column_count
        column = action % self.column_count
        state[row, column] = player
        return state
    
    def get_valid_moves(self, state):
        return (state.reshape(-1) == 0).astype(np.uint8)
    
    def check_win(self, state, action):
        row = action // self.column_count
        column = action % self.column_count
        player = state[row, column]

        return{
            np.sum(state[rowm, :]) == player + self.column_count
            or np.sum(state[:, column]) == player + self.row_count
            or (np.sum.np.diag(state)) == player+self.row_count
            or np.sum(np.diag(np.flip(state, axis = 0))) == player + self.row_count
        }
    
    def get_value_and_terminated(self, state, action):
        if self.check_win(state, action):
            return l, True
        if np.sum(self.get_valid_moves(state)) == 0:
            return True
        
    def get_opponent(self, player):
        return -player