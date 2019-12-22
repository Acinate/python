import sys

import matplotlib.pyplot as plt
from keras.models import load_model

from machine_learning.alpha.alpha_file import AlphaFile
from machine_learning.q_trader.agent import Agent
from machine_learning.q_trader.functions import *

if len(sys.argv) != 3:
    print("Usage: python evaluate.py [stock] [model]")
    exit()

stock_name, model_name = sys.argv[1], sys.argv[2]
model_path = "models/" + model_name
model = load_model(model_path)
window_size = model.layers[0].input.shape.as_list()[1]

agent = Agent(window_size, action_size=3, load_models=True, actor_model_file=model_path)
data = format_alpha_data(AlphaFile(stock_name).read_datapoints_from_csv())
data_size = len(data) - 1
batch_size = 32

state = get_state(data, 0, window_size + 1)
total_profit = 0
agent.inventory = []

# Setup our plot
fig, ax = plt.subplots()
plt_index = 0
plt_data = []

# Iterate through all datapoints
for t in range(data_size):
    # Get best action based on policy
    action = agent.act(state)
    # Get the previous 10 days of price history
    next_state = get_state(data, t + 1, window_size + 1)
    # Initialize our reward as zero
    reward = 0

    # Action 0 = HOLD
    if action == 0:
        plt_data.append((plt_index, data[t][0], 0))
    # Action 1 = BUY
    elif action == 1 and len(agent.inventory) == 0:
        agent.inventory.append(data[t][0])
        plt_data.append((plt_index, data[t][0], 1))
    # Action 2 = SELL
    elif action == 2 and len(agent.inventory) > 0:
        bought_price = agent.inventory.pop(0)
        reward = data[t][0] - bought_price
        total_profit += data[t][0] - bought_price
        plt_data.append((plt_index, data[t][0], 2))
    else:
        plt_data.append((plt_index, data[t][0], 0))

    # Increment our index (plotting)
    plt_index += 1
    # Check if we are at the last datapoint
    done = True if t == data_size - 1 else False
    if done:
        # Sell Remaining Shares
        while len(agent.inventory) > 0:
            bought_price = agent.inventory.pop(0)
            reward = data[t][0] - bought_price
            total_profit += data[t][0] - bought_price
        # Show Simulation Results
        print("--------------------------------")
        print(stock_name + " Total Profit: " + formatPrice(total_profit))
        print("--------------------------------")
    # Add Q-Values to Q-Table
    agent.memory.append((state, action, reward, next_state, done))
    # Transition to the next state
    state = next_state
    # If memory is getting full, train the actor and critic nn
    # Then clear recent memory
    if len(agent.memory) > batch_size:
        agent.exp_replay(batch_size)


def get_color(n):
    if n == 0:
        return [0 / 255, 0 / 255, 0 / 255, 0]
    elif n == 1:
        return [0 / 255, 255 / 255, 0 / 255, 1]
    elif n == 2:
        return [255 / 255, 0 / 255, 0 / 255, 1]
    else:
        return get_color(0)


# Plot simulation results
plt_data = np.array(plt_data)
colors = []
for data in plt_data:
    colors.append(get_color(data[2]))
xs, ys = plt_data[:, 0], plt_data[:, 1]
plt.plot(xs, ys, c='black', alpha=0.5)
plt.scatter(xs, ys, c=colors, s=8)
plt.show()
