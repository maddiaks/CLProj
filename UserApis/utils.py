import re
from urllib.parse import urlparse

def extract_domain_name(domain_url):
    url_parts = re.split(r'\s+', domain_url)
    domain_url = "".join(url_parts)
    # print("Final Domain URL: ", domain_url)
    # domain_url = 'www.google.com'
    # www.google.com
    # https: // www.google.com
    # http: // net.tutsplus.com / about
    # https://www.hello.org/bye/
    data = urlparse(domain_url)

    domain_parts = re.split(r'\.', data.netloc)
    # print(domain_parts)

    result = []
    if domain_parts[0] == 'www':
        result.append('.'.join(domain_parts[1:]))

    result.append(data.netloc)

    return tuple(result)


if __name__ == '__main__':
    print(extract_domain_name('http: // net.tutsplus.com / about'))
    print(extract_domain_name('http://www.google.com'))
    print(extract_domain_name('https://www.hello.org/bye/'))