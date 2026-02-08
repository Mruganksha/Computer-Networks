import socket
import cv2
import pickle
import winsound 

video_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
audio_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

video_socket.bind(("0.0.0.0", 5000))
audio_socket.bind(("0.0.0.0", 5001))

print("Client ready... Receiving audio + video")

while True:
    video_data, _ = video_socket.recvfrom(65536)
    buffer = pickle.loads(video_data)
    frame = cv2.imdecode(buffer, cv2.IMREAD_COLOR)
    cv2.imshow("Live Video", frame)

    audio_data, _ = audio_socket.recvfrom(1024)

    with open("received.wav", "ab") as f:
        f.write(audio_data)

    if cv2.waitKey(1) == 27:  
        break

cv2.destroyAllWindows()
