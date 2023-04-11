import pytest


def test_audit_sample_sorted_fraction_parent_child_check(
    testapp,
    biosample_sorted_child,
    tissue_unsorted_parent,
    rodent_donor
):
    # A Sample that is a sorted_fraction of a parent sample should
    # share most of the parent's metadata properties
    res = testapp.get(biosample_sorted_child['@id'] + '@@index-data')
    assert any(
        error['category'] == 'inconsistent sorted fraction metadata'
        for error in res.json['audit'].get('ERROR', [])
    )
    testapp.patch_json(
        biosample_sorted_child['@id'],
        {'donors': [rodent_donor['@id']],
         'taxa': 'Mus musculus',
         'embryonic': True}
    )
    testapp.patch_json(
        tissue_unsorted_parent['@id'],
        {'nih_institutional_certification': 'NIC000ABCD'}
    )
    res = testapp.get(biosample_sorted_child['@id'] + '@@index-data')
    assert 'inconsistent sorted fraction metadata' not in (
        error['category'] for error in res.json['audit'].get('ERROR', [])
    )