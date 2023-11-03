import numpy as np


class rotation_matrix:
    def rotationMatrix(self, degree):
        axis = np.array([0.0, 0.6, 0.4])
        axis = axis / np.linalg.norm(axis)
        radian = degree * np.pi / 180.0
        rotateMat = np.array([
            [axis[0] * axis[0] * (1 - axis[0] * axis[0]) + np.cos(radian),
             axis[0] * axis[1] * (1 - np.cos(radian)) - axis[2] * np.sin(radian),
             axis[0] * axis[2] * (1 - np.cos(radian)) + axis[1] * np.sin(radian), 0.0],
            [axis[0] * axis[1] * (1 - np.cos(radian)) + axis[2] * np.sin(radian),
             axis[1] * axis[1] * (1 - axis[1] * axis[1]) + np.cos(radian),
             axis[1] * axis[2] * (1 - np.cos(radian)) - axis[0] * np.sin(radian), 0.0],
            [axis[0] * axis[2] * (1 - np.cos(radian)) - axis[1] * np.sin(radian),
             axis[1] * axis[2] * (1 - np.cos(radian)) + axis[0] * np.sin(radian),
             axis[2] * axis[2] * (1 - axis[2] * axis[2]) + np.cos(radian), 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ])
        return rotateMat

