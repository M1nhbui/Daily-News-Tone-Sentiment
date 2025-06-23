import subprocess

def run_pipeline():
    print("▶ Step 1: Fetching news...")
    subprocess.run(["python", "update_script/fetch_news.py"], check=True)

    print("▶ Step 2: Cleaning articles...")
    subprocess.run(["python", "update_script/data_cleaning.py"], check=True)

    print("▶ Step 3: Predicting + storing...")
    subprocess.run(["python", "update_script/process_and_store.py"], check=True)

    print("✅ Pipeline complete.")

if __name__ == "__main__":
    run_pipeline()
