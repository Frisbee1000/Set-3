def relationship_status(from_member, to_member, social_graph):
    follows = to_member in social_graph.get(from_member, {}).get('following', [])
    followed = from_member in social_graph.get(to_member, {}).get('following', [])
    
    if follows and followed:
        return "friends"
    elif follows:
        return "follower"
    elif followed:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(board):
    def check_winner(line):
        
        if len(set(line)) == 1:
            return line[0]
        return None

    n = len(board)
    
    for row in board:
        winner = check_winner(row)
        if winner:
            return winner

    for col in range(n):
        column = [board[row][col] for row in range(n)]
        winner = check_winner(column)
        if winner:
            return winner

    main_diagonal = [board[i][i] for i in range(n)]
    winner = check_winner(main_diagonal)
    if winner:
        return winner

    anti_diagonal = [board[i][n - 1 - i] for i in range(n)]
    winner = check_winner(anti_diagonal)
    if winner:
        return winner

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    total_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        
        for (start, end), leg in route_map.items():
            if start == current_stop:
                total_time += leg['travel_time_mins']
                current_stop = end
                break
        else:
            print("Not possible")

    return total_time
