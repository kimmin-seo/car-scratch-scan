import cv2
from ultralytics import YOLO
import torch

def main():
    # 0. GPU 사용 가능 여부 확인 및 디바이스 설정 (YOLOv8m 가속용)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"🔌 [디바이스 설정] 현재 사용 중인 연산 장치: {device.upper()}")

    # 1. 학습된 가중치 파일(best.pt) 불러오기, GPU 할당 및 디버그 로그 끄기
    model = YOLO("best.pt")
    model.to(device)
    model.overrides["verbose"] = False

    # 2. 웹캠 연결 (0번은 기본 내장/연결된 웹캠) 및 해상도 최적화
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("❌ 카메라를 열 수 없습니다. 연결 상태를 확인해주세요.")
        return

    print("🚗 [2D 모드] 실시간 자동차 기스 탐지 프로그램 구동 중... (종료하려면 'q'를 누르세요)")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("프레임을 읽어올 수 없습니다.")
            break

        # 3. 실시간 프레임마다 YOLOv8m 모델로 예측 수행 (GPU 및 최적화 파라미터 적용)
        results = model(frame, conf=0.3, imgsz=640, device=device)

        # 4. 탐지된 결과 박스들을 화면에 그려서 프레임으로 반환
        annotated_frame = results[0].plot()

        # 5. 화면에 실시간 출력
        cv2.imshow("Car Scratch Detection System (YOLOv8m)", annotated_frame)

        # 'q' 키를 누르면 프로그램 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 6. 자원 해제 및 창 닫기
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()