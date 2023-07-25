country = str(input("Where are you living? "))
country_split = country.split()

print("You're living in a city that starts with Santo: {}.".format('santo' in country_split[0].lower()))
