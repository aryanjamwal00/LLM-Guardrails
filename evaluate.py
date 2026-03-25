import pandas as pd
from classifier import classify_prompt
import pandas as pd

df = pd.read_csv("dataset.csv")
print(df.head())

print("Starting evaluation...")

df = pd.read_csv("dataset.csv")

correct = 0
total = len(df)

for index, row in df.iterrows():
    prompt = row['prompt']
    actual = row['label']

    result = classify_prompt(prompt)
    predicted = result["category"]

    if predicted == actual:
        correct += 1
    else:
        print(f"Wrong: {prompt} → Predicted: {predicted}, Actual: {actual}")

accuracy = correct / total

print("\nTotal:", total)
print("Correct:", correct)
print("Accuracy:", accuracy)