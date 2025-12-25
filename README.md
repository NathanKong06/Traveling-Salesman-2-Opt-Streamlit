# Traveling Salesman Problem (TSP) with 2-Opt and Streamlit Visualization

This project provides an interactive visualization of the Traveling Salesman Problem (TSP) solved using the 2-Opt heuristic. The solver runs with a fixed number of restarts, and the Streamlit app displays a live animated visualization of the optimization process.

<https://tsp-2-opt.streamlit.app>

## Features

- Generate random points representing cities.
- Solve TSP using 2-Opt with multiple restarts.
- Live visualization of the current tour during optimization.
- Animation effects with arrows indicating the direction of the tour.
- Adjustable visualization speed via a slider.
- Sidebar metrics showing current tour length and best tour length.
- Final best tour highlighted in purple with a thicker line.

## Usage

Run the Streamlit app:

```bash
streamlit run main.py
```

### Controls

- **Number of cities:** Choose how many cities to generate (10 to 300).
- **Max restarts:** Set the fixed number of restarts for the 2-Opt solver.
- **Seed:** Optional seed for reproducible random city generation.
- **Visualization speed:** Adjust the delay between animation frames (seconds).
- **Run solver:** Start the solver and watch the live visualization.

## How It Works

- The app generates random city coordinates based on the seed.
- The 2-Opt solver runs with a fixed number of restarts.
- After each iteration, the current tour is drawn with arrows showing the tour direction.
- The sidebar displays real-time metrics for the current tour length and the best tour length found so far.
- The final best tour is displayed in purple with a thicker line to highlight it.

## Additional Information

- Logic is adapted from <https://github.com/NathanKong06/Traveling-Salesman-2-Opt-Anytime-Algorithm/tree/main>
