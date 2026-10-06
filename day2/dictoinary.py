emp={"name": "shiva", "department": "apprentice", "salary": 2000}
type(emp)
print(emp["name"])
print(emp["department"])
print(emp["salary"])


# adding new to the dictionary
emp["location"] = "hyderabad"
print(emp)

# modifying an existing key in the dictionary
emp["salary"] = 2500
print(emp)

# deleting a key from the dictionary
emp.pop("salary")
print(emp)


del emp["location"]
print(emp)




for e in emp:
    print(f"{e}: {emp[e]}")