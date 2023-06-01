from HashMap import HashMap

def main():
    population = HashMap()
    population.add("Canada", 38.25)
    population.add("China", 1412)
    population.add("Spain", 47.42)
    population.add("Mexico", 126.7)
    
    print("Trying to get Germany: ", population.get("Germany"))
    print("Getting Canada: ", population.get("Canada"))
    print("keys before removing: ", population.get_keys())

    # expect to remove "China" and ignore "France"
    population.remove("France")
    population.remove("China")

    print("keys after removing: ", population.get_keys())
    print("formated print: ", population)

if __name__ == "__main__":
    main()