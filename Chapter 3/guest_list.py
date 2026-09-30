guest_list = ["Rachel", "Nishan", "Ellie"]

print(f"you are invited to dinner, {guest_list[0]}")
print(f"you are invited to dinner, {guest_list[1]}")
print(f"you are invited to dinner, {guest_list[2]}")

print(f"Oh no, Dea cant make it")

print(f"Oh, rad, we found a bigger table!")

guest_list.insert(0, "Sarah")
guest_list.insert(2, "Whitney")
guest_list.append("Joe")

print(f"People who are invited: {guest_list}")

print(f"There are {len(guest_list)} guests right now.")

print(guest_list[6])

print("Oh shit, i guess i can only invite 2 people")

popped = guest_list.pop(0)
print(f"Sorry, {popped}, you can't come anymore")
popped = guest_list.pop(1)
print(f"Sorry, {popped}, you can't come anymore")
popped = guest_list.pop(2)
print(f"Sorry, {popped}, you can't come anymore")
popped = guest_list.pop(2)
print(f"Sorry, {popped}, you can't come anymore")

print(f"Guests who are still invited: {guest_list}")

del guest_list[0]
del guest_list[0]

print(f"Empty list: {guest_list}")