import pytest


@pytest.fixture
def construct_library_set_genome_wide(testapp, lab, award):
    item = {
        'award': award['@id'],
        'lab': lab['@id'],
        'file_set_type': 'guide library',
        'scope': 'genome-wide',
        'selection_criteria': [
            'TF binding sites'
        ],
        'product_id': 'addgene:81225',
        'lower_bound_guide_coverage': 15,
        'upper_bound_guide_coverage': 20,
        'guide_type': 'sgRNA'
    }
    return testapp.post_json('/construct_library_set', item).json['@graph'][0]


@pytest.fixture
def base_expression_construct_library_set(testapp, lab, award, gene_myc_hs):
    item = {
        'award': award['@id'],
        'lab': lab['@id'],
        'file_set_type': 'expression vector library',
        'scope': 'exon',
        'exon': 'E3',
        'genes': [gene_myc_hs['@id']],
        'selection_criteria': [
            'genes'
        ]
    }
    return testapp.post_json('/construct_library_set', item).json['@graph'][0]


@pytest.fixture
def construct_library_set_reporter(testapp, lab, award):
    item = {
        'award': award['@id'],
        'lab': lab['@id'],
        'file_set_type': 'reporter library',
        'scope': 'genome-wide',
        'selection_criteria': [
            'accessible genome regions'
        ],
        'average_insert_size': 50
    }
    return testapp.post_json('/construct_library_set', item).json['@graph'][0]