# Sample user-item ratings matrix 
# Rows: Users, Columns: Items
# Example: Ratings matrix for movies
ratings = {
    'User1': {'Movie1': 5, 'Movie2': 4, 'Movie3': 0, 'Movie4': 1},
    'User2': {'Movie1': 0, 'Movie2': 5, 'Movie3': 4, 'Movie4': 2},
    'User3': {'Movie1': 4, 'Movie2': 0, 'Movie3': 0, 'Movie4': 5},
    'User4': {'Movie1': 1, 'Movie2': 2, 'Movie3': 4, 'Movie4': 0},
}

# Function to calculate similarity between users based on ratings
def calculate_similarity(user1, user2):
    common_items = [item for item in ratings[user1] if item in ratings[user2]]
    if len(common_items) == 0:
        return 0  # No common items, similarity is 0
    
    sum_of_squares = sum((ratings[user1][item] - ratings[user2][item]) ** 2 for item in common_items)
    return 1 / (1 + sum_of_squares)  # Similarity score based on Euclidean distance

# Function to recommend items to a target user
def recommend_items(target_user):
    # Calculate similarity between the target user and other users
    similarities = {other_user: calculate_similarity(target_user, other_user) for other_user in ratings if other_user != target_user}
    
    # Sort users by similarity in descending order
    sorted_users = sorted(similarities, key=similarities.get, reverse=True)
    
    # Create a dictionary to store recommended items and their scores
    recommended_items = {}
    
    # Iterate through other users to find items to recommend
    for other_user in sorted_users:
        for item in ratings[other_user]:
            # Recommend items not rated by the target user and with high similarity users' ratings
            if item not in ratings[target_user] or ratings[target_user][item] == 0:
                if item not in recommended_items:
                    recommended_items[item] = 0
                recommended_items[item] += ratings[other_user][item] * similarities[other_user]
    
    # Sort recommended items by their scores in descending order
    recommended_items = sorted(recommended_items, key=recommended_items.get, reverse=True)
    
    return recommended_items

# Example usage: Recommend items to 'User1'
target_user = 'User4'
recommended_items = recommend_items(target_user)

print(f"Recommended items for {target_user}: {recommended_items}")
