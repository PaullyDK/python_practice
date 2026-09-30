cities = {
    'Austin': {
        'country': 'america',
        'population': '961,855',
        'fact': "it's where I live." 
    },
    'Columbia': {
        'country': 'america',
        'population': '133,193',
        'fact': "it's my hometown."
    },
    'New York': {
        'country': 'america',
        'population': '19,867,248',
        'fact': "where i want to visit."
    }
    }

for key, value in cities.items():
    print(f"\nCity: {key.title()}")

    for name, info in value.items():
        if name == 'country':
            print(f"{name.title()}: {info.title()}")
        else:
            print(f"{name.title()}: {info}")