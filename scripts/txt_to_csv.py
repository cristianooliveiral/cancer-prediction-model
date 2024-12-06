import pandas as pd

df = pd.read_csv('/Users/cristianooliveiralopes/Developer/cancer-prediction-model/data/c07a64a0-7588-4653-95ef-982b41a1a804/nationwidechildrens.org_clinical_patient_laml.txt', sep='\t')

df.to_csv('/Users/cristianooliveiralopes/Developer/cancer-prediction-model/data/laml.csv', index='False')