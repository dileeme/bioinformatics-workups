import numpy as np
import matplotlib.pyplot as plt

def smith_waterman(seq1, seq2, match=2, mismatch=-1, gap=-2):
    rows, cols = len(seq1) + 1, len(seq2) + 1
    score_matrix = np.zeros((rows, cols), dtype=int)
    traceback = np.zeros((rows, cols), dtype=int)
    max_score, max_pos = 0, (0, 0)
    
    for i in range(1, rows):
        for j in range(1, cols):
            match_score = match if seq1[i-1] == seq2[j-1] else mismatch
            scores = [
                0,  # we cannot have -ve values
                score_matrix[i-1, j-1] + match_score,  # diagonal
                score_matrix[i-1, j] + gap,  # up
                score_matrix[i, j-1] + gap  # left
            ]
            best_score = max(scores)
            score_matrix[i, j] = best_score
            traceback[i, j] = scores.index(best_score)
            
            if best_score > max_score:
                max_score, max_pos = best_score, (i, j)
    
    return score_matrix, traceback, max_pos

def visualize_matrix(matrix, seq1, seq2, title="Smith-Waterman Score Matrix"):
    plt.figure(figsize=(8, 6))
    plt.imshow(matrix, cmap='coolwarm', interpolation='nearest')
    plt.colorbar(label='Score')
    plt.xticks(np.arange(1, len(seq2) + 1), list(seq2))
    plt.yticks(np.arange(1, len(seq1) + 1), list(seq1))
    plt.xlabel("Sequence 2")
    plt.ylabel("Sequence 1")
    plt.title(title)
    plt.show()

# example
seq1 = "AGTACGCA"
seq2 = "TATGC"
score_matrix, traceback, max_pos = smith_waterman(seq1, seq2)
visualize_matrix(score_matrix, seq1, seq2)
