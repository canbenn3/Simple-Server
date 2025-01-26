from endpoints import home

def router(req):
    print("inside router!!!")
    print(f"req:\n{req.toString()}")
    if req.uri == '/index.html' or req.uri == '/':
        return home()