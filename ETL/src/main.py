from ETL.src.stages.extract.extract_csv import ExtractCSV
from ETL.src.stages.transform.transform_data import TransformData
from ETL.src.stages.load.load_to_sql import LoadToSQL


def main():

    extractor = ExtractCSV(
        "ETL/src/drives/csv/World_Universites_Ranking_2023.csv"
    )

    df = extractor.extract()

    transformer = TransformData()

    df = transformer.transform(df)

    df.to_csv(
        "ETL/src/drives/csv/WUR_2023_tratados.csv",
        index=False,
        encoding="latin1"
    )

    loader = LoadToSQL()

    loader.load(
        df,
        "universities_ranking"
    )

    print("ETL executado com sucesso!")


if __name__ == "__main__":
    main()