def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k_rec = recommended[:k]
    relevant_set = set(relevant)
    num_rele = len([item for item in top_k_rec if item in relevant_set])

    precision = num_rele / k if k > 0 else 0.0
    recall = num_rele / len(relevant) if len(relevant) > 0 else 0.0

    res = []
    res.append(precision)
    res.append(recall)

    return res