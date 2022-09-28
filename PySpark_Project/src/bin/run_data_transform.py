from udfs import column_split_cnt
from pyspark.sql.functions import countDistinct, sum, col, dense_rank
from pyspark.sql.window import Window
import logging.config
logging.config.fileConfig(fname='../util/logging_file.conf')
logger = logging.getLogger('data_transform')


def city_report(df_city,df_fact):
    try:
        logger.info('Transform - city_report Started')
        df_city_split = df_city.withColumn('zip_counts', column_split_cnt(df_city.zips))
        df_fact_grp = df_fact.groupBy(df_fact.presc_state, df_fact.presc_city).\
            agg(countDistinct('presc_id').alias('presc_counts'), sum('trx_count').alias('trx_counts'))
        df_city_join = df_city_split.join(df_fact_grp, (df_city_split.state_id == df_fact_grp.presc_state) & \
                                          (df_city_split.city == df_fact_grp.presc_city), 'inner')
        df_city_final = df_city_join.\
            select('city','state_name','county_name','population', 'zip_counts','trx_counts','presc_counts')
    except Exception as e:
        logger.error(e)
        raise
    else:
        logger.info('Transform - city_report Completed')
    return df_city_final


def presc_report(df_fact):
    try:
        logger.info('Transform - presc_report Started')
        spec = Window.partitionBy('presc_state').orderBy(col('trx_count').desc())
        df_fact_filter = df_fact.filter((df_fact.years_of_exp >= 20) & (df_fact.years_of_exp <= 50))
        df_presc_final = df_fact_filter.withColumn('dense_rank', dense_rank().over(spec))
    except Exception as e:
        logger.error(e)
        raise
    else:
        logger.info('Transform - presc_report Completed')
    return df_presc_final

