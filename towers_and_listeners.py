"""
This problem was asked by Spotify.

You are the technical director of WSPT radio, serving listeners
nationwide. For simplicity's sake we can consider each listener to live
along a horizontal line stretching from 0 (west) to 1000 (east).

Given a list of N listeners, and a list of M radio towers, each placed
at various locations along this line, determine what the minimum
broadcast range would have to be in order for each listener's home to be covered.

For example, suppose listeners = [1, 5, 11, 20], and
towers = [4, 8, 15]. In this case the minimum range
would be 5, since that would be required for the tower at
position 15 to reach the listener at position 20.

"""



def find_min_range(listeners_array, towers_array):
    listeners_array = sorted(listeners_array)
    towers_array = sorted(towers_array)

    m_towers_last_id = len(towers_array) - 1

    min_distance_to_cover_listener = [0 for listener in range(len(listeners_array))]

    current_chosen_tower_id = 0

    for listener_id, listener_coord in enumerate(listeners_array):

        distance_to_previously_chosen_tower = 1001
        distance_to_current_chosen_tower = abs(towers_array[current_chosen_tower_id] - listener_coord)

        # while every next tower is closer to user
        # find the nearest tower to user
        while distance_to_current_chosen_tower <= distance_to_previously_chosen_tower:
            found_distance = distance_to_current_chosen_tower

            # if we measure distance to the last tower
            if current_chosen_tower_id == m_towers_last_id:
                break
            else:
                current_chosen_tower_id += 1
                distance_to_previously_chosen_tower = distance_to_current_chosen_tower
                distance_to_current_chosen_tower = abs(towers_array[current_chosen_tower_id] - listener_coord)


        min_distance_to_cover_listener[listener_id] = found_distance

        # so next listener is measured from the found tower
        current_chosen_tower_id -= 1

    print(min_distance_to_cover_listener)
    return max(min_distance_to_cover_listener)


def test_correctness():
    listeners = [1, 5, 11, 20]
    towers = [4, 8, 15]
    assert find_min_range(listeners, towers) == 5, "hasn't pass test 1"

    listeners = [100, 105, 111, 120]
    towers = [4, 8, 15]
    assert find_min_range(listeners, towers) == 105, "hasn't pass test 2"

    listeners = [100, 105, 111, 120]
    towers = [14, 15, 16, 4, 8, 15]
    assert find_min_range(listeners, towers) == 104, "hasn't pass test 3"

    listeners = [6]
    towers = [14, 15, 16, 4, 8, 15]
    assert find_min_range(listeners, towers) == 2, "hasn't pass test 4"

    listeners = [1, 6, 10]
    towers = [1]
    assert find_min_range(listeners, towers) == 9, "hasn't pass test 5"

if __name__ == '__main__':
    test_correctness()