
from abc import ABC, abstractmethod
import pandas as pd
import yaml
import os
from utils.enums import CSV_DUMP_DIR


class Worker(ABC):
    @abstractmethod
    def __init__(self, 
                 explore_name: str,
                 table_name: str,
                 schema_file: str = 'schema.yaml', 
                 *args, **kwargs) -> None:
        with open(schema_file) as f:
            self.schema_data = yaml.safe_load(f)
        
        self.explore_name = explore_name
        self.table_name = table_name
        self.table_data : dict = self.schema_data[explore_name][table_name]
        self.schema_info = self.table_data['schema']
        self.csv_target_path = os.path.join(CSV_DUMP_DIR,self.explore_name)
        self.csv_name = os.path.join(self.csv_target_path,f"{self.table_name}.csv")

    @abstractmethod
    def fetch(self, **kwargs) -> dict | pd.DataFrame | str | None:
        """Fetch data (e.g., Looker API call)."""
        pass

    @abstractmethod
    def dump(self, **kwargs):
        """Save data locally (e.g., CSV file)."""
        pass