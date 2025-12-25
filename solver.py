from tour import create_random_tour
from geometry import tour_length
from two_opt import try_two_opt

def tsp(points, max_restarts):
    best_length = float("inf")

    for restart in range(1, max_restarts + 1):
        tour = create_random_tour(len(points))
        length = tour_length(tour, points)

        current_best_length = length
        yield tour, current_best_length, restart

        improved = True
        while improved:
            improved = False
            result = try_two_opt(tour, points)

            if result is not None:
                new_tour, new_length = result
                if new_length < length:
                    tour, length = new_tour, new_length
                    improved = True

                    yield tour, length, restart

                    if length < best_length:
                        best_length = length