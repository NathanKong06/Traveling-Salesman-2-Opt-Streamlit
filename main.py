import random
import streamlit as st
import matplotlib.pyplot as plt
import time

from solver import tsp
from geometry import tour_length

def generate_random_points(n, seed=0):
    random.seed(seed)
    return [(random.random(), random.random()) for _ in range(n)]

def draw_tour(points, tour, ax, title, final=False):
    x = [points[i][0] for i in tour] + [points[tour[0]][0]]
    y = [points[i][1] for i in tour] + [points[tour[0]][1]]
    ax.clear()
    linewidth = 1.0 if not final else 1.5
    color = 'tab:blue' if not final else '#800080'
    ax.plot(x, y, marker="o", markersize=12 if final else 10, linestyle="-", linewidth=linewidth, color=color)
    ax.scatter(points[tour[0]][0], points[tour[0]][1], color='red', s=120 if final else 100, zorder=5, label='Start')
    ax.scatter(points[tour[-1]][0], points[tour[-1]][1], color='green', s=120 if final else 100, zorder=5, label='End')
    ax.grid(True, linestyle='--', color='lightgray', alpha=0.3)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax.set_title(title, fontsize=8)
    ax.set_aspect('equal')

def main():
    st.set_page_config(page_title="TSP with 2-Opt Visualization", layout="wide")
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("TSP with 2-Opt Visualization")

    st.sidebar.header("Parameters")
    num_cities = st.sidebar.slider("Number of cities", 10, 300, 50, step=10)
    max_iterations = st.sidebar.number_input(
        "Max restarts", min_value=1, value=10, step=1
    )
    seed_input = st.sidebar.text_input("Seed (optional)", "")
    if seed_input.strip():
        try:
            seed = int(seed_input)
        except ValueError:
            seed = seed_input
    else:
        seed = random.random()

    speed = st.sidebar.slider("Visualization speed (seconds delay)", 0.0, 1.0, 0.0, step=0.01)

    run = st.sidebar.button("Run solver")

    if not run:
        st.info("Set parameters and click **Run solver**.")
        return

    points = generate_random_points(num_cities, seed=seed)

    _,col_plot,_ = st.columns([1, 3, 1])

    with col_plot:
        plot_placeholder = st.empty()
        plot_placeholder.empty()
        fig, ax = plt.subplots(figsize=(5, 4.5), dpi=100)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        plot_placeholder.pyplot(fig)

    best_length = float("inf")
    best_tour = None

    progress_bar = st.progress(0)
    status = st.empty()

    current_length_metric = st.sidebar.empty()
    best_length_metric = st.sidebar.empty()

    solver = tsp(points, max_iterations)

    for data in solver:
        if len(data) == 3:
            tour, length, restart = data
        else:
            tour, restart = data
            length = tour_length(tour, points)

        is_improvement = length < best_length
        if is_improvement:
            best_length = length
            best_tour = tour[:]

        draw_tour(
            points,
            tour,
            ax,
            title="TSP 2-Opt Visualization",
        )

        plot_placeholder.pyplot(fig)

        progress_bar.progress(min(restart / max_iterations, 1.0))
        color_style = "color: green;" if is_improvement else ""
        status.markdown(
            f"<div style='height:40px; font-family: monospace; {color_style}'>Restart {restart}/{max_iterations} — "
            f"Current length: {length:.4f} | Best so far: {best_length:.4f}</div>",
            unsafe_allow_html=True
        )

        current_length_metric.metric("Current Tour Length", f"{length:.4f}")
        best_length_metric.metric("Best Tour Length", f"{best_length:.4f}")

        if speed > 0:
            time.sleep(speed)

    st.success("Solver finished")

    with col_plot:
        draw_tour(
            points,
            best_tour,
            ax,
            title="TSP 2-Opt Visualization",
            final=True,
        )
        ax.set_title("TSP 2-Opt Visualization", fontsize=8)
        plot_placeholder.pyplot(fig)

if __name__ == "__main__":
    main()