from servis import app

def route(**args):
    url = args.get('url', "/")
    method = args.get('method', ["GET"])

    def decorator(func):
        app.route(url, methods=method)(func)
        return func
    return decorator
