from pyspark.sql import SparkSession
import logging
import logging.config

logging.config.fileConfig(fname='../util/logging_file.conf')
logger = logging.getLogger('create_objects')


def get_spark_object(env, appname):
    logger.info(f"Using master as {env}")
    try:
        spark = SparkSession\
            .builder \
            .master(env) \
            .appName(appname) \
            .getOrCreate()
    except Exception as e:
        logger.error(e)
        raise
    else:
        logger.info("Spark Object created successfully")
    return spark
