import socket
import cv2
import pickle

# UDP Sockets
video_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
audio_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

SERVER_IP = "127.0.0.1"
VIDEO_PORT = 5000
AUDIO_PORT = 5001

cap = cv2.VideoCapture(0)

audio_file = open("sample.wav", "rb")

print("Server started... Sending audio + video")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (160, 120))  
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 40]  
    _, buffer = cv2.imencode(".jpg", frame, encode_param)

    video_data = pickle.dumps(buffer)
    video_socket.sendto(video_data, (SERVER_IP, VIDEO_PORT))

    audio_data = audio_file.read(1024)  
    if not audio_data:   
        audio_file.seek(0)
        audio_data = audio_file.read(1024)

    audio_socket.sendto(audio_data, (SERVER_IP, AUDIO_PORT))
