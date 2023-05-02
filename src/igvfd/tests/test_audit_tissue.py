import pytest


def test_audit_tissue_ccf_id(
    testapp,
    human_tissue
):
    res = testapp.get(human_tissue['@id'] + '@@index-data')
    assert any(
        error['category'] == 'missing ccf_id'
        for error in res.json['audit'].get('NOT_COMPLIANT', [])
    )
    testapp.patch_json(
        human_tissue['@id'],
        {
            'ccf_id': 'af29d0d8-f274-4107-8e8b-e2025cd5adf4'
        }
    )
    res = testapp.get(human_tissue['@id'] + '@@index-data')
    assert all(
        error['category'] != 'missing ccf_id'
        for error in res.json['audit'].get('NOT_COMPLIANT', [])
    )