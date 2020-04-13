import cv2, win32api, win32con, os, ctypes, time, pyautogui

def closest_to(ob, og, oR):
    colors = [(239, 19, 11), (255, 113, 0), (255, 228, 0), (0, 204, 0), (0, 178, 255), (35, 31, 211), (163, 0, 186), (211, 124, 170), (160, 82, 45), (193, 193, 193),
                (255, 255, 255), (0, 0, 0), (76, 76, 76), (116, 11, 7), (194, 56, 0), (232, 162, 0), (0, 85, 16), (0, 86, 158), (14, 8, 101), (85, 0, 105), (167, 85, 116), (99, 48, 13)]

    closest = min(colors, key=lambda p: (oR - p[0])**2 + (ob - p[2])**2 + (og - p[1])**2)

    return closest

def draw(image):
    user32 = ctypes.windll.user32
    rath, ratw = int(user32.GetSystemMetrics(0) / 1920), int(user32.GetSystemMetrics(1) / 1080)
    DRAW_CENTERX, DRAW_CENTERY = 579 * ratw, 844 * rath
    color_pos = {(239, 19, 11):(DRAW_CENTERX + 25 * 2, DRAW_CENTERY), (255, 113, 0):(DRAW_CENTERX + 25 * 3, DRAW_CENTERY), (255, 228, 0):(DRAW_CENTERX + 25 * 4, DRAW_CENTERY), (0, 204, 0):(DRAW_CENTERX + 25 * 5, DRAW_CENTERY), (0, 178, 255):(DRAW_CENTERX + 25 * 6, DRAW_CENTERY), 
                (35, 31, 211):(DRAW_CENTERX + 25 * 7, DRAW_CENTERY), (163, 0, 186):(DRAW_CENTERX + 25 * 8, DRAW_CENTERY), (211, 124, 170):(DRAW_CENTERX + 25 * 9, DRAW_CENTERY), (160, 82, 45):(DRAW_CENTERX + 25 * 10, DRAW_CENTERY), (193, 193, 193):(DRAW_CENTERX + 25, DRAW_CENTERY),
                (255, 255, 255):(DRAW_CENTERX, DRAW_CENTERY), (0, 0, 0):(DRAW_CENTERX, DRAW_CENTERY + 25), (76, 76, 76):(DRAW_CENTERX + 25, DRAW_CENTERY + 25), (116, 11, 7):(DRAW_CENTERX + 25 * 2, DRAW_CENTERY + 25), 
                (194, 56, 0):(DRAW_CENTERX + 25 * 3, DRAW_CENTERY + 25), (232, 162, 0):(DRAW_CENTERX + 25 * 4, DRAW_CENTERY + 25), (0, 85, 16):(DRAW_CENTERX + 25 * 6, DRAW_CENTERY + 25), (0, 86, 158):(DRAW_CENTERX + 25 * 7, DRAW_CENTERY + 25), (14, 8, 101):(DRAW_CENTERX + 25 * 8, DRAW_CENTERY + 25), 
                (85, 0, 105):(DRAW_CENTERX + 25 * 9, DRAW_CENTERY + 25), (167, 85, 116):(DRAW_CENTERX + 25 * 10, DRAW_CENTERY + 25), (99, 48, 13):(DRAW_CENTERX + 25 * 11, DRAW_CENTERY + 25)}

    center_x = 484 * rath
    center_y = 218 * ratw
    curColor = (0, 0, 0)

    SMALL_SIZEX = 1019
    SMALL_SIZEY = 844

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, SMALL_SIZEX, SMALL_SIZEY, 0, 0)
    time.sleep(1/1000)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, SMALL_SIZEX, SMALL_SIZEY, 0, 0)
    time.sleep(1/1000)

    b, g, r = cv2.split(image)
    for i in range(len(b)):
        for j in range(len(b[i])):
            nr, ng, nb = closest_to(b[i][j], g[i][j], r[i][j])
            if (nr, ng, nb) != curColor:

                curColor = (nr, ng, nb)
                x, y = color_pos.get(curColor)
                win32api.SetCursorPos((x,y))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
                time.sleep(1/1000)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

            curx = center_x + j * 3
            cury = center_y + i * 3
            win32api.SetCursorPos((curx, cury))
            time.sleep(1/1000)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, curx, cury, 0, 0)
            time.sleep(1/1000)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, curx, cury, 0, 0)


def main():
    time.sleep(5)
    selection = input("Path to image:    ")
    dimage = cv2.imread(selection)
    dimage = cv2.resize(dimage, (200, 100))
    ih, iw = dimage.shape[:2]

    draw(dimage)

if __name__ == "__main__":
    main()