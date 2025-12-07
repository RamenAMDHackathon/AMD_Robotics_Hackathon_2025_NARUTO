# AMD Robotics Hackathon 2025 - Project NARUTO
## Modular Waste Sorter: YOLOv11とACTモデルの連携による高精度な分別システム
(Multi-Task Robot Framework: 物体認識駆動型のタスク切り替えシステム)

---

## チーム情報 (Team Information)

| 項目 | 内容 |
| :--- | :--- |
| **Team Number** | 18 |
| **Team Name** | RAMEN |
| **Members** | Fumitaka Hara, Keisuke Otani, Y Nakamura, Masamichi Nisiwaki |

---

## 概要 (Project Overview)

SO101ロボットアームを使用し、机上に散在するごみを認識・自律的に把持し、指定のゴミ箱へ分別して廃棄するシステムを構築しました。

画像認識AI（YOLO）が対象物を瞬時に検知し、その物体の種類に応じた個別の動作モデル（ACT）を動的に呼び出すことで、複数の異なるアイテムを連続的かつ正確に処理するシステムを実現しています。

https://github.com/user-attachments/assets/67743540-97d0-45f7-9ba4-49cd9b814531

---

## 提出の詳細 (Project Details)

### 1. ミッションの説明（課題と背景）
ロボットアームを実社会で活用する際、単一の動作だけでなく、複数のアイテムを扱ったり、状況に応じて異なるタスクを連続してこなしたりする能力が求められます。

しかし、あらゆるタスクを単一の巨大なAIモデルで処理しようとすると、学習難易度が高まり、動作の精度が安定しないという課題があります。そこで本プロジェクトでは、「認識」と「動作」を切り分け、タスクごとに最適なモデルを適用する実用的なフレームワークの構築を目指しました。

### 2. 創造性（アプローチの独自性）
本システムの最大の特徴は、**「モジュラー型タスク処理」**のアプローチです。
すべての動作を一度に学習させるのではなく、タスク（例：「コップを捨てる」「ペットボトルを捨てる」）ごとに個別のACT（Action Chunking with Transformers）モデルを作成しました。

これにより、以下のメリットを生み出しています。
* **高精度化:** 1つのモデルが1つのタスクに集中するため、少ないデータ数でも高い成功率を実現。
* **柔軟なワークフロー:** プログラム側で処理順序を制御できるため、複雑な連続処理も安定して実行可能。

また、YOLOでうまく認識できるように10枚程度の写真を作成、アノテーションし、転移学習で一部の層だけ学習して認識率を上げました。

### 3. 技術的な実装
本システムは「視覚（認識）」と「身体（制御）」を明確に連携させています。

#### 画像認識とタスク管理: YOLO11
* 最新のYOLO11を用いて、ワークスペース内の物体（紙コップ、ペットボトル）をリアルタイムに検知・リスト化します。
* 検知されたクラスIDに基づき、その物体を処理するために必要な推論モデル（ポリシー）を動的にロードし、ロボットへ実行指示を出します。

#### ロボット制御: ACT (LeRobot)
* ロボットアーム（SO101）の制御には、LeRobotのガイドラインに準拠したACTのファインチューニングを採用しました。
* **データセット:** リーダーアームを用いたテレオペレーションにより収集。物体の向きや回転角度を変え、ロバスト性向上を狙いました。
* **学習規模:** 各タスクにつき20エピソード（1エピソード20秒）という軽量なデータセットで効率的に学習させています。

#### 利用機材 (equipment)
<img src="./assets/images/ramen_kizai.jpg" alt="equipment" width="400">
SO101、俯瞰カメラ,横からのカメラ、ライト、マット、PC

#### 推論処理フロー (Evaluation System Flow) 

<img src="./assets/images/ramen_system_flow.png" alt="Evaluation system Architecture" width="400">

### 4. 使いやすさ（拡張性と今後の展望）
本システムは拡張性を重視した設計となっており、新たな「ゴミの種類」や「捨て場所」を追加することが容易です。

