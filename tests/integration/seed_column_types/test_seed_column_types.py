from cProfile import run
from tests.integration.base import DBTIntegrationTest, use_profile
import dbt.exceptions


class TestSeedColumnTypeCast(DBTIntegrationTest):
    @property
    def schema(self):
        return "seed_column_types"
        
    @property
    def models(self):
        return "models"

    @property
    def project_config(self):
        return {
            'seeds': {
                'quote_columns': False,
            },
        }

    @use_profile("databricks_cluster")
    def test_seed_column_types_databricks_cluster(self):
        self.run_dbt(["seed"])

    @use_profile("databricks_sql_endpoint")
    def test_seed_column_types_databricks_sql_endpoint(self):
        self.run_dbt(["seed"])
