from tests._apeirons.placements._apeiron import FIXTURES
from orm.models import *

import pytest
from typing import List


@pytest.fixture(scope='class', autouse=True)
def p_placements(session):

    for fixture in FIXTURES.values():

        h_label = session.query(HubLabels).filter_by(h_label_name=fixture['h_labels']['h_label_name']).first()
        if not h_label:
            h_label = HubLabels(
                h_label_name=fixture['h_labels']['h_label_name'],
                h_label_notional=fixture['h_labels']['h_label_notional']
            )

        h_protocol = session.query(HubProtocols).filter_by(h_protocol_name=fixture['h_protocols']['h_protocol_name']).first()
        if not h_protocol:
            h_protocol = HubProtocols(
                h_protocol_name=fixture['h_protocols']['h_protocol_name'],
                h_protocol_type=fixture['h_protocols']['h_protocol_type']
            )

        h_chain = session.query(HubChains).filter_by(h_network_name=fixture['h_chains']['h_network_name']).first()
        if not h_chain:
            h_chain = HubChains(
                h_network_name=fixture['h_chains']['h_network_name'],
                h_network_id=fixture['h_chains']['h_network_id'],
                h_network_endpoint=fixture['h_chains']['h_network_endpoint']
            )

        h_address_wallet = session.query(HubAddresses).filter_by(h_address=fixture['h_addresses']['wallet']).first()
        if not h_address_wallet:
            h_address_wallet = HubAddresses(
                h_address=fixture['h_addresses']['wallet']
            )

        h_address_pool = session.query(HubAddresses).filter_by(h_address=fixture['h_addresses']['pool']).first()
        if not h_address_pool:
            h_address_pool = HubAddresses(
                h_address=fixture['h_addresses']['pool']
            )

        h_abi_pool = session.query(HubAbis).filter_by(h_abi_list=fixture['h_abis']).first()
        if not h_abi_pool:
            h_abi_pool = HubAbis(
                h_abi_list=fixture['h_abis']
            )

        # supp instances [(h_supp_address, h_supp_abi_list), ...]
        supports: List[dict] = list()

        h_supp_addresses = fixture['h_supp_addresses'].values()
        h_supp_abis = fixture['h_supp_abis'].values()
        for address, abi in zip(h_supp_addresses, h_supp_abis):
            h_supp_address = session.query(HubSupportAddresses).filter_by(h_supp_address=address).first()
            if not h_supp_address:
                h_supp_address = HubSupportAddresses(
                    h_supp_address=address
                )
            h_supp_abi = session.query(HubSupportAbis).filter_by(h_supp_abi_list=abi).first()
            if not h_supp_abi:
                h_supp_abi = HubSupportAbis(
                    h_supp_abi_list=abi
                )

            supports.append({
                h_supp_address: h_supp_abi
            })

            session.add_all([
                h_supp_address, h_supp_abi
            ])
            session.commit()

        hubs = [
            h_label,
            h_protocol,
            h_chain,
            h_address_wallet,
            h_address_pool,
            h_abi_pool
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

        for n, support in enumerate(supports):
            for h_supp_address, h_supp_abi in support.items():
                l_supp_address_abi_token_protocol_chain = LinkSupportAddressesAbisTokensProtocolsChains(
                    h_supp_address_id=h_supp_address.h_supp_address_id,
                    h_supp_abi_id=h_supp_abi.h_supp_abi_id,
                    l_address_abi_token_protocol_chain_id=l_address_abi_token_protocol_chain.l_address_abi_token_protocol_chain_id,
                    l_supp_address_abi_token_protocol_chain_n=f'n+{n+1}'
                )
                session.add(l_supp_address_abi_token_protocol_chain)
                session.commit()

                try:
                    pid = fixture['s_supp_addresses']['s_supp_address_pid']
                except KeyError:
                    continue

                s_supp_address = SatelliteSupportAddresses(
                    h_supp_address_id=h_supp_address.h_supp_address_id,
                    s_supp_address_pid=pid
                )

                session.add(s_supp_address)
                session.commit()

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
