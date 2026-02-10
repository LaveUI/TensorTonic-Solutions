import numpy as np

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    x1 = np.asarray(x1, dtype=float)
    x2 = np.asarray(x2, dtype=float)
    dot = np.dot(x1, x2)

    norm = np.linalg.norm(x1) * np.linalg.norm(x2)

    cos_sim = dot / norm if norm != 0 else 0.0

    if label == 1:
        loss= 1 - cos_sim
    elif label == -1:
        loss = max(0.0, cos_sim - margin)
    else:
        raise ValueError("label must be +1 or -1")
    return loss