import json
from develop.summain import data_to_send
def data():
    x = dict()
    x = data_to_send()
    dat = [  { "key":"textrank",
                     "values":[  # textrank
            {'axis': "Cosine Similarity", 'tech': 'textrank','value': x['textrank'][0]/2.15},
            {'axis': "Unit Overlap", 'tech': 'textrank','value': x['textrank'][1]},
            {'axis': "Precision",'tech': 'textrank', 'value': x['textrank'][2]},
            {'axis': "Recall",'tech': 'textrank', 'value': x['textrank'][3]},
            {'axis': "F Score",'tech': 'textrank', 'value': x['textrank'][4]}]},

             {"key": "luhn",
              "values":[ # luhn
              {'axis': "Cosine Similarity",'tech': 'luhn', 'value':x['luhn'][0]/2.15},
              {'axis': "Unit Overlap", 'tech': 'luhn','value':x['luhn'][1]},
              {'axis': "Precision", 'tech': 'luhn','value':x['luhn'][2]},
              {'axis': "Recall", 'tech': 'luhn','value':x['luhn'][3]},
              {'axis': "F Score", 'tech': 'luhn','value':x['luhn'][4]}]},
             {"key": "lsa",
              "values":[  #lsa
        {'axis': "Cosine Similarity",'tech': 'lsa', 'value':x['lsa'][0]/2.15},
        {'axis': "Unit Overlap", 'tech': 'lsa','value': x['lsa'][1]},
        {'axis': "Precision",'tech': 'lsa', 'value': x['lsa'][2]},
        {'axis': "Recall",'tech': 'lsa', 'value': x['lsa'][3]},
        {'axis': "F Score",'tech': 'lsa', 'value': x['lsa'][4]}]},
             {"key": "klsum",
              "values":[  # klsum
            {'axis': "Cosine Similarity",'tech': 'klsum', 'value': x['klsum'][0]/2.15},
            {'axis': "Unit Overlap",'tech': 'klsum', 'value': x['klsum'][1]},
            {'axis': "Precision",'tech': 'klsum', 'value': x['klsum'][2]},
            {'axis': "Recall",'tech': 'klsum', 'value': x['klsum'][3]},
            {'axis': "F Score",'tech': 'klsum', 'value': x['klsum'][4]}]},

             {"key": "lexrank",
              "values":
                  [  # lexrank
            {'axis': "Cosine Similarity",'tech': 'lexrank', 'value': x['lexrank'][0] / 2.15},
            {'axis': "Unit Overlap", 'tech': 'lexrank','value': x['lexrank'][1]},
            {'axis': "Precision",'tech': 'lexrank', 'value': x['lexrank'][2]},
            {'axis': "Recall",'tech': 'lexrank', 'value': x['lexrank'][3]},
            {'axis': "F Score", 'tech': 'lexrank','value': x['lexrank'][4]}]}
    ]

    return json.dumps(dat)

