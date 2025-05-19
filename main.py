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
LET'S NAME IT POISON JAR !!!! THAT'S SICK !!!!

things
- HTML smuggling
- Other C2 Comms
- Environment Keying and Encryption
- Shannon Entropy Averaging
- Payload Emulation - on host sandbox fro EDR, cant go on forever, peg the CPU
- What the hell is an EDR silencer!!! (Look it up)

overview
- Shellcode loader
- Secondary C2
- Start reading malware books !

"""