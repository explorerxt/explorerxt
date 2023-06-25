import sys
import time
import math


def main():
    width, height = 80, 24

    while True:
        time.sleep(0.1)
        sys.stdout.write("\033[2J")

        for y in range(height):
            for x in range(width):
                # Compute the z coordinate based on x and y positions
                z = (math.sin(x * 0.1) + math.cos(y * 0.1)) * 0.4
                z = int(z * 10)

                # Adjust the z coordinate to fit within the ASCII character range
                z = max(0, min(z, 9))

                # Map the z coordinate to an ASCII character
                if x in range(33, 41) and y == 12 and z == 0:
                    sys.stdout.write("E")
                elif x in range(41, 49) and y == 12 and z == 0:
                    sys.stdout.write("x")
                elif x in range(49, 57) and y == 12 and z == 0:
                    sys.stdout.write("p")
                elif x in range(57, 65) and y == 12 and z == 0:
                    sys.stdout.write("l")
                elif x in range(65, 73) and y == 12 and z == 0:
                    sys.stdout.write("o")
                elif x in range(73, 81) and y == 12 and z == 0:
                    sys.stdout.write("r")
                else:
                    sys.stdout.write(" ")

            sys.stdout.write("\n")

        sys.stdout.flush()


if __name__ == "__main__":
    main()
