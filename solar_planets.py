import cv2

espacioImagen = cv2.imread('solar-system.jpg')

cv2.putText(
    espacioImagen,
    'Sol',
    (20,80),
    cv2.FONT_HERSHEY_PLAIN,
    2,
    (255,250,255)
)

cv2.putText(
    espacioImagen,
    'Mercurio',
    (110,300),
    cv2.FONT_HERSHEY_PLAIN,
    1,
    (255,255,255)
)

cv2.putText(
    espacioImagen,
    'Venus',
    (195,300),
    cv2.FONT_HERSHEY_PLAIN,
    1,
    (255,255,255)
)

cv2.putText(
    espacioImagen,
    'Tierra',
    (290,300),
    cv2.FONT_HERSHEY_PLAIN,
    1,
    (255,255,255)
)

cv2.putText(
    espacioImagen,
    'Marte',
    (385,300),
    cv2.FONT_HERSHEY_PLAIN,
    1,
    (255,255,255)
)

cv2.putText(
    espacioImagen,
    'Jupiter',
    (550,300),
    cv2.FONT_HERSHEY_PLAIN,
    1,
    (0,0,255)
)

cv2.putText(
    espacioImagen,
    'Saturno',
    (750,300),
    cv2.FONT_HERSHEY_PLAIN,
    1,
    (255,255,255)
)

cv2.putText(
    espacioImagen,
    'Urano',
    (980,300),
    cv2.FONT_HERSHEY_PLAIN,
    1,
    (255,255,255)
)

cv2.putText(
    espacioImagen,
    'Neptuno',
    (1120,300),
    cv2.FONT_HERSHEY_PLAIN,
    1,
    (255,255,255)
)

cv2.imwrite('espacioConNombre.jpg', espacioImagen)

cv2.imshow('Imagen del Espacio', espacioImagen)
cv2.waitKey(0)