def rps_game_winner(args):
    if len(args) > 2:
        raise Exception('WrongNumberOfPlayersError')
    for i in args:
        if i[1] not in ['P', 'R', 'S']:
            raise Exception('NoSuchStrategyError')
    if args[0][1] == args[1][1] or args[0][1] + args[1][1] in ['PR', 'RS', 'SP']:
        return f"{args[0][0]} {args[0][1]}"
    else:
        return f"{args[1][0]} {args[1][1]}"