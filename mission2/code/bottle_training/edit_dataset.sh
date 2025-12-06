# 学習時Errorとなったため学習側で制御した。
# 学習時のBug：No files have been modified since last commit. Skipping to prevent empty commit.
lerobot-edit-dataset \
  --repo_id=AmdRamen/mission2_record_bottle \
  --new_repo_id=AmdRamen/mission2_record_bottle_edited \
  --operation.type=delete_episodes \
  --operation.episode_indices="[14]" \
  --push_to_hub=True