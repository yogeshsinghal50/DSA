import logging
import logging.config
from pyspark.sql.functions import upper, lit, regexp_extract, col, concat_ws
logging.config.fileConfig(fname='../util/logging_file.conf')
logger = logging.getLogger('data_pre')


def perform_clean(df, df_name):
    try:
        logger.info(f"Data preprocessing for {df_name} started!")
        df_city_sel = df.select(upper(df.city).alias('city'),
                                df.state_id,
                                upper(df.state_name).alias('state_name'),
                                upper(df.county_name).alias('county_name'),
                                df.population,
                                df.zips)
    except Exception as e:
        logger.error(e)
        raise
    else:
        logger.info(f"Data preprocessing for {df_name} completed!")
    return df_city_sel


def perform_clean_fact(df, df_name):
    try:
        logger.info(f"Data preprocessing for {df_name} started!")
        df_fact_sel = df.select(df.npi.alias('presc_id'),
                                df.total_drug_cost,
                                df.total_day_supply,
                                df.drug_name,
                                df.total_claim_count.alias('trx_count'),
                                df.years_of_exp,
                                df.specialty_description.alias('presc_spclt'),
                                df.nppes_provider_state.alias('presc_state'),
                                df.nppes_provider_city.alias('presc_city'),
                                df.nppes_provider_first_name.alias('presc_fname'),
                                df.nppes_provider_last_org_name.alias('presc_lname'))
        df_fact_sel = df_fact_sel.withColumn('country_name', lit("USA"))  # Add Literal or Constant to DataFrame
        pattern = '\d+'
        idx = 0
        df_fact_sel = df_fact_sel.withColumn('years_of_exp', regexp_extract(col('years_of_exp'),pattern=pattern,idx=idx))
        df_fact_sel = df_fact_sel.withColumn('years_of_exp', col('years_of_exp').cast('int'))
        df_fact_sel = df_fact_sel.withColumn('presc_fullname', concat_ws(" ",'presc_fname','presc_lname')) #concat with separator
        df_fact_sel = df_fact_sel.drop('presc_fname','presc_lname')
        # find nan or null values
        # df_fact.select([count(when(isnan(c) | isnull(c), c)).alias(c) for c in df_fact.columns]).show()
        # df_fact = df_fact.dropna(subset="column_name")
        # impute
        # spec = window.partitionBy('presc_id')
        #df_fact = df_fact.withColumn('trx_count',coalesce('trx_count',round(avg('trx_count').over(spec))))
    except Exception as e:
        logger.error(e)
        raise
    else:
        logger.info(f"Data preprocessing for {df_name} completed!")
    return df_fact_sel
