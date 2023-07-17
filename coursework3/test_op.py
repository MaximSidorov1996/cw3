from utils import get_formatted, get_data, get_filtered_data


# Тест списка json
def test_load():
    assert len(get_data('operations.json')) == 101

# Тест формата даты
def test_date():
    assert get_formatted("2019-02-14T03:09:23.006652") == '14.02.2019'





