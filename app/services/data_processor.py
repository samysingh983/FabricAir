import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fastapi import HTTPException
from typing import Dict, List
from uuid import uuid4

class DataProcessor:
    """Handles data processing, transformation, and visualization."""

    @staticmethod
    def get_summary(df: pd.DataFrame) -> Dict:
        return {
            "summary": {
                col: {
                    "mean": df[col].mean(),
                    "median": df[col].median(),
                    "std": df[col].std(),
                    "dtype": str(df[col].dtype)
                }
                for col in df.select_dtypes(include=[np.number]).columns
            }
        }

    @staticmethod
    def transform_data(df: pd.DataFrame, transformations: Dict) -> pd.DataFrame:
        df = df.copy()
        if "normalize" in transformations:
            for col in transformations["normalize"]:
                if col in df.columns:
                    df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
        if "fill_missing" in transformations:
            for col, value in transformations["fill_missing"].items():
                df[col] = df[col].fillna(value)
        return df

    @staticmethod
    def generate_visualization(df: pd.DataFrame, chart_type: str, columns: List[str]) -> str:
        if not all(col in df.columns for col in columns):
            raise HTTPException(status_code=400, detail="Invalid columns specified")
        plt.figure()
        if chart_type == "histogram" and len(columns) == 1:
            df[columns[0]].hist()
        elif chart_type == "scatter" and len(columns) == 2:
            plt.scatter(df[columns[0]], df[columns[1]])
        else:
            raise HTTPException(status_code=400, detail="Invalid chart type or column count")
        static_dir = "static"
        os.makedirs(static_dir, exist_ok=True)
        image_path = os.path.join(static_dir, f"{uuid4()}.png")
        plt.savefig(image_path)
        plt.close()
        return image_path
