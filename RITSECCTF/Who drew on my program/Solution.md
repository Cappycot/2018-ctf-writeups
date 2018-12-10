Who drew on my program?
=======================
Long story short: CBC is ECB on a small dose of steroids and an IV.

Despite not knowing some of the bytes of the key and encrypted data, since the data is encrypted by block, you can still get the IV because of how xor works.

https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_Codebook_(ECB)
