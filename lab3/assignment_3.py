import numpy as np

class TrajectoryGenerator:

    def __init__(self, x_i=0, x_f=0, v_i=0, v_f=0, a_i=0, a_f=0):
        self.update_states()

    # Set starting and ending positions, velocities, and accelerations
    def update_states(self, x_i=0, x_f=0, v_i=0, v_f=0, a_i=0, a_f=0):
        self.x_i = x_i
        self.x_f = x_f
        self.v_i = v_i
        self.v_f = v_f
        self.a_i = a_i
        self.a_f = a_f

    def solve(self):
        A = np.array(
            [[0, 0, 0, 0, 0, 1],
             [T**5, T**4, T**3, T**2, T, 1],
             [0, 0, 0, 0, 1, 0],
             [5*T**4, 4*T**3, 3*T**2, 2*T, 1, 0],
             [0, 0, 0, 2*D, 0, 0],
             [20*T**3, 12*T**2, 6*T, 2*D, 0, 0]]
             )
        b = np.array([x_i, x_f, v_i, v_f, a_i, a_f])

        x = np.linalg.solve(A, b)