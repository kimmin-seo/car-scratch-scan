<div align="center">

# 🚗 Real-Time Car Scratch Detection & 3D Spatial Mapping
**실시간 비전 AI와 3D 공간 시뮬레이션을 융합한 지능형 결함 검출 프로토타입**


## ⚡ 01. OVERVIEW & CONCEPT
> **"단순한 이미지 인식을 넘어, 3D 가상 공간에 결함을 입체적으로 기록합니다."**

본 프로젝트는 차량 외관 스크래치를 정밀 타겟팅하는 **YOLOv8m 2D Object Detection** 모델과, 추출된 픽셀 좌표를 가상의 3D 공간 매트릭스로 실시간 변환하는 **Open3D** 엔진을 통합하여 구현되었습니다. 

향후 스마트 팩토리 자동화 라인 및 로봇팔(Robotic Arm) 궤적 제어로 확장 가능한 시스템 아키텍처를 지향합니다.

<br/>

## 🛠️ 02. SYSTEM ARCHITECTURE
```text
 ┌──────────────────────┐      ┌─────────────────────────┐
 │   WebCam Real-time   │ ───> │  YOLOv8m Custom Model   │
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
직접 수집 및 정제한 데이터셋으로 학습된 best.pt 가중치를 기반으로 미세 스크래치 결점 포착

640x640 입력 해상도 최적화 및 torch.cuda 강제 병렬 연산을 통한 실시간 고속 프레임 확보

🧊 Dynamic Open3D Spatial Simulation
2D 화면상의 바운딩 박스 중심 좌표(cx, cy)를 가상 3D 차체 표면 좌표계로 실시간 매핑

메모리 누수 원천 차단: 매 프레임 객체를 새로 생성하지 않고, 단일 포인트 클라우드를 동적으로 갱신(vis.update_geometry)하는 고효율 루프 설계

🛡️ Production-Ready Structure
불필요한 콘솔 로그 오버헤드를 줄이고, 예외 처리(Exception Handling)를 적용하여 장시간 구동 시 안정성 확보

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

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white">
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white">
  <img src="https://img.shields.io/badge/YOLOv8-00FFFF?style=for-the-badge&logo=yolo&logoColor=black">
</p>

<!-- GitHub Repository QR Code -->
<p align="center">
  <img src="https://api.qrserver.com/v1/create-qr-code/?size=140x140&data=https://github.com/kimmin-seo/car-scratch-scan" alt="GitHub QR Code">
  <br>
  <em>📷 스마트폰 카메라로 QR 코드를 스캔하여 모바일로 저장소에 방문해 보세요!</em>
</p>

</div>

<br/>
