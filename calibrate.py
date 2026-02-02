import cv2
import numpy as np
import glob

# ================== SETTINGS ==================
CHECKERBOARD = (9, 6)   # inner corners
square_size = 28.6      # mm (MacBook 13-inch screen)
# ==============================================

criteria = (cv2.TERM_CRITERIA_EPS +
            cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Prepare object points
objp = np.zeros((CHECKERBOARD[0]*CHECKERBOARD[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:CHECKERBOARD[0],
                       0:CHECKERBOARD[1]].T.reshape(-1, 2)
objp *= square_size

objpoints = []
imgpoints = []

images = glob.glob("calibration_images/*.jpeg")
print("Found images:", len(images))

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCornersSB(
        gray,
        CHECKERBOARD,
        cv2.CALIB_CB_EXHAUSTIVE | cv2.CALIB_CB_ACCURACY
    )

    if ret:
        corners2 = cv2.cornerSubPix(
            gray, corners, (11,11), (-1,-1), criteria)
        objpoints.append(objp)
        imgpoints.append(corners2)

        cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)
        cv2.imshow("Detected", img)
        cv2.waitKey(200)
    else:
        print("FAILED:", fname)

cv2.destroyAllWindows()

print("Valid detections:", len(objpoints))

if len(objpoints) < 10:
    raise RuntimeError("Not enough valid calibration images")

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
    objpoints, imgpoints, gray.shape[::-1], None, None)

print("\nCamera Matrix:\n", mtx)
print("\nDistortion Coefficients:\n", dist)
