import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'GUKGEONGYEONGSANG'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

    #선공일 때와 후공일 때를 나눠서 targetball 정하기 
    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수

    if order==1:
        if balls[1][0]<0 and balls[3][0]<0:
            targetBall_x=balls[5][0]
            targetBall_y=balls[5][1]
        elif balls[1][0]<0 and balls[3][0]>0:
            targetBall_x=balls[3][0]
            targetBall_y=balls[3][1]
        elif balls[1][0]>0 and balls[3][0]<0:
            targetBall_x=balls[1][0]
            targetBall_y=balls[1][1]
        else:
            wto1=math.hypot(balls[0][0]-balls[1][0],balls[0][1]-balls[1][1])
            wto3=math.hypot(balls[0][0]-balls[3][0],balls[0][1]-balls[3][1])
            if wto1<wto3:
                targetBall_x=balls[1][0]
                targetBall_y=balls[1][1]
            else:
                targetBall_x=balls[3][0]
                targetBall_y=balls[3][1]

    elif order==2: 
        if balls[2][0]<0 and balls[4][0]<0:
            targetBall_x=balls[5][0]
            targetBall_y=balls[5][1]
        elif balls[2][0]<0 and balls[4][0]>0:
            targetBall_x=balls[4][0]
            targetBall_y=balls[4][1]
        elif balls[2][0]>0 and balls[4][0]<0:
            targetBall_x=balls[2][0]
            targetBall_y=balls[2][1]
        else:
            wto2=math.hypot(balls[0][0]-balls[2][0],balls[0][1]-balls[2][1])
            wto4=math.hypot(balls[0][0]-balls[4][0],balls[0][1]-balls[4][1])
            if wto2<wto4:
                targetBall_x=balls[2][0]
                targetBall_y=balls[2][1]
            else:
                targetBall_x=balls[4][0]
                targetBall_y=balls[4][1]

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    ttohv=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]] #targetball 에서 6개 각각의 hole로의 벡터 변수
    for i in range(6):
        ttohv[i][0]=HOLES[i][0]-targetBall_x
        ttohv[i][1]=HOLES[i][1]-targetBall_y 
    wtotv=[targetBall_x-whiteBall_x,targetBall_y-whiteBall_y] #whiteball에서 targetball로의 벡터 변수
    theta=[0,0,0,0,0,0] #white to target 벡터와 target to hole 벡터가 이루는 각도
    for i in range(6):
        theta[i]=math.acos((wtotv[0]*ttohv[i][0]+wtotv[1]*ttohv[i][1])/(math.hypot(wtotv[0],wtotv[1])*math.hypot(ttohv[i][0],ttohv[i][1])))
    theta=list(map(math.degrees,theta))
    print(theta)
    hole=theta.index(min(theta)) #위 5개의 각도중 각도가 가장 작은 hole 을 정해서 목표로 한다.
    hole_x=HOLES[hole][0]
    hole_y=HOLES[hole][1]

    

    vector=[targetBall_x-hole_x,targetBall_y-hole_y] #hole to target 벡터
    length=math.sqrt(vector[0]**2+vector[1]**2) #hole to target 벡터의 크기

    wtot_len=math.sqrt(wtotv[0]**2+wtotv[1]**2)
    distance=wtot_len+length
    diam_vector=list(map(lambda x:(x/length)*4.3*(750-wtot_len)/750,vector)) #각도를 맞춰서 조준하기 위해 targetball 의 좌표에 더해줄 벡터
    objectball=[targetBall_x+diam_vector[0],targetBall_y+diam_vector[1]] #조준할 위치
    angle=math.atan2(objectball[0]-whiteBall_x,objectball[1]-whiteBall_y) #조준할 각도
    angle=math.degrees(angle)
    
    
    # power: 거리 distance에 따른 힘의 세기를 계산
    # power = (wtot_len+math.sin(min(theta)*length))*0.5
    power=65





    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')