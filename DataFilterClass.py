# Isabella Dube-Miglioli (SN : 18093541)
class DataFilter:
    """
        Filters the data according to the preferences of the user
    """

    default_regions = ["Western Europe", "Eastern Europe", "Northern Europe", "Southern Europe", "Central Europe"]
    default_start_year = 2010
    default_end_year = 2017
    default_shown_data = ["environmental_tax_revenues", "air_pollutants_by_source_sector",
                          "corporate_environmental_protection_investments", "greenhouse_gas_emissions"]

    def __init__(self, default_regions, default_start_year, default_end_year, default_shown_data):
        self.region = default_regions
        self.start_year = default_start_year
        self.end_year = default_end_year
        self.shown_data = default_shown_data

    def select_regions(self, selected_regions: list):
        self.region = selected_regions

    def select_year(self, selected_year: int):
        if default_start_year <= selected_year <= default_end_year:
            self.start_year = selected_year
            self.end_year = selected_year
        else:
            return False

    def select_start_year(self, selected_start_year: int):
        if self.end_year <= selected_start_year < self.end_year:
            self.start_year = selected_start_year
        else:
            return False

    def select_end_year(self, selected_end_year: int):
        if self.start_year < selected_end_year <= self.end_year:
            self.end_year = selected_end_year
        else:
            return False

    def select_data_option(self, selected_data: list):
        self.shown_data = selected_data

    def reset(self):
        self.region = default_regions
        self.start_year = default_start_year
        self.end_year = default_end_year
        self.shown_data = default_shown_data

    def get_data_filter(self):
        return [selected_regions, selected_start_year, selected_end_year, selected_data]


import unittest
from DataFilterClass import DataFilter


class DataFilterTestCase(unittest.TestCase):

    # Set Up
    def setUp(self) -> None:
        self.start_of_year_range = DataFilter.default_start_year
        self.end_of_year_range = DataFilter.default_end_year
        self.list_of_valid_regions = DataFilter.default_regions
        self.list_of_valid_shown_data = DataFilter.default_shown_data

    # tests for select_regions
    def test_select_regions(self):
        my_region = "Mediterranean area"
        # is 2020 in the list of valid regions ? No.
        self.assertNotIn(my_region, self.list_of_valid_regions)

    # tests for select_data_shown
    def test_select_data_shown(self):
        my_data = "GDP per capita"
        # is 2020 in the list of valid regions ? No.
        self.assertNotIn(my_data, self.list_of_valid_shown_data)

    # tests for select_year
    def test_year(self):
        my_year = 2020
        # is 2020 in the range of available years ? No.
        self.assertFalse(self.start_of_year_range <= my_year <= self.end_of_year_range)

    # tests for select_start_year and select_end_year
    def test_start_and_end_years_not_greater(self):
        my_start_year = 2015
        my_end_year = 2012
        # is the start year at an earlier date than the end year ? No.
        self.assertTrue(self.start_of_year_range <= my_start_year <= self.end_of_year_range)
        self.assertTrue(self.start_of_year_range <= my_end_year <= self.end_of_year_range)
        self.assertFalse(my_start_year <= my_end_year)

    # tests for select_start_year and select_end_year
    def test_start_and_end_years_start_out_of_range(self):
        my_start_year = 2008
        my_end_year = 2012
        # is my start year earlier than the default end year, and equal or later than the default start year ? No.
        self.assertTrue(my_start_year <= my_end_year)
        self.assertTrue(self.start_of_year_range <= my_end_year <= self.end_of_year_range)
        self.assertFalse(self.start_of_year_range <= my_start_year <= self.end_of_year_range)

    # tests for select_start_year and select_end_year
    def test_start_and_end_years_end_out_of_range(self):
        my_start_year = 2014
        my_end_year = 2030
        # is my end year earlier than the default end year, and equal or later than the default start year ? No.
        self.assertTrue(my_start_year <= my_end_year)
        self.assertTrue(self.start_of_year_range <= my_start_year <= self.end_of_year_range)
        self.assertFalse(self.start_of_year_range <= my_end_year <= self.end_of_year_range)


