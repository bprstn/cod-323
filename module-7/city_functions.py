def city_country(city, country, population=None, language=None):
    """Return a formatted string. Population and language are optional."""
    if population and language:
        return f"{city}, {country} - population {population}, language {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    return f"{city}, {country}"

# Example calls to test the function
print(city_country("Madrid", "Spain"))
print(city_country("Paris", "France", 12000000))
print(city_country("Tokyo", "Japan", 14000000, "Japanese"))






