#!/usr/bin/env python3

import math
import random
import re
import sys

# Method to Show What A valid IP Looks Like, Exits
def invalid_IP():
	print('[-] Invalid IP Address!')
	print('[*] Examples of Valid IP Addresses: ')
	print('\t[>] 127.0.0.1')
	print('\t[>] 192.168.10.0')
	print('\t[>] 10.10.10.10')
	sys.exit(1)

# Method to Validate IP Address
def validate(IP):
	pattern = re.compile(r"^\d{1,3}(\.\d{1,3}){3}$")
	return bool(pattern.match(IP))

# Decimal --> Octal
def to_octal(octet):
	return str(oct(int(octet))).replace('0o', '0')

# Decimal --> Hex
def to_hex(octet):
	return str(hex(int(octet)))

# Method to Split IP to Octets, Find Conversions
def gen_converted_octets(IP):
	octets = re.split(r"\.", IP)
	octet_lst = list()
	for octet in octets:
		conversion_dict = dict()
		conversion_dict['Decimal'] = octet
		conversion_dict['Octal'] = to_octal(octet)
		conversion_dict['Hex'] = to_hex(octet)
		octet_lst.append(conversion_dict)
	return octet_lst

# Method to Output Raw Conversions
def output_raw(octet_convert):
	raw_decimal = int(math.pow(256, 3) * int(octet_convert[0]['Decimal']) + math.pow(256, 2) * int(octet_convert[1]['Decimal']) + 256 * int(octet_convert[2]['Decimal']) + int(octet_convert[3]['Decimal']))
	raw_octal = oct(raw_decimal)
	raw_hex = hex(raw_decimal)
	print('[+] Raw IP Conversions')
	print(f"\t[>] Decimal:     {str(raw_decimal)}")
	print(f"\t[>] Octal:       {str(raw_octal).replace('0o', '0')}")
	print(f"\t[>] Hexadecimal: {str(raw_hex)}")


# Method to Output Octets with All the Same Encoding
def output_matching(octet_convert):
	octal_IP = '.'.join([ x['Octal'] for x in octet_convert ])
	hex_IP = '.'.join([ x['Hex'] for x in octet_convert ])
	print('[+] Encoded IP Addresses')
	print(f"\t[>] Octal:       {octal_IP}")
	print(f"\t[>] Hexadecimal: {hex_IP}")

# Method to Output with Random Encodings
def output_random(octet_convert):
	encode_lst = ['Decimal', 'Octal', 'Hex']
	print('[+] Random Octet Encoding')
	for _ in range(5):
		octets = [
			octet_convert[0][encode_lst[random.randint(0,2)]], 
			octet_convert[1][encode_lst[random.randint(0,2)]], 
			octet_convert[2][encode_lst[random.randint(0,2)]], 
			octet_convert[3][encode_lst[random.randint(0,2)]]
		]
		print(f"\t[>] {'.'.join(octets)}")

# Method to Output with Random Padding/Encoding
def output_padded(octet_convert):
	encode_lst = ['Decimal', 'Octal', 'Hex']
	print('[+] Random Octet Encoding with Random Padding')
	for _ in range(5):
		parts = list()
		for index in range(4):
			rand = random.randint(0,2)
			if rand == 0:
				parts.append(octet_convert[index][encode_lst[rand]])
			elif rand == 1:
				parts.append('0' * random.randint(3,9) + octet_convert[index][encode_lst[rand]])
			elif rand == 2:
				parts.append(octet_convert[index][encode_lst[rand]].replace('0x', '0x' + '0' * random.randint(3,9)))
		print(f"\t[>] {'.'.join(parts)}")

def main():
	# Get/Validate Input
	original_IP = input('IP Address> ')
	if not validate(original_IP):
		invalid_IP()
	
	# Convert to Decimal (Input), Binary, Octal, and Hex
	octet_conversions = gen_converted_octets(original_IP)
	
	# Output Raw Number Conversions
	output_raw(octet_conversions)

	# Output All of Matching Encodings Per Octet
	output_matching(octet_conversions)

	# Output With Random Encodings Per Octet
	output_random(octet_conversions)

	# Output with Random Padding/Encodings Per Octet
	output_padded(octet_conversions)

if __name__ == '__main__':
	main()
