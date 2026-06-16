"""
指纹PCA降维工具

将高维稀疏Morgan指纹压缩到低维稠密表示。
训练集上fit，验证/测试集只transform，防止数据泄露。
"""
import numpy as np
import pickle
from pathlib import Path
from sklearn.decomposition import PCA


class FingerprintPCAReducer:
    """指纹PCA降维器"""

    def __init__(self, n_components: int = 128):
        self.n_components = n_components
        self.pca = PCA(n_components=n_components)
        self.is_fitted = False

    def fit(self, fingerprints: np.ndarray):
        """在训练集指纹上拟合PCA"""
        self.pca.fit(fingerprints)
        self.is_fitted = True
        explained = np.sum(self.pca.explained_variance_ratio_) * 100
        print(f"PCA fitted: {fingerprints.shape[1]}D → {self.n_components}D, "
              f"explained variance: {explained:.1f}%")

    def transform(self, fingerprints: np.ndarray) -> np.ndarray:
        """降维"""
        if not self.is_fitted:
            raise RuntimeError("PCA not fitted yet. Call fit() first.")
        return self.pca.transform(fingerprints).astype(np.float32)

    def fit_transform(self, fingerprints: np.ndarray) -> np.ndarray:
        """拟合并降维"""
        self.fit(fingerprints)
        return self.transform(fingerprints)

    def save(self, path: str):
        """保存PCA参数"""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'wb') as f:
            pickle.dump({
                'n_components': self.n_components,
                'pca': self.pca,
            }, f)
        print(f"PCA saved to {path}")

    def load(self, path: str):
        """加载PCA参数"""
        with open(path, 'rb') as f:
            data = pickle.load(f)
        self.n_components = data['n_components']
        self.pca = data['pca']
        self.is_fitted = True
        print(f"PCA loaded from {path} ({self.n_components} components)")
