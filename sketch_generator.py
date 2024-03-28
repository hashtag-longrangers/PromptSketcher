class Sketch:
    def __init__(self):
        self.sketch = {}

    def add_feature(self, feature, description):
        self.sketch[feature] = description

    def generate_sketch(self):
        print("\nGenerating Sketch...\n")
        print("Sketch Details:")
        print("====================")
        for feature, description in self.sketch.items():
            print(f"{feature.capitalize()}: {description}")
        print("====================\n")
        print("Sketch Complete!")
