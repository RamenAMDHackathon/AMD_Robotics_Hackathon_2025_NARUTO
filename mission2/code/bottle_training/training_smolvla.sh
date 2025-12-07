# install必要->cd lerobot && pip install -e ".[smolvla]"
# 学習時editedではErrorになったため14エピソードを除外し学習を行った。
# smolVLAはデフォルト３つのカメラらしいが減らすことができる。
lerobot-train \
  --dataset.repo_id=AmdRamen/mission2_record_bottle \
  --dataset.episodes="[0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19]" \
  --policy.path=lerobot/smolvla_base \
  --policy.empty_cameras=1 \
  --rename_map='{"observation.images.side": "observation.images.camera1", "observation.images.top": "observation.images.camera2"}' \
  --output_dir=outputs/train/mission2_bottle_smolvla \
  --job_name=mission2_bottle_smolvla \
  --policy.device=cuda \
  --wandb.enable=True \
  --policy.repo_id=AmdRamen/mission2_bottle_smolvla \
  --policy.push_to_hub=true \
  --wandb.entity=amd_hackathon_ramen \
  --wandb.project=mission2_bottle_smolvla  