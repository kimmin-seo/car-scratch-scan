import cv2
from ultralytics import YOLO
import open3d as o3d
import numpy as np
import torch


def main():
    # 0. GPU 사용 가능 여부 확인 및 디바이스 설정 (YOLOv8m 가속용)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"🔌 [디바이스 설정] 현재 사용 중인 연산 장치: {device.upper()}")

    # 1. 커스텀 학습된 YOLOv8m 모델 로드 및 GPU 할당
    model = YOLO("best.pt")
    model.to(device)
    model.overrides["verbose"] = False  # 불필요한 로그 출력 차단

    # 2. 웹캠 연결 (기본 카메라: 0)
    camera_source = 0
    cap = cv2.VideoCapture(camera_source)

    # 웹캠 해상도 최적화 (필요시 조절)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("❌ 카메라를 열 수 없습니다. 연결 상태를 확인해주세요.")
        return

    print("🚀 [시스템 가동] YOLOv8m 실시간 스크래치 탐지 및 3D 매핑 시뮬레이터 구동 중...")

    # 3. Open3D 3D 시각화 창 설정
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name="3D Scratch Spatial Mapping (YOLOv8m Optimized)", width=1024, height=768)

    # 가상의 차체 표면 포인트 클라우드 생성
    points = np.random.rand(1000, 3) * [2.0, 1.0, 0.1]
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    pcd.paint_uniform_color([0.7, 0.7, 0.7])  # 회색 차체 색상
    vis.add_geometry(pcd)

    # [핵심 수정] 스크래치 포인트들을 누적 관리할 리스트와 단일 포인트 클라우드 객체 (메모리 누수 방지)
    scratch_points = []
    scratch_pcd = o3d.geometry.PointCloud()
    scratch_pcd.paint_uniform_color([1.0, 0.0, 0.0])  # 빨간색 (스크래치 경고)
    vis.add_geometry(scratch_pcd)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("프레임을 정상적으로 읽어오지 못했습니다.")
            break

        # YOLOv8m 실시간 추론 수행 (YOLOv8m 속도/정확도 밸런스를 위해 imgsz=640, conf=0.3 권장)
        results = model(frame, conf=0.3, imgsz=640, device=device)
        annotated_frame = results[0].plot()

        # 스크래치가 감지된 경우 3D 공간 매핑 좌표 업데이트
        boxes = results[0].boxes
        if len(boxes) > 0:
            for box in boxes:
                xyxy = box.xyxy[0].cpu().numpy()
                cx, cy = int((xyxy[0] + xyxy[2]) / 2), int((xyxy[1] + xyxy[3]) / 2)

                # 2D 픽셀 좌표를 3D 공간 좌표계로 매핑
                mapped_3d_point = np.array([cx / 500.0, cy / 500.0, 0.05])
                scratch_points.append(mapped_3d_point)

            # 누적된 포인트 데이터를 하나의 Open3D 객체에 업데이트 (메모리 누수 해결)
            if scratch_points:
                scratch_pcd.points = o3d.utility.Vector3dVector(np.array(scratch_points))
                vis.update_geometry(scratch_pcd)

        # 2D 웹캠 화면 출력
        cv2.imshow("Robotic Vision - YOLOv8m 2D Scratch Detection", annotated_frame)

        # Open3D 3D 렌더링 프레임 업데이트
        vis.poll_events()
        vis.update_renderer()

        # 'q'를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    vis.destroy_window()


if __name__ == "__main__":
    main()