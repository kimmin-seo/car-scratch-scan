<div align="center">

# 🚗 :: Car Scratch Detection & 3D Spatial Mapping System
### **[ Advanced Computer Vision & Virtual Simulation Portfolio ]**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8m-00FFFF?style=for-the-badge&logo=ultralytics&logoColor=black)](https://github.com/ultralytics/ultralytics)
[![Open3D](https://img.shields.io/badge/Open3D-00796B?style=for-the-badge&logo=opensearch&logoColor=white)](http://www.open3d.org/)
[![CUDA](https://img.shields.io/badge/CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://developer.nvidia.com/cuda-toolkit)

</div>

---

## ⚡ 01. OVERVIEW & CONCEPT
> **실시간 비전 AI와 3D 공간 시뮬레이션을 융합한 지능형 결함 검출 프로토타입**
> 
> * 본 프로젝트는 차량 외관 스크래치를 정밀 타겟팅하는 **YOLOv8m 2D Object Detection** 모델과, 추출된 픽셀 좌표를 가상의 3D 공간 매트릭스로 실시간 변환하는 **Open3D 엔진**을 통합하여 구현되었습니다.
> * 단순한 이미지 인식을 넘어 향후 **스마트 팩토리 자동화 라인 및 로봇팔(Robotic Arm) 궤적 제어**로 확장 가능한 시스템 아키텍처를 지향합니다.

---

## 🛠️ 02. SYSTEM ARCHITECTURE
```text
 ┌──────────────────────┐      ┌─────────────────────────┐
 │   WebCam Real-time   │ ───> │  YOLOv8m Custom Model   │
 │   Stream (640x640)   │      │  (GPU CUDA Acceleration)│
 └──────────────────────┘      └─────────────────────────┘
                                            │
                                            ▼ (Bounding Box & Center: cx, cy)
 ┌──────────────────────┐      ┌─────────────────────────┐
 │ Virtual 3D Rendering │ <─── │   Open3D Spatial Engine │
 │ & Telemetry Monitor  │      │  (Zero Memory-Leak Map) │
 └──────────────────────┘      └─────────────────────────┘


💎 03. CORE FEATURES
🔥 Custom YOLOv8m Inference Engine

직접 수집·정제한 데이터셋으로 학습된 best.pt 가중치를 기반으로 미세 스크래치 결점 포착

640x640 입력 해상도 최적화 및 torch.cuda 강제 병렬 연산을 통한 실시간 고속 프레임 확보

🧊 Dynamic Open3D Spatial Simulation

2D 화면상의 바운딩 박스 중심 좌표(cx, cy)를 가상 3D 차체 표면 좌표계로 실시간 매핑

메모리 누수 원천 차단: 매 프레임 객체를 새로 생성하지 않고, 단일 포인트 클라우드를 동적으로 갱신(vis.update_geometry)하는 고효율 루프 설계

🛡️ Production-Ready Structure

불필요한 콘솔 로그 오버헤드를 줄이고, 예외 처리(Exception Handling)를 적용하여 장시간 구동 시 안정성 확보

📂 04. REPOSITORY STRUCTURE
Plaintext
📁 car-scratch-scan
 ┣ 📜 app.py      # [Main Engine] 2D 탐지 + Open3D 3D 매핑 시뮬레이터
 ┣ 📜 cam.py      # [Sub Script] 실시간 2D 웹캠 단독 추론 테스트
 ┗ 📜 README.md   # [Documentation] 프로젝트 가이드

🚀 05. GETTING STARTED
⚙️ Prerequisite Libraries
Bash
pip install ultralytics opencv-python open3d torch numpy
▶️ Execution
커스텀 학습된 가중치 파일인 best.pt를 프로젝트 루트 디렉토리에 위치시킵니다.

실행 모드에 맞게 스크립트를 구동합니다.

실시간 2D 모니터링 (cam.py):

Bash
python cam.py
3D 공간 매핑 시뮬레이터 (app.py):

Bash
python app.py
(프로그램 종료는 실행 중인 윈도우 창에서 q 키를 누르세요.)

📌 NOTE
대용량 바이너리 가중치 파일인 best.pt는 깃허브 저장소 용량 정책에 따라 제외되어 있습니다. 로컬 환경에서 별도 빌드한 가중치를 주입 후 실행해 주세요.

