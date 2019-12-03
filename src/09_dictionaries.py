"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with 
lists!). 

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
new_place = {
    "lat": 42,
    "lon": -121,
    "name": "a new place"
}

waypoints.append(new_place)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
waypoints[0]["name"] = "not a real place"
waypoints[0]["lon"] = -130

# Write a loop that prints out all the field values for all the waypoints
for waypoint in waypoints:
    name = waypoint["name"]
    lat, lon = waypoint["lat"], waypoint["lon"]
    print(f"Name: {name}")
    print(f"Position (lat, lon): ({lat}, {lon})")
    print("")