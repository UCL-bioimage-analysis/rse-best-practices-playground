from .times import calculate_fastest_time

def test_fastest_time():
    time_list = [0, 3, 7.3]
    assert calculate_fastest_time(time_list) == 0
    