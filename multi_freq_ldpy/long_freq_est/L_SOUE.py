import numpy as np
from pure_frequency_oracles.UE import UE_Client

def L_SOUE_Client(input_data, k, eps_perm, eps_1):
    # SUE parameters
    p1 = np.exp(eps_perm / 2) / (np.exp(eps_perm / 2) + 1)
    q1 = 1 - p1

    # OUE parameters
    p2 = 0.5
    q2 = (3.35410196624968 * (np.exp(eps_1) - 1) * (
                np.exp(0.5 * eps_perm) + 2 * np.exp(eps_perm) + np.exp(1.5 * eps_perm)) * np.sqrt(
        0.0111111111111111 * np.exp(eps_1) + 0.00555555555555556 * np.exp(2 * eps_1) + 0.0444444444444444 * np.exp(
            0.5 * eps_perm) + 0.155555555555556 * np.exp(eps_perm) + 0.311111111111111 * np.exp(
            1.5 * eps_perm) + 0.388888888888889 * np.exp(2 * eps_perm) + 0.311111111111111 * np.exp(
            2.5 * eps_perm) + 0.155555555555556 * np.exp(3 * eps_perm) + 0.0444444444444444 * np.exp(
            3.5 * eps_perm) + 0.00555555555555556 * np.exp(4 * eps_perm) - 0.222222222222222 * np.exp(
            eps_1 + eps_perm) - 0.711111111111111 * np.exp(eps_1 + 1.5 * eps_perm) - np.exp(
            eps_1 + 2 * eps_perm) - 0.711111111111111 * np.exp(eps_1 + 2.5 * eps_perm) - 0.222222222222222 * np.exp(
            eps_1 + 3 * eps_perm) + 0.0111111111111111 * np.exp(eps_1 + 4 * eps_perm) + 0.0444444444444444 * np.exp(
            2 * eps_1 + 0.5 * eps_perm) + 0.155555555555556 * np.exp(2 * eps_1 + eps_perm) + 0.311111111111111 * np.exp(
            2 * eps_1 + 1.5 * eps_perm) + 0.388888888888889 * np.exp(
            2 * eps_1 + 2 * eps_perm) + 0.311111111111111 * np.exp(
            2 * eps_1 + 2.5 * eps_perm) + 0.155555555555556 * np.exp(
            2 * eps_1 + 3 * eps_perm) + 0.0444444444444444 * np.exp(
            2 * eps_1 + 3.5 * eps_perm) + 0.00555555555555556 * np.exp(
            2 * eps_1 + 4 * eps_perm) + 0.00555555555555556) - 0.25 * (
                      np.exp(0.5 * eps_perm) + 2 * np.exp(eps_perm) + np.exp(1.5 * eps_perm) - np.exp(
                  eps_1 + 0.5 * eps_perm) - 2 * np.exp(eps_1 + eps_perm) - np.exp(eps_1 + 1.5 * eps_perm)) * (
                      np.exp(eps_1) + 4 * np.exp(0.5 * eps_perm) + 4 * np.exp(eps_perm) - np.exp(
                  2 * eps_perm) - 4 * np.exp(eps_1 + eps_perm) - 4 * np.exp(eps_1 + 1.5 * eps_perm) - np.exp(
                  eps_1 + 2 * eps_perm) + 1)) / (
                     (np.exp(eps_1) - 1) * (np.exp(0.5 * eps_perm) + 2 * np.exp(eps_perm) + np.exp(1.5 * eps_perm)) * (
                         np.exp(0.5 * eps_perm) + 2 * np.exp(eps_perm) + np.exp(1.5 * eps_perm) - np.exp(
                     eps_1 + 0.5 * eps_perm) - 2 * np.exp(eps_1 + eps_perm) - np.exp(eps_1 + 1.5 * eps_perm)))

    if (np.array([p1, q1, p2, q2]) >= 0).all():
        pass
    else:
        raise ValueError('Probabilities are negative.')

    # Unary encoding
    input_ue_data = np.zeros(k)

    if input_data != None:
        input_ue_data[input_data] = 1

    first_sanitization = np.zeros(k)
    for ind in range(k):
        if input_ue_data[ind] != 1:
            rnd = np.random.random()
            if rnd <= q1:
                first_sanitization[ind] = 1
        else:
            rnd = np.random.random()
            if rnd <= p1:
                first_sanitization[ind] = 1

    second_sanitization = np.zeros(k)
    for ind in range(k):
        if first_sanitization[ind] != 1:
            rnd = np.random.random()
            if rnd <= q2:
                second_sanitization[ind] = 1
        else:
            rnd = np.random.random()
            if rnd <= p2:
                second_sanitization[ind] = 1

    return second_sanitization


