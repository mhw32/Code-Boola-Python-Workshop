To generate a key + encrypt a file: 
  python encrypt.py < secret.txt > encrypted 

To decrypt that file (using same key):
  python encrypt.py --decrypt --key pWz1o0LfxsCgNzhpt93emQ== < encrypted