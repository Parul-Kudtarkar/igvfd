from snovault.elasticsearch.searches.configs import search_config


@search_config(
    name='Lab'
)
def lab():
    return {
        'facets': {
            'status': {
                'title': 'Status'
            },
        },
        'columns': {
            'uuid': {
                'title': 'UUID'
            },
            'title': {
                'title': 'Title'
            },
            'aliases': {
                'title': 'Aliases'
            },
            'awards': {
                'title': 'Awards'
            },
            'name': {
                'title': 'Name'
            },
            'status': {
                'title': 'Status'
            },
            'pi': {
                'title': 'Principle Investigator'
            },
            'institute_label': {
                'title': 'Institute Label'
            },
            'submitted_by': {
                'title': 'Submitted By'
            },
        }
    }