from tests.apeirons.placements.apeiron import FIXTURES
from orm.models import *

import pytest


@pytest.fixture(scope='class', autouse=True)
def p_placements(session):

    for fixture in FIXTURES.values():

        h_label = HubLabels(
            h_label_name=fixture['h_labels']['h_label_name'],
            h_label_notional=fixture['h_labels']['h_label_notional']
        )

        h_protocol = HubProtocols(
            h_protocol_name=fixture['h_protocols']['h_protocol_name'],
            h_protocol_type=fixture['h_protocols']['h_protocol_type']
        )

        h_chain = HubChains(
            h_network_name=fixture['h_chains']['h_network_name'],
            h_network_id=fixture['h_chains']['h_network_id'],
            h_network_endpoint=fixture['h_chains']['h_network_endpoint']
        )

        h_address_wallet = HubAddresses(
            h_address=fixture['h_addresses']['wallet']
        )

        # 3crv instance
        h_address_pool = HubAddresses(
            h_address=fixture['h_addresses']['pool']
        )
        h_abi_pool = HubAbis(
            h_abi_list=fixture['h_abis']
        )

        # gauge instance
        h_supp_address_gauge = HubSupportAddresses(
            h_supp_address=fixture['h_supp_addresses']
        )
        h_supp_abi_gauge = HubSupportAbis(
            h_supp_abi_list=fixture['h_supp_abis']
        )

        hubs = [
            h_label,
            h_protocol,
            h_chain,
            h_address_wallet,
            h_address_pool,
            h_abi_pool,
            h_supp_address_gauge,
            h_supp_abi_gauge
        ]
        session.add_all(hubs)
        session.commit()

        l_protocol_chain = LinkProtocolsChains(
            h_protocol_id=h_protocol.h_protocol_id,
            h_chain_id=h_chain.h_chain_id
        )

        l_address_chain_wallet = LinkAddressesChains(
            h_address_id=h_address_wallet.h_address_id,
            h_chain_id=h_chain.h_chain_id
        )

        l_address_chain_pool = LinkAddressesChains(
            h_address_id=h_address_pool.h_address_id,
            h_chain_id=h_chain.h_chain_id
        )

        links = [
            l_protocol_chain,
            l_address_chain_wallet,
            l_address_chain_pool
        ]
        session.add_all(links)
        session.commit()

        l_address_label_chain = LinkAddressesLabelsChains(
            l_address_chain_id=l_address_chain_wallet.l_address_chain_id,
            h_label_id=h_label.h_label_id
        )

        l_address_abi_chain = LinkAddressesAbisChains(
            l_address_chain_id=l_address_chain_pool.l_address_chain_id,
            h_abi_id=h_abi_pool.h_abi_id
        )

        links = [
            l_address_label_chain,
            l_address_abi_chain
        ]
        session.add_all(links)
        session.commit()

        l_address_abi_token_protocol_chain = LinkAddressesAbisTokensProtocolsChains(
            l_protocol_chain_id=l_protocol_chain.l_protocol_chain_id,
            l_address_abi_chain_id=l_address_abi_chain.l_address_abi_chain_id
        )
        session.add(l_address_abi_token_protocol_chain)
        session.commit()

        l_supp_address_abi_token_protocol_chain = LinkSupportAddressesAbisTokensProtocolsChains(
            h_supp_address_id=h_supp_address_gauge.h_supp_address_id,
            h_supp_abi_id=h_supp_abi_gauge.h_supp_abi_id,
            l_address_abi_token_protocol_chain_id=l_address_abi_token_protocol_chain.l_address_abi_token_protocol_chain_id,
            l_supp_address_abi_token_protocol_chain_n='n+1'
        )

        l_address_abi_token_protocol_label_chain = LinkAddressesAbisTokensProtocolsLabelsChains(
            l_address_abi_token_protocol_chain_id=l_address_abi_token_protocol_chain.l_address_abi_token_protocol_chain_id,
            l_address_label_chain_id=l_address_label_chain.l_address_label_chain_id
        )

        s_address_abi_token_protocol_chain = SatelliteAddressesAbisTokensProtocolsChains(
            l_address_abi_token_protocol_chain_id=l_address_abi_token_protocol_chain.l_address_abi_token_protocol_chain_id,
            s_address_abi_token_protocol_chain_name=fixture['s_addresses_abis_tokens_protocols_chains']['name'],
            s_address_abi_token_protocol_chain_is_impermanent_loss=fixture['s_addresses_abis_tokens_protocols_chains']['is_impermanent_loss']
        )

        links = [
            l_supp_address_abi_token_protocol_chain,
            l_address_abi_token_protocol_label_chain,
            s_address_abi_token_protocol_chain
        ]
        session.add_all(links)
        session.commit()


@pytest.mark.usefixtures(
    'p_placements'
)
class TestFixtures:

    def test_fixture(self, session):
        assert True
