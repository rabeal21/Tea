from solana.keypair import Keypair

def generate_bulk_solana_wallets(count):
    wallets = []
    for _ in range(count):
        keypair = Keypair()
        pubkey = str(keypair.public_key)
        secret_key = keypair.secret_key.hex()
        wallets.append((pubkey, secret_key))
    return wallets

def save_wallets_to_file(wallets, filename="tea_wallets.txt"):
    with open(filename, "w") as f:
        for pubkey, secret_key in wallets:
            f.write(f"{pubkey},{secret_key}\n")

if __name__ == "__main__":
    count = int(input("How many TEA (Solana) wallets do you want to generate? "))
    wallets = generate_bulk_solana_wallets(count)
    save_wallets_to_file(wallets)
    print(f"{count} wallets saved to tea_wallets.txt")
