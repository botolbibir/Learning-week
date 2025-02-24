import time
import cv2
from ultralytics import YOLO

# Mulai penghitungan waktu eksekusi
start_time = time.time()

# Load model YOLOv8
model = YOLO('yolov8n.pt')

# Buka video atau webcam
cap = cv2.VideoCapture(0)  # Ganti dengan 'video.mp4' jika ingin pakai file video

# Periksa apakah kamera berhasil dibuka
if not cap.isOpened():
    print("❌ Kamera tidak terdeteksi! Periksa koneksi.")
    exit()

# Dapatkan ukuran frame untuk menyimpan video output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (frame_width, frame_height))

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Deteksi objek pada frame
    results = model(frame)
    
    # Gambar hasil deteksi pada frame
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0].item()
            cls = int(box.cls[0].item())
            label = f'{model.names[cls]} {conf:.2f}'

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Simpan frame ke video
    out.write(frame)

    # Tampilkan frame
    cv2.imshow('YOLOv8 Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Hitung total execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"waktu eksekusi adalah {execution_time:.2f} detik")

cap.release()
out.release()
cv2.destroyAllWindows()
