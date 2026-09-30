def get_formatted_city(name, country, population=None):
    full_city_name = f"{name}, {country}"
    if population:
        return full_city_name.title() + f" - population {population}"
    else:
        return full_city_name.title()