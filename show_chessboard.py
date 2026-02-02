import cv2
import numpy as np

# INNER CORNERS (what OpenCV detects)
inner_cols = 8
inner_rows = 5

# Squares = inner + 1
cols = inner_cols + 1
rows = inner_rows + 1

square_px = 180  # LARGE on screen

board = np.zeros((rows * square_px, cols * square_px), dtype=np.uint8)

for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            board[i*square_px:(i+1)*square_px,
                  j*square_px:(j+1)*square_px] = 255

cv2.namedWindow("Chessboard", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Chessboard",
                      cv2.WND_PROP_FULLSCREEN,
                      cv2.WINDOW_FULLSCREEN)
cv2.imshow("Chessboard", board)
cv2.waitKey(0)
cv2.destroyAllWindows()
