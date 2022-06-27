def default_error(url, error):
    return {
        'url': url,
        'error': error
    }

def create_select(params):
    select = {}
    if 'field' in params:
        select = {
            params['field']: True,
            '_id': False
        }
        params[params['field']] = {'$exists': True}
        del params['field']
    return select, params