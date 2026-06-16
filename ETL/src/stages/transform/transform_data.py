import pandas as pd
import numpy as np


class TransformData:

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:

        df.drop_duplicates(inplace=True)

        # Padronização dos nomes das colunas
        df.rename(
            columns={
                'Rank': 'rank',
                'Name': 'university_name',
                'No. of FTE Students': 'num_students_enrolled',
                'No. of students per staff': 'num_students_employee',
                'International Students': 'percentual_international_students',
                'Female:Male Ratio': 'female_male_ratio'
            },
            inplace=True
        )

        np.random.seed(42)

        start = pd.Timestamp('2023-01-01')
        end = pd.Timestamp('2023-12-31')

        df['date_random'] = pd.to_datetime(
            np.random.randint(
                start.value,
                end.value,
                size=len(df)
            )
        )


        # Tratando quantidade de alunos
        df['num_students_enrolled'] = (
            df['num_students_enrolled']
            .str.replace(',', '', regex=False)
        )

        df['num_students_enrolled'] = pd.to_numeric(
            df['num_students_enrolled'],
            errors='coerce'
        )

        # Tratando percentual internacional
        df['percentual_international_students'] = (
            df['percentual_international_students']
            .str.replace('%', '', regex=False)
        )

        df['percentual_international_students'] = pd.to_numeric(
            df['percentual_international_students'],
            errors='coerce'
        )

        # Tipo
        df['category_type'] = 'Country'

        mask = df['university_name'].str.contains(
            'University|Institute|Universidade|LMU|TU|ETH|Polytechnic|College|School',
            case=False,
            na=False
        )

        df.loc[mask, 'category_type'] = 'University'

        # Ratio
        ratio = df['female_male_ratio'].str.extract(
            r'(\d+)\s*:\s*(\d+)'
        )

        df['female_pct'] = pd.to_numeric(
            ratio[0],
            errors='coerce'
        )

        df['male_pct'] = pd.to_numeric(
            ratio[1],
            errors='coerce'
        )

        df.drop(
            columns=['female_male_ratio'],
            inplace=True
        )

        return df