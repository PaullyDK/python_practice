sandwich_orders = ['tuna', 'pastrami', 'pastrami', 'sub', 'pastrami', 'grilled cheese']
finished_sandwiches = []

print("We are out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nSandwiches made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)


