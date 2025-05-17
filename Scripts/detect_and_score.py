import pandas as pd
from ultralytics import YOLO
import cv2
from datetime import datetime

# Load model
model = YOLO('model/best.pt')

RISK_SCORES = {
    'larvae': 5,
    'black_water': 3,
    'large_area': 2,
    'container': 2,
    'vegetation': 1,
    'shadow': 1,
    'urban_area': 2
}

def calculate_risk(detected_classes):
    score = sum([RISK_SCORES.get(obj, 0) for obj in detected_classes])
    if score >= 8:
        return "High", score
    elif 5 <= score <= 7:
        return "Medium", score
    elif score < 5:
        return "Low", score
    else:
        return "Noisy", score

def process_image(image_path):
    results = model(image_path)[0]
    detected_classes = [results.names[int(cls)] for cls in results.boxes.cls]

    risk_level, score = calculate_risk(detected_classes)

    # Save results
    log = {
        'image': image_path,
        'risk_level': risk_level,
        'score': score,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    df = pd.DataFrame([log])
    df.to_csv('data/detection_log.csv', mode='a', header=not pd.read_csv('data/detection_log.csv').empty, index=False)
    
    return risk_level, score
