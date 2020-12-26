mod = 20201227

pubkey_1 = int(input())
pubkey_2 = int(input())
print('Pubkeys:', pubkey_1, pubkey_2)

secret_1 = 0
secret_2 = 0

while pow(7, secret_1, mod) != pubkey_1:
    secret_1 += 1

while pow(7, secret_2, mod) != pubkey_2:
    secret_2 += 1

print('Secrets:', secret_1, secret_2)
print('Encrypt:', pow(7, secret_1 * secret_2, mod))
