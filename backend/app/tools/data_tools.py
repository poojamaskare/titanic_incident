import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io
import base64

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'Titanic-Dataset.csv')


def load_titanic_df():
    """Load the Titanic dataset as a pandas DataFrame."""
    try:
        print(f"[DEBUG] Attempting to load CSV from: {DATA_PATH}")
        df = pd.read_csv(DATA_PATH)
        print(f"[DEBUG] Loaded CSV with shape: {df.shape}")
        return df
    except Exception as e:
        print(f"[ERROR] Failed to load CSV: {e}")
        raise


import json
def get_column_info():
    """Return column names, dtypes, and a small sample of the Titanic dataset."""
    try:
        df = load_titanic_df()
        return {
            'columns': df.columns.tolist(),
            'dtypes': df.dtypes.astype(str).to_dict(),
            'sample': json.loads(df.head(3).to_json(orient='records'))
        }
    except Exception as e:
        print(f"[ERROR] get_column_info failed: {e}")
        return {'error': str(e)}


def calculate_percentage(column):
    return column.value_counts(normalize=True) * 100


def summarize_ticket_fares(df):
    return {
        'mean': float(df['Fare'].mean()),
        'median': float(df['Fare'].median()),
        'std_dev': float(df['Fare'].std()),
        'min': float(df['Fare'].min()),
        'max': float(df['Fare'].max())
    }


def generate_histogram(df, column):
    """Generate a histogram for `column` and return base64 PNG bytes string."""
    plt.close('all')
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df[column].dropna(), bins=30, color='steelblue')
    ax.set_title(f'Histogram of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=120)
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')