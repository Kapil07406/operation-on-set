# Operations on Set

colors = {"Red", "Blue", "Green"}

print("Original Set:")
print(colors)

# Add
colors.add("Yellow")

# Update
colors.update(["Black", "White"])

print("\nAfter Adding:")
print(colors)

# Remove
colors.remove("Blue")

print("\nAfter Removing Blue:")
print(colors)

# Pop
removed = colors.pop()

print("\nRemoved Item:", removed)
print(colors)

# Length
print("\nTotal Items:", len(colors))