from ultralytics import YOLO

# Load a model
model = YOLO("best.pt")  # pretrained YOLO11n model

# Run batched inference on a list of images
result = model(
                '8ca489afedc19b3306d8b7a1e55ad67_0031.jpg'
               )  # return a list of Results objects

# Process results list
for i in result:
    i.save("result1.jpg")