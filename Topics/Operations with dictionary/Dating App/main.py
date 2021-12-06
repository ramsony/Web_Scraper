def select_dates(potential_date):
    return ", ".join([val["name"] for val in potential_date
                      if val['age'] > 30 and 'art' in val['hobbies'] and val['city'] == 'Berlin'])
