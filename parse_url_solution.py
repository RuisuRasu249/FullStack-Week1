# Create an input variable
url = input("Please enter a URL >>")

# we can split the url into parts
parts = url.split('?')

# This will help print and split the host name and its parameters
host = parts[0].split("//")[1]
print("Host is " + host)

# this will print out each parameters key and value in the URL
params = parts[1].split('&')
for param in params:
    values = param.split('=')
    print("Name is " + values[0] + ", value is " + values[1])