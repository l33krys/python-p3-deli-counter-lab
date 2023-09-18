katz_deli = []

def line(katz_deli):
    if len(katz_deli) > 0:
        sentence = ["The line is currently:"]
        for num, item in enumerate(katz_deli):
          sentence.append(f"{num + 1}. {item}")
        print(" ".join(sentence))
    else:
        print("The line is currently empty.")

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    if len(katz_deli) > 0:
        next = katz_deli.pop(0)
        print(f"Currently serving {next}.")
    else:
        print("There is nobody waiting to be served!")