from collections import deque

import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import Adam


class Agent:
    def __init__(self, state_size, action_size, load_models=False, actor_model_file='', critic_model_file=''):
        # Initialize neural network properties
        self.state_size = state_size
        self.action_size = action_size
        self.value_size = 1
        self.layer_size = 16
        # Hyper parameters for learning
        self.discount_factor = 0.99
        self.actor_learning_rate = 0.0005
        self.critic_learning_rate = 0.005
        self.memory = deque(maxlen=1000)
        # Create actor and critic neural networks
        self.actor = self.build_actor()
        self.critic = self.build_critic()
        if load_models:
            if actor_model_file:
                self.actor.load_weights(actor_model_file)
            if critic_model_file:
                self.critic.load_weights(critic_model_file)

    # The actor takes a state and outputs probabilities of each possible action
    def build_actor(self):
        layer1 = Dense(self.layer_size, input_dim=self.state_size, activation='relu', kernel_initializer='he_uniform')
        layer2 = Dense(self.layer_size, input_dim=self.layer_size, activation='relu', kernel_initializer='he_uniform')
        # Use softmax activation so that the sum of probabilities of the actions becomes 1
        layer3 = Dense(self.action_size, activation='softmax', kernel_initializer='he_uniform')
        actor = Sequential(layers=[layer1, layer2, layer3])
        # Print a summary of the network
        actor.summary()
        # We use categorical cross-entropy loss since we have a probability distribution
        actor.compile(loss='categorical_crossentropy', optimizer=Adam(lr=self.actor_learning_rate))
        return actor

    # The critic takes a state and outputs the predicted value of the state
    def build_critic(self):
        layer1 = Dense(self.layer_size, input_dim=self.state_size, activation='relu', kernel_initializer='he_uniform')
        layer2 = Dense(self.layer_size, input_dim=self.layer_size, activation='relu', kernel_initializer='he_uniform')
        layer3 = Dense(self.value_size, activation='linear', kernel_initializer='he_uniform')
        critic = Sequential(layers=[layer1, layer2, layer3])
        # Print a summary of the network
        critic.summary()
        critic.compile(loss='mean_squared_error', optimizer=Adam(lr=self.critic_learning_rate))
        return critic

    def act(self, state):
        # Get probabilities for each action
        policy = self.actor.predict(state, batch_size=1).flatten()
        # Return the action with the highest probability
        return np.argmax(policy)

    def exp_replay(self, batch_size):
        mini_batch = []
        l = len(self.memory)
        for i in range(l - batch_size + 1, l):
            mini_batch.append(self.memory.popleft())

        for state, action, reward, next_state, done in mini_batch:
            previous_state = state
            current_state = next_state

            # Make predictions of the value using the critic
            predicted_value_previous_state = self.critic.predict(previous_state)[0]
            predicted_value_current_state = self.critic.predict(current_state)[0] if not done else 0.

            # Estimate the 'real' value as the reward + the (discounted) predicted value of the current state
            real_previous_value = reward + self.discount_factor * predicted_value_current_state

            # The advantage is the difference between what we got and what we predicted
            # - put it in the 'slot' of the current action
            advantages = np.zeros((1, self.action_size))
            advantages[0][action] = real_previous_value - predicted_value_previous_state

            # Train the actor and the critic
            self.actor.fit(previous_state, advantages, epochs=1, verbose=0)
            self.critic.fit(previous_state, reshape(real_previous_value), epochs=1, verbose=0)


# Reshape array for input into keras
def reshape(state):
    return np.reshape(state, (1, -1))
