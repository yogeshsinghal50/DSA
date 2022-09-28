import logging
import logging.config
import get_all_variables as gav
logging.config.fileConfig(fname='../util/logging_file.conf')
logger = logging.getLogger('data_ingest')


def get_schema(file):
    if file.split('.')[1] == 'csv':
        file_format = 'csv'
        header = gav.header
        inferSchema = gav.inferSchema
    elif file.split('.')[1] == 'parquet':
        file_format = 'parquet'
        header = 'NA'
        inferSchema = 'NA'
    return file_format,header,inferSchema

def load_files(spark, file_dir, file_format, header, inferSchema):
    try:
        logger.info(f'Loading {file_dir}')
        if file_format == 'parquet':
            df = spark.\
                read.\
                format(file_format).\
                load(file_dir)
        elif file_format == 'csv':
            df = spark. \
                read. \
                format(file_format). \
                options(header=header).\
                options(inferSchema=inferSchema).\
                load(file_dir)
    except Exception as e:
        logger.error(e)
        raise
    else:
        logger.info('File has been loaded')
    return df

