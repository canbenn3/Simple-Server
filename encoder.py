from request import Request

def encode(response):
    headers = f""
    for header in response.headers:
        headers += f"{header}: {response.headers[header]}\n"
    return f"{response.version} {response.code} {response.reason}\n{headers}\n{response.body}".encode("UTF-8")

def decode(data):
    parsed = data.decode("UTF-8")
    startLine, info = parsed.split('\n', 1)
    method, uri, version = startLine.split(" ", 2)
    sections = info.split('\n\n')
    headerStr = sections[0]
    if len(sections) > 1:
        body = sections[1]
    else:
        body = ""

    headers = {}
    headLines = headerStr.replace('\r', '').split('\n')
    for line in headLines:
        if len(line) < 2:
            continue
        lineSplit = line.split(': ')
        headers[lineSplit[0]] = lineSplit[1]

    return Request(
        method=method,
        uri=uri,
        version=version,
        headers=headers,
        body=body,
        )