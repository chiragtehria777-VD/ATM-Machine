def print_statement(transactions):
    print("\n--- Transaction Statement ---")
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print(t)