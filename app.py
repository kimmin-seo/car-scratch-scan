
import cv2
from ultralytics import YOLO
import open3d as o3d
import numpy as np
import torch


def main():
    # 사용할 디바이스 설정
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"사용 중인 디바이스: {device.upper()}")

    # YOLO 모델 로드
    model = YOLO("best.pt")
    model.to(device)
    model.overrides["verbose"] = False

    # 웹캠 연결
    camera_source = 0
    cap = cv2.VideoCapture(camera_source)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return

    print("실시간 스크래치 탐지를 시작합니다.")

    # 3D 시각화 창 생성
    vis = o3d.visualization.Visualizer()
    vis.create_window(
        window_name="3D Scratch Mapping",
        width=1024,
        height=768
    )

    # 차체 표면을 가정한 포인트 클라우드
    points = np.random.rand(1000, 3) * [2.0, 1.0, 0.1]
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    pcd.paint_uniform_color([0.7, 0.7, 0.7])
    vis.add_geometry(pcd)

    # 탐지된 스크래치 좌표 저장
    scratch_points = []
    scratch_pcd = o3d.geometry.PointCloud()
    scratch_pcd.paint_uniform_color([1.0, 0.0, 0.0])
    vis.add_geometry(scratch_pcd)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        # 객체 탐지
        results = model(
            frame,
            conf=0.3,
            imgsz=640,
            device=device
        )
        annotated_frame = results[0].plot()

        # 탐지 결과를 3D 좌표로 변환
        boxes = results[0].boxes

        if len(boxes) > 0:
            for box in boxes:
                xyxy = box.xyxy[0].cpu().numpy()

                cx = int((xyxy[0] + xyxy[2]) / 2)
                cy = int((xyxy[1] + xyxy[3]) / 2)

                mapped_3d_point = np.array([
                    cx / 500.0,
                    cy / 500.0,
                    0.05
                ])

                scratch_points.append(mapped_3d_point)

            # 포인트 클라우드 갱신
            if scratch_points:
                scratch_pcd.points = o3d.utility.Vector3dVector(
                    np.array(scratch_points)
                )
                vis.update_geometry(scratch_pcd)

        # 탐지 결과 출력
        cv2.imshow(
            "Scratch Detection",
            annotated_frame
        )

        # 3D 화면 갱신
        vis.poll_events()
        vis.update_renderer()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    vis.destroy_window()


if __name__ == "__main__":
    main()
