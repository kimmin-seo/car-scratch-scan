<div align="center">

# 🚗 Real-Time Car Scratch Detection & 3D Spatial Mapping
**실시간 비전 AI와 3D 공간 시뮬레이션을 융합한 지능형 결함 검출 프로토타입**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white">
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white">
  <img src="https://img.shields.io/badge/YOLOv8-00FFFF?style=for-the-badge&logo=yolo&logoColor=black">
</p>

</div>

<br/>

## ⚡ 01. OVERVIEW & CONCEPT
> **"단순한 이미지 인식을 넘어, 자율주행 검사 로봇의 눈을 통해 3D 가상 공간에 결함을 입체적으로 기록합니다."**

본 프로젝트는 차량 외관 스크래치를 정밀 타겟팅하는 **YOLOv8m 2D Object Detection** 모델과, 추출된 픽셀 좌표를 가상의 3D 공간 매트릭스로 실시간 변환하는 **Open3D** 엔진을 통합하여 구현되었습니다. 

향후 스마트 팩토리 환경에서 **AGV(무인 자율주행 로봇) 기반의 모바일 순회 검사 시스템**으로 확장하기 위한 핵심 비전(Vision) 및 텔레메트리(Telemetry) 아키텍처를 지향합니다.

<br/>

## 🛠️ 02. SYSTEM ARCHITECTURE
```text
 ┌──────────────────────┐      ┌─────────────────────────┐
 │   AGV Vision Node    │ ───> │  YOLOv8m Custom Model   │
 │   Stream (640x640)   │      │ (GPU CUDA Acceleration) │
 └──────────────────────┘      └─────────────────────────┘
                                            │
                                            ▼ (Bounding Box & Center: cx, cy)
 ┌──────────────────────┐      ┌─────────────────────────┐
 │ Virtual 3D Rendering │ <─── │  Open3D Spatial Engine  │
 │ & Telemetry Monitor  │      │ (Zero Memory-Leak Map)  │
 └──────────────────────┘      └─────────────────────────┘

💎 03. CORE FEATURES
🔥 Custom YOLOv8m Inference Engine
고정밀 미세 결함 포착: 직접 수집 및 정제한 맞춤형 데이터셋으로 학습된 best.pt 가중치 활용

실시간 최적화: 640x640 입력 해상도 최적화 및 torch.cuda 강제 병렬 연산을 통해 자율주행 로봇의 이동 속도에 구애받지 않는 고속 프레임 확보

🧊 Dynamic Open3D Spatial Simulation
실시간 공간 변환: 2D 화면상의 바운딩 박스 중심 좌표(cx, cy)를 가상 3D 차체 표면 좌표계로 실시간 매핑

메모리 누수 원천 차단: 매 프레임 객체를 새로 생성하지 않고, 단일 포인트 클라우드를 동적으로 갱신(vis.update_geometry)하는 고효율 루프 설계 적용

🎯 AGV Integration Ready (Future Scope)
단일 스크립트(app.py) 구조로 모듈화되어, 향후 ROS/ROS2(Gazebo 시뮬레이터) 환경에서 AGV의 카메라 토픽(/camera/image_raw)을 구독(Subscribe)하는 형태로 즉각적인 시스템 확장이 가능하도록 설계

📂 04. REPOSITORY STRUCTURE
Plaintext
📁 car-scratch-scan
 ┣ 📜 app.py      # [Main Engine] 2D 탐지 + Open3D 3D 매핑 통합 시뮬레이터
 ┣ 📜 best.pt     # [Model Weights] 커스텀 학습된 YOLOv8m 가중치 (로컬 주입 필요)
 ┗ 📜 README.md   # [Documentation] 프로젝트 가이드
🚀 05. GETTING STARTED
⚙️ Prerequisite Libraries
가상환경(Virtual Environment) 세팅 후 아래의 명령어를 통해 필수 라이브러리를 설치합니다.

Bash
pip install ultralytics opencv-python open3d torch numpy
▶️ Execution
커스텀 학습된 가중치 파일인 best.pt를 프로젝트 루트 디렉토리에 위치시킵니다.

통합 메인 엔진인 app.py를 구동합니다.

Bash
python app.py
Tip: 프로그램 실행 중 언제든 윈도우 창에서 q 키를 누르면 프로세스가 안전하게 종료(Release)됩니다.

📌 NOTE
대용량 바이너리 가중치 파일인 best.pt는 깃허브 저장소 용량 정책에 따라 업로드 목록에서 제외되었습니다. 로컬 환경에서 별도 빌드한 가중치를 주입 후 실행해 주세요.


---
 <img width="380" height="407" alt="image" src="https://github.com/user-attachments/assets/28b34ac9-f52c-4065-8329-17feb76e0f76" />
