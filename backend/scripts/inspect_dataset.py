import logging
from datasets import load_dataset_builder

logging.basicConfig(level=logging.INFO)

def inspect_dataset():
    ds_builder = load_dataset_builder("axonstan/LogoDet-3K")
    print(f"Features: {ds_builder.info.features}")
    
if __name__ == "__main__":
    inspect_dataset()
