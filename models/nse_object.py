import json

class nse_object:
    data_dict = {}
    def __init__(self, json_dict):
        self.data_dict = json_dict
    
    def title(self):
        return dict(title=self.data_dict['companyName'])

    def retrieve_info(self, info_names):
        data = {}
        if(not info_names):
            return self.data_dict
        for names in info_names:
            print(f' Fetching info for the info : {names}')
            data[names] = self.data_dict[names]
        return data
