import math

def haversine(lat1: float, lng1: float, lat2: float, lng2: float):
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lng1 = math.radians(lng1)
    lng2 = math.radians(lng2)
    a = math.sin((lat1-lat2)/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((lng1-lng2)/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return 6371000 * c

def a_star():
    pass