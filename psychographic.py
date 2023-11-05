import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import random
random.seed(0)
np.random.seed(0)
n_samples = 200
data = {
    'Income': np.random.randint(20000, 100000, n_samples),
    'Age': np.random.randint(18, 75, n_samples),
    'Environment_Friendly': np.random.rand(n_samples),
    'Tech_Savvy': np.random.rand(n_samples),
}
df = pd.DataFrame(data)
n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(df)
df['Segment'] = kmeans.labels_
print(df)
df.to_csv('psychographic_data.csv', index=False)
import matplotlib.pyplot as plt
df['Segment'].value_counts().plot(kind='bar')
plt.title('Psychographic Segments')
plt.xlabel('Segment')
plt.ylabel('Count')
plt.show()


