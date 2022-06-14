from dataclasses import dataclass
from torch.distributed.fsdp import ShardingStrategy


@dataclass
class train_config:
    # general
    host_port: str = "12368"

    # model
    model_name = "google/t5-v1_1-xl"  # "google/t5-v1_1-small"
    tokenizer = "t5-large"
    # available models
    ## t5-base
    # google/t5-v1_1-small
    # google/t5-v1_1-base
    # google/t5-v1_1-large
    # google/t5-v1_1-xl  #3b
    # google/t5-v1_1-xxl #11b

    # save models
    save_model: bool = True
    save_folder = "model_checkpoints"

    # sharding policy
    sharding_strategy: ShardingStrategy = ShardingStrategy.FULL_SHARD
    print_sharding_plan: bool = False

    # dataloaders
    num_workers_dataloader: int = 0

    # policies
    fsdp_unit_size = 1000000
    use_mixed_precision: bool = True

    activation_checkpointing: bool = True

    # datasets
    dataset_train = "datasets_grammar/gtrain_150K.csv"
    dataset_test = "datasets_grammar/grammar_validation.csv"

    # training
    batch_size: int = 32
    num_epochs: int = 12

    # validation
    run_validation: bool = True
    val_batch_size = 8
    block_for_validation: bool = False

    # logging
    track_memory = True
    memory_report: bool = True
    nccl_debug_handler: bool = True
    distributed_debug: bool = True

    # Fine Tuning
    use_child_tuning: bool = True
    use_mirror_optimizer = False
    lr: float = 4e-8

    use_task_free: bool = True
    use_fisher_matrix: bool = False
    percent_F: float = 0.35
