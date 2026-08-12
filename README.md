# AI Agent: Logical OR Perceptron

Welcome to **shreyas-s-first-repo**! This repository contains a foundational Python script that demonstrates how a basic Artificial Intelligence agent learns using a single-layer perceptron model.

## 📌 Project Overview

The code trains a simple AI agent to understand and replicate the **Logical OR** operation. It does this entirely from scratch without using external machine learning libraries like TensorFlow or PyTorch. 

The AI learns by adjusting its internal "weights" and "bias" over a series of training epochs until it can perfectly predict the correct outputs based on the provided inputs.

## ⚙️ How It Works

* **The Environment:** The agent is fed a truth table for the Logical OR operation (Inputs: `[0,0], [0,1], [1,0], [1,1]`).
* **The Brain:** It uses randomized initial weights and a bias.
* **Activation Function:** A basic binary `step_function` determines if the artificial neuron "fires" (returns 1) or stays dormant (returns 0).
* **The Learning Loop:** The agent iterates through the data up to 20 times (epochs). It calculates its error rate and updates its weights using a learning rate of `0.1` until the total error reaches zero.

## 🚀 How to Run the Code

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/shreyasbolake10-boop/shreyas-s-first-repo.git](https://github.com/shreyasbolake10-boop/shreyas-s-first-repo.git)