#### 容易なタスク追加
* **認識:** 新規アイテムをYOLOで学習（または既存モデルで検知可能な場合）させます。
* **動作:** そのアイテム専用の動作データを収集し、ACTをファインチューニングします。
* **実装:** 設定ファイル（Config）にて、検知したIDと参照するモデルパス、タスク記述（task_text）を紐付けるだけで、プログラムを変更することなく機能拡張が可能です。

#### 現在の制約と今後の課題
現在は動作モデルの特性上、アイテムの配置場所は学習データに近い位置である必要があります。ただし、この課題は配置場所をシャッフルしたデータセットで学習することで、解決可能と考えています。

---

## ロボット制御インターフェース (Usage)

### 起動コマンド
実運用モード（Production）にて、信頼度閾値（CONF）を設定しマネージャープログラムを起動します。

```bash
CONF=0.5 RUN_MODE=production python manager.py
```


# Additional Links

Cup
Dataset:https://huggingface.co/datasets/AmdRamen/mission2_record_cup_clean
Model:https://huggingface.co/AmdRamen/mission2_cup_clean

Bottle
Dataset:https://huggingface.co/datasets/AmdRamen/mission2_record_bottle_clean
Model:https://huggingface.co/AmdRamen/mission2_bottle_clean

# Code submission
```
AMD_Robotics_Hackathon_2025_NARUTO/
├── README.md
├── assets/
│   ├── images/
│   │   ├── ramen_kizai.jpg
│   │   └── ramen_system_flow.png
│   └── movies/
│       ├── ramen_amd_20251206_01.mp4
│       └── ramen_amd_20251207_01.mp4
├── mission1/
│   ├── code/
│   │   ├── create_dataset.sh
│   │   ├── edit_dataset.sh
│   │   ├── evaluate.sh
│   │   └── training.sh
│   └── wandb/
│       ├── debug-cli.root.log
│       ├── debug-internal.log
│       ├── debug.log
│       ├── latest-run/
│       │   ├── files/
│       │   │   ├── config.yaml
│       │   │   ├── output.log
│       │   │   ├── requirements.txt
│       │   │   ├── wandb-metadata.json
│       │   │   └── wandb-summary.json
│       │   ├── logs/
│       │   │   ├── debug-core.log
│       │   │   ├── debug-internal.log
│       │   │   └── debug.log
│       │   ├── run-iwarsqft.wandb
│       │   └── run-iwarsqft.wandb.synced
│       └── run-20251206_001239-iwarsqft/
│           ├── files/
│           │   ├── config.yaml
│           │   ├── output.log
│           │   ├── requirements.txt
│           │   ├── wandb-metadata.json
│           │   └── wandb-summary.json
│           ├── logs/
│           │   ├── debug-core.log
│           │   ├── debug-internal.log
│           │   └── debug.log
│           ├── run-iwarsqft.wandb
│           └── run-iwarsqft.wandb.synced
└── mission2/
    ├── code/
    │   ├── bottle_training/
    │   │   ├── continue_create_dataset.sh
    │   │   ├── create_dataset.sh
    │   │   ├── edit_dataset.sh
    │   │   ├── training_act.sh
    │   │   ├── training_nvidia_N15.sh
    │   │   ├── training_nvidia_XVLA.sh
    │   │   ├── training_pi0.sh
    │   │   ├── training_pi05.sh
    │   │   └── training_smolvla.sh
    │   ├── check_dataset.py
    │   ├── cup_training/
    │   │   ├── continue_create_dataset.sh
    │   │   ├── create_dataset.sh
    │   │   └── training.sh
    │   ├── dataset_merge.sh
    │   ├── fix_dataset_task.py
    │   ├── merge_training.sh
    │   ├── push_to_hub.py
    │   ├── scripts/
    │   │   ├── README.md
    │   │   ├── check_camera.py
    │   │   ├── config.yaml
    │   │   ├── garbage_sort_yolo.py
    │   │   ├── homereset.py
    │   │   ├── log.txt
    │   │   ├── log_legacy.py
    │   │   ├── manager.py
    │   │   ├── requirements.md
    │   │   └── run_task.sh
    │   └── yolo_training/
    │       ├── yolo_dataset/
    │       │   ├── data.yaml
    │       │   ├── images/
    │       │   │   ├── train/
    │       │   │   │   ├── 0d74073c-IMG_1838.png
    │       │   │   │   ├── 25035c69-IMG_1836.png
    │       │   │   │   ├── 40438cde-IMG_1835.png
    │       │   │   │   ├── 6932e1f9-IMG_1833.png
    │       │   │   │   ├── 6f9ab418-IMG_1834.png
    │       │   │   │   ├── 77f011b2-IMG_1840.png
    │       │   │   │   ├── 848b3fc6-IMG_1841.png
    │       │   │   │   └── 9901eed1-IMG_1839.png
    │       │   │   └── val/
    │       │   │       ├── ba5f0953-IMG_1832.png
    │       │   │       └── d5dbeab6-IMG_1837.png
    │       │   └── labels/
    │       │       ├── train/
    │       │       │   ├── 0d74073c-IMG_1838.txt
    │       │       │   ├── 25035c69-IMG_1836.txt
    │       │       │   ├── 40438cde-IMG_1835.txt
    │       │       │   ├── 6932e1f9-IMG_1833.txt
    │       │       │   ├── 6f9ab418-IMG_1834.txt
    │       │       │   ├── 77f011b2-IMG_1840.txt
    │       │       │   ├── 848b3fc6-IMG_1841.txt
    │       │       │   └── 9901eed1-IMG_1839.txt
    │       │       └── val/
    │       │           ├── ba5f0953-IMG_1832.txt
    │       │           └── d5dbeab6-IMG_1837.txt
    │       ├── yolo_model/
    │       │   ├── yolo11m_bottle_cup.pt
    │       │   ├── yolo11n_bottle_cup_all.pt
    │       │   └── yolo11s_bottle_cup_all.pt
    │       ├── yolo_training.py
    │       └── yolo_training_all.py
    └── wandb/
        ├── bottle_model/
        │   ├── debug-internal.log
        │   ├── debug.log
        │   ├── latest-run/
        │   │   ├── files/
        │   │   │   ├── config.yaml
        │   │   │   ├── output.log
        │   │   │   ├── requirements.txt
        │   │   │   ├── wandb-metadata.json
        │   │   │   └── wandb-summary.json
        │   │   ├── logs/
        │   │   │   ├── debug-core.log
        │   │   │   ├── debug-internal.log
        │   │   │   └── debug.log
        │   │   └── run-86qwm99j.wandb
        │   └── run-20251207_030827-86qwm99j/
        │       ├── files/
        │       │   ├── config.yaml
        │       │   ├── output.log
        │       │   ├── requirements.txt
        │       │   ├── wandb-metadata.json
        │       │   └── wandb-summary.json
        │       ├── logs/
        │       │   ├── debug-core.log
        │       │   ├── debug-internal.log
        │       │   └── debug.log
        │       └── run-86qwm99j.wandb
        └── cup_model/
            ├── debug-internal.log
            ├── debug.log
            ├── latest-run/
            │   ├── files/
            │   │   ├── config.yaml
            │   │   ├── output.log
            │   │   ├── requirements.txt
            │   │   ├── wandb-metadata.json
            │   │   └── wandb-summary.json
            │   ├── logs/
            │   │   ├── debug-core.log
            │   │   ├── debug-internal.log
            │   │   └── debug.log
            │   └── run-bfwlb645.wandb
            └── run-20251207_041246-bfwlb645/
                ├── files/
                │   ├── config.yaml
                │   ├── output.log
                │   ├── requirements.txt
                │   ├── wandb-metadata.json
                │   └── wandb-summary.json
                ├── logs/
                │   ├── debug-core.log
                │   ├── debug-internal.log
                │   └── debug.log
                └── run-bfwlb645.wandb
```