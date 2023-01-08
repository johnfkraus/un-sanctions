import xmltodict
import json

with open('consolidated.xml', 'r') as f:
    data = f.read()

print(data[:300])

undict = xmltodict.parse(data)

# string = json.dumps(undict, indent=4)
# print(string[:6000], '...TRUNCATED..')
# # print(json.dumps(xmltodict.parse(data)), indent=4)

# def all_keys(dict_obj):
#     ''' This function generates all keys of
#         a nested dictionary. 
#     '''
#     # Iterate over all keys of the dictionary
#     for key , value in dict_obj.items():
#         yield key
#         # If value is of dictionary type then yield all keys
#         # in that nested dictionary
#         print(value, 'isinstance(dict) = ', isinstance(value,dict))
#         if isinstance(value, dict):
#             for k, value2 in value.items():
#                 yield k
#                 print(str(value2)[:100], 'isinstance(value2, dict) = ', isinstance(value2,dict))
#                 if isinstance(value2, dict):
#                     for k, val3 in value2.items():
#                         yield k
                        
#                 elif isinstance(value2,list):
#                      print('is lit')
#                         # if isinstance(val3, dict):
#                         #     for k, val4 in val3.items():
#                         #         yield k


# # Iterate over all keys of a nested dictionary 
# # and print them one by one.
# for key in all_keys(undict):
#     print(key)