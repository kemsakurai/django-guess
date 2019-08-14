from django.core.management.base import BaseCommand, CommandError
from ...models import GuessResult
from google2pandas import *
import numpy as np
from django.conf import settings
from django.db import transaction


class Command(BaseCommand):

    def handle(self, *args, **options):
        record_dicts = self.fetch_ga()
        self.store(record_dicts)

    def store(self, record_dicts):
        with transaction.atomic():
            # Delete All
            GuessResult.objects.all().delete()
            for record_dict in record_dicts:
                # Save
                result = GuessResult.objects.create()
                result.page_path = record_dict['pagePath']
                result.previous_page_path = record_dict['previousPagePath']
                result.page_view_percent = record_dict['pageview_percent']
                result.page_views = record_dict['pageviews']
                result.save()

    def fetch_ga(self):
        query = {
            'reportRequests': [{
                'viewId': settings.GUESS_SETTINGS["VIEW_ID"],
                'dateRanges': [{
                    'startDate': '180daysAgo',
                    'endDate': 'today'}],
                'dimensions': [
                    {'name': 'ga:pagePath'},
                    {'name': 'ga:previousPagePath'},
                ],
                'metrics': [
                    {'expression': 'ga:pageviews'},
                    {'expression': 'ga:exits'},
                ],
            }]
        }
        conn = GoogleAnalyticsQueryV4(secrets=settings.GUESS_SETTINGS["CREDENTIALS"])
        df = conn.execute_query(query)
        df['exits'] = df['exits'].astype(np.int64)
        df['pageviews'] = df['pageviews'].astype(np.int64)

        # ----------------
        #  データの加工
        # --------
        ## データ抽出
        # previousPagePath が `(entrance)` のデータを除外
        df_excluded_entrance = df[df['previousPagePath'] != '(entrance)']
        # previousPagePath ごとの合計を算出
        df_groupby_pagepath = df_excluded_entrance.groupby('previousPagePath').sum()

        rasio_to_evaluate = settings.GUESS_SETTINGS["COMMAND_CONFIG"]['RATIO_TO_EVALUATE']
        # 上位20%のデータのみ抽出する
        import pandas as pd
        df_cutback = df_groupby_pagepath[
            df_groupby_pagepath['pageviews'] > df_groupby_pagepath.quantile(rasio_to_evaluate)["pageviews"]]
        df_edited = df_excluded_entrance[df_excluded_entrance['previousPagePath'].isin(df_cutback.index.tolist())]

        ## 元データに対して処理を行い、最終的なアウトプットへ加工する
        page_grouped = df_edited.groupby(["previousPagePath", "pagePath"]).sum()
        del page_grouped["exits"]
        page_grouped['pageview_percent'] = page_grouped.groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))[
            'pageviews']
        page_grouped = page_grouped.reset_index()
        lower_limit_transition_probability = settings.GUESS_SETTINGS["COMMAND_CONFIG"][
            'LOWER_LIMIT_TRANSITION_PROBABILITY']
        page_grouped = page_grouped[
            (page_grouped['pageview_percent'] >= lower_limit_transition_probability) & ~(
                        page_grouped['previousPagePath'] == page_grouped['pagePath'])]

        # pandas の編集結果を登録する
        record_dicts = page_grouped.to_dict(orient="records")
        return record_dicts
