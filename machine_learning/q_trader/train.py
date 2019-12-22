from machine_learning.alpha.alpha_file import AlphaFile
from machine_learning.q_trader.agent import Agent
from machine_learning.q_trader.functions import *

stock_name = "MSFT"
window_size = 10
epoch_count = 1000

agent = Agent(window_size, action_size=3)
data = format_alpha_data(AlphaFile(stock_name).read_datapoints_from_csv())
data_size = len(data) - 1
batch_size = 32

for e in range(epoch_count + 1):
    print("Episode ", e, "/", epoch_count)
    state = get_state(data, 0, window_size + 1)

    total_profit = 0
    agent.inventory = []

    for t in range(data_size):
        # Get best action based on policy
        action = agent.act(state)
        # Get the previous 10 days of price history
        next_state = get_state(data, t + 1, window_size + 1)
        # Initialize our reward as zero
        reward = 0
        # Action 1 = BUY
        if action == 1 and len(agent.inventory) == 0:
            agent.inventory.append(data[t][0])
        # Action 2 = SELL
        elif action == 2 and len(agent.inventory) > 0:
            bought_price = agent.inventory.pop(0)
            reward = data[t][0] - bought_price
            total_profit += data[t][0] - bought_price
        # Check if we are at the last datapoint
        done = True if t == data_size - 1 else False
        if done:
            # Sell Remaining Shares
            while len(agent.inventory) > 0:
                bought_price = agent.inventory.pop(0)
                reward = data[t][0] - bought_price
                total_profit += data[t][0] - bought_price
            print("--------------------------------")
            print("Total Profit: " + formatPrice(total_profit))
            print("--------------------------------")
        # Add the current frame to memory
        agent.memory.append((state, action, reward, next_state, done))
        # Transition to the next state
        state = next_state
        # If memory is getting full, train the actor and critic nn
        # Calculate Q-Values, Update Q-Table, and clear memory
        if len(agent.memory) > batch_size:
            agent.exp_replay(batch_size)

    if e % 10 == 0:
        agent.actor.save("models/" + stock_name + "_model_ep" + str(e) + ".hdf5")
        agent.actor.save("models/" + stock_name + "_model_ep" + str(e) + ".hdf5")
