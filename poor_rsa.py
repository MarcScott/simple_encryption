prime1 = 19
prime2 = 17
prime3 = 13

public_key = (prime1 * prime2, prime3)

phi1 = prime1 - 1
phi2 = prime2 - 1

for d in range(1,phi1*phi2):
    if (d * prime3)%(phi1 * phi2) == 1:
	private_ey = prime1*prime2,d
	break
print('Your public_key is', public_key)
print('Your private key is', private_key)
