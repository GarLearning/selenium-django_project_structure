import json

def types():
    with open("base_data/filter_category_data/types", "r+", encoding="utf8") as file:
        types_list = file.read().split('\n')
        fixtures_type_data = []

        for index, item in enumerate(types_list):
            fixtures_type_data.append({
                "model": "ticket.Type",
                "pk": index,
                "fields": {
                    "name": item
                }
            })

        create_features(json.dumps(fixtures_type_data), 'type')

def categories():
    with open("base_data/filter_category_data/categories", "r+", encoding="utf8") as file:
        types_list = file.read().split('\n')
        fixtures_categories_data = []

        for index, item in enumerate(types_list):
            fixtures_categories_data.append({
                "model": "ticket.Category",
                "pk": index,
                "fields": {
                    "name": item
                }
            })
        
        create_features(json.dumps(fixtures_categories_data), 'category')

def type_category():
    with open("base_data/database_data/type.json", "r+", encoding="utf8") as file:
        data_type = json.loads(file.read())

    with open("base_data/database_data/category.json", "r+", encoding="utf8") as file:
        data_category = json.loads(file.read())
    
    with open("base_data/filter_category_data/type_category.json", "r+", encoding="utf8") as file:
        data = json.loads(file.read())

        type_category = []
        for index, item in enumerate(data):
            temp_type_category = {
                "model": "ticket.TypeCategory",
                "pk": index,
                "fields": {}
            }


            for type in data_type:
                if item['type'] == type['name']:
                    temp_type_category['fields']['type'] = [type['id']]
                    break
            
            id_category = []
            for category_list in item['category']:
                for category_item in data_category:
                    if category_item['name'] == category_list:
                        id_category.append(category_item['id'])

            temp_type_category['fields']['category'] = id_category


            type_category.append(temp_type_category)

        create_features(json.dumps(type_category), 'type_category')

def system():
    with open("base_data/database_data/type_category_descriptive.json", "r+", encoding="utf8") as file:
        type_category = json.loads(file.read())

    with open("base_data/filter_category_data/all_filter.json", "r+", encoding="utf8") as file:
        all_data = json.loads(file.read())

        def are_lists_equal(list1, list2):
            if len(list1) != len(list2):
                return False
            return all(item in list2 for item in list1)          

        system = []
        for index, sys in enumerate(all_data):
            temp_type_category = {
                "model": "ticket.System",
                "pk": index,
                "fields": {
                    "name": '',
                    "categories": []
                }
            }

            temp_type_category['fields']['name'] = sys

            sys_types = list(all_data[sys].keys())

            for data in type_category:
                for type in sys_types:
                    if data['type'] == type:
                        are_in = are_lists_equal(all_data[sys][type], data['category'])
                        if are_in:
                            temp_type_category['fields']['categories'].append(data['id'])

            system.append(temp_type_category)

        create_features(json.dumps(system), 'system')

def create_features(data, file_name):
    with open(f"../fixtures/{file_name}_data.json", "w+", encoding="utf8") as file:
        file.write(data)
        print(f'Create {file_name}_data.json in fixtures!')


system()