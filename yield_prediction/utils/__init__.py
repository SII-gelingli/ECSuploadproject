from .data_processor import ReactionDataProcessor

# Lazy imports to avoid loading torch/rdkit when not needed
def get_feature_extractor():
    from .feature_extractor import (
        MolecularFeatureExtractor,
        ConditionEncoder,
        ReactionFeaturizer,
        ReactionDataset
    )
    return MolecularFeatureExtractor, ConditionEncoder, ReactionFeaturizer, ReactionDataset
