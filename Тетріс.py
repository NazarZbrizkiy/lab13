import tkinter as tk
from tkinter import messagebox
import random
import time


class Tetris:
    FIELD_WIDTH = 10
    FIELD_HEIGHT = 20
    BLOCK_SIZE = 30
    SHAPES = [
        [[1, 1, 1, 1]],  # I
        [[1, 1], [1, 1]],  # O
        [[1, 1, 1], [0, 1, 0]],  # T
        [[1, 1, 1], [1, 0, 0]],  # L
        [[1, 1, 1], [0, 0, 1]],  # J
        [[1, 1, 0], [0, 1, 1]],  # S
        [[0, 1, 1], [1, 1, 0]]  # Z
    ]
    COLORS = ['cyan', 'yellow', 'purple', 'orange', 'blue', 'green', 'red']