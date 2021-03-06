import re
from urllib.parse import urlparse

def extract_domain_name(domain_url):
    domain_url = domain_url.strip('//')
    url_parts = re.split(r'\s+', domain_url)
    domain_url = "".join(url_parts)
    print("Final Domain URL: ", domain_url)
    # domain_url = 'www.google.com'
    # www.google.com
    # https: // www.google.com
    # http: // net.tutsplus.com / about
    # https://www.hello.org/bye/
    data = urlparse(domain_url)
    print(data)

    domain_parts = re.split(r'\.', data.netloc)
    print(domain_parts)

    result = []
    if domain_parts[0] == 'www':
        result.append('.'.join(domain_parts[1:]))

    if data.netloc != "":
        result.append(data.netloc)

    if data.path != "":
        result.append(data.path)

    return tuple(result)


if __name__ == '__main__':
    print(extract_domain_name('http: // net.tutsplus.com / about'))
    print(extract_domain_name('http://www.google.com'))
    print(extract_domain_name('https://www.hello.org/bye/'))
    print(extract_domain_name('27lelchgcvs2wpm7.adevf4.top/'))
    print(extract_domain_name('zutzt67dcxr6mxcn.onion.to'))