from Socket_Encryptor import GetSocketEncryptor

encryptor = GetSocketEncryptor()
plaintext = b'is a playable Pyro character. She is the daughter and the current owner of Fireworks. With her colorful fireworks and outgoing personality, loved by everyone on Island, as they believe summer is not the same without her.'
ciphertext = encryptor.encrypt(plaintext)
decryptedtext = encryptor.decrypt(ciphertext)

print(ciphertext)
print(decryptedtext)