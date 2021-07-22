TODO: Reflect on what you learned this week and what is still unclear.

<!-- import requests

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41"
}
targeturl = "http:https://opensea.io/assets"
Response = requests.get(url=targeturl, headers=header)
print(Response) -->

can not solve this two problem

#SyntaxError: invalid syntax
#NameError: name 'Response' is not defined

How to use with open:
https://blog.csdn.net/chenmozhe22/article/details/81434549
'r' reading
'w' writing
methon1 three steps
1.open f = open( '/Users/michael/test.txt', 'r' )
2.read f.read()
'Hello, world!'
3.close f.close()

methon2

1.          with open( '/path/to/file', 'r' ) as f:

    print( f.read() )

2.           for line in f.readlines():
    print( line.strip() )
3.           f = open('/Users/michael/test.txt', 'w')
    f.write('Hello, world!')
    f.close()
