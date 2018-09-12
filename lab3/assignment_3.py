import numpy as np

class TrajectoryGenerator:

    def __init__(self, p_i=[0,0,0], p_f=[0,0,0], v_i=[0,0,0], 
        v_f=[0,0,0], a_i=[0,0,0], a_f=[0,0,0]):

        self.update_states()

    # Set starting and ending positions, velocities, and accelerations
    def update_states(self, p_i=[0,0,0], p_f=[0,0,0], v_i=[0,0,0], 
        v_f=[0,0,0], a_i=[0,0,0], a_f=[0,0,0]):

        self.p_i = p_i
        self.p_f = p_f
        self.v_i = v_i
        self.v_f = v_f
        self.a_i = a_i
        self.a_f = a_f

    def solve(self, time=1.0):
        T = time
        A = np.array(
            [[0, 0, 0, 0, 0, 1],
             [T**5, T**4, T**3, T**2, T, 1],
             [0, 0, 0, 0, 1, 0],
             [5*T**4, 4*T**3, 3*T**2, 2*T, 1, 0],
             [0, 0, 0, 2, 0, 0],
             [20*T**3, 12*T**2, 6*T, 2, 0, 0]]
             )
        x = np.array(
            [self.p_i[0], 
             self.p_f[0], 
             self.v_i[0], 
             self.v_f[0], 
             self.a_i[0], 
             self.a_f[0]
             ])

        y = np.array(
            [self.p_i[1], 
             self.p_f[1], 
             self.v_i[1], 
             self.v_f[1], 
             self.a_i[1], 
             self.a_f[1]
             ])

        z = np.array(
            [self.p_i[2], 
             self.p_f[2], 
             self.v_i[2], 
             self.v_f[2], 
             self.a_i[2], 
             self.a_f[2]
             ])

        xCo = np.linalg.solve(A, x)
        yCo = np.linalg.solve(A, y)
        zCo = np.linalg.solve(A, z)
        return xCo, yCo, zCo
