import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.decomposition import PCA

# Cada linha representa a amostra retirada de uma pessoa
# As colunas são os tipos de microRNA e cada entrada representa a intensidade com que aquele mRNA está expresso
# Valores próximos a zero indicam pouca expressão enquanto que o contrário indica uma alta expressão
# Sendo TP: primary solid tumor e NT: normal tissue

clinical_data = pd.read_csv('../data/brca_mirnaseq.csv', sep=';', header=0, decimal=',')

ax = sns.countplot(x='class', data=clinical_data, palette='deep', legend=False)
ax.set_title('Comparison of Primary Solid Tumor (TP) and Normal Tissue (NT)', fontsize=14)
ax.set_xlabel('Tissue Type', fontsize=12)
ax.set_ylabel('Gene Expression Value', fontsize=12)
plt.savefig(f'../outputs/Comparison_TP_NT.png', dpi=300)
plt.show()
