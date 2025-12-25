from tour import create_random_tour
from geometry import tour_length
from two_opt import try_two_opt

def tsp(points, max_iterations):
    tour = create_random_tour(len(points))
    length = tour_length(tour, points)

    best_tour = tour[:]
    best_length = length

    yield best_tour, best_length

    for _ in range(max_iterations):
        result = try_two_opt(tour, points)

        if result is None:
            tour = create_random_tour(len(points))
            length = tour_length(tour, points)
        else:
            tour, length = result

        if length < best_length:
            best_tour = tour[:]
            best_length = length

        yield best_tour, best_length