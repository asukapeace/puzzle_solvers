def move_disk(source, destination, spare):
    print(f"Move disk from {source} to {destination}")

def hanoi(num_disks, source, destination, spare):
    if num_disks == 1:
        move_disk(source, destination, spare)
    else:
        hanoi(num_disks - 1, source, spare, destination)
        move_disk(source, destination, spare)
        hanoi(num_disks - 1, spare, destination, source)

def main():
    num_disks = int(input("Enter number of disks: "))
    hanoi(num_disks, 'A', 'B', 'C')

if __name__ == "__main__":
    main()