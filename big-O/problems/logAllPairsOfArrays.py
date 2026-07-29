
boxes = ["a","b","c","d","e"]

#   Brut
def log_all_pairs_of_boxes(boxes):
    pairs = []
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            pairs.append((boxes[i],boxes[j]))
    
    return pairs

    # O(n * n) -> O(n^2)

print(log_all_pairs_of_boxes(boxes))