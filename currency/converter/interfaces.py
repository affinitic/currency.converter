from zope.interface import Interface

from currency.converter import CurrencyConverterMessageFactory as _

class ICurrencyData(Interface):
    """CurrencyData itself: for methods which return currency rate, they return currency code as well. (currency_code, currency_rate) tuple?"""

    def currency_data():
        """Returns the most recent currency data."""

    def currency_data_list():
        """Returns the most recent currency data as a list of dictionaries.
        ex)
        [
            {
            code: "EUR",
            rate: [156.05, 160.25, ...],
            name: u"Euro",
            unit: u"\u20ac"
            },
            {...},{...},...
        ]
        """

    def updated_date():
        """Returns updated date."""

    def currency_codes():
        """Retrurns currency codes."""

    def currency_code_tuples():
        """Returns currency code and its tuples."""

    def currency_code_data():
        """Returns dictionary of currency code and rate list."""

    def currency_code_average(days):
        """Returns code and average rate of days."""

    def days():
        """Returns maximum gotten days."""

    def currency_rate_against_base_code(days, code):
        """Returns currency rate gainst base code."""

    def currency_rate_against_base_code_with_margin(days, code, margin):
        """Returns currency rate gainst base code with margin."""

    def currency_rate(days, margin, base_currency_code, base_rate, currency_code, currency_rate):
        """Returns calculated currency rate."""

class IRateAgainstBaseRate(Interface):
    """A component which provides member's currency."""
    def __call__(base_currency_rate, base_currency_code, currency_code):
        """Returns currency rate for base currency rate, margin and days."""
