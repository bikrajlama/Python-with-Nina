#this will throw an error

try: 
    int ("a")
except ValueError:
    print("Opps")

print("This is end")