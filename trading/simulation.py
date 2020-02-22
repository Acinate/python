from random import randint


def sim1(capital, max_trades, max_risk, max_reward):
    trades = 0
    winners = 0
    losers = 0
    while trades < max_trades:
        trades += 1
        outcome = randint(0, 1)
        if outcome == 1:
            winners += 1
            gain = randint(0, max_reward * 100)
            capital *= float('1.0' + str(gain))
        else:
            losers += 1
            capital *= (1 - max_risk)
    print('==Simulation Completed==')
    print('Capital: ', capital)
    print('# winners: ', winners)
    print('# losers: ', losers)
    print('\n\n')
    return capital, winners, losers


def sim2():
    capital = 100000
    max_trades = 500
    max_risk = 0.01
    max_reward = 0.04
    simulations = 0

    avg_capital = 0
    avg_winners = 0
    avg_losers = 0
    while simulations < 1000:
        simulations += 1
        results = sim1(capital, max_trades, max_risk, max_reward)
        avg_capital += results[0]
        avg_winners += results[1]
        avg_losers += results[2]

    avg_capital /= simulations
    avg_winners /= simulations
    avg_losers /= simulations
    print('==Simulation Completed==')
    print('Average Capital: ', avg_capital)
    print('Average winners: ', avg_winners)
    print('Average losers: ', avg_losers)
    print('\n\n')


sim2()
