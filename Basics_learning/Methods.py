def is_metro(city):
    state = ['bangalore','mumbai','chennai','kolkatta']
    if city in state:
        return True
    else:
        return False
metro = is_metro('bangalore')
print(metro)