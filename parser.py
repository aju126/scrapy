import logging
from nsetools import Nse
from models.nse_object import nse_object

class Parser():
    nse = None
    log_infix = 'Parser::'
    default_query_list = [
        'symbol',
        'companyName',
        'dayHigh',
        'basePrice',
        'dayLow',
        'averagePrice',
        'high52',
        'low52'

    ]
    def __init__(self):
        self.nse = Nse()
        self.log_infix + '__init__ '
        logging.info('%s %s', (self.log_infix, self.nse))
    
    def quote_by_stock_name(self, name, query_list = []):
        self.log_infix + 'quote_by_stock_name '
        if(not name):
            message = 'Name should be present'
            logging.error(self.log_infix + message)
            raise NameError(message)

        if (not self.nse):
            message = 'NSE Object Failure'
            logging.error(self.log_infix + message)
            raise  ValueError(message)
        print(f'nse value is {self.nse} and name is {name}')
        query = self.nse.get_quote(name)
        if(len(query_list) > 0):
            queries = query_list
        else:
            queries = self.default_query_list
        nse_obj = nse_object(query).retrieve_info(queries)
        return nse_obj

    def get_top_gainers(self):
        self.log_infix + 'get_top_gainers '
        if (not self.nse):
            message = 'NSE Object Failure'
            logging.error(self.log_infix + message)
            raise  ValueError(message)

        query = self.nse.get_top_gainers()
        nse_obj = nse_object(query).retrieve_info([])
        return nse_obj
