#!/usr/bin/python3
alphabet = ""
for letter in range(97, 123):
	if letter != 101 and letter != 113:
		alphabet += chr(letter)
print(alphabet)
