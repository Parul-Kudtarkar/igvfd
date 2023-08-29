import pytest


@pytest.fixture
def base_auxiliary_set(testapp, lab, award):
    item = {
        'award': award['@id'],
        'lab': lab['@id'],
        'file_set_type': 'gRNA sequencing'
    }
    return testapp.post_json('/auxiliary_set', item).json['@graph'][0]


@pytest.fixture
def auxiliary_set_v1(base_auxiliary_set):
    item = base_auxiliary_set.copy()
    item.update({
        'schema_version': '1',
        'references': ['10.1101/2023.08.02']
    })
    return item


@pytest.fixture
def auxiliary_set_v2(lab, award):
    item = {
        'schema_version': '2',
        'award': award['@id'],
        'lab': lab['@id'],
        'auxiliary_type': 'gRNA sequencing'
    }
    return item
