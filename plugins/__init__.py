from __future__ import division, absolute_import, print_function

from airflow.plugins_manager import AirflowPlugin

import plugins.operators
import plugins.helpers


class UdacityPlugin(AirflowPlugin):

    name = 'udacity_plugin'
    operators = [
        operators.CreateTablesOperator,
        operators.DataQualityOperator,
        operators.LoadDimensionOperator,
        operators.LoadFactOperator,
        operators.StageToRedshiftOperator
    ]

    helpers = [
        helpers.SqlQueries
    ]
