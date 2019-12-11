from alpha.alpha_file import AlphaFile
from q_trader.agent import A2CAgent
from q_trader.functions import *

symbol = "JNUG"
window_size = 10
epoch_count = 1000

agent = A2CAgent(window_size, action_size=3)
data = formatAlphaData(AlphaFile(symbol).read_datapoints_from_csv())
l = len(data) - 1
batch_size = 32

for e in range(epoch_count + 1):
    print("Episode ", e, "/", epoch_count)
    state = getState(data, 0, window_size + 1)

    total_profit = 0
    agent.inventory = []

    for t in range(l):
        action = agent.act(state)

        # hold
        next_state = getState(data, t + 1, window_size + 1)
        reward = 0

        if action == 1:  # buy
            agent.inventory.append(data[t][0])
            # print("Buy: ", formatPrice(data[t][0]))
        elif action == 2 and len(agent.inventory) > 0:  # sell
            bought_price = agent.inventory.pop(0)
            # reward = max(data[t][0] - bought_price, 0)
            reward = data[t][0] - bought_price
            total_profit += data[t][0] - bought_price
            # print("Sell: ", formatPrice(data[t][0]), " | Profit: " + formatPrice(data[t][0] - bought_price))
        done = True if t == l - 1 else False
        agent.memory.append((state, action, reward, next_state, done))
        state = next_state

        if done:
            print("--------------------------------")
            print("Total Profit: " + formatPrice(total_profit))
            print("--------------------------------")

        if len(agent.memory) > batch_size:
            agent.expReplay(batch_size)

    if e % 10 == 0:
        agent.actor.save("models/model_ep" + str(e) + ".hdf5")
        agent.actor.save("models/model_ep" + str(e) + ".hdf5")
