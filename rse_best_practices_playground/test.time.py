from .times import calculate_fastest_time

def test_negative_time():
      time_list = [0, 3, 5, 7, 1, 8]
      assert calculate_fastest_time(time_list) == 0
      