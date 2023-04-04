import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1676035524 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    from scipy.stats import chi2
    return np.sqrt(np.sum(x ** 2) / 45 / chi2.ppf((1 + p) / 2, x.shape[0])), np.sqrt(np.sum(x ** 2) / 45 / chi2.ppf((1 - p) / 2, x.shape[0]))
