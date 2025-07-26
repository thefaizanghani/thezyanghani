import os
import random
import time

WIDTH = 3
HEIGHT = 10


def clear_screen():
    """Clear the terminal screen."""
    print("\033c", end="")


def draw_board(car_lane, obstacles, score):
    """Draw the current state of the board."""
    clear_screen()
    for y in range(HEIGHT):
        row = '|'  # left boundary
        for x in range(WIDTH):
            char = ' '
            for ox, oy in obstacles:
                if ox == x and oy == y:
                    char = 'X'
                    break
            if y == HEIGHT - 1 and x == car_lane:
                char = 'A'
            row += char
        row += '|'  # right boundary
        print(row)
    print(f"Score: {score}")


def main():
    car_lane = WIDTH // 2
    obstacles = []
    score = 0

    while True:
        draw_board(car_lane, obstacles, score)
        move = input("Move (a=left, d=right, q=quit): ").strip().lower()
        if move == 'a' and car_lane > 0:
            car_lane -= 1
        elif move == 'd' and car_lane < WIDTH - 1:
            car_lane += 1
        elif move == 'q':
            print("Goodbye!")
            break

        # update obstacles
        obstacles = [(x, y + 1) for (x, y) in obstacles if y + 1 < HEIGHT]
        if not obstacles or obstacles[-1][1] > 1:
            obstacles.append((random.randint(0, WIDTH - 1), 0))

        # check collision
        if any(x == car_lane and y == HEIGHT - 1 for (x, y) in obstacles):
            draw_board(car_lane, obstacles, score)
            print("Game Over!")
            break

        score += 1
        time.sleep(0.1)


if __name__ == "__main__":
    main()
