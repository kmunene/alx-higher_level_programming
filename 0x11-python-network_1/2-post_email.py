#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    post_data = {'email': sys.argv[2]}

    encoded_data = urllib.parse.urlencode(post_data).encode('utf-8')

    request = urllib.request.Request(url, data=encoded_data, method='POST')

    with urllib.request.urlopen(request) as response:
        req_data = response.read()
        print(req_data.decode('utf-8'))
