from AuthRPC.client import ServerProxy

user = str(input('Enter your username: '))
passw = str(input('Enter your password: '))

client = ServerProxy('http://localhost:1234/',
                     username=user,
                     password=passw,
                     user_agent='myprogram')       
inp = input('Enter the number to find the square of it: ')
retval = client.square(int(inp))
print(retval)
