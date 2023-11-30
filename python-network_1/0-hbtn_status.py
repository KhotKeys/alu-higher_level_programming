#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status."""

if __name__ == '__main__':
    import urllib.request
    from urllib.error import HTTPError

    try:
        with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
            content = resp.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
    except HTTPError as e:
        print("HTTP Error: {}".format(e))
