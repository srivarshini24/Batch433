# Initialize EasyOCR
reader = easyocr.Reader(['en'])

# Loop through detected boxes
if len(results[0].boxes) > 0:
    for (x1, y1, x2, y2) in results[0].boxes.xyxy.cpu().numpy().astype(int):
        crop = img2[y1:y2, x1:x2]
        crop_rgb = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)

        # Show cropped image
        plt.imshow(crop_rgb)
        plt.axis("off")
        plt.show()

        # OCR
        ocr_result = reader.readtext(crop_rgb)
        for (bbox, text, prob) in ocr_result:
            print(f"Detected Plate: {text} (Confidence: {prob:.2f})")
else:
    print("No license plate detected.")