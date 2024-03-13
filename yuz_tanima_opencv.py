import cv2 #terminale pip install opencv-python yazarak kurabilirsiniz.

# Kamerayı başlatır
cap = cv2.VideoCapture(0)

while True:
    # Kameradan kare yakalamayı sağlar
    ret, frame = cap.read()

    # Kare alınamazsa döngüyü sonlandır
    if not ret:
        break

    # Görüntü tonlamasnı arttırır. renk,ton,doygunluk değerini ayarlar
    ton = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # cv2 için Yüz tanıma algoritmasını kullanıyoruz
    yuz_algila = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    yuz = yuz_algila.detectMultiScale(ton, 1.3, 5)

    # Belirli koordinatlarda yüzü algıladığında çerçeve içine alır ve text ekler
    for (x, y, w, h) in yuz:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, "Yuz Bulundu", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Gösterilecek görüntüyü gösterir
    cv2.imshow('Yuz Algilama -MBURAK', frame)

    # Çıkmak istenilirse q tuşuna basılabilir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı kapatır
cap.release()
cv2.destroyAllWindows()
