from pathlib import Path

ROOT = r"C:\Users\Mink\OneDrive\Documents\GitHub\data\adversarial-eval"
split = "train"

for label in ["clean", "defected"]:
    for model_name in ["resnet18", "efficientnet_b0"]:
        folder = Path(ROOT) / split / label / model_name
        print(f"Checking folder: {folder}")
        if not folder.exists():
            print("❌ Folder not found!")
        else:
            images = list(folder.glob("*.png"))
            print(f"✅ Found {len(images)} images.")
            if not images:
                print("❌ No images found in this folder!")
            else:
                print(f"✅ Images: {', '.join([img.name for img in images[:5]])}...")