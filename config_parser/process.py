from input import *
s['inactive'] = []

def test(s):
    return s

def main():
    global s
    print s
    s['list'] = s['proxy_url_list'] + s['account_url_list']
    s = test(s)
    print s

if __name__ == '__main__':
    main()