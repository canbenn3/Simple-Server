from request import Request

def encode(data):
    pass

def decode(data):
    parsed = str(data)
    lines = parsed.split('\n')
    start = lines[0].split(" ", 2)
    method = start[0]
    uri = start[1]
    version = start[2]
    headers = {}
    lastLine = 1
    for i in range(1, len(lines)):
        if lines[i] == '':
            break
        line = lines[i].split(': ')
        name = line[0]
        value = line[1]
        headers[name] = value
        lastLine = i + 1

    body = lines[lastLine]

    return Request(
        method=method,
        uri=uri,
        version=version,
        headers=headers,
        body=body,
        )