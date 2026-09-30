from city_functions import get_formatted_city

def test_city_country():
    city_name = get_formatted_city('austin', 'texas')
    assert city_name == "Austin, Texas"

def test_city_country_population():
    city_name = get_formatted_city('columbia', 'missouri', 130000)
    assert city_name == "Columbia, Missouri - population 130000"
