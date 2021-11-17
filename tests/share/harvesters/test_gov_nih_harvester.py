import pytest

from share.harvest.base import FetchResult
from share.models import SourceConfig, RawDatum

xml = """
<row xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<APPLICATION_ID>6828756</APPLICATION_ID>
<ACTIVITY>N01</ACTIVITY>
<ADMINISTERING_IC>AG</ADMINISTERING_IC>
<APPLICATION_TYPE>5</APPLICATION_TYPE>
<ARRA_FUNDED xsi:nil="true"/>
<BUDGET_START xsi:nil="true"/>
<BUDGET_END xsi:nil="true"/>
<FOA_NUMBER xsi:nil="true"/>
<FULL_PROJECT_NUM>N01AG062101-013</FULL_PROJECT_NUM>
<FUNDING_ICs xsi:nil="true"/>
<FY>2003</FY>
<NIH_SPENDING_CATS xsi:nil="true"/>
<ORG_CITY xsi:nil="true"/>
<ORG_COUNTRY xsi:nil="true"/>
<ORG_DISTRICT xsi:nil="true"/>
<ORG_DUNS xsi:nil="true"/>
<ORG_DEPT xsi:nil="true"/>
<ORG_FIPS xsi:nil="true"/>
<ORG_STATE xsi:nil="true"/>
<ORG_ZIPCODE xsi:nil="true"/>
<IC_NAME>NATIONAL INSTITUTE ON AGING</IC_NAME>
<ORG_NAME>UNIVERSITY OF PITTSBURGH AT PI</ORG_NAME>
<PIS xsi:nil="true"/>
<PROJECT_TERMS xsi:nil="true"/>
<PROJECT_TITLE>DYNAMICS OF HEALTH,AGING, AND BODY COMPOSITION-260962101</PROJECT_TITLE>
<PROJECT_START xsi:nil="true"/>
<PROJECT_END xsi:nil="true"/>
<PHR xsi:nil="true"/>
<SERIAL_NUMBER>62101</SERIAL_NUMBER>
<STUDY_SECTION xsi:nil="true"/>
<STUDY_SECTION_NAME xsi:nil="true"/>
<SUPPORT_YEAR xsi:nil="true"/>
<SUFFIX xsi:nil="true"/>
<SUBPROJECT_ID xsi:nil="true"/>
<TOTAL_COST xsi:nil="true"/>
<TOTAL_COST_SUB_PROJECT xsi:nil="true"/>
<CORE_PROJECT_NUM>N01AG062101</CORE_PROJECT_NUM>
<CFDA_CODE xsi:nil="true"/>
<PROGRAM_OFFICER_NAME xsi:nil="true"/>
<ED_INST_TYPE xsi:nil="true"/>
<AWARD_NOTICE_DATE xsi:nil="true"/>
</row>
"""


@pytest.mark.django_db
def test_gov_nih_transformer():
    config = SourceConfig.objects.get(label=('gov.nih'))
    transformer = config.get_transformer()
    fetch_result = FetchResult('6828756', data)
    # fetch_result = FetchResult('http://gov_nih.org/seinet/collections/misc/collprofiles.php?collid=187', data)
    raw_datum = RawDatum.objects.store_data(config, fetch_result)

    graph = transformer.transform(raw_datum)

    dataset = graph.filter_nodes(lambda n: n.type == 'dataset')[0]

    assert dataset.type == 'dataset'
    assert dataset['description'] == 'Sample description'
    assert dataset['title'] == 'A. Michael Powell Herbarium (SRSC)'
    assert dataset['extra']['usage_rights'] == 'CC BY-NC (Attribution-Non-Commercial)'
    assert dataset['extra']['access_rights'] == 'Sul Ross University'
    assert dataset['extra']['collection_statistics'] == {
        "(25%) georeferenced": "1,195",
        "(59%) identified to species": "2,849",
        "(61%) with images": "2,954",
        "families": "104",
        "genera": "361",
        "species": "661",
        "specimen records": "4,868",
        "total taxa (including subsp. and var.)": "762"
    }

    agent_relations = dataset['agent_relations']
    assert len(agent_relations) == 1
    agent = agent_relations[0]['agent']
    assert agent['given_name'] == 'Test'
    assert agent['identifiers'][0]['uri'] == 'mailto:author@email.com'

    identifiers = dataset['identifiers']
    assert len(identifiers) == 1
    assert identifiers[0]['uri'] == 'http://gov_nih.org/seinet/collections/misc/collprofiles.php?collid=187'
