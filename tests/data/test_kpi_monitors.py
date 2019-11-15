import pytest
import math
import numpy

#from utilities.helpers.db_queries import get_pending_user_product_application_counts_by_day


@pytest.mark.kpi_monitor
class TestKPIMonitor:
    """ Collections of pytests that montior KPIs for Aspiration"""

    def test_product_incepted_events(self, web_db_connection):
        days_to_gather_pending_apps = 30
        total_count = []
        last_seven_day_pending_apps = get_pending_user_product_application_counts_by_day(
            web_db_connection, days_to_gather_pending_apps)
        print(last_seven_day_pending_apps)
        for day in last_seven_day_pending_apps:
            total_count.append(int(last_seven_day_pending_apps[day]))
        # average_count = sum(total_count) / days_to_gather_pending_apps
        # print(average_count)
        # differences = [(count - average_count) for count in total_count]
        # print(differences)
        # differences_squared = [int(math.pow(diff, 2)) for diff in differences]
        # print(differences_squared)
        # variance = sum(differences_squared) / days_to_gather_pending_apps
        # print(variance)
        # standard_deviation = int(math.sqrt(variance))
        standard_deviation = numpy.std(total_count)
        print(standard_deviation)
        for day in last_seven_day_pending_apps:
            # check lower boundary
            count_of_pending_apps = int(last_seven_day_pending_apps[day])
            lower_bound = ((standard_deviation * 2) - int(count_of_pending_apps))
            print(lower_bound)
            upper_bound = ((standard_deviation * 2) + int(count_of_pending_apps))
            print(upper_bound)
            print(f'Is {count_of_pending_apps} > {lower_bound}?')
            assert count_of_pending_apps > lower_bound
            # check Upper boundary
            print(f'Is {count_of_pending_apps} < {upper_bound}?')
            assert count_of_pending_apps < upper_bound
