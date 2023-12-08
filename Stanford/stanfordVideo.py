import cv2

def calcular_diferenca(frame_anterior, frame_atual):

    gray_anterior = cv2.cvtColor(frame_anterior, cv2.COLOR_BGR2GRAY)
    gray_atual = cv2.cvtColor(frame_atual, cv2.COLOR_BGR2GRAY)
    diff_frame = cv2.absdiff(gray_anterior, gray_atual)
    _, thresh = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)

    return thresh

video_capture = cv2.VideoCapture('output.avi')
ret, frame_anterior = video_capture.read()

while True:
    ret, frame_atual = video_capture.read()
    if not ret:
        break
    diff_frame = calcular_diferenca(frame_anterior, frame_atual)
    cv2.imshow('Detecção de Movimento', diff_frame)
    frame_anterior = frame_atual
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    video_capture.release()
    cv2.destroyAllWindows()