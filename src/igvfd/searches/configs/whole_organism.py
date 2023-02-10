from snovault.elasticsearch.searches.configs import search_config


@search_config(
    name='WholeOrganism'
)
def whole_organism():
    return {
        'columns': {
            'uuid': {
                'title': 'UUID'
            },
            'accession': {
                'title': 'Accession'
            },
            'biosample_term': {
                'title': 'Biosample Term'
            },
            'donor': {
                'title': 'Donor'
            },
            'date_obtained': {
                'title': 'Date Obtained'
            },
            'taxa': {
                'title': 'Taxa'
            },
            'award': {
                'title': 'Award'
            },
            'lab': {
                'title': 'Lab'
            },
            'status': {
                'title': 'Status'
            },
            'submitted_by': {
                'title': 'Submitted By'
            },
        }
    }