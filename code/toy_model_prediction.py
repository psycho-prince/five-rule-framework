import numpy as np
import matplotlib.pyplot as plt

def simulate_prediction_error_minimization(
    actual_stimulus_value,
    initial_prediction=0.0,
    learning_rate=0.1,
    num_iterations=50
):
    """
    Simulates a simple system trying to predict a fixed actual stimulus value.
    The internal prediction is updated based on the prediction error over iterations.

    Args:
        actual_stimulus_value (float): The constant value the system is trying to predict.
        initial_prediction (float): The system's starting belief about the stimulus.
        learning_rate (float): How quickly the system updates its prediction based on error.
        num_iterations (int): Number of steps to simulate.

    Returns:
        tuple: (list of predictions, list of errors)
    """
    
    predictions = [initial_prediction]
    errors = []

    current_prediction = initial_prediction

    for i in range(num_iterations):
        # Calculate prediction error
        error = actual_stimulus_value - current_prediction
        errors.append(error)

        # Update the prediction (learning based on error)
        current_prediction += learning_rate * error
        predictions.append(current_prediction)
        
        # Optional: Add some noise to the actual stimulus to make it more realistic
        # actual_stimulus_value += np.random.randn() * 0.05 

    return predictions, errors

if __name__ == "__main__":
    # --- Simulation Parameters ---
    actual_value = 5.0  # The true value the system is trying to predict
    initial_model_prediction = 1.0 # The system's starting guess
    alpha = 0.1 # Learning rate (how fast the model adapts)
    iterations = 100 # How many timesteps

    # --- Run the simulation ---
    model_predictions, prediction_errors = simulate_prediction_error_minimization(
        actual_stimulus_value=actual_value,
        initial_prediction=initial_model_prediction,
        learning_rate=alpha,
        num_iterations=iterations
    )

    # --- Plotting Results ---
    plt.figure(figsize=(12, 6))

    # Plot predictions over time
    plt.subplot(1, 2, 1)
    plt.plot(model_predictions, label="Model's Prediction", color='blue')
    plt.axhline(y=actual_value, color='red', linestyle='--', label="Actual Stimulus Value")
    plt.title(f"Model's Prediction vs. Actual Stimulus (Actual: {actual_value})")
    plt.xlabel("Iteration")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)

    # Plot prediction error over time
    plt.subplot(1, 2, 2)
    plt.plot(prediction_errors, label="Prediction Error", color='green')
    plt.axhline(y=0, color='red', linestyle='--', label="Zero Error")
    plt.title("Prediction Error Over Time")
    plt.xlabel("Iteration")
    plt.ylabel("Error")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    print(f"Final Prediction: {model_predictions[-1]:.2f}")
    print(f"Final Error: {prediction_errors[-1]:.2f}")
