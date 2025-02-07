def read_transactions(file_path):
    success_pending_transactions = []

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) < 3:
                continue
            time_id, unique_number, status = parts
            time, transaction_info = time_id.split(":", 1)
            transaction_id, date = transaction_info.split("-", 1)

            if status in ('S', 'P'):
                success_pending_transactions.append({
                    "date": date,
                    "transaction_id": transaction_id,
                    "status": status
                })

    return success_pending_transactions


file_path = "pending.txt"
transactions = read_transactions(file_path)
for txn in transactions:
    print(txn)
