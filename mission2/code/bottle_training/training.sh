# 学習時editedではErrorになったため14エピソードを除外し学習を行った。
lerobot-train \
  --dataset.repo_id=AmdRamen/mission2_record_bottle \
  --dataset.episodes="[0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19]" \
  --policy.type=act \
  --output_dir=outputs/train/mission2_bottle \
  --job_name=mission2_bottle \
  --policy.device=cuda \
  --wandb.enable=True \
  --policy.repo_id=AmdRamen/mission2_bottle \
  --policy.push_to_hub=True \
  --wandb.entity=amd_hackathon_ramen \
  --wandb.project=mission2_bottle  