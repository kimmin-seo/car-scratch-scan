# 🚗 Real-time Car Scratch Detection & 3D Spatial Mapping Simulator

> **YOLOv8m과 Open3D를 활용한 실시간 자동차 스크래치 2D 탐지 및 3D 공간 매핑 시뮬레이터**  
> (Real-time 2D Object Detection & 3D Spatial Simulation Project)

---

## 📌 프로젝트 소개 (Introduction)
본 프로젝트는 딥러닝 컴퓨터 비전 기술을 활용하여 차량 표면의 스크래치(결함)를 실시간으로 탐지하고, 이를 가상의 3D 공간 좌표계에 매핑하여 시각화하는 프로토타입 시뮬레이터입니다. 
단순한 2D 영상 처리에서 나아가, 향후 **스마트 팩토리 자동화 공정 및 로봇팔(Robotic Arm) 연동**을 염두에 두고 확장성을 고려하여 설계되었습니다.

---

## 🛠️ 주요 기능 및 특징 (Key Features)

1. **YOLOv8m 커스텀 모델 기반 고정밀 2D 탐지**
   * 직접 수집 및 정제한 데이터셋으로 학습된 `best.pt` 가중치를 적용하여 미세한 스크래치 특징까지 정밀하게 감지합니다.
   * 실시간 추론 시 `conf` 및 `imgsz` 최적화를 통해 정확도와 속도의 밸런스를 맞췄습니다.
2. **GPU 가속(CUDA) 최적화**
   * `torch.cuda`를 통한 하드웨어 가속을 강제 적용하여, Medium(`yolov8m`) 체급의 모델임에도 부드러운 실시간 프레임레이트(FPS)를 보장합니다.
3. **Open3D 기반 3D 공간 좌표 매핑 시뮬레이션**
   * 2D 바운딩 박스의 중심 좌표(`cx, cy`)를 추출하여 가상의 3D 차체 표면 좌표계로 변환합니다.
   * **메모리 누수(Memory Leak) 방지 설계**: 매 프레임 새로운 객체를 생성하지 않고, 단일 포인트 클라우드 데이터를 동적으로 갱신(`vis.update_geometry`)하여 장시간 구동 시에도 안정적인 성능을 유지합니다.

---

## 📂 파일 구조 (File Structure)

```text
📁 PythonProject
 ┣ 📜 app.py      # YOLOv8m 2D 탐지 + Open3D 3D 매핑 시뮬레이터
 ┣ 📜 cam.py      # 실시간 2D 웹캠 스크래치 탐지 전용 스크립트
 ┗ 📜 best.pt     # 커스텀 학습된 YOLOv8m 스크래치 탐지 가중치 파일
