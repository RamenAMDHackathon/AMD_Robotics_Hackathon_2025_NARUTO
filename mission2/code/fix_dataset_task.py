from lerobot.datasets.lerobot_dataset import LeRobotDataset
import pandas as pd
from pathlib import Path
from huggingface_hub import HfApi

# キャッシュにダウンロード
cup = LeRobotDataset("AmdRamen/mission2_record_cup")
import pandas as pd
from pathlib import Path

repo_id = "AmdRamen/mission2_record_cup"
cache_dir = Path("/root/.cache/huggingface/lerobot") / repo_id

old_task = "put a paper bottle in a trash bag"
new_task = "put a paper cup in a trash bag"

# ========================================
# 1. tasks.parquet を修正（インデックス名を変更）
# ========================================
tasks_path = cache_dir / "meta" / "tasks.parquet"
tasks_df = pd.read_parquet(tasks_path)
tasks_df = tasks_df.rename(index={old_task: new_task})
tasks_df.to_parquet(tasks_path)
print("tasks.parquet 更新完了")

# ========================================
# 2. episodes parquet - リスト形式を維持して変更
# ========================================
episodes_dir = cache_dir / "meta" / "episodes"
for chunk_dir in episodes_dir.glob("chunk-*"):
    for ep_file in chunk_dir.glob("*.parquet"):
        ep_df = pd.read_parquet(ep_file)
        
        if 'tasks' in ep_df.columns:
            def fix_and_replace(val):
                # 文字列の場合はリストに変換
                if isinstance(val, str):
                    task = new_task if val == old_task or val == new_task else val
                    return [task]
                # リストの場合は中身を置換
                elif isinstance(val, list):
                    return [new_task if v == old_task else v for v in val]
                return val
            
            ep_df['tasks'] = ep_df['tasks'].apply(fix_and_replace)
            ep_df.to_parquet(ep_file, index=False)
            
            # 確認
            sample = ep_df['tasks'].iloc[0]
            print(f"更新: {ep_file.name}")
            print(f"  サンプル: {sample} (type: {type(sample).__name__})")

print("\n完了")