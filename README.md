# SNN-DNN Perf Profiling 


## 환경 세팅 (Prerequisites)
- **OS:** Ubuntu (WSL2 `5.15.167.4-microsoft-standard` 테스트 완료)
- **Python:** `3.12.3`
- **perf:** `6.8.12`

### 1. 파이썬 가상환경 및 패키지 설치
```bash
python3 -m venv venv
source venv/bin/activate

# 요구 패키지 설치
pip install -r requirements.txt
```

## 실행 가이드 (Quick Start)
### 단계 1: 쉘 스크립트 실행

```bash
chmod +x src/run_stat.sh
./src/run_stat.sh
```

### 단계 2: 결과확인
각 지표들을 시간별로 확인 가능합니다. `tool/graph.py`를 이용하면 시각화하여 그래프로 확인 가능합니다.

```bash
ls result
python3 tool/graph.py result/perf_stat.log
```

#### 실행 결과 예시
<img width="1040" height="537" alt="image" src="https://github.com/user-attachments/assets/463a9ef6-0cab-4dcf-b678-fb193b23d7e8" />