def L_SOUE_Aggregator(ue_reports, eps_perm, eps_1):
    n = len(ue_reports)

    # SUE parameters
    p1 = np.exp(eps_perm / 2) / (np.exp(eps_perm / 2) + 1)
    q1 = 1 - p1

    # OUE parameters
    p2 = 0.5
    q2 = (3.35410196624968 * (np.exp(eps_1) - 1) * (
            np.exp(0.5 * eps_perm) + 2 * np.exp(eps_perm) + np.exp(1.5 * eps_perm)) * np.sqrt(
        0.0111111111111111 * np.exp(eps_1) + 0.00555555555555556 * np.exp(2 * eps_1) + 0.0444444444444444 * np.exp(
            0.5 * eps_perm) + 0.155555555555556 * np.exp(eps_perm) + 0.311111111111111 * np.exp(
            1.5 * eps_perm) + 0.388888888888889 * np.exp(2 * eps_perm) + 0.311111111111111 * np.exp(
            2.5 * eps_perm) + 0.155555555555556 * np.exp(3 * eps_perm) + 0.0444444444444444 * np.exp(
            3.5 * eps_perm) + 0.00555555555555556 * np.exp(4 * eps_perm) - 0.222222222222222 * np.exp(
            eps_1 + eps_perm) - 0.711111111111111 * np.exp(eps_1 + 1.5 * eps_perm) - np.exp(
            eps_1 + 2 * eps_perm) - 0.711111111111111 * np.exp(eps_1 + 2.5 * eps_perm) - 0.222222222222222 * np.exp(
            eps_1 + 3 * eps_perm) + 0.0111111111111111 * np.exp(eps_1 + 4 * eps_perm) + 0.0444444444444444 * np.exp(
            2 * eps_1 + 0.5 * eps_perm) + 0.155555555555556 * np.exp(2 * eps_1 + eps_perm) + 0.311111111111111 * np.exp(
            2 * eps_1 + 1.5 * eps_perm) + 0.388888888888889 * np.exp(
            2 * eps_1 + 2 * eps_perm) + 0.311111111111111 * np.exp(
            2 * eps_1 + 2.5 * eps_perm) + 0.155555555555556 * np.exp(
            2 * eps_1 + 3 * eps_perm) + 0.0444444444444444 * np.exp(
            2 * eps_1 + 3.5 * eps_perm) + 0.00555555555555556 * np.exp(
            2 * eps_1 + 4 * eps_perm) + 0.00555555555555556) - 0.25 * (
                  np.exp(0.5 * eps_perm) + 2 * np.exp(eps_perm) + np.exp(1.5 * eps_perm) - np.exp(
              eps_1 + 0.5 * eps_perm) - 2 * np.exp(eps_1 + eps_perm) - np.exp(eps_1 + 1.5 * eps_perm)) * (
                  np.exp(eps_1) + 4 * np.exp(0.5 * eps_perm) + 4 * np.exp(eps_perm) - np.exp(
              2 * eps_perm) - 4 * np.exp(eps_1 + eps_perm) - 4 * np.exp(eps_1 + 1.5 * eps_perm) - np.exp(
              eps_1 + 2 * eps_perm) + 1)) / (
                 (np.exp(eps_1) - 1) * (np.exp(0.5 * eps_perm) + 2 * np.exp(eps_perm) + np.exp(1.5 * eps_perm)) * (
                 np.exp(0.5 * eps_perm) + 2 * np.exp(eps_perm) + np.exp(1.5 * eps_perm) - np.exp(
             eps_1 + 0.5 * eps_perm) - 2 * np.exp(eps_1 + eps_perm) - np.exp(eps_1 + 1.5 * eps_perm)))

    if (np.array([p1, q1, p2, q2]) >= 0).all():
        pass
    else:
        raise ValueError('Probabilities are negative.')

    est_freq = ((sum(ue_reports) - n * q1 * (p2 - q2) - n * q2) / (n * (p1 - q1) * (p2 - q2))).clip(0)

    norm_est_freq = est_freq / sum(est_freq)  # re-normalized estimated frequency

    return norm_est_freq