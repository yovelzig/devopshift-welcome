serverlist = ["server1" ,"server2", "server3", "server4"]
serverdict = {"ngnix", "docker", "server"}
try:
    user_input = input("please enter the name of your server : ")
    
    if not user_input.strip():
        raise ValueError("input cannot be empty")
    
    if not user_input.isalnum():
        raise ValueError("the input should contains characters only")
    if user_input in serverdict:
        print("server is running")
    else:
        print("server not recognized")
except ValueError as e:
    print(f"invalid input :{e}")
    


    
try:
        server_name = input("Please enter your server name: ")
        
        # Check for empty input
        if not server_name.strip():
            raise ValueError("Input cannot be empty.")
        
        # Check for non-alphanumeric characters
        if not server_name.isalnum():
            raise ValueError("Input must contain only alphanumeric characters.")
        if server_name in serverlist:
            print("Server is running")
        else:
            print("Server not recognize")


except ValueError as e:
        print(f"Invalid input: {e}")