from pathlib import Path
from huggingface_hub import HfApi

api = HfApi()
repo_id = "AmdRamen/mission2_record_cup"
old_task = "put a paper bottle in a trash bag"
new_task = "put a paper cup in a trash bag"

cache_dir = Path("/root/.cache/huggingface/lerobot") / repo_id
api = HfApi()

# upload_folder で差分のみアップロード
api.upload_folder(
    folder_path=str(cache_dir),
    repo_id=repo_id,
    repo_type="dataset",
    commit_message=f"Fix task name: '{old_task}' -> '{new_task}'"
)