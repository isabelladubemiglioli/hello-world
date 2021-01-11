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

