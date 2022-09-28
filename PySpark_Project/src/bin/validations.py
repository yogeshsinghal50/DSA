import logging
import logging.config

logging.config.fileConfig(fname='../util/logging_file.conf')
logger = logging.getLogger('validations')


def get_df_count(df,df_name):
    try:
        df_count = df.count()
        logger.info(f"Df {df_name} has {df_count} rows")
    except Exception as e:
        logger.error(f"Unable to perform df_count on {df_name}")
        logger.error(e)
        raise
    else:
        logger.info(f"DF {df_name} validated successful")


def get_curr_date(spark):
    try:
        curr_date = spark.sql("select current_date")
        logger.info(f"Current Date -> {str(curr_date.collect())}")
    except Exception as e:
        logger.error(e)
        raise


def df_print_schema(df, df_name):
    try:
        logger.info(f"Validating DF {df_name} schema")
        sch = df.schema.fields
        for i in sch:
            logger.info(f'\t{i}')
    except Exception as e:
        logger.error(e)
        raise
    else:
        logger.info(f"DF {df_name} schema validated successful")

