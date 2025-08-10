from datasets import load_dataset

def load_ag_news_dataset():
    dataset = load_dataset("ag_news")
    print("AG News dataset loaded successfully")
    print("Availability splits:", dataset.keys())

    # Preview a sample for the training set
    print("\nSample record from train split:")
    print(dataset['train'][0])

if __name__ == "__main__":
        load_ag_news_dataset()
