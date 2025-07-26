import curses
from random import randint


def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.nodelay(True)
    w.timeout(100)

    car_x = sw // 2
    car_y = sh - 2
    obstacles = []
    score = 0

    while True:
        key = w.getch()
        if key == curses.KEY_LEFT and car_x > 1:
            car_x -= 1
        elif key == curses.KEY_RIGHT and car_x < sw - 2:
            car_x += 1
        elif key == ord('q'):
            break

        if not obstacles or obstacles[-1][1] > sh // 5:
            obstacle_x = randint(1, sw - 2)
            obstacles.append([obstacle_x, 0])

        obstacles = [[x, y + 1] for x, y in obstacles if y + 1 < sh]

        if [car_x, car_y] in obstacles:
            w.nodelay(False)
            msg = f"Game Over! Score: {score}"
            w.addstr(sh // 2, max(0, sw // 2 - len(msg) // 2), msg)
            w.getch()
            break

        w.clear()
        for i in range(sh):
            w.addch(i, 0, '|')
            w.addch(i, sw - 1, '|')

        for x, y in obstacles:
            if 0 <= y < sh:
                w.addch(y, x, 'X')

        w.addch(car_y, car_x, 'A')
        w.addstr(0, 2, f"Score: {score}")
        score += 1
        w.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
