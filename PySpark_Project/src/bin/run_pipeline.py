import os
from run_data_ingest import load_files, get_schema
import get_all_variables as gav
from create_objects import get_spark_object
from validations import get_curr_date, get_df_count, df_print_schema
from run_data_transform import city_report, presc_report
import sys
import logging
import logging.config
from run_data_preprocessing import perform_clean, perform_clean_fact

logging.config.fileConfig(fname='../util/logging_file.conf')


def main():
    try:
        spark = get_spark_object(env='local', appName=gav.appName)
        get_curr_date(spark)
        logging.info("Spark Object is validated!")
        #data ingestion
        for file in os.listdir(gav.staging_dim_city):
            file_dir = gav.staging_dim_city + '\\' + file
            file_format, header, inferSchema = get_schema(file)
        df_city = load_files(spark=spark, file_dir=file_dir, file_format=file_format, header=header, inferSchema=inferSchema)
        for file in os.listdir(gav.staging_fact):
            file_dir = gav.staging_fact + '\\' + file
            file_format, header, inferSchema = get_schema(file)
        df_fact = load_files(spark=spark, file_dir=file_dir, file_format=file_format, header=header,inferSchema=inferSchema)
        get_df_count(df_city, "df_city")
        get_df_count(df_fact, "df_fact")
        #data preprocessing
        df_city = perform_clean(df_city, "df_city")
        get_df_count(df_city, "df_city")
        df_fact = perform_clean_fact(df_fact, "df_fact")
        get_df_count(df_fact, "df_fact")
        #print schema
        df_print_schema(df_fact, "df_fact")
        df_print_schema(df_city, "df_city")
        #get report
        df_city_final = city_report(df_city,df_fact)
        get_df_count(df_city_final, "df_city_final")
        df_presc_final = presc_report(df_fact)
        get_df_count(df_presc_final, "df_presc_final")


    except Exception as e:
        logging.error(e, exc_info=True)
        sys.exit(1)
    else:
        logging.info("Pipeline completed")


if __name__ == '__main__':
    logging.info('Pipeline has started')
    main()
