from servis.route import route

@route(url="/<name>")
def index(name):
    return f"merhaba {name}!" # merhaba is mean hello in turkish