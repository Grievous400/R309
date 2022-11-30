from client_nul import client
import sys

def main():
    c1:client=client('127.0.0.1',1003)
    client.connexion(c1)
    client.envoyer(c1,"OS")

if __name__ == "__main__":
    sys.exit(main())