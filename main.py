import random, sys, os

ALPHABET_UPPERCASE = "abcdefghijklmnopqrstuvwxyz".upper()
NUMERIC = "0123456789"

def clr():
	os.system('cls' if os.name == 'nt' else 'clear')

def banner():
	print("""
 █▀█ █▀█ █▀█ █▀▄ █░█ █▀▀ ▀█▀   █▄▀ █▀▀ █▄█
 █▀▀ █▀▄ █▄█ █▄▀ █▄█ █▄▄ ░█░   █░█ ██▄ ░█░
 
 █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
 █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄

 Coder by : https://github.com/nux-xader
 Contact  : https://wa.me/6281251389915
 Version  : 1.0.0
 _________________________________________
""")


def generate():
	result = ""
	source = [ALPHABET_UPPERCASE for x in range(random.randint(5, 6))]
	source.append(NUMERIC)
	for i in range(25):
		char = random.choice(random.choice(source))
		result+=char
		if ((i+1)%5 == 0) and (i != 24):
			result+="-"

	return result



def main():
	clr()
	banner()
	while True:
		saveto = str(input(" Save result to : "))
		if saveto.split(".")[-1] != "txt": saveto+=".txt"
		try:
			open(saveto, "r")
			print(f" [!] File {saveto} already exists, please use another file name")
			continue
		except:
			break

	while True:
		try:
			count = int(input(" Count result (e.g 10000): "))
			break
		except:
			print(" [!] Invalid input")

	clr()
	banner()
	for i in range(count):
		product_key = generate()
		open(saveto, "a").write(product_key+"\n")
		print(f" [{i+1}] {product_key}")

	print(f" [+] Result has saved to {saveto}")


if __name__ == '__main__':
	main()