from .assign_seating import assign_seating

def main():
  print("WELCOME TO MARS AIR SEATING")
  print("")

  while True:
    input_str = input("How many passengers in your group? ")
    seating = assign_seating(input_str)
    print(f"Seating assignments: {' '.join(seating)}")

if __name__ == "__main__":
  main()