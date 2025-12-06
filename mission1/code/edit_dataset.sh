# 失敗したエピソードがあった場合に抜く->trainingで特定のエピソードを抜くこともできる
lerobot-edit-dataset \
  --repo_id=AmdRamen/mission1_record \
  --new_repo_id=AmdRamen/mission1_record_edited \
  --operation.type=delete_episodes \
  --operation.episode_indices="[14, 16]" \
  --push_to_hub=True