import os

os.environ['header'] = 'True'
os.environ['inferSchema'] = 'True'

header = os.environ['header']
inferSchema = os.environ['inferSchema']

appName = "Analytics_Report"
current_path = os.getcwd()

staging_dim_city = current_path + '\..\staging\dimension_city'
staging_fact = current_path + '\..\staging\\fact'


