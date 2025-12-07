import pandas as pd
from pathlib import Path
import json

cache_dir = Path("/root/.cache/huggingface/lerobot/AmdRamen/mission2_record_cup")

print("=" * 60)
print("1. meta/tasks.parquet")
print("=" * 60)
tasks_df = pd.read_parquet(cache_dir / "meta" / "tasks.parquet")
print(tasks_df)
print(f"インデックス: {tasks_df.index.tolist()}")

print("\n" + "=" * 60)
print("2. meta/episodes/*.parquet の tasks カラム")
print("=" * 60)
episodes_dir = cache_dir / "meta" / "episodes"
for chunk_dir in sorted(episodes_dir.glob("chunk-*")):
    for ep_file in sorted(chunk_dir.glob("*.parquet")):
        ep_df = pd.read_parquet(ep_file)
        if 'tasks' in ep_df.columns:
            unique_tasks = ep_df['tasks'].apply(lambda x: tuple(x) if isinstance(x, list) else x).unique()
            print(f"\n{ep_file.relative_to(cache_dir)}:")
            print(f"  ユニークなタスク: {unique_tasks}")
            print(f"  行数: {len(ep_df)}")

print("\n" + "=" * 60)
print("3. data/*.parquet の task_index カラム")
print("=" * 60)
data_dir = cache_dir / "data"
for chunk_dir in sorted(data_dir.glob("chunk-*")):
    for data_file in sorted(chunk_dir.glob("*.parquet")):
        data_df = pd.read_parquet(data_file)
        if 'task_index' in data_df.columns:
            unique_indices = data_df['task_index'].unique()
            print(f"\n{data_file.relative_to(cache_dir)}:")
            print(f"  ユニークなtask_index: {unique_indices}")
            print(f"  行数: {len(data_df)}")

print("\n" + "=" * 60)
print("4. info.json")
print("=" * 60)
with open(cache_dir / "meta" / "info.json") as f:
    info = json.load(f)
    print(f"total_tasks: {info.get('total_tasks')}")
    print(f"tasks関連キー: {[k for k in info.keys() if 'task' in k.lower()]}")

print("\n" + "=" * 60)
print("5. README.md のタスク情報")
print("=" * 60)
readme_path = cache_dir / "README.md"
if readme_path.exists():
    content = readme_path.read_text()
    # タスク関連の行を探す
    for line in content.split('\n'):
        if 'task' in line.lower() or 'bottle' in line.lower() or 'cup' in line.lower():
            print(line)