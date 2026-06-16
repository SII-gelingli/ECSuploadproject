"""
SMILES parsing and reaction fingerprint utilities.

Adapted from yield_prediction/scripts/recommend_conditions.py.
"""
import numpy as np
from typing import List, Tuple, Dict, Optional
from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors


def parse_reaction_smiles(reaction_smiles: str) -> Tuple[List[str], List[str]]:
    """
    Parse a reaction SMILES string into reactants and products.

    Supported formats:
        "reactants>>products"
        "reactant1.reactant2>>product1.product2"

    Returns:
        (reactant_smiles_list, product_smiles_list)
    """
    reaction_smiles = reaction_smiles.strip()
    if '>>' not in reaction_smiles:
        raise ValueError("Invalid reaction SMILES: must contain '>>', e.g. 'CC=CC>>CC(O)CC'")

    parts = reaction_smiles.split('>>')
    if len(parts) != 2:
        raise ValueError("Invalid reaction SMILES: '>>' should appear exactly once")

    reactants_str, products_str = parts[0].strip(), parts[1].strip()
    if not reactants_str or not products_str:
        raise ValueError("Reactants and products cannot be empty")

    reactants = [s.strip() for s in reactants_str.split('.') if s.strip()]
    products = [s.strip() for s in products_str.split('.') if s.strip()]

    return reactants, products


def validate_smiles(smiles: str) -> Dict:
    """
    Validate a single SMILES string and return molecular info.

    Returns dict with: valid, canonical_smiles, molecular_weight, formula, num_atoms, etc.
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return {
            'smiles': smiles,
            'valid': False,
            'error': 'Could not parse SMILES',
        }

    try:
        canonical = Chem.MolToSmiles(mol)
        return {
            'smiles': smiles,
            'valid': True,
            'canonical_smiles': canonical,
            'molecular_formula': rdMolDescriptors.CalcMolFormula(mol),
            'molecular_weight': round(Descriptors.MolWt(mol), 2),
            'num_heavy_atoms': mol.GetNumHeavyAtoms(),
            'num_rings': rdMolDescriptors.CalcNumRings(mol),
            'num_aromatic_rings': Descriptors.NumAromaticRings(mol),
            'logp': round(Descriptors.MolLogP(mol), 2),
            'tpsa': round(Descriptors.TPSA(mol), 2),
            'num_h_donors': Descriptors.NumHDonors(mol),
            'num_h_acceptors': Descriptors.NumHAcceptors(mol),
        }
    except Exception as e:
        return {
            'smiles': smiles,
            'valid': False,
            'error': str(e),
        }


def compute_reaction_fingerprint(
    reactant_smiles: List[str],
    product_smiles: List[str],
    mol_extractor,
    xtb_lookup=None,
) -> np.ndarray:
    """
    Compute reaction feature vector.

    Base: 6144D = reactant_fp(2048) + product_fp(2048) + diff_fp(2048)
    Optional: +33D xTB/RDKit features = reactant(11) + product(11) + diff(11)

    Args:
        reactant_smiles: list of reactant SMILES
        product_smiles: list of product SMILES
        mol_extractor: MolecularFeatureExtractor instance
        xtb_lookup: optional XTBFeatureLookup instance

    Returns:
        numpy array of shape (6144,) or (6177,)
    """
    reactant_fp = mol_extractor.encode_molecules(reactant_smiles)
    product_fp = mol_extractor.encode_molecules(product_smiles)
    diff_fp = np.abs(product_fp - reactant_fp)
    fp = np.concatenate([reactant_fp, product_fp, diff_fp])

    if xtb_lookup is not None:
        r_feat = xtb_lookup.get_aggregated_features(reactant_smiles)
        p_feat = xtb_lookup.get_aggregated_features(product_smiles)
        diff_feat = [p_feat[i] - r_feat[i] for i in range(len(r_feat))]
        xtb_feat = np.array(r_feat + p_feat + diff_feat, dtype=np.float32)
        fp = np.concatenate([fp, xtb_feat])

    return fp


def get_molecular_info(smiles_list: List[str]) -> List[Dict]:
    """Get molecular information for a list of SMILES."""
    return [validate_smiles(s) for s in smiles_list]
