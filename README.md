24.0v full build from bottom: hardfork and sync and mining and fork block script stamping(about 2000)
and segwit height change 3000
=============================================
NODE A

daemon=1

# --- P2P ---
port=8333                # 외부 노드와 블록/트랜잭션 교환

# --- RPC ---
server=1
rpcuser=user
rpcpassword=pass
rpcbind=127.0.0.1
rpcallowip=127.0.0.1
rpcport=8334             # electrs가 붙는 포트(로컬 전용)

# --- 인덱싱/보관 ---
txindex=1                # explorer/electrs 용으로 필수
prune=0                  # 전체 보관(권장). 용량 부족 시 값 조정 가능

# --- (선택) 실시간 반영용 ZMQ: 지금 electrs v3.2.0에서는 미사용이므로 주석 유지 ---
# zmqpubrawblock=tcp://0.0.0.0:28332
# zmqpubrawtx=tcp://0.0.0.0:28333

# --- 기타 권장 ---
listen=1                 # P2P 수신


fallbackfee=0.00001000
maxmempool=50 # 1MB로 제한하여 오래된 트랜잭션 자동 제거
mempoolexpiry=1 # 1시간 후 만료


====================================
NODE B

# 네트워크 설정
listen=1
server=1
daemon=1
port=8333

# RPC 설정
rpcuser=user
rpcpassword=pass
rpcport=8334
rpcbind=127.0.0.1
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24

# 채굴 비활성화
gen=0

# 네트워크 연결 설정
maxconnections=20
connect=34.64.45.122:8333

# DNS 시드 비활성화 (중요!)
dnsseed=0

# 로깅 설정
debug=1
logips=1

# 데이터 디렉토리 (선택사항)
# datadir=/path/to/bitsteal/node2

# 메모리 풀 설정
maxmempool=50

# P2P 메시지 로깅 (디버깅용)
debug=net
debug=addrman

# 블록 동기화 설정
assumevalid=0

fallbackfee=0.00001000
maxmempool=1 # 1MB로 제한하여 오래된 트랜잭션 자동 제거
mempoolexpiry=1 # 1시간 후 만료






