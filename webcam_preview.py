# webcam_preview.py

import cv2

def main(cam_index=1, width=640, height=480):
    # 카메라 열기 (DirectShow 백엔드 강제)
    cap = cv2.VideoCapture(cam_index, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    if not cap.isOpened():
        print(f"Error: Cannot open camera {cam_index}")
        return

    print("Press 'Q' to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow("Webcam Preview", frame)

        # 'Q' 키로 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 필요하면 카메라 번호, 해상도 변경 가능
    main(cam_index=0, width=640, height=480)
